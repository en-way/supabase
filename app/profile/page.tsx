"use client";

import { useState, useEffect } from "react";
import { supabase } from "@/lib/supabase";
import { 
  getLocalState, 
  getSanitizedLearningBackup,
  uploadBackupToCloud, 
  downloadBackupFromCloud, 
  fetchCloudBackupInfo, 
  clearLocalData, 
  reconcileLearningState,
  LocalLearningState 
} from "@/lib/storage";
import { computeDataHash } from "@/lib/dataHash";
import { 
  User, 
  CloudUpload, 
  CloudDownload, 
  Trash2, 
  CheckCircle2, 
  AlertTriangle, 
  Clock, 
  Database, 
  Shield, 
  Edit2, 
  Save, 
  RotateCcw,
  Sparkles,
  KeyRound,
  AlertCircle,
  ShieldCheck
} from "lucide-react";

export default function ProfilePage() {
  const [profile, setProfile] = useState<any>(null);
  const [user, setUser] = useState<any>(null);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);
  const [cloudInfo, setCloudInfo] = useState<any>(null);
  const [localHash, setLocalHash] = useState<string>("");

  const isDataIdentical = Boolean(
    cloudInfo?.exists &&
    cloudInfo?.dataHash &&
    localHash &&
    cloudInfo.dataHash === localHash
  );

  // Edit nickname
  const [isEditingNick, setIsEditingNick] = useState(false);
  const [nicknameInput, setNicknameInput] = useState("");

  // Password management state
  const [passwordInput, setPasswordInput] = useState("");
  const [confirmPasswordInput, setConfirmPasswordInput] = useState("");
  const [pwdLoading, setPwdLoading] = useState(false);
  const [pwdNotice, setPwdNotice] = useState<{ type: "success" | "error"; text: string } | null>(null);
  const [activePwdRequest, setActivePwdRequest] = useState<any>(null);

  // Loading states
  const [uploading, setUploading] = useState(false);
  const [downloading, setDownloading] = useState(false);
  const [notice, setNotice] = useState<{ type: "success" | "error"; text: string } | null>(null);

  // Wipe modal
  const [showWipeModal, setShowWipeModal] = useState(false);
  const [wipeScope, setWipeScope] = useState<"all" | "mistakes" | "vocab" | "drafts">("all");

  useEffect(() => {
    loadProfileAndStats();
  }, []);

  const loadPasswordResetRequest = async (userId: string) => {
    try {
      const { data } = await supabase
        .from("password_reset_requests")
        .select("id, status, created_at, reviewed_at, review_note")
        .eq("user_id", userId)
        .order("created_at", { ascending: false })
        .limit(1)
        .maybeSingle();
      setActivePwdRequest(data || null);
    } catch (err) {
      console.warn("Load password reset request failed:", err);
    }
  };

  const loadProfileAndStats = async () => {
    const { data: { user } } = await supabase.auth.getUser();
    setUser(user);
    if (user) {
      const { data } = await supabase
        .from("profiles")
        .select("id, username, nickname, role, created_at, last_active_at")
        .eq("id", user.id)
        .maybeSingle();
      if (data) {
        setProfile(data);
        if (data.nickname) setNicknameInput(data.nickname);
      }
      await loadPasswordResetRequest(user.id);
    }
    const lState = getLocalState();
    setLocalState(lState);
    if (lState) {
      const clean = getSanitizedLearningBackup(lState);
      const hash = await computeDataHash(clean);
      setLocalHash(hash);
    }
    const cInfo = await fetchCloudBackupInfo();
    setCloudInfo(cInfo);
  };

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
        // Super admin direct password update via GoTrue auth
        const { error } = await supabase.auth.updateUser({ password: passwordInput });
        if (error) throw error;
        setPwdNotice({ type: "success", text: "👑 超级管理员密码修改成功，即刻生效！" });
        setPasswordInput("");
        setConfirmPasswordInput("");
      } else {
        // Student / Admin request submission
        const { data, error } = await supabase.rpc("submit_password_reset_request", {
          new_plain_password: passwordInput,
        });
        if (error) throw error;
        setPwdNotice({
          type: "success",
          text: data?.message || "已成功提交改密申请！请等待超级管理员审批，审批通过后生效。",
        });
        setPasswordInput("");
        setConfirmPasswordInput("");
        if (user) await loadPasswordResetRequest(user.id);
      }
    } catch (err: any) {
      setPwdNotice({ type: "error", text: err.message || "操作失败，请重试" });
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
    } catch (err: any) {
      setPwdNotice({ type: "error", text: err.message || "撤销失败" });
    } finally {
      setPwdLoading(false);
    }
  };

  const handleUpdateNickname = async () => {
    if (!profile || !nicknameInput.trim()) return;
    const { error } = await supabase
      .from("profiles")
      .update({ nickname: nicknameInput.trim(), updated_at: new Date().toISOString() })
      .eq("id", profile.id);
    if (!error) {
      setProfile((prev: any) => ({ ...prev, nickname: nicknameInput.trim() }));
      setIsEditingNick(false);
      window.dispatchEvent(new Event("enway_profile_updated"));
      setNotice({ type: "success", text: "昵称修改成功" });
      setTimeout(() => setNotice(null), 2500);
    }
  };

  const handleUploadBackup = async () => {
    if (isDataIdentical) {
      setNotice({ type: "success", text: "🛡️ 本地研习数据与云端存档 100% 一致，无需重复上传，已为您节省云端配额！" });
      setTimeout(() => setNotice(null), 3000);
      return;
    }
    if (!window.confirm("⚠️ 备份到云端将使用当前设备的做题数据【完全覆盖】云端的历史存档快照。确定继续上传覆盖吗？")) {
      return;
    }
    setUploading(true);
    setNotice(null);
    const res = await uploadBackupToCloud();
    if (res.success) {
      if (res.isIdentical) {
        setNotice({ type: "success", text: "🛡️ 本地数据与云端存档完全一致，无需重复上传，已为您节省云端配额！" });
      } else {
        setNotice({ type: "success", text: "🎉 本地数据已成功打包并覆盖备份至云端！" });
      }
      await loadProfileAndStats();
    } else {
      setNotice({ type: "error", text: res.error || "上传备份失败" });
    }
    setUploading(false);
    setTimeout(() => setNotice(null), 3000);
  };

  const [reconciling, setReconciling] = useState(false);

  const handleDownloadBackup = async () => {
    if (isDataIdentical) {
      setNotice({ type: "success", text: "🛡️ 本地数据与云端存档完全一致，无需重复恢复！" });
      setTimeout(() => setNotice(null), 3000);
      return;
    }
    if (!window.confirm("⚠️ 从云端恢复将直接【完全覆盖】当前设备的本地数据。确定继续吗？")) {
      return;
    }
    setDownloading(true);
    setNotice(null);
    const res = await downloadBackupFromCloud();
    if (res.success) {
      if (res.isIdentical) {
        setNotice({ type: "success", text: "🛡️ 云端存档内容与当前本地数据完全一致，无需重复覆盖！" });
      } else {
        // Automatically run reconciliation after restoring from Storage
        const recon = await reconcileLearningState();
        if (recon.hasChanges) {
          setNotice({ type: "success", text: `🎉 已从云端对象存储还原并完成校对：${recon.summaryText}` });
        } else {
          setNotice({ type: "success", text: "🎉 已成功从云端对象存储拉取最新快照并还原至本地！" });
        }
      }
      await loadProfileAndStats();
    } else {
      setNotice({ type: "error", text: res.error || "下载恢复失败" });
    }
    setDownloading(false);
    setTimeout(() => setNotice(null), 3500);
  };

  const handleReconcile = async () => {
    setReconciling(true);
    setNotice(null);
    try {
      const recon = await reconcileLearningState();
      setLocalState(getLocalState());
      if (recon.hasChanges) {
        setNotice({ type: "success", text: recon.summaryText });
      } else {
        setNotice({ type: "success", text: "✅ 存档数据完美吻合，无任何已下架题目或待修正项！" });
      }
    } catch (e: any) {
      setNotice({ type: "error", text: `校对失败: ${e.message}` });
    } finally {
      setReconciling(false);
      setTimeout(() => setNotice(null), 3500);
    }
  };

  const handleConfirmClear = () => {
    clearLocalData(wipeScope);
    setLocalState(getLocalState());
    setShowWipeModal(false);
    setNotice({ type: "success", text: "所选本地数据已彻底清除！" });
    setTimeout(() => setNotice(null), 2500);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in duration-150">
      {/* Notice Banner */}
      {notice && (
        <div className={`p-4 rounded-2xl flex items-center space-x-2 text-sm font-semibold shadow-sm animate-in fade-in duration-150 ${
          notice.type === "success" 
            ? "bg-emerald-50 border border-emerald-200 text-emerald-800" 
            : "bg-rose-50 border border-rose-200 text-rose-800"
        }`}>
          {notice.type === "success" ? <CheckCircle2 className="w-5 h-5 text-emerald-600" /> : <AlertTriangle className="w-5 h-5 text-rose-600" />}
          <span>{notice.text}</span>
        </div>
      )}

      {/* User Info Card */}
      <div className="bg-white dark:bg-[#11131a] p-6 sm:p-7 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card flex flex-col sm:flex-row sm:items-center justify-between gap-4 transition-colors duration-300">
        <div className="flex items-center space-x-4">
          <div className="w-14 h-14 rounded-2xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] flex items-center justify-center text-xl font-bold shadow-subtle dark:shadow-glow-cyan">
            {profile?.nickname?.[0] || profile?.username?.[0] || "U"}
          </div>
          <div>
            <div className="flex items-center space-x-2">
              {!isEditingNick ? (
                <>
                  <h2 className="text-lg font-bold text-stone-900 dark:text-zinc-100">
                    {profile?.nickname || profile?.username}
                  </h2>
                  <button
                    onClick={() => setIsEditingNick(true)}
                    className="text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-300 p-1 rounded-md transition-colors"
                    title="修改昵称"
                  >
                    <Edit2 className="w-3.5 h-3.5" />
                  </button>
                </>
              ) : (
                <div className="flex items-center space-x-1.5">
                  <input
                    type="text"
                    value={nicknameInput}
                    onChange={(e) => setNicknameInput(e.target.value)}
                    className="text-xs font-bold border border-stone-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 rounded-lg px-2.5 py-1 text-stone-900 dark:text-zinc-100 focus:outline-none focus:ring-1 focus:ring-emerald-600 dark:focus:ring-cyan-500"
                  />
                  <button
                    onClick={handleUpdateNickname}
                    className="p-1.5 bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] rounded-lg text-xs"
                  >
                    <Save className="w-3.5 h-3.5" />
                  </button>
                  <button
                    onClick={() => setIsEditingNick(false)}
                    className="p-1.5 bg-stone-100 dark:bg-zinc-800 text-stone-600 dark:text-zinc-400 rounded-lg text-xs"
                  >
                    取消
                  </button>
                </div>
              )}
            </div>

            <div className="flex items-center space-x-2 mt-1">
              <span className="text-xs text-stone-500 dark:text-zinc-400 font-mono">
                账号/学号: <strong className="text-stone-800 dark:text-zinc-200">{profile?.username}</strong>
              </span>
              <span className={`px-2 py-0.5 rounded-md text-[10px] font-bold font-mono ${
                profile?.role === "super_admin" 
                  ? "bg-purple-50 dark:bg-purple-950/50 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-500/30" 
                  : profile?.role === "admin"
                  ? "bg-stone-100 dark:bg-zinc-800 text-stone-800 dark:text-zinc-200 border border-stone-200 dark:border-zinc-700"
                  : "bg-stone-100 dark:bg-zinc-800 text-stone-600 dark:text-zinc-400 border border-stone-200 dark:border-zinc-700"
              }`}>
                {profile?.role === "super_admin" 
                  ? "👑 超管" 
                  : profile?.role === "admin" 
                  ? "🛡️ 管理员" 
                  : "🎓 学员"}
              </span>
            </div>
          </div>
        </div>

        <div className="text-xs text-stone-400 dark:text-zinc-500 font-mono">
          注册时间: {profile ? new Date(profile.created_at).toLocaleDateString() : "--"}
        </div>
      </div>

      {/* Local Data Stats (4 Minimalist Stat Cards) */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="bg-white dark:bg-[#11131a] p-5 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card text-center transition-colors duration-300">
          <span className="text-xs text-stone-400 dark:text-zinc-500 block font-medium">待复习错题</span>
          <span className="text-2xl font-bold text-stone-900 dark:text-cyber-300 mt-1 block">
            {localState?.mistakes.filter(m => !m.isMastered).length || 0}
          </span>
          <span className="text-[10px] text-stone-400 dark:text-zinc-500">已攻克: {localState?.mistakes.filter(m => m.isMastered).length || 0} 道</span>
        </div>
        <div className="bg-white dark:bg-[#11131a] p-5 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card text-center transition-colors duration-300">
          <span className="text-xs text-stone-400 dark:text-zinc-500 block font-medium">已存生词</span>
          <span className="text-2xl font-bold text-stone-900 dark:text-cyber-300 mt-1 block">
            {localState?.vocabulary.length || 0}
          </span>
          <span className="text-[10px] text-stone-400 dark:text-zinc-500">真题阅读双击收录</span>
        </div>
        <div className="bg-white dark:bg-[#11131a] p-5 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card text-center transition-colors duration-300">
          <span className="text-xs text-stone-400 dark:text-zinc-500 block font-medium">收藏题目</span>
          <span className="text-2xl font-bold text-stone-900 dark:text-cyber-300 mt-1 block">
            {localState?.favorites.length || 0}
          </span>
          <span className="text-[10px] text-stone-400 dark:text-zinc-500">含专属做题心得</span>
        </div>
        <div className="bg-white dark:bg-[#11131a] p-5 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card text-center transition-colors duration-300">
          <span className="text-xs text-stone-400 dark:text-zinc-500 block font-medium">已测模考</span>
          <span className="text-2xl font-bold text-stone-900 dark:text-cyber-300 mt-1 block">
            {Object.keys(localState?.examResults || {}).length}
          </span>
          <span className="text-[10px] text-stone-400 dark:text-zinc-500">百分制自动核算</span>
        </div>
      </div>

      {/* Cloud Backup & Local-First Data Sovereignty Panel */}
      <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-6 sm:p-8 shadow-card space-y-6 transition-colors duration-300">
        <div className="flex items-center space-x-3 pb-4 border-b border-stone-100 dark:border-zinc-800">
          <div className="w-10 h-10 rounded-xl bg-stone-100 dark:bg-zinc-800 text-stone-800 dark:text-cyber-400 flex items-center justify-center font-bold">
            <Database className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-stone-900 dark:text-zinc-100">
              学员研习档案与多端同步中心
            </h3>
            <p className="text-xs text-stone-400 dark:text-zinc-500 mt-0.5">
              研习数据本机即时留存 · 一键加密归档至专属云端档案空间 · 跨设备随心续学
            </p>
          </div>
        </div>

        {/* Cloud Status Snapshot */}
        <div className="p-4 rounded-xl bg-stone-50/80 dark:bg-zinc-900/80 border border-black/[0.04] dark:border-cyan-500/20 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center space-x-2">
              <span className="text-xs font-bold text-stone-900 dark:text-zinc-100">云端研习档案状态:</span>
              <span className={`px-2 py-0.5 rounded-md text-[10px] font-bold ${
                isDataIdentical
                  ? "bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border border-emerald-200/80 dark:border-emerald-500/30"
                  : cloudInfo?.exists
                  ? "bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 border border-amber-200/80 dark:border-amber-500/30"
                  : "bg-stone-200 dark:bg-zinc-800 text-stone-600 dark:text-zinc-400"
              }`}>
                {isDataIdentical
                  ? "● 本地与云端已 100% 同步"
                  : cloudInfo?.exists
                  ? "○ 本地存在未归档变动"
                  : "尚未创建云端归档"}
              </span>
            </div>
            {cloudInfo?.exists ? (
              <p className="text-xs text-stone-600 dark:text-zinc-400">
                上次归档: {new Date(cloudInfo.updatedAt).toLocaleString()} · 
                已归纳 {cloudInfo.summary?.mistakesCount} 道错题、{cloudInfo.summary?.vocabCount} 个生词、{cloudInfo.summary?.examsCount} 份模考
                {isDataIdentical && (
                  <span className="ml-1 text-emerald-600 dark:text-emerald-400 font-semibold">
                    (数据指纹一致，已启用防滥用硬拦截)
                  </span>
                )}
              </p>
            ) : (
              <p className="text-xs text-stone-400 dark:text-zinc-500">
                建议阶段性点击“备份到云端”，研习进度将安全存入专属加密档案空间。
              </p>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2 shrink-0">
            <button
              onClick={handleUploadBackup}
              disabled={uploading || isDataIdentical}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold shadow-subtle flex items-center space-x-1.5 transition-all active:scale-[0.98] ${
                isDataIdentical
                  ? "bg-stone-100 dark:bg-zinc-800/80 text-stone-400 dark:text-zinc-500 border border-stone-200/60 dark:border-zinc-800 cursor-not-allowed opacity-70"
                  : "bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] dark:shadow-glow-cyan disabled:opacity-50"
              }`}
              title={isDataIdentical ? "本地研习数据与云端存档 100% 一致，已自动为您节省云端配额" : "将当前本地研习记录打包并安全覆盖备份至云端"}
            >
              <CloudUpload className={`w-3.5 h-3.5 ${isDataIdentical ? "text-stone-400 dark:text-zinc-500" : "text-emerald-100 dark:text-[#090a0f]"}`} />
              <span>
                {uploading
                  ? "正在归档..."
                  : isDataIdentical
                  ? "✅ 云端已是最新 (无变动)"
                  : "备份到云端"}
              </span>
            </button>

            <button
              onClick={handleDownloadBackup}
              disabled={downloading || !cloudInfo?.exists || isDataIdentical}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold shadow-subtle flex items-center space-x-1.5 transition-all active:scale-[0.98] ${
                isDataIdentical || !cloudInfo?.exists
                  ? "bg-stone-100 dark:bg-zinc-800/80 text-stone-400 dark:text-zinc-500 border border-stone-200/60 dark:border-zinc-800 cursor-not-allowed opacity-70"
                  : "border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 hover:bg-stone-50 dark:hover:bg-zinc-700 text-stone-700 dark:text-zinc-300 disabled:opacity-40"
              }`}
              title={isDataIdentical ? "本地数据已与云端最新存档完全一致，无需重复覆盖" : "从云端对象存储拉取最新备份还原至本地"}
            >
              <CloudDownload className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400" />
              <span>
                {downloading
                  ? "正在恢复..."
                  : isDataIdentical
                  ? "✅ 本地已是最新 (无需拉取)"
                  : "从云端恢复"}
              </span>
            </button>

            <button
              onClick={handleReconcile}
              disabled={reconciling}
              className="px-3.5 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 hover:bg-stone-50 dark:hover:bg-zinc-700 text-stone-700 dark:text-zinc-300 text-xs font-bold shadow-subtle flex items-center space-x-1.5 transition-all active:scale-[0.98] disabled:opacity-40"
              title="比对题库删改，自动清理下架试题并自愈答案"
            >
              <RotateCcw className={`w-3.5 h-3.5 text-stone-500 dark:text-zinc-400 ${reconciling ? "animate-spin" : ""}`} />
              <span>{reconciling ? "校对中..." : "校对云端题库"}</span>
            </button>
          </div>
        </div>

        {/* Clear Local Data Section */}
        <div className="pt-4 border-t border-stone-100 dark:border-zinc-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <span className="text-xs font-bold text-stone-800 dark:text-zinc-200 block">清除本机临时缓存</span>
            <span className="text-[11px] text-stone-400 dark:text-zinc-500">
              用于公共阅览设备退出或重置本机真题研习记录（建议操作前先同步归档至云端）
            </span>
          </div>

          <button
            onClick={() => setShowWipeModal(true)}
            className="w-full sm:w-auto justify-center px-3.5 py-2 rounded-xl border border-rose-200 dark:border-rose-500/40 text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
          >
            <Trash2 className="w-4 h-4" />
            <span>清除本地数据</span>
          </button>
        </div>
      </div>

      {/* Password Management & Account Security Panel */}
      <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-6 sm:p-8 shadow-card space-y-6 transition-colors duration-300">
        <div className="flex items-center space-x-3 pb-4 border-b border-stone-100 dark:border-zinc-800">
          <div className="w-10 h-10 rounded-xl bg-stone-100 dark:bg-zinc-800 text-stone-800 dark:text-cyber-400 flex items-center justify-center font-bold">
            <KeyRound className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-stone-900 dark:text-zinc-100">
              {profile?.role === "super_admin" 
                ? "超级管理员密码安全维护" 
                : "账号密码安全管理"}
            </h3>
            <p className="text-xs text-stone-400 dark:text-zinc-500 mt-0.5">
              {profile?.role === "super_admin"
                ? "👑 最高权限专属：密码即时修改生效，无需任何第三方审批"
                : "自主申请 · 超管审批 · 保护考研做题记录防篡改"}
            </p>
          </div>
        </div>

        {/* Notice Banner */}
        {pwdNotice && (
          <div
            className={`p-3.5 rounded-xl text-xs flex items-start space-x-2.5 ${
              pwdNotice.type === "success"
                ? "bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200/80 dark:border-emerald-500/30 text-emerald-800 dark:text-emerald-300"
                : "bg-rose-50 dark:bg-rose-950/40 border border-rose-200/80 dark:border-rose-500/30 text-rose-700 dark:text-rose-300"
            }`}
          >
            {pwdNotice.type === "success" ? (
              <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
            ) : (
              <AlertCircle className="w-4 h-4 text-rose-600 dark:text-rose-400 shrink-0 mt-0.5" />
            )}
            <span className="flex-1 font-medium">{pwdNotice.text}</span>
          </div>
        )}

        {profile?.role === "super_admin" ? (
          /* Super Admin Direct Change */
          <div className="space-y-4">
            <div className="p-3.5 rounded-xl bg-purple-50/70 dark:bg-purple-950/30 border border-purple-200/80 dark:border-purple-500/30 text-xs text-purple-900 dark:text-purple-300 leading-relaxed">
              您当前以<strong>超级管理员</strong>身份登录。出于系统主权隔离，您的密码修改即刻生效，无需审批；任何他人（包括普通管理员）亦无权在此强行修改任何人的密码。
            </div>

            <form onSubmit={handlePasswordAction} className="max-w-md space-y-3.5">
              <div>
                <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                  设置超级管理员新密码
                </label>
                <input
                  type="password"
                  required
                  value={passwordInput}
                  onChange={(e) => setPasswordInput(e.target.value)}
                  placeholder="至少 6 位新密码"
                  className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                  确认超级管理员新密码
                </label>
                <input
                  type="password"
                  required
                  value={confirmPasswordInput}
                  onChange={(e) => setConfirmPasswordInput(e.target.value)}
                  placeholder="再次输入新密码"
                  className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                />
              </div>

              <div className="pt-1">
                <button
                  type="submit"
                  disabled={pwdLoading}
                  className="px-4 py-2 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 disabled:opacity-50 text-white dark:text-[#090a0f] text-xs font-bold rounded-xl shadow-sm dark:shadow-glow-cyan transition-all flex items-center space-x-1.5"
                >
                  {pwdLoading && (
                    <div className="w-3.5 h-3.5 border-2 border-white dark:border-[#090a0f] border-t-transparent rounded-full animate-spin" />
                  )}
                  <span>{pwdLoading ? "正在更新..." : "即刻更新密码"}</span>
                </button>
              </div>
            </form>
          </div>
        ) : (
          /* Student & Regular Admin Approval Flow */
          <div className="space-y-4">
            {activePwdRequest?.status === "pending" ? (
              /* Active Pending Request Card */
              <div className="p-4 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200/80 dark:border-amber-500/30 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <span className="relative flex h-2.5 w-2.5">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-amber-500"></span>
                    </span>
                    <span className="text-xs font-bold text-amber-900 dark:text-amber-200">
                      改密申请待审批中
                    </span>
                  </div>
                  <span className="text-[11px] text-amber-700 dark:text-amber-400 font-mono">
                    提交于 {new Date(activePwdRequest.created_at).toLocaleString()}
                  </span>
                </div>
                <p className="text-xs text-amber-800 dark:text-amber-300 leading-relaxed">
                  您的改密申请已提交并生成不可逆安全密文存入审批队列。请联系超级管理员在后台审核通过；通过后新密码将正式生效，原密码失效。在此之前，原密码仍可正常使用。
                </p>
                <div className="pt-1 flex items-center space-x-2">
                  <button
                    type="button"
                    onClick={handleCancelPasswordRequest}
                    disabled={pwdLoading}
                    className="px-3.5 py-1.5 rounded-lg border border-amber-300 dark:border-amber-600 bg-white dark:bg-zinc-900 text-amber-900 dark:text-amber-200 hover:bg-amber-100/50 dark:hover:bg-zinc-800 text-xs font-medium transition-colors"
                  >
                    {pwdLoading ? "正在撤回..." : "撤回此申请"}
                  </button>
                </div>
              </div>
            ) : (
              /* Can Submit New Request */
              <div className="space-y-4">
                {activePwdRequest?.status === "rejected" && (
                  <div className="p-3 rounded-xl bg-rose-50/70 dark:bg-rose-950/30 border border-rose-200/80 dark:border-rose-500/30 text-xs text-rose-800 dark:text-rose-300">
                    您于 {new Date(activePwdRequest.reviewed_at || activePwdRequest.created_at).toLocaleDateString()} 提交的上一条改密申请已被超级管理员驳回。原因: {activePwdRequest.review_note || "管理员驳回"}。如需修改，请重新提交申请。
                  </div>
                )}
                {activePwdRequest?.status === "approved" && (
                  <div className="p-3 rounded-xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200/80 dark:border-emerald-500/30 text-xs text-emerald-800 dark:text-emerald-300">
                    您最近一次改密申请已于 {new Date(activePwdRequest.reviewed_at || activePwdRequest.created_at).toLocaleDateString()} 审核通过并已生效。
                  </div>
                )}

                <div className="p-3.5 rounded-xl bg-stone-50 dark:bg-zinc-900 border border-stone-200/70 dark:border-zinc-800 text-xs text-stone-600 dark:text-zinc-400 leading-relaxed">
                  为保障考研学员数据安全，系统实行<strong>自主申请审批制</strong>。任何人员（包括超级管理员）均无法直接在后台强行修改您的密码。提交期望密码后，将由超级管理员审批通过后生效。
                </div>

                <form onSubmit={handlePasswordAction} className="max-w-md space-y-3.5">
                  <div>
                    <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                      期望设置的新密码
                    </label>
                    <input
                      type="password"
                      required
                      value={passwordInput}
                      onChange={(e) => setPasswordInput(e.target.value)}
                      placeholder="至少 6 位新密码"
                      className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                      确认期望新密码
                    </label>
                    <input
                      type="password"
                      required
                      value={confirmPasswordInput}
                      onChange={(e) => setConfirmPasswordInput(e.target.value)}
                      placeholder="再次输入新密码"
                      className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                    />
                  </div>

                  <div className="pt-1">
                    <button
                      type="submit"
                      disabled={pwdLoading}
                      className="px-4 py-2 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 disabled:opacity-50 text-white dark:text-[#090a0f] text-xs font-bold rounded-xl shadow-sm dark:shadow-glow-cyan transition-all flex items-center space-x-1.5"
                    >
                      {pwdLoading && (
                        <div className="w-3.5 h-3.5 border-2 border-white dark:border-[#090a0f] border-t-transparent rounded-full animate-spin" />
                      )}
                      <span>{pwdLoading ? "正在提交..." : "提交改密申请"}</span>
                    </button>
                  </div>
                </form>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Wipe Confirmation Modal */}
      {showWipeModal && (
        <div className="fixed inset-0 z-50 bg-black/40 dark:bg-black/70 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-[#11131a] rounded-2xl max-w-md w-full p-6 shadow-2xl border border-black/[0.08] dark:border-cyan-500/25 space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-3 text-rose-600 dark:text-rose-400">
              <AlertTriangle className="w-6 h-6 shrink-0" />
              <h3 className="font-bold text-stone-900 dark:text-zinc-100 text-base">危险操作: 清除本地数据</h3>
            </div>

            <p className="text-xs text-stone-600 dark:text-zinc-400 leading-relaxed">
              清除后本地存储的相关学习记录将被永久抹除。如果有重要进度，请确保已经点击“备份到云端”。
            </p>

            <div className="space-y-2 bg-stone-50 dark:bg-zinc-900 p-3 rounded-xl border border-stone-200 dark:border-zinc-800 text-xs text-stone-700 dark:text-zinc-300">
              <label className="flex items-center space-x-2 cursor-pointer">
                <input
                  type="radio"
                  name="wipeScope"
                  checked={wipeScope === "all"}
                  onChange={() => setWipeScope("all")}
                  className="text-rose-600"
                />
                <span className="font-bold text-rose-700 dark:text-rose-400">彻底清空全部本地数据 (恢复出厂全新状态)</span>
              </label>
              <label className="flex items-center space-x-2 cursor-pointer">
                <input
                  type="radio"
                  name="wipeScope"
                  checked={wipeScope === "mistakes"}
                  onChange={() => setWipeScope("mistakes")}
                />
                <span>仅清空【错题本】</span>
              </label>
              <label className="flex items-center space-x-2 cursor-pointer">
                <input
                  type="radio"
                  name="wipeScope"
                  checked={wipeScope === "vocab"}
                  onChange={() => setWipeScope("vocab")}
                />
                <span>仅清空【生词本】</span>
              </label>
              <label className="flex items-center space-x-2 cursor-pointer">
                <input
                  type="radio"
                  name="wipeScope"
                  checked={wipeScope === "drafts"}
                  onChange={() => setWipeScope("drafts")}
                />
                <span>仅清空【未交卷模考草稿】</span>
              </label>
            </div>

            <div className="flex justify-end space-x-2 pt-2">
              <button
                type="button"
                onClick={() => setShowWipeModal(false)}
                className="px-4 py-2 text-xs font-semibold text-stone-600 dark:text-zinc-400 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-xl"
              >
                取消
              </button>
              <button
                type="button"
                onClick={handleConfirmClear}
                className="px-4 py-2 text-xs font-semibold bg-rose-600 hover:bg-rose-700 text-white rounded-xl shadow-sm"
              >
                确认清除
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
