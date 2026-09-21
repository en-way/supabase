import { supabase } from "./supabase";

export interface QuestionOption {
  key: string;
  text: string;
}

/**
 * Resilient Options Parser:
 * Normalizes options whether entered in Supabase Table Editor as:
 * 1. Standard Array: [{"key":"A","text":"..."}, {"key":"B","text":"..."}]
 * 2. Simple Object: {"A":"...", "B":"..."}
 * 3. Array of strings: ["Option A text", "Option B text"]
 */
export function normalizeOptions(raw: any): QuestionOption[] {
  if (!raw) return [];
  if (Array.isArray(raw)) {
    return raw.map((item, idx) => {
      if (typeof item === "string") {
        const key = String.fromCharCode(65 + idx);
        return { key, text: item };
      }
      return {
        key: String(item?.key || String.fromCharCode(65 + idx)).trim().toUpperCase(),
        text: String(item?.text || ""),
      };
    });
  }
  if (typeof raw === "object") {
    const keys = Object.keys(raw).sort();
    return keys.map((k) => ({
      key: k.trim().toUpperCase(),
      text: String(raw[k] || ""),
    }));
  }
  if (typeof raw === "string") {
    try {
      const parsed = JSON.parse(raw);
      return normalizeOptions(parsed);
    } catch {
      return [];
    }
  }
  return [];
}

export interface MistakeItem {
  questionId: string;
  examId?: string;
  categoryId?: string;
  wrongAnswer: string;
  wrongCount: number;
  isMastered: boolean;
  lastWrongAt: string;
  // Optional legacy fields that may exist in older backups
  stem?: string;
  options?: QuestionOption[];
  correctAnswer?: string;
  explanation?: string;
}

export interface VocabItem {
  word: string;
  phonetic?: string;
  translation: string;
  context?: string;
  addedAt: string;
}

export interface FavoriteItem {
  questionId: string;
  examId: string;
  stem: string;
  options: QuestionOption[];
  correctAnswer: string;
  explanation: string;
  note?: string;
  addedAt: string;
}

export interface ExamDraft {
  examId: string;
  answers: Record<string, string>;
  remainingSeconds: number;
  focusedIndex?: number;
  lastUpdated: string;
}

export interface PracticeDraft {
  examId: string;
  answers: Record<string, string>;
  currentIndex: number;
  lastUpdated: string;
}

export interface ExamResult {
  examId: string;
  examTitle: string;
  score: number;
  totalScore: number;
  isPassed: boolean;
  durationSeconds: number;
  submittedAt: string;
  answers: Record<string, { userAnswer: string; isCorrect: boolean }>;
}

export interface LocalLearningState {
  mistakes: MistakeItem[];
  vocabulary: VocabItem[];
  favorites: FavoriteItem[];
  examResults: Record<string, ExamResult>;
  examDrafts: Record<string, ExamDraft>;
  practiceDrafts?: Record<string, PracticeDraft>;
}

const STORAGE_KEY = "enway_local_learning_data";

export function getLocalState(): LocalLearningState {
  const defaultState: LocalLearningState = {
    mistakes: [],
    vocabulary: [],
    favorites: [],
    examResults: {},
    examDrafts: {},
    practiceDrafts: {},
  };
  if (typeof window === "undefined") {
    return defaultState;
  }
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      return defaultState;
    }
    const parsed = JSON.parse(raw);
    return {
      mistakes: Array.isArray(parsed?.mistakes) ? parsed.mistakes.filter(Boolean) : [],
      vocabulary: Array.isArray(parsed?.vocabulary) ? parsed.vocabulary.filter(Boolean) : [],
      favorites: Array.isArray(parsed?.favorites) ? parsed.favorites.filter(Boolean) : [],
      examResults: parsed?.examResults && typeof parsed.examResults === "object" ? parsed.examResults : {},
      examDrafts: parsed?.examDrafts && typeof parsed.examDrafts === "object" ? parsed.examDrafts : {},
    };
  } catch (e) {
    console.error("Error reading local state", e);
    return defaultState;
  }
}

export function saveLocalState(state: LocalLearningState) {
  if (typeof window === "undefined") return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (e) {
    console.error("Error saving local state", e);
  }
}

// ------------------- Mistake Book (Index-only Lean Footprint) -------------------
export function recordMistake(item: {
  questionId: string;
  examId?: string;
  categoryId?: string;
  wrongAnswer: string;
  [key: string]: any;
}) {
  if (!item?.questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.mistakes)) state.mistakes = [];
  const existingIndex = state.mistakes.findIndex((m) => m && m.questionId === item.questionId);
  const now = new Date().toISOString();

  if (existingIndex >= 0) {
    state.mistakes[existingIndex].wrongCount = (state.mistakes[existingIndex].wrongCount || 1) + 1;
    state.mistakes[existingIndex].wrongAnswer = item.wrongAnswer || "未作答";
    state.mistakes[existingIndex].lastWrongAt = now;
    state.mistakes[existingIndex].isMastered = false; // Reset to unmastered on new error
    if (item.examId) state.mistakes[existingIndex].examId = item.examId;
    if (item.categoryId) state.mistakes[existingIndex].categoryId = item.categoryId;
  } else {
    state.mistakes.unshift({
      questionId: item.questionId,
      examId: item.examId,
      categoryId: item.categoryId,
      wrongAnswer: item.wrongAnswer || "未作答",
      wrongCount: 1,
      isMastered: false,
      lastWrongAt: now,
    });
  }

  // Sanitize all mistakes to strictly retain lightweight index fields (save Supabase cloud quota)
  state.mistakes = state.mistakes
    .filter((m) => m && m.questionId)
    .map((m) => ({
      questionId: m.questionId,
      examId: m.examId,
      categoryId: m.categoryId,
      wrongAnswer: m.wrongAnswer || "未作答",
      wrongCount: m.wrongCount || 1,
      isMastered: !!m.isMastered,
      lastWrongAt: m.lastWrongAt || now,
    }));

  saveLocalState(state);
}

export function toggleMistakeMastered(questionId: string, isMastered?: boolean) {
  if (!questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.mistakes)) return;
  const target = state.mistakes.find((m) => m && m.questionId === questionId);
  if (target) {
    target.isMastered = isMastered !== undefined ? isMastered : !target.isMastered;
    saveLocalState(state);
  }
}

export function removeMistake(questionId: string) {
  if (!questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.mistakes)) return;
  state.mistakes = state.mistakes.filter((m) => m && m.questionId !== questionId);
  saveLocalState(state);
}

// ------------------- Vocabulary -------------------
export function addVocab(word: string, translation: string, phonetic?: string, context?: string) {
  if (!word) return;
  const state = getLocalState();
  if (!Array.isArray(state.vocabulary)) state.vocabulary = [];
  const cleanWord = word.trim().toLowerCase();
  const exists = state.vocabulary.some((v) => v && v.word && v.word.toLowerCase() === cleanWord);
  if (!exists) {
    state.vocabulary.unshift({
      word: cleanWord,
      translation,
      phonetic,
      context,
      addedAt: new Date().toISOString(),
    });
    saveLocalState(state);
  }
}

export function removeVocab(word: string) {
  if (!word) return;
  const state = getLocalState();
  if (!Array.isArray(state.vocabulary)) return;
  const cleanWord = word.trim().toLowerCase();
  state.vocabulary = state.vocabulary.filter((v) => v && v.word && v.word.toLowerCase() !== cleanWord);
  saveLocalState(state);
}

// ------------------- Favorites -------------------
export function toggleFavorite(item: Omit<FavoriteItem, "addedAt">) {
  if (!item?.questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.favorites)) state.favorites = [];
  const index = state.favorites.findIndex((f) => f && f.questionId === item.questionId);
  if (index >= 0) {
    state.favorites.splice(index, 1);
  } else {
    state.favorites.unshift({
      ...item,
      addedAt: new Date().toISOString(),
    });
  }
  saveLocalState(state);
}

export function updateFavoriteNote(questionId: string, note: string) {
  if (!questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.favorites)) return;
  const target = state.favorites.find((f) => f && f.questionId === questionId);
  if (target) {
    target.note = note;
    saveLocalState(state);
  }
}

// ------------------- Exam Drafts (Auto-Save Resilience) -------------------
export function saveExamDraft(examId: string, answers: Record<string, string>, remainingSeconds: number, focusedIndex?: number) {
  if (!examId) return;
  const state = getLocalState();
  if (!state.examDrafts || typeof state.examDrafts !== "object") {
    state.examDrafts = {};
  }
  state.examDrafts[examId] = {
    examId,
    answers: answers || {},
    remainingSeconds: typeof remainingSeconds === "number" ? remainingSeconds : 3600,
    focusedIndex: typeof focusedIndex === "number" ? focusedIndex : 0,
    lastUpdated: new Date().toISOString(),
  };
  saveLocalState(state);
}

export function getExamDraft(examId: string): ExamDraft | null {
  if (!examId) return null;
  const state = getLocalState();
  return state.examDrafts?.[examId] || null;
}

export function clearExamDraft(examId: string) {
  if (!examId) return;
  const state = getLocalState();
  if (state.examDrafts && typeof state.examDrafts === "object") {
    delete state.examDrafts[examId];
    saveLocalState(state);
  }
}

// ------------------- Practice Drafts (Smart Practice Resume) -------------------
export function savePracticeDraft(examId: string, answers: Record<string, string>, currentIndex: number) {
  if (!examId) return;
  const state = getLocalState();
  if (!state.practiceDrafts || typeof state.practiceDrafts !== "object") {
    state.practiceDrafts = {};
  }
  state.practiceDrafts[examId] = {
    examId,
    answers: answers || {},
    currentIndex: typeof currentIndex === "number" ? currentIndex : 0,
    lastUpdated: new Date().toISOString(),
  };
  saveLocalState(state);
}

export function getPracticeDraft(examId: string): PracticeDraft | null {
  if (!examId) return null;
  const state = getLocalState();
  return state.practiceDrafts?.[examId] || null;
}

export function clearPracticeDraft(examId: string) {
  if (!examId) return;
  const state = getLocalState();
  if (state.practiceDrafts && typeof state.practiceDrafts === "object") {
    delete state.practiceDrafts[examId];
    saveLocalState(state);
  }
}

// ------------------- Exam Results (Latest Overwrite) -------------------
export function saveExamResult(result: ExamResult) {
  if (!result?.examId) return;
  const state = getLocalState();
  if (!state.examResults || typeof state.examResults !== "object") {
    state.examResults = {};
  }
  if (!state.examDrafts || typeof state.examDrafts !== "object") {
    state.examDrafts = {};
  }
  state.examResults[result.examId] = result;
  // Clear draft once submitted
  delete state.examDrafts[result.examId];
  saveLocalState(state);

  // Touch active timestamp on exam submission
  if (typeof window !== "undefined") {
    try {
      supabase.rpc("touch_user_activity").then(() => {}, () => {});
    } catch {}
  }
}

// ------------------- Cloud Backup & Restore via Supabase 1GB Storage -------------------

export async function uploadBackupToCloud(): Promise<{ success: boolean; error?: string }> {
  try {
    const { data: { user }, error: userErr } = await supabase.auth.getUser();
    if (userErr || !user) {
      return { success: false, error: "未登录，无法备份到云端" };
    }

    const state = getLocalState();
    // Ensure mistakes are purely index-based to save egress and storage
    state.mistakes = (state.mistakes || []).map((m) => ({
      questionId: m.questionId,
      examId: m.examId,
      categoryId: m.categoryId,
      wrongAnswer: m.wrongAnswer || "未作答",
      wrongCount: m.wrongCount || 1,
      isMastered: !!m.isMastered,
      lastWrongAt: m.lastWrongAt || new Date().toISOString(),
    }));

    const jsonString = JSON.stringify(state);

    // 🗜️ Free Quota Optimization: Native Gzip compression before uploading to Storage Bucket
    let blob: Blob;
    if (typeof CompressionStream !== "undefined") {
      const stream = new Blob([jsonString], { type: "application/json" })
        .stream()
        .pipeThrough(new CompressionStream("gzip"));
      blob = await new Response(stream).blob();
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

    // 2. Update metadata summary in public.user_backups table (tiny footprint ~50 bytes)
    const summary = {
      mistakesCount: state.mistakes.length,
      vocabCount: state.vocabulary.length,
      favoritesCount: state.favorites.length,
      examsCount: Object.keys(state.examResults).length,
      storageType: "supabase_storage_bucket_gzip",
      backedUpAt: new Date().toISOString(),
    };

    const { error: dbErr } = await supabase
      .from("user_backups")
      .upsert({
        user_id: user.id,
        summary,
        file_path: filePath,
        updated_at: new Date().toISOString(),
      });

    if (dbErr) console.warn("Notice: updated storage file, metadata sync:", dbErr.message);

    // Touch active timestamp on cloud backup
    try {
      await supabase.rpc("touch_user_activity");
    } catch {}

    return { success: true };
  } catch (err: any) {
    return { success: false, error: err.message || "上传云端对象存储失败" };
  }
}

export async function downloadBackupFromCloud(): Promise<{ success: boolean; summary?: any; error?: string }> {
  try {
    const { data: { user }, error: userErr } = await supabase.auth.getUser();
    if (userErr || !user) {
      return { success: false, error: "未登录，无法拉取云端数据" };
    }

    const filePath = `${user.id}/backup.json`;

    // 1. Download file from private Storage Bucket
    const { data: fileBlob, error: storageErr } = await supabase.storage
      .from("user-backups")
      .download(filePath);

    if (storageErr || !fileBlob) {
      return { success: false, error: "云端对象存储中暂无备份文件" };
    }

    // 🗜️ Smart decompression: auto-detects gzip magic bytes 0x1f 0x8b, fully backward-compatible
    let text = "";
    try {
      const buffer = await fileBlob.slice(0, 2).arrayBuffer();
      const header = new Uint8Array(buffer);
      const isGzip = header[0] === 0x1f && header[1] === 0x8b;

      if (isGzip && typeof DecompressionStream !== "undefined") {
        const stream = fileBlob.stream().pipeThrough(new DecompressionStream("gzip"));
        text = await new Response(stream).text();
      } else {
        text = await fileBlob.text();
      }
    } catch {
      text = await fileBlob.text();
    }

    if (!text) {
      return { success: false, error: "云端存档内容为空" };
    }

    const parsedState = JSON.parse(text) as LocalLearningState;
    saveLocalState(parsedState);

    return { success: true };
  } catch (err: any) {
    return { success: false, error: err.message || "从云端存储下载恢复失败" };
  }
}

export async function fetchCloudBackupInfo(): Promise<{ exists: boolean; summary?: any; updatedAt?: string }> {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return { exists: false };

    const { data } = await supabase
      .from("user_backups")
      .select("summary, updated_at")
      .eq("user_id", user.id)
      .maybeSingle();

    if (data) {
      return { exists: true, summary: data.summary, updatedAt: data.updated_at };
    }
    return { exists: false };
  } catch {
    return { exists: false };
  }
}

// ------------------- Reconciliation Engine (存档智能校对与更正自愈) -------------------

export interface ReconcileResult {
  hasChanges: boolean;
  deletedQuestionsCount: number;
  fixedAnswersCount: number;
  deletedExamsCount: number;
  summaryText: string;
}

export async function reconcileLearningState(
  targetState?: LocalLearningState
): Promise<ReconcileResult> {
  const state = targetState || getLocalState();
  let hasChanges = false;
  let deletedQuestionsCount = 0;
  let fixedAnswersCount = 0;
  let deletedExamsCount = 0;

  try {
    // 1. Collect all Question IDs
    const mistakeQIds = (state.mistakes || []).map((m) => m.questionId);
    const favQIds = (state.favorites || []).map((f) => f.questionId);
    const allQIds = Array.from(new Set([...mistakeQIds, ...favQIds]));

    // 2. Collect all Exam IDs
    const draftExamIds = Object.keys(state.examDrafts || {});
    const resultExamIds = Object.keys(state.examResults || {});
    const mistakeExamIds = (state.mistakes || []).map((m) => m.examId).filter(Boolean) as string[];
    const allExamIds = Array.from(new Set([...draftExamIds, ...resultExamIds, ...mistakeExamIds]));

    // 3. Batch query valid questions
    const validQuestionsMap: Record<string, { id: string; correct_answer: string; exam_id: string; category_id: string }> = {};
    if (allQIds.length > 0) {
      const { data: qRows, error: qErr } = await supabase
        .from("questions")
        .select("id, correct_answer, exam_id, category_id")
        .in("id", allQIds);

      if (!qErr && qRows) {
        qRows.forEach((q: any) => {
          validQuestionsMap[q.id] = q;
        });
      }
    }

    // 4. Batch query valid approved exams
    const validExamsMap: Record<string, boolean> = {};
    if (allExamIds.length > 0) {
      const { data: eRows, error: eErr } = await supabase
        .from("exams")
        .select("id, is_published, approval_status")
        .in("id", allExamIds);

      if (!eErr && eRows) {
        eRows.forEach((e: any) => {
          if (e.approval_status === "approved") {
            validExamsMap[e.id] = true;
          }
        });
      }
    }

    // 5. Reconcile mistakes
    if (state.mistakes && state.mistakes.length > 0) {
      const originalCount = state.mistakes.length;
      // Filter out physically deleted questions
      state.mistakes = state.mistakes.filter((m) => Boolean(validQuestionsMap[m.questionId]));
      const pruned = originalCount - state.mistakes.length;
      if (pruned > 0) {
        deletedQuestionsCount += pruned;
        hasChanges = true;
      }

      // Check if admin corrected answers
      state.mistakes.forEach((m) => {
        const q = validQuestionsMap[m.questionId];
        if (q) {
          if (q.category_id && m.categoryId !== q.category_id) {
            m.categoryId = q.category_id;
            hasChanges = true;
          }
          if (q.exam_id && m.examId !== q.exam_id) {
            m.examId = q.exam_id;
            hasChanges = true;
          }
          // Answer correction self-healing: if student's wrong answer now matches new correct answer
          if (m.wrongAnswer && m.wrongAnswer === q.correct_answer && !m.isMastered) {
            m.isMastered = true;
            fixedAnswersCount += 1;
            hasChanges = true;
          }
        }
      });
    }

    // 6. Reconcile favorites
    if (state.favorites && state.favorites.length > 0) {
      const originalFavCount = state.favorites.length;
      state.favorites = state.favorites.filter((f) => Boolean(validQuestionsMap[f.questionId]));
      const prunedFav = originalFavCount - state.favorites.length;
      if (prunedFav > 0) {
        deletedQuestionsCount += prunedFav;
        hasChanges = true;
      }
    }

    // 7. Reconcile exam drafts (remove drafts of deleted or unapproved exams)
    if (state.examDrafts) {
      Object.keys(state.examDrafts).forEach((examId) => {
        if (!validExamsMap[examId]) {
          delete state.examDrafts[examId];
          deletedExamsCount += 1;
          hasChanges = true;
        }
      });
    }

    // 8. Reconcile exam results
    if (state.examResults) {
      Object.keys(state.examResults).forEach((examId) => {
        if (!validExamsMap[examId]) {
          delete state.examResults[examId];
          deletedExamsCount += 1;
          hasChanges = true;
        }
      });
    }

    // 9. If modified, persist to local storage and silently write back clean JSON to Storage!
    if (hasChanges) {
      saveLocalState(state);
      try {
        await uploadBackupToCloud();
      } catch (err) {
        console.warn("Silent cloud writeback failed during reconcile:", err);
      }
    }
  } catch (err) {
    console.error("Reconciliation error:", err);
  }

  const parts: string[] = [];
  if (deletedQuestionsCount > 0) parts.push(`清理了 ${deletedQuestionsCount} 道已下线题目`);
  if (fixedAnswersCount > 0) parts.push(`更正了 ${fixedAnswersCount} 道已修正答案错题`);
  if (deletedExamsCount > 0) parts.push(`清除了 ${deletedExamsCount} 份已下线试卷`);
  const summaryText = parts.length > 0 ? `已为您自动校对并更新存档：${parts.join("，")}` : "";

  return {
    hasChanges,
    deletedQuestionsCount,
    fixedAnswersCount,
    deletedExamsCount,
    summaryText,
  };
}

// ------------------- Clear Local Data -------------------
export function clearLocalData(scope: "all" | "mistakes" | "vocab" | "drafts") {
  const state = getLocalState();
  if (scope === "all") {
    saveLocalState({ mistakes: [], vocabulary: [], favorites: [], examResults: {}, examDrafts: {} });
  } else if (scope === "mistakes") {
    state.mistakes = [];
    saveLocalState(state);
  } else if (scope === "vocab") {
    state.vocabulary = [];
    saveLocalState(state);
  } else if (scope === "drafts") {
    state.examDrafts = {};
    saveLocalState(state);
  }
}
