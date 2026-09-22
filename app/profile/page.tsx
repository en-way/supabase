"use client";

import { useState, useEffect } from "react";
import { supabase } from "@/lib/supabase";
import { 
  getLocalState, 
  uploadBackupToCloud, 
  downloadBackupFromCloud, 
  fetchCloudBackupInfo, 
  clearLocalData, 
  reconcileLearningState,
  LocalLearningState 
} from "@/lib/storage";
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
  Sparkles
} from "lucide-react";

export default function ProfilePage() {
  const [profile, setProfile] = useState<any>(null);
  const [user, setUser] = useState<any>(null);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);
  const [cloudInfo, setCloudInfo] = useState<any>(null);

  // Edit nickname
  const [isEditingNick, setIsEditingNick] = useState(false);
  const [nicknameInput, setNicknameInput] = useState("");

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
    }
    setLocalState(getLocalState());
    const cInfo = await fetchCloudBackupInfo();
    setCloudInfo(cInfo);
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
    if (!window.confirm("⚠️ 备份到云端将使用当前设备的做题数据【完全覆盖】云端的历史存档快照。确定继续上传覆盖吗？")) {
      return;
    }
    setUploading(true);
    setNotice(null);
    const res = await uploadBackupToCloud();
    if (res.success) {
      setNotice({ type: "success", text: "🎉 本地数据已成功打包并覆盖备份至云端！" });
      const cInfo = await fetchCloudBackupInfo();
      setCloudInfo(cInfo);
    } else {
      setNotice({ type: "error", text: res.error || "上传备份失败" });
    }
    setUploading(false);
    setTimeout(() => setNotice(null), 3000);
  };

  const [reconciling, setReconciling] = useState(false);

  const handleDownloadBackup = async () => {
    if (!window.confirm("⚠️ 从云端恢复将直接【完全覆盖】当前设备的本地数据。确定继续吗？")) {
      return;
    }
    setDownloading(true);
    setNotice(null);
    const res = await downloadBackupFromCloud();
    if (res.success) {
      // Automatically run reconciliation after restoring from Storage
      const recon = await reconcileLearningState();
      setLocalState(getLocalState());
      if (recon.hasChanges) {
        setNotice({ type: "success", text: `🎉 已从云端对象存储还原并完成校对：${recon.summaryText}` });
      } else {
        setNotice({ type: "success", text: "🎉 已成功从云端对象存储拉取最新快照并还原至本地！" });
      }
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
                cloudInfo?.exists ? "bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border border-emerald-200/80 dark:border-emerald-500/30" : "bg-stone-200 dark:bg-zinc-800 text-stone-600 dark:text-zinc-400"
              }`}>
                {cloudInfo?.exists ? "云端已有最新档案" : "尚未创建云端归档"}
              </span>
            </div>
            {cloudInfo?.exists ? (
              <p className="text-xs text-stone-600 dark:text-zinc-400">
                上次归档: {new Date(cloudInfo.updatedAt).toLocaleString()} · 
                已归纳 {cloudInfo.summary?.mistakesCount} 道错题、{cloudInfo.summary?.vocabCount} 个生词、{cloudInfo.summary?.examsCount} 份模考
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
              disabled={uploading}
              className="px-3.5 py-1.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle dark:shadow-glow-cyan flex items-center space-x-1.5 transition-all active:scale-[0.98] disabled:opacity-50"
            >
              <CloudUpload className="w-3.5 h-3.5 text-emerald-100 dark:text-[#090a0f]" />
              <span>{uploading ? "正在归档..." : "备份到云端"}</span>
            </button>

            <button
              onClick={handleDownloadBackup}
              disabled={downloading || !cloudInfo?.exists}
              className="px-3.5 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 hover:bg-stone-50 dark:hover:bg-zinc-700 text-stone-700 dark:text-zinc-300 text-xs font-bold shadow-subtle flex items-center space-x-1.5 transition-all active:scale-[0.98] disabled:opacity-40"
            >
              <CloudDownload className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400" />
              <span>{downloading ? "正在恢复..." : "从云端恢复"}</span>
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
        <div className="pt-4 border-t border-stone-100 dark:border-zinc-800 flex items-center justify-between">
          <div>
            <span className="text-xs font-bold text-stone-800 dark:text-zinc-200 block">清除本机临时缓存</span>
            <span className="text-[11px] text-stone-400 dark:text-zinc-500">
              用于公共阅览设备退出或重置本机真题研习记录（建议操作前先同步归档至云端）
            </span>
          </div>

          <button
            onClick={() => setShowWipeModal(true)}
            className="px-3.5 py-2 rounded-xl border border-rose-200 dark:border-rose-500/40 text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
          >
            <Trash2 className="w-4 h-4" />
            <span>清除本地数据</span>
          </button>
        </div>
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
