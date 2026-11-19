import { supabase } from "../supabase";
import { computeDataHash } from "../dataHash";
import type {
  CloudBackupActionResult,
  CloudBackupInfo,
  CloudBackupSummary,
  LocalLearningState,
  SanitizedLearningBackup,
} from "@/types/storage";
import {
  getLastLocalUserId,
  getLocalState,
  normalizeLearningState,
  saveLocalState,
  setLastLocalUserId,
  touchUserActivityThrottled,
} from "./local";

function getErrorMessage(err: unknown, fallback: string): string {
  if (err instanceof Error && err.message) return err.message;
  if (typeof err === "object" && err !== null && "message" in err) {
    const msg = (err as { message?: unknown }).message;
    if (typeof msg === "string" && msg) return msg;
  }
  return fallback;
}

// ------------------- Cloud Backup & Restore via Supabase 1GB Storage -------------------

/**
 * 提取去除了瞬态草稿（examDrafts / practiceDrafts）的纯净研习数据，
 * 保证数据指纹在跨设备比对时的纯粹性与稳定性。
 */
export function getSanitizedLearningBackup(state: LocalLearningState): SanitizedLearningBackup {
  const sanitizedMistakes = (state.mistakes || []).map((m) => ({
    questionId: m.questionId,
    examId: m.examId || "",
    categoryId: m.categoryId || "",
    wrongAnswer: m.wrongAnswer || "未作答",
    wrongCount: m.wrongCount || 1,
    isMastered: !!m.isMastered,
    lastWrongAt: m.lastWrongAt || "",
  }));

  const sanitizedVocabulary = (state.vocabulary || []).map((v) => ({
    word: (v?.word || "").trim().toLowerCase(),
    phonetic: v?.phonetic || "",
    translation: v?.translation || "",
    context: v?.context || "",
    addedAt: v?.addedAt || "",
    mastered: !!v?.mastered,
    reviewCount: v?.reviewCount || 0,
    lastReviewedAt: v?.lastReviewedAt || "",
  }));

  const sanitizedFavorites = (state.favorites || []).map((f) => ({
    questionId: f.questionId,
    examId: f.examId || "",
    note: f.note || "",
    addedAt: f.addedAt || "",
  }));

  return {
    mistakes: sanitizedMistakes,
    vocabulary: sanitizedVocabulary,
    favorites: sanitizedFavorites,
    examResults: state.examResults || {},
  };
}

export async function uploadBackupToCloud(): Promise<CloudBackupActionResult> {
  try {
    // Use getSession() (reads local JWT) instead of getUser() (triggers a network request)
    const { data: { session }, error: sessionErr } = await supabase.auth.getSession();
    if (sessionErr || !session?.user) {
      return { success: false, error: "未登录，无法备份到云端" };
    }
    const user = session.user;
    if (!getLastLocalUserId()) {
      setLastLocalUserId(user.id);
    }

    const state = getLocalState();
    const cleanBackupState = getSanitizedLearningBackup(state);

    // 🔒 计算当前本地纯净研习数据的 SHA-256 指纹
    const localDataHash = await computeDataHash(cleanBackupState);

    // 🛡️ 防滥用校验：拉取当前云端轻量摘要指纹比对
    const cloudInfo = await fetchCloudBackupInfo();
    if (cloudInfo.exists && cloudInfo.dataHash && cloudInfo.dataHash === localDataHash) {
      console.log("[Storage Backup] 🛡️ 本地数据与云端存档哈希完全一致，硬阻断上传以节省配额。");
      return {
        success: true,
        isIdentical: true,
        message: "本地数据与云端存档完全一致，无需重复上传，已为您节省云端存储与调用配额！",
      };
    }

    const jsonString = JSON.stringify(cleanBackupState);

    // 🗜️ Free Quota Optimization: Native Gzip compression before uploading to Storage Bucket
    let blob: Blob;
    if (typeof CompressionStream !== "undefined") {
      const stream = new Blob([jsonString], { type: "application/json" })
        .stream()
        .pipeThrough(new CompressionStream("gzip"));
      const rawBlob = await new Response(stream).blob();
      blob = new Blob([await rawBlob.arrayBuffer()], { type: "application/json" });
    } else {
      blob = new Blob([jsonString], { type: "application/json" });
    }

    const filePath = `${user.id}/backup.json`;

    // 1. Upload file into private Storage Bucket: 'user-backups' (1GB free space)
    const { error: storageErr } = await supabase.storage
      .from("user-backups")
      .upload(filePath, blob, {
        contentType: "application/json",
        upsert: true,
      });

    if (storageErr) throw storageErr;

    // 2. Update metadata summary in public.user_backups table (含 SHA-256 防重哈希)
    const summary: CloudBackupSummary = {
      mistakesCount: state.mistakes.length,
      vocabCount: state.vocabulary.length,
      favoritesCount: state.favorites.length,
      examsCount: Object.keys(state.examResults).length,
      storageType: "supabase_storage_bucket_gzip",
      backedUpAt: new Date().toISOString(),
      dataHash: localDataHash,
    };

    const { error: dbErr } = await supabase
      .from("user_backups")
      .upsert({
        user_id: user.id,
        summary,
        file_path: filePath,
        updated_at: new Date().toISOString(),
      });

    if (dbErr) {
      return {
        success: false,
        error: `云端备份文件已写入，但云端摘要同步失败，请稍后重试 (${dbErr.message})`,
      };
    }

    // Touch active timestamp on cloud backup (throttled across tabs/actions)
    await touchUserActivityThrottled();

    return { success: true };
  } catch (err: unknown) {
    return { success: false, error: getErrorMessage(err, "上传云端对象存储失败") };
  }
}

export async function downloadBackupFromCloud(): Promise<CloudBackupActionResult> {
  try {
    // Use getSession() (reads local JWT cache) first to avoid unnecessary network latency/errors
    const { data: { session } } = await supabase.auth.getSession();
    let user = session?.user;
    if (!user) {
      const { data: { user: fetchedUser }, error: userErr } = await supabase.auth.getUser();
      if (userErr || !fetchedUser) {
        return { success: false, error: "未登录，无法拉取云端数据" };
      }
      user = fetchedUser;
    }
    if (!getLastLocalUserId()) {
      setLastLocalUserId(user.id);
    }

    // 🛡️ 下载防滥用预检：先对比元数据哈希与本地哈希
    const cloudInfo = await fetchCloudBackupInfo();
    if (cloudInfo.error) {
      return { success: false, error: `查询云端备份状态失败: ${cloudInfo.error}` };
    }
    if (!cloudInfo.exists) {
      return { success: false, error: "云端对象存储中暂无备份文件" };
    }

    const currentLocal = getLocalState();
    const currentLocalClean = getSanitizedLearningBackup(currentLocal);
    const currentLocalHash = await computeDataHash(currentLocalClean);

    if (cloudInfo.dataHash && cloudInfo.dataHash === currentLocalHash) {
      console.log("[Storage Download] 🛡️ 云端存档指纹与本地完全一致，硬阻断下载以节省出网流量与配额。");
      return {
        success: true,
        isIdentical: true,
        message: "本地数据与云端存档完全一致，无需重复拉取覆盖！",
      };
    }

    const filePath = `${user.id}/backup.json`;

    // 1. Download file from private Storage Bucket
    const { data: fileBlob, error: storageErr } = await supabase.storage
      .from("user-backups")
      .download(filePath);

    if (storageErr || !fileBlob) {
      const errObj =
        typeof storageErr === "object" && storageErr !== null
          ? (storageErr as { statusCode?: unknown; status?: unknown; message?: string })
          : null;
      const statusCode = errObj?.statusCode ?? errObj?.status;
      const errMsg = errObj?.message || "";
      const isNotFound =
        !storageErr ||
        String(statusCode) === "404" ||
        /not found|object not found/i.test(errMsg);
      return {
        success: false,
        error: isNotFound ? "云端对象存储中暂无备份文件" : `下载云端备份失败: ${errMsg}`,
      };
    }

    // 🗜️ Smart decompression: auto-detects gzip magic bytes 0x1f 0x8b, fully backward-compatible
    let text = "";
    const buffer = await fileBlob.slice(0, 2).arrayBuffer();
    const header = new Uint8Array(buffer);
    const isGzip = header[0] === 0x1f && header[1] === 0x8b;

    if (isGzip) {
      if (typeof DecompressionStream === "undefined") {
        return { success: false, error: "当前浏览器不支持 Gzip 解压，请升级浏览器后重试" };
      }
      try {
        const stream = fileBlob.stream().pipeThrough(new DecompressionStream("gzip"));
        text = await new Response(stream).text();
      } catch {
        return { success: false, error: "云端备份文件解压失败或已损坏" };
      }
    } else {
      text = await fileBlob.text();
    }

    if (!text) {
      return { success: false, error: "云端存档内容为空" };
    }

    let parsedRaw: unknown;
    try {
      parsedRaw = JSON.parse(text);
    } catch {
      return { success: false, error: "云端存档 JSON 解析失败或已损坏" };
    }

    if (!parsedRaw || typeof parsedRaw !== "object" || Array.isArray(parsedRaw)) {
      return { success: false, error: "云端存档格式异常" };
    }

    const normalizedCloudState = normalizeLearningState(parsedRaw);
    const downloadedClean = getSanitizedLearningBackup(normalizedCloudState);
    const downloadedHash = await computeDataHash(downloadedClean);

    // 🛡️ 若下载解压后的内容其实与本地相同（如旧版无 dataHash 的备份）：
    if (downloadedHash === currentLocalHash) {
      // 顺便回填云端元数据的 dataHash，让后续检查可以免下载直判
      if (!cloudInfo.dataHash) {
        supabase
          .from("user_backups")
          .update({
            summary: {
              ...(cloudInfo.summary || {}),
              dataHash: downloadedHash,
            },
          })
          .eq("user_id", user.id)
          .then(() => {}, () => {});
      }
      return {
        success: true,
        isIdentical: true,
        message: "云端存档内容与当前本地数据完全一致，无需重复覆盖！",
      };
    }

    // Merge local unfinished exam/practice drafts so cloud restore never wipes in-progress work
    const mergedState: LocalLearningState = {
      ...normalizedCloudState,
      examDrafts: {
        ...(normalizedCloudState.examDrafts || {}),
        ...(currentLocal.examDrafts || {}),
      },
      practiceDrafts: {
        ...(normalizedCloudState.practiceDrafts || {}),
        ...(currentLocal.practiceDrafts || {}),
      },
    };
    saveLocalState(mergedState);

    // 若云端元数据缺失指纹，异步回填
    if (!cloudInfo.dataHash) {
      supabase
        .from("user_backups")
        .update({
          summary: {
            ...(cloudInfo.summary || {}),
            dataHash: downloadedHash,
          },
        })
        .eq("user_id", user.id)
        .then(() => {}, () => {});
    }

    return { success: true };
  } catch (err: unknown) {
    return { success: false, error: getErrorMessage(err, "从云端存储下载恢复失败") };
  }
}

export async function fetchCloudBackupInfo(): Promise<CloudBackupInfo> {
  try {
    const { data: { session } } = await supabase.auth.getSession();
    let user = session?.user;
    if (!user) {
      const { data: { user: fetchedUser }, error: userErr } = await supabase.auth.getUser();
      if (userErr) {
        return { exists: false, error: userErr.message };
      }
      user = fetchedUser || undefined;
    }
    if (!user) return { exists: false };

    const { data, error } = await supabase
      .from("user_backups")
      .select("summary, updated_at")
      .eq("user_id", user.id)
      .maybeSingle();

    if (error) {
      return { exists: false, error: error.message };
    }

    if (data) {
      const summary = data.summary as CloudBackupSummary | undefined;
      return {
        exists: true,
        summary,
        updatedAt: data.updated_at,
        dataHash: summary?.dataHash,
      };
    }
    return { exists: false };
  } catch (err: unknown) {
    return { exists: false, error: getErrorMessage(err, "查询云端备份状态失败") };
  }
}
