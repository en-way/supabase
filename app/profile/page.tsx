"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { supabase } from "@/lib/supabase";
import {
  getLocalState,
  subscribeLocalState,
  getSanitizedLearningBackup,
  uploadBackupToCloud,
  downloadBackupFromCloud,
  fetchCloudBackupInfo,
  clearLocalData,
  reconcileLearningState,
  setLastReconcileTimestamp,
  type LocalLearningState,
  type CloudBackupInfo,
} from "@/lib/storage";
import { computeDataHash } from "@/lib/dataHash";
import type { User as AuthUser } from "@supabase/supabase-js";
import type { PasswordResetRequestRecord, UserProfile } from "@/types/user";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Spinner } from "@/components/ui/Feedback";
import { Input } from "@/components/ui/Field";
import { Modal } from "@/components/ui/Modal";
import {
  CloudUpload,
  CloudDownload,
  Trash2,
  CheckCircle2,
  AlertTriangle,
  Database,
  Edit2,
  Save,
  RotateCcw,
  KeyRound,
  AlertCircle,
} from "lucide-react";

function getErrorMessage(err: unknown, fallback: string): string {
  if (err instanceof Error && err.message) return err.message;
  if (typeof err === "object" && err !== null && "message" in err) {
    const msg = (err as { message?: unknown }).message;
    if (typeof msg === "string" && msg) return msg;
  }
  return fallback;
}

export default function ProfilePage() {
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [user, setUser] = useState<AuthUser | null>(null);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);
  const [cloudInfo, setCloudInfo] = useState<CloudBackupInfo | null>(null);
  const [localHash, setLocalHash] = useState<string>("");

  const isDataIdentical = Boolean(
    cloudInfo?.exists &&
      cloudInfo?.dataHash &&
      localHash &&
      cloudInfo.dataHash === localHash
  );

  const [isEditingNick, setIsEditingNick] = useState(false);
  const [nicknameInput, setNicknameInput] = useState("");

  const [passwordInput, setPasswordInput] = useState("");
  const [confirmPasswordInput, setConfirmPasswordInput] = useState("");
  const [pwdLoading, setPwdLoading] = useState(false);
  const [pwdNotice, setPwdNotice] = useState<{
    type: "success" | "error";
    text: string;
  } | null>(null);
  const [activePwdRequest, setActivePwdRequest] =
    useState<PasswordResetRequestRecord | null>(null);

  const [uploading, setUploading] = useState(false);
  const [downloading, setDownloading] = useState(false);
  const [reconciling, setReconciling] = useState(false);
  const [notice, setNotice] = useState<{
    type: "success" | "error";
    text: string;
  } | null>(null);

  const [showWipeModal, setShowWipeModal] = useState(false);
  const [wipeScope, setWipeScope] = useState<
    "all" | "mistakes" | "vocab" | "drafts"
  >("all");

  const mountedRef = useRef(true);
  const noticeTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const snapshotSeqRef = useRef(0);

  const showTimedNotice = useCallback(
    (type: "success" | "error", text: string, durationMs = 3000) => {
      if (!mountedRef.current) return;
      if (noticeTimerRef.current !== null) {
        clearTimeout(noticeTimerRef.current);
      }
      setNotice({ type, text });
      noticeTimerRef.current = setTimeout(() => {
        noticeTimerRef.current = null;
        if (mountedRef.current) setNotice(null);
      }, durationMs);
    },
    []
  );

  const refreshLocalSnapshot = useCallback(async () => {
    const seq = ++snapshotSeqRef.current;
    const lState = getLocalState();
    if (mountedRef.current) setLocalState(lState);
    const clean = getSanitizedLearningBackup(lState);
    const hash = await computeDataHash(clean);
    if (mountedRef.current && seq === snapshotSeqRef.current) {
      setLocalHash(hash);
    }
  }, []);

  const loadPasswordResetRequest = useCallback(async (userId: string) => {
    try {
      const { data } = await supabase
        .from("password_reset_requests")
        .select("id, status, created_at, reviewed_at, review_note")
        .eq("user_id", userId)
        .order("created_at", { ascending: false })
        .limit(1)
        .maybeSingle();
      if (mountedRef.current) {
        setActivePwdRequest((data as PasswordResetRequestRecord | null) || null);
      }
    } catch (err) {
      console.warn("Load password reset request failed:", err);
    }
  }, []);

  const loadProfileAndStats = useCallback(async () => {
    const {
      data: { session },
    } = await supabase.auth.getSession();
    const currentUser = session?.user || null;
    if (!mountedRef.current) return;
    setUser(currentUser);
    if (currentUser) {
      const { data } = await supabase
        .from("profiles")
        .select("id, username, nickname, role, created_at, last_active_at")
        .eq("id", currentUser.id)
        .maybeSingle();
      if (!mountedRef.current) return;
      if (data) {
        setProfile(data as UserProfile);
        if (data.nickname) setNicknameInput(data.nickname);
      }
      await loadPasswordResetRequest(currentUser.id);
    }
    await refreshLocalSnapshot();
    const cInfo = await fetchCloudBackupInfo();
    if (mountedRef.current) setCloudInfo(cInfo);
  }, [loadPasswordResetRequest, refreshLocalSnapshot]);

  useEffect(() => {
    mountedRef.current = true;
    loadProfileAndStats();
    const unsubscribe = subscribeLocalState(() => {
      refreshLocalSnapshot();
    });
    return () => {
      mountedRef.current = false;
      unsubscribe();
      if (noticeTimerRef.current !== null) {
        clearTimeout(noticeTimerRef.current);
        noticeTimerRef.current = null;
      }
    };
  }, [loadProfileAndStats, refreshLocalSnapshot]);

  const handlePasswordAction = async (e: React.FormEvent) => {
    e.preventDefault();
    setPwdNotice(null);

    if (passwordInput.length < 6) {
      setPwdNotice({ type: "error", text: "新密码长度至少需要 6 位" });
      return;
    }
    if (passwordInput !== confirmPasswordInput) {
      setPwdNotice({ type: "error", text: "两次输入的新密码不一致" });
      return;
    }

    setPwdLoading(true);
    try {
      if (profile?.role === "super_admin") {
        const { error } = await supabase.auth.updateUser({
          password: passwordInput,
        });
        if (error) throw error;
        setPwdNotice({
          type: "success",
          text: "超级管理员密码修改成功，即刻生效！",
        });
        setPasswordInput("");
        setConfirmPasswordInput("");
      } else {
        const { data, error } = await supabase.rpc(
          "submit_password_reset_request",
          {
            new_plain_password: passwordInput,
          }
        );
        if (error) throw error;
        setPwdNotice({
          type: "success",
          text:
            data?.message ||
            "已成功提交改密申请！请等待超级管理员审批，审批通过后生效。",
        });
        setPasswordInput("");
        setConfirmPasswordInput("");
        if (user) await loadPasswordResetRequest(user.id);
      }
    } catch (err: unknown) {
      setPwdNotice({
        type: "error",
        text: getErrorMessage(err, "操作失败，请重试"),
      });
    } finally {
      setPwdLoading(false);
    }
  };

  const handleCancelPasswordRequest = async () => {
    if (!window.confirm("确定要撤回当前的改密申请吗？")) return;
    setPwdLoading(true);
    setPwdNotice(null);
    try {
      const { error } = await supabase.rpc("cancel_own_password_reset_request");
      if (error) throw error;
      setPwdNotice({ type: "success", text: "已成功撤销改密申请。" });
      if (user) await loadPasswordResetRequest(user.id);
    } catch (err: unknown) {
      setPwdNotice({
        type: "error",
        text: getErrorMessage(err, "撤销失败"),
      });
    } finally {
      setPwdLoading(false);
    }
  };

  const handleUpdateNickname = async () => {
    if (!profile || !nicknameInput.trim()) return;
    const nextNick = nicknameInput.trim();
    const { error } = await supabase
      .from("profiles")
      .update({ nickname: nextNick, updated_at: new Date().toISOString() })
      .eq("id", profile.id);
    if (error) {
      showTimedNotice("error", `修改昵称失败: ${error.message}`, 3500);
      return;
    }
    setProfile((prev) => (prev ? { ...prev, nickname: nextNick } : prev));
    setIsEditingNick(false);
    window.dispatchEvent(new Event("enway_profile_updated"));
    showTimedNotice("success", "昵称修改成功", 2500);
  };

  const handleUploadBackup = async () => {
    if (isDataIdentical) {
      showTimedNotice(
        "success",
        "本地研习数据与云端存档 100% 一致，无需重复上传，已为您节省云端配额！",
        3000
      );
      return;
    }
    if (
      !window.confirm(
        "备份到云端将使用当前设备的做题数据【完全覆盖】云端的历史存档快照。确定继续上传覆盖吗？"
      )
    ) {
      return;
    }
    setUploading(true);
    setNotice(null);
    const res = await uploadBackupToCloud();
    if (res.success) {
      if (res.isIdentical) {
        showTimedNotice(
          "success",
          "本地数据与云端存档完全一致，无需重复上传，已为您节省云端配额！",
          3000
        );
      } else {
        showTimedNotice("success", "本地数据已成功打包并覆盖备份至云端！", 3000);
      }
      await loadProfileAndStats();
    } else {
      showTimedNotice("error", res.error || "上传备份失败", 3500);
    }
    if (mountedRef.current) setUploading(false);
  };

  const handleDownloadBackup = async () => {
    if (isDataIdentical) {
      showTimedNotice("success", "本地数据与云端存档完全一致，无需重复恢复！", 3000);
      return;
    }
    if (
      !window.confirm(
        "从云端恢复将直接【完全覆盖】当前设备的本地数据。确定继续吗？"
      )
    ) {
      return;
    }
    setDownloading(true);
    setNotice(null);
    const res = await downloadBackupFromCloud();
    if (res.success) {
      if (res.isIdentical) {
        showTimedNotice(
          "success",
          "云端存档内容与当前本地数据完全一致，无需重复覆盖！",
          3000
        );
      } else {
        const recon = await reconcileLearningState();
        if (recon.completed && user?.id) {
          setLastReconcileTimestamp(user.id, Date.now());
        }
        if (!recon.completed) {
          showTimedNotice(
            "success",
            `已从云端对象存储还原至本地（校对未完成，本地记录已保留：${recon.summaryText}）`,
            4000
          );
        } else if (recon.hasChanges) {
          showTimedNotice(
            "success",
            `已从云端对象存储还原并完成校对：${recon.summaryText}`,
            4000
          );
        } else {
          showTimedNotice(
            "success",
            "已成功从云端对象存储拉取最新快照并还原至本地！",
            3500
          );
        }
      }
      await loadProfileAndStats();
    } else {
      showTimedNotice("error", res.error || "下载恢复失败", 3500);
    }
    if (mountedRef.current) setDownloading(false);
  };

  const handleReconcile = async () => {
    setReconciling(true);
    setNotice(null);
    try {
      const recon = await reconcileLearningState();
      if (recon.completed && user?.id) {
        setLastReconcileTimestamp(user.id, Date.now());
      }
      await refreshLocalSnapshot();
      const cInfo = await fetchCloudBackupInfo();
      if (mountedRef.current) setCloudInfo(cInfo);
      if (!recon.completed) {
        showTimedNotice(
          "error",
          recon.summaryText || "校对未完成，已安全保留本地学习记录",
          3500
        );
      } else if (recon.hasChanges) {
        showTimedNotice("success", recon.summaryText, 3500);
      } else {
        showTimedNotice(
          "success",
          "存档数据完美吻合，无任何已下架题目或待修正项！",
          3500
        );
      }
    } catch (e: unknown) {
      showTimedNotice(
        "error",
        `校对失败: ${getErrorMessage(e, "未知错误")}`,
        3500
      );
    } finally {
      if (mountedRef.current) setReconciling(false);
    }
  };

  const handleConfirmClear = async () => {
    clearLocalData(wipeScope);
    await refreshLocalSnapshot();
    setShowWipeModal(false);
    showTimedNotice("success", "所选本地数据已彻底清除！", 2500);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 sm:space-y-8 animate-in fade-in duration-150">
      {notice && (
        <div
          className={`p-4 rounded-2xl flex items-center gap-2.5 text-sm font-semibold border animate-in fade-in duration-150 ${
            notice.type === "success"
              ? "bg-success-soft border-success/30 text-success"
              : "bg-danger-soft border-danger/30 text-danger"
          }`}
        >
          {notice.type === "success" ? (
            <CheckCircle2 className="w-5 h-5 shrink-0" />
          ) : (
            <AlertTriangle className="w-5 h-5 shrink-0" />
          )}
          <span>{notice.text}</span>
        </div>
      )}

      {/* User Info Card */}
      <Card className="p-6 sm:p-7 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-center gap-4">
          <div className="w-14 h-14 rounded-2xl bg-primary text-primary-fg flex items-center justify-center text-xl font-bold shadow-1 shrink-0">
            {profile?.nickname?.[0] || profile?.username?.[0] || "U"}
          </div>
          <div>
            <div className="flex items-center gap-2">
              {!isEditingNick ? (
                <>
                  <h2 className="text-lg font-bold text-fg">
                    {profile?.nickname || profile?.username}
                  </h2>
                  <button
                    type="button"
                    onClick={() => setIsEditingNick(true)}
                    className="text-fg-subtle hover:text-fg p-1 rounded-md transition-colors"
                    title="修改昵称"
                    aria-label="修改昵称"
                  >
                    <Edit2 className="w-3.5 h-3.5" />
                  </button>
                </>
              ) : (
                <div className="flex items-center gap-1.5">
                  <Input
                    compact
                    type="text"
                    value={nicknameInput}
                    onChange={(e) => setNicknameInput(e.target.value)}
                    className="h-8 text-xs font-bold w-36"
                  />
                  <Button size="sm" onClick={handleUpdateNickname}>
                    <Save className="w-3.5 h-3.5" />
                  </Button>
                  <Button
                    variant="secondary"
                    size="sm"
                    onClick={() => setIsEditingNick(false)}
                  >
                    取消
                  </Button>
                </div>
              )}
            </div>

            <div className="flex items-center gap-2 mt-1">
              <span className="text-xs text-fg-muted font-mono">
                账号/学号：<strong className="text-fg">{profile?.username}</strong>
              </span>
              <Badge tone={profile?.role === "super_admin" ? "info" : "neutral"}>
                {profile?.role === "super_admin"
                  ? "超管"
                  : profile?.role === "admin"
                    ? "管理员"
                    : "学员"}
              </Badge>
            </div>
          </div>
        </div>

        <div className="text-xs text-fg-subtle font-mono tabular-nums">
          注册时间：
          {profile?.created_at
            ? new Date(profile.created_at).toLocaleDateString()
            : "--"}
        </div>
      </Card>

      {/* Local Data Stats */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <Card className="p-5 text-center">
          <span className="text-xs text-fg-subtle block font-medium">待复习错题</span>
          <span className="text-2xl font-bold font-mono tabular-nums text-fg mt-1 block">
            {localState?.mistakes.filter((m) => !m.isMastered).length || 0}
          </span>
          <span className="text-[10px] text-fg-subtle">
            已攻克：{localState?.mistakes.filter((m) => m.isMastered).length || 0} 道
          </span>
        </Card>
        <Card className="p-5 text-center">
          <span className="text-xs text-fg-subtle block font-medium">已存生词</span>
          <span className="text-2xl font-bold font-mono tabular-nums text-fg mt-1 block">
            {localState?.vocabulary.length || 0}
          </span>
          <span className="text-[10px] text-fg-subtle">真题阅读双击收录</span>
        </Card>
        <Card className="p-5 text-center">
          <span className="text-xs text-fg-subtle block font-medium">收藏题目</span>
          <span className="text-2xl font-bold font-mono tabular-nums text-fg mt-1 block">
            {localState?.favorites.length || 0}
          </span>
          <span className="text-[10px] text-fg-subtle">含专属做题心得</span>
        </Card>
        <Card className="p-5 text-center">
          <span className="text-xs text-fg-subtle block font-medium">已测模考</span>
          <span className="text-2xl font-bold font-mono tabular-nums text-primary mt-1 block">
            {Object.keys(localState?.examResults || {}).length}
          </span>
          <span className="text-[10px] text-fg-subtle">客观题精准计分</span>
        </Card>
      </div>

      {/* Cloud Backup & Local-First Data Sovereignty Panel */}
      <Card className="p-6 sm:p-8 space-y-6">
        <div className="flex items-center gap-3 pb-4 border-b border-border">
          <div className="w-10 h-10 rounded-xl bg-surface-2 border border-border text-primary flex items-center justify-center shrink-0">
            <Database className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-fg">
              学员研习档案与多端同步中心
            </h3>
            <p className="text-xs text-fg-subtle mt-0.5">
              研习数据本机即时留存 · 一键 Gzip 压缩归档至专属云端档案空间 · 跨设备随心续学
            </p>
          </div>
        </div>

        <div className="p-4 rounded-xl bg-surface-2/80 border border-border flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-xs font-bold text-fg">云端研习档案状态：</span>
              <Badge
                tone={
                  isDataIdentical
                    ? "success"
                    : cloudInfo?.exists
                      ? "warning"
                      : cloudInfo?.error
                        ? "danger"
                        : "neutral"
                }
              >
                {isDataIdentical
                  ? "本地与云端已 100% 同步"
                  : cloudInfo?.exists
                    ? "本地存在未归档变动"
                    : cloudInfo?.error
                      ? "云端状态获取异常"
                      : "尚未创建云端归档"}
              </Badge>
            </div>
            {cloudInfo?.exists ? (
              <p className="text-xs text-fg-muted">
                上次归档：
                {cloudInfo.updatedAt
                  ? new Date(cloudInfo.updatedAt).toLocaleString()
                  : "--"}{" "}
                · 已归纳 {cloudInfo.summary?.mistakesCount} 道错题、
                {cloudInfo.summary?.vocabCount} 个生词、
                {cloudInfo.summary?.examsCount} 份模考
                {isDataIdentical && (
                  <span className="ml-1 text-success font-semibold">
                    （数据指纹一致，已启用防滥用拦截）
                  </span>
                )}
              </p>
            ) : cloudInfo?.error ? (
              <p className="text-xs text-danger">
                获取云端归档状态失败：{cloudInfo.error}，请稍后刷新重试。
              </p>
            ) : (
              <p className="text-xs text-fg-subtle">
                建议阶段性点击“备份到云端”，研习进度将安全归档存入个人专属云空间。
              </p>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2 shrink-0">
            <Button
              size="sm"
              onClick={handleUploadBackup}
              disabled={uploading || isDataIdentical}
              title={
                isDataIdentical
                  ? "本地研习数据与云端存档 100% 一致"
                  : "将当前本地研习记录打包并安全覆盖备份至云端"
              }
            >
              <CloudUpload className="w-3.5 h-3.5" />
              <span>
                {uploading
                  ? "正在归档..."
                  : isDataIdentical
                    ? "云端已是最新"
                    : "备份到云端"}
              </span>
            </Button>

            <Button
              variant="secondary"
              size="sm"
              onClick={handleDownloadBackup}
              disabled={downloading || !cloudInfo?.exists || isDataIdentical}
            >
              <CloudDownload className="w-3.5 h-3.5" />
              <span>
                {downloading
                  ? "正在恢复..."
                  : isDataIdentical
                    ? "本地已是最新"
                    : "从云端恢复"}
              </span>
            </Button>

            <Button
              variant="secondary"
              size="sm"
              onClick={handleReconcile}
              disabled={reconciling}
              title="比对题库删改，自动清理下架试题并自愈答案"
            >
              <RotateCcw
                className={`w-3.5 h-3.5 ${reconciling ? "animate-spin" : ""}`}
              />
              <span>{reconciling ? "校对中..." : "校对云端题库"}</span>
            </Button>
          </div>
        </div>

        <div className="pt-4 border-t border-border flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <span className="text-xs font-bold text-fg block">清除本机临时缓存</span>
            <span className="text-[11px] text-fg-subtle">
              用于公共阅览设备退出或重置本机真题研习记录（建议操作前先同步归档至云端）
            </span>
          </div>

          <Button
            variant="danger"
            size="sm"
            onClick={() => setShowWipeModal(true)}
            className="w-full sm:w-auto"
          >
            <Trash2 className="w-4 h-4" />
            <span>清除本地数据</span>
          </Button>
        </div>
      </Card>

      {/* Password Management & Account Security Panel */}
      <Card className="p-6 sm:p-8 space-y-6">
        <div className="flex items-center gap-3 pb-4 border-b border-border">
          <div className="w-10 h-10 rounded-xl bg-surface-2 border border-border text-primary flex items-center justify-center shrink-0">
            <KeyRound className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-fg">
              {profile?.role === "super_admin"
                ? "超级管理员密码安全维护"
                : "账号密码安全管理"}
            </h3>
            <p className="text-xs text-fg-subtle mt-0.5">
              {profile?.role === "super_admin"
                ? "最高权限专属：密码即时修改生效，无需任何第三方审批"
                : "自主申请 · 超管审批 · 保护考研做题记录防篡改"}
            </p>
          </div>
        </div>

        {pwdNotice && (
          <div
            className={`p-3.5 rounded-xl text-xs flex items-start gap-2.5 border ${
              pwdNotice.type === "success"
                ? "bg-success-soft border-success/30 text-success"
                : "bg-danger-soft border-danger/30 text-danger"
            }`}
          >
            {pwdNotice.type === "success" ? (
              <CheckCircle2 className="w-4 h-4 shrink-0 mt-0.5" />
            ) : (
              <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />
            )}
            <span className="flex-1 font-medium">{pwdNotice.text}</span>
          </div>
        )}

        {profile?.role === "super_admin" ? (
          <div className="space-y-4">
            <div className="p-3.5 rounded-xl bg-info-soft border border-info/30 text-xs text-fg leading-relaxed">
              您当前以<strong>超级管理员</strong>
              身份登录。出于系统主权隔离，您的密码修改即刻生效，无需审批；任何他人（包括普通管理员）亦无权在此强行修改任何人的密码。
            </div>

            <form onSubmit={handlePasswordAction} className="max-w-md space-y-3.5">
              <div>
                <label className="block text-xs font-medium text-fg mb-1">
                  设置超级管理员新密码
                </label>
                <Input
                  compact
                  type="password"
                  required
                  value={passwordInput}
                  onChange={(e) => setPasswordInput(e.target.value)}
                  placeholder="至少 6 位新密码"
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-fg mb-1">
                  确认超级管理员新密码
                </label>
                <Input
                  compact
                  type="password"
                  required
                  value={confirmPasswordInput}
                  onChange={(e) => setConfirmPasswordInput(e.target.value)}
                  placeholder="再次输入新密码"
                />
              </div>

              <Button type="submit" size="sm" disabled={pwdLoading}>
                {pwdLoading && <Spinner className="w-3.5 h-3.5 text-primary-fg" />}
                <span>{pwdLoading ? "正在更新..." : "即刻更新密码"}</span>
              </Button>
            </form>
          </div>
        ) : (
          <div className="space-y-4">
            {activePwdRequest?.status === "pending" ? (
              <div className="p-4 rounded-xl bg-warning-soft border border-warning/30 space-y-3">
                <div className="flex items-center justify-between gap-2 flex-wrap">
                  <div className="flex items-center gap-2">
                    <span className="relative flex h-2.5 w-2.5">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-warning opacity-75" />
                      <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-warning" />
                    </span>
                    <span className="text-xs font-bold text-fg">
                      改密申请待审批中
                    </span>
                  </div>
                  <span className="text-[11px] text-warning font-mono tabular-nums">
                    提交于 {new Date(activePwdRequest.created_at).toLocaleString()}
                  </span>
                </div>
                <p className="text-xs text-fg-muted leading-relaxed">
                  您的改密申请已提交并生成不可逆安全密文存入审批队列。请联系超级管理员在后台审核通过；通过后新密码将正式生效，原密码失效。在此之前，原密码仍可正常使用。
                </p>
                <Button
                  type="button"
                  variant="secondary"
                  size="sm"
                  onClick={handleCancelPasswordRequest}
                  disabled={pwdLoading}
                >
                  {pwdLoading ? "正在撤回..." : "撤回此申请"}
                </Button>
              </div>
            ) : (
              <div className="space-y-4">
                {activePwdRequest?.status === "rejected" && (
                  <div className="p-3 rounded-xl bg-danger-soft border border-danger/30 text-xs text-danger">
                    您于{" "}
                    {new Date(
                      activePwdRequest.reviewed_at || activePwdRequest.created_at
                    ).toLocaleDateString()}{" "}
                    提交的上一条改密申请已被超级管理员驳回。原因：
                    {activePwdRequest.review_note || "管理员驳回"}
                    。如需修改，请重新提交申请。
                  </div>
                )}
                {activePwdRequest?.status === "approved" && (
                  <div className="p-3 rounded-xl bg-success-soft border border-success/30 text-xs text-success">
                    您最近一次改密申请已于{" "}
                    {new Date(
                      activePwdRequest.reviewed_at || activePwdRequest.created_at
                    ).toLocaleDateString()}{" "}
                    审核通过并已生效。
                  </div>
                )}

                <div className="p-3.5 rounded-xl bg-surface-2 border border-border text-xs text-fg-muted leading-relaxed">
                  为保障考研学员数据安全，系统实行<strong>自主申请审批制</strong>
                  。任何人员（包括超级管理员）均无法直接在后台强行修改您的密码。提交期望密码后，将由超级管理员审批通过后生效。
                </div>

                <form onSubmit={handlePasswordAction} className="max-w-md space-y-3.5">
                  <div>
                    <label className="block text-xs font-medium text-fg mb-1">
                      期望设置的新密码
                    </label>
                    <Input
                      compact
                      type="password"
                      required
                      value={passwordInput}
                      onChange={(e) => setPasswordInput(e.target.value)}
                      placeholder="至少 6 位新密码"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-medium text-fg mb-1">
                      确认期望新密码
                    </label>
                    <Input
                      compact
                      type="password"
                      required
                      value={confirmPasswordInput}
                      onChange={(e) => setConfirmPasswordInput(e.target.value)}
                      placeholder="再次输入新密码"
                    />
                  </div>

                  <Button type="submit" size="sm" disabled={pwdLoading}>
                    {pwdLoading && (
                      <Spinner className="w-3.5 h-3.5 text-primary-fg" />
                    )}
                    <span>{pwdLoading ? "正在提交..." : "提交改密申请"}</span>
                  </Button>
                </form>
              </div>
            )}
          </div>
        )}
      </Card>

      <Modal
        open={showWipeModal}
        onClose={() => setShowWipeModal(false)}
        title="危险操作：清除本地数据"
      >
        <div className="space-y-4">
          <div className="flex items-start gap-2.5 text-danger text-xs leading-relaxed">
            <AlertTriangle className="w-5 h-5 shrink-0 mt-0.5" />
            <span>
              清除后本地存储的相关学习记录将被永久抹除。如果有重要进度，请确保已经点击“备份到云端”。
            </span>
          </div>

          <div className="space-y-2 bg-surface-2 p-3 rounded-xl border border-border text-xs text-fg">
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                name="wipeScope"
                checked={wipeScope === "all"}
                onChange={() => setWipeScope("all")}
              />
              <span className="font-bold text-danger">
                彻底清空全部本地数据（恢复出厂全新状态）
              </span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                name="wipeScope"
                checked={wipeScope === "mistakes"}
                onChange={() => setWipeScope("mistakes")}
              />
              <span>仅清空【错题本】</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                name="wipeScope"
                checked={wipeScope === "vocab"}
                onChange={() => setWipeScope("vocab")}
              />
              <span>仅清空【生词本】</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                name="wipeScope"
                checked={wipeScope === "drafts"}
                onChange={() => setWipeScope("drafts")}
              />
              <span>仅清空【未交卷模考草稿】</span>
            </label>
          </div>

          <div className="flex justify-end gap-2 pt-2">
            <Button
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => setShowWipeModal(false)}
            >
              取消
            </Button>
            <Button type="button" variant="danger" size="sm" onClick={handleConfirmClear}>
              确认清除
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
}
