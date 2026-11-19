import {
  Activity,
  AlertCircle,
  AlertTriangle,
  Check,
  Info,
  Loader2,
  Megaphone,
  RefreshCw,
  Save,
  Shield,
  Sparkles,
  Trash2,
} from "lucide-react";
import type { SentinelStats } from "@/lib/quotaSentinel";
import type {
  AdminAnnouncementState,
  AdminSettingsState,
  SentinelStatusState,
} from "./types";

interface AdminSettingsTabProps {
  totalUsersCount: number;
  settings: AdminSettingsState;
  isSettingsClean: boolean;
  isSavingSettings: boolean;
  onChangeSettings: (next: AdminSettingsState) => void;
  onSaveSettings: () => void;
  announcementSettings: AdminAnnouncementState;
  isAnnouncementClean: boolean;
  isSavingAnnouncement: boolean;
  onChangeAnnouncement: (next: AdminAnnouncementState) => void;
  onSaveAnnouncement: () => void;
  onClearAnnouncement: () => void;
  sentinelStats: SentinelStats;
  sentinelStatus: SentinelStatusState;
  onResetSentinel: () => void;
}

export function AdminSettingsTab({
  totalUsersCount,
  settings,
  isSettingsClean,
  isSavingSettings,
  onChangeSettings,
  onSaveSettings,
  announcementSettings,
  isAnnouncementClean,
  isSavingAnnouncement,
  onChangeAnnouncement,
  onSaveAnnouncement,
  onClearAnnouncement,
  sentinelStats,
  sentinelStatus,
  onResetSentinel,
}: AdminSettingsTabProps) {
  return (
    <div className="space-y-6 max-w-3xl">
      {/* Card 0: Exam Quota Watermark & Health Panel */}
      <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/20 p-6 sm:p-8 space-y-5 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 dark:border-zinc-800 pb-4">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-indigo-50 dark:bg-cyan-500/10 text-indigo-600 dark:text-cyan-400 flex items-center justify-center font-bold shadow-xs">
              <Activity className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">考务配额水位与准入运行监控</h3>
              <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
                实时监控全站注册学员总量、配额安全水位与开放注册总准入状态
              </p>
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <span
              className={`px-2.5 py-1 rounded-xl text-xs font-bold border flex items-center space-x-1.5 ${
                settings.registrationEnabled
                  ? "bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-500/30"
                  : "bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-500/30"
              }`}
            >
              <span
                className={`w-2 h-2 rounded-full ${settings.registrationEnabled ? "bg-emerald-500 animate-pulse" : "bg-rose-500"}`}
              />
              <span>{settings.registrationEnabled ? "注册通道：开放中" : "注册通道：已关闭"}</span>
            </span>

            <span
              className={`px-2.5 py-1 rounded-xl text-xs font-bold border flex items-center space-x-1.5 ${
                sentinelStatus.state === "OPEN"
                  ? "bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-500/30"
                  : "bg-indigo-50 dark:bg-cyan-950/40 text-indigo-700 dark:text-cyan-300 border-indigo-200 dark:border-cyan-500/30"
              }`}
            >
              <Shield className="w-3.5 h-3.5 text-indigo-500 dark:text-cyan-400" />
              <span>
                {sentinelStatus.state === "OPEN"
                  ? `哨兵熔断中 (${sentinelStatus.remainingCooldown}s)`
                  : "哨兵监控：健康"}
              </span>
            </span>
          </div>
        </div>

        {/* Quota Progress Bar */}
        <div className="space-y-2.5 pt-1">
          <div className="flex items-center justify-between text-xs">
            <div className="flex items-center space-x-2">
              <span className="font-bold text-slate-700 dark:text-zinc-300">当前已注册学员配额占用</span>
              {settings.maxStudentsLimit === 0 ? (
                <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300">
                  无限准入模式 (不设上限)
                </span>
              ) : (
                <span
                  className={`px-2 py-0.5 rounded-md text-[10px] font-bold ${
                    totalUsersCount / settings.maxStudentsLimit >= 0.95
                      ? "bg-rose-100 text-rose-700 dark:bg-rose-950/60 dark:text-rose-300"
                      : totalUsersCount / settings.maxStudentsLimit >= 0.75
                      ? "bg-amber-100 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300"
                      : "bg-emerald-100 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300"
                  }`}
                >
                  占用率 {Math.min(100, Math.round((totalUsersCount / settings.maxStudentsLimit) * 100))}%
                </span>
              )}
            </div>

            <div className="font-mono text-xs">
              <span className="font-bold text-slate-900 dark:text-zinc-100">{totalUsersCount}</span>
              <span className="text-slate-400 dark:text-zinc-500">
                {" "}
                / {settings.maxStudentsLimit === 0 ? "∞ 无限制" : `${settings.maxStudentsLimit} 人`}
              </span>
            </div>
          </div>

          {/* Visual Progress Bar Track */}
          <div className="w-full h-3 bg-slate-100 dark:bg-zinc-800/80 rounded-full overflow-hidden p-0.5 border border-slate-200/60 dark:border-zinc-800">
            <div
              className={`h-full rounded-full transition-all duration-500 ${
                settings.maxStudentsLimit === 0
                  ? "w-full bg-gradient-to-r from-emerald-500 to-teal-400"
                  : totalUsersCount / settings.maxStudentsLimit >= 0.95
                  ? "bg-gradient-to-r from-amber-500 to-rose-500"
                  : totalUsersCount / settings.maxStudentsLimit >= 0.75
                  ? "bg-gradient-to-r from-blue-500 to-amber-500"
                  : "bg-gradient-to-r from-indigo-500 via-cyan-400 to-emerald-400"
              }`}
              style={{
                width:
                  settings.maxStudentsLimit === 0
                    ? "100%"
                    : `${Math.min(100, Math.max(3, Math.round((totalUsersCount / settings.maxStudentsLimit) * 100)))}%`,
              }}
            />
          </div>

          <div className="flex items-center justify-between text-[11px] text-slate-400 dark:text-zinc-500 pt-0.5">
            <span>0 人</span>
            <span>
              {settings.maxStudentsLimit === 0
                ? "全站开放注册中，当前共有 " + totalUsersCount + " 位注册学员"
                : `安全剩余名额: ${Math.max(0, settings.maxStudentsLimit - totalUsersCount)} 人`}
            </span>
            <span>{settings.maxStudentsLimit === 0 ? "无限" : `${settings.maxStudentsLimit} 人`}</span>
          </div>
        </div>
      </div>

      {/* Card 1: Sitewide Announcement */}
      <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/20 p-6 sm:p-8 space-y-6 shadow-sm">
        <div className="flex items-center justify-between border-b border-slate-100 dark:border-zinc-800 pb-4">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-indigo-50 dark:bg-cyan-500/10 text-indigo-600 dark:text-cyan-400 flex items-center justify-center font-bold shadow-xs">
              <Megaphone className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">全站置顶公告管理</h3>
              <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
                发布置顶全站横幅，关闭后自动收纳至导航栏小喇叭，零数据库写消耗
              </p>
            </div>
          </div>

          <label className="flex items-center space-x-2 cursor-pointer bg-slate-50 dark:bg-zinc-900/80 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-zinc-800 hover:bg-slate-100 dark:hover:bg-zinc-800 transition-colors">
            <span className="text-xs font-bold text-slate-700 dark:text-zinc-300">启用置顶</span>
            <input
              type="checkbox"
              checked={announcementSettings.enabled}
              onChange={(e) => onChangeAnnouncement({ ...announcementSettings, enabled: e.target.checked })}
              className="w-4 h-4 text-indigo-600 dark:text-cyan-500 rounded focus:ring-indigo-500 dark:focus:ring-cyan-500 cursor-pointer"
            />
          </label>
        </div>

        <div className="space-y-4">
          {/* Theme style selector */}
          <div>
            <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-2">公告主题风格</label>
            <div className="grid grid-cols-3 gap-3">
              <button
                type="button"
                onClick={() => onChangeAnnouncement({ ...announcementSettings, type: "info" })}
                className={`p-3 rounded-2xl border text-xs font-bold flex items-center justify-center space-x-2 transition-all ${
                  announcementSettings.type === "info"
                    ? "bg-blue-50 dark:bg-blue-950/40 border-blue-500 dark:border-blue-500/50 text-blue-800 dark:text-blue-300 ring-2 ring-blue-400/20 shadow-xs"
                    : "bg-slate-50 dark:bg-zinc-900/60 border-slate-200 dark:border-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800"
                }`}
              >
                <Info className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                <span>信息蓝 (日常通知)</span>
              </button>

              <button
                type="button"
                onClick={() => onChangeAnnouncement({ ...announcementSettings, type: "warning" })}
                className={`p-3 rounded-2xl border text-xs font-bold flex items-center justify-center space-x-2 transition-all ${
                  announcementSettings.type === "warning"
                    ? "bg-amber-50 dark:bg-amber-950/40 border-amber-500 dark:border-amber-500/50 text-amber-800 dark:text-amber-300 ring-2 ring-amber-400/20 shadow-xs"
                    : "bg-slate-50 dark:bg-zinc-900/60 border-slate-200 dark:border-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800"
                }`}
              >
                <AlertTriangle className="w-4 h-4 text-amber-600 dark:text-amber-400" />
                <span>警示黄 (维护/提醒)</span>
              </button>

              <button
                type="button"
                onClick={() => onChangeAnnouncement({ ...announcementSettings, type: "alert" })}
                className={`p-3 rounded-2xl border text-xs font-bold flex items-center justify-center space-x-2 transition-all ${
                  announcementSettings.type === "alert"
                    ? "bg-rose-50 dark:bg-rose-950/40 border-rose-500 dark:border-rose-500/50 text-rose-800 dark:text-rose-300 ring-2 ring-rose-400/20 shadow-xs"
                    : "bg-slate-50 dark:bg-zinc-900/60 border-slate-200 dark:border-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800"
                }`}
              >
                <AlertCircle className="w-4 h-4 text-rose-600 dark:text-rose-400" />
                <span>紧急红 (重大事项)</span>
              </button>
            </div>
          </div>

          {/* Textarea */}
          <div>
            <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-1">公告正文文案</label>
            <textarea
              rows={3}
              value={announcementSettings.text}
              onChange={(e) => onChangeAnnouncement({ ...announcementSettings, text: e.target.value })}
              placeholder="请输入面向全站考生的公告通知内容（例如：2024考研真题已更新，支持查词与左右键换题...）"
              className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-2xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
            />
          </div>

          {/* Action Button & Link */}
          <div className="grid sm:grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-1">
                附带跳转按钮文字 (可选)
              </label>
              <input
                type="text"
                value={announcementSettings.linkText}
                onChange={(e) => onChangeAnnouncement({ ...announcementSettings, linkText: e.target.value })}
                placeholder="例如: 立即前往做题"
                className="w-full px-4 py-2 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-xl text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
              />
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-1">
                跳转目标路由或链接 (可选)
              </label>
              <input
                type="text"
                value={announcementSettings.linkUrl}
                onChange={(e) => onChangeAnnouncement({ ...announcementSettings, linkUrl: e.target.value })}
                placeholder="例如: /practice?id=xxx 或 https://..."
                className="w-full px-4 py-2 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-xl text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
              />
            </div>
          </div>

          {/* Live Preview */}
          <div>
            <label className="block text-xs font-bold text-slate-400 dark:text-zinc-500 mb-1.5">
              所见即所得前台实时预览
            </label>
            <div
              className={`p-3 rounded-2xl border flex items-center justify-between gap-3 text-xs ${
                announcementSettings.type === "info"
                  ? "bg-blue-50 dark:bg-blue-950/40 border-blue-200 dark:border-blue-500/30 text-blue-950 dark:text-blue-200"
                  : announcementSettings.type === "warning"
                  ? "bg-amber-50 dark:bg-amber-950/40 border-amber-200 dark:border-amber-500/30 text-amber-950 dark:text-amber-200"
                  : "bg-rose-50 dark:bg-rose-950/40 border-rose-200 dark:border-rose-500/30 text-rose-950 dark:text-rose-200"
              }`}
            >
              <div className="flex items-center space-x-2 flex-1 min-w-0">
                <Megaphone className="w-4 h-4 shrink-0 text-indigo-600 dark:text-cyan-400" />
                <span className="font-semibold truncate">
                  {announcementSettings.text || "公告内容将在此实时预览呈现..."}
                </span>
                {announcementSettings.linkText && (
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-slate-900 dark:bg-cyan-500 text-white dark:text-zinc-950 shrink-0">
                    {announcementSettings.linkText} →
                  </span>
                )}
              </div>
              <div className="text-slate-400 dark:text-zinc-500 text-[10px] shrink-0 font-mono">
                {announcementSettings.enabled ? "● 开启展示" : "○ 未开启"}
              </div>
            </div>
          </div>

          {/* Actions: Clear & Save */}
          <div className="pt-2 flex flex-wrap items-center justify-between gap-3">
            <button
              type="button"
              onClick={onClearAnnouncement}
              disabled={isSavingAnnouncement || (!announcementSettings.text && !announcementSettings.enabled)}
              className="px-4 py-2.5 bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 dark:hover:bg-rose-950/50 disabled:opacity-40 disabled:cursor-not-allowed text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-500/20 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition-all"
              title="一键清空文案并关闭全站公告"
            >
              <Trash2 className="w-4 h-4" />
              <span>一键清空并下架公告</span>
            </button>

            <button
              onClick={onSaveAnnouncement}
              disabled={isSavingAnnouncement || isAnnouncementClean}
              className={`px-6 py-2.5 rounded-xl text-xs font-bold flex items-center space-x-2 transition-all ${
                isAnnouncementClean
                  ? "bg-slate-100 dark:bg-zinc-800 text-slate-400 dark:text-zinc-500 cursor-not-allowed border border-slate-200 dark:border-zinc-700/60"
                  : "bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 shadow-md shadow-indigo-200 dark:shadow-none"
              }`}
              title={isAnnouncementClean ? "当前公告文案与配置已与云端一致，无需重复提交" : "保存并全站发布公告"}
            >
              {isSavingAnnouncement ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : isAnnouncementClean ? (
                <Check className="w-4 h-4 text-emerald-500" />
              ) : (
                <Sparkles className="w-4 h-4" />
              )}
              <span>
                {isSavingAnnouncement
                  ? "正在发布..."
                  : isAnnouncementClean
                  ? "✅ 公告与云端一致 (无需保存)"
                  : "保存并全站发布公告"}
              </span>
            </button>
          </div>
        </div>
      </div>

      {/* Card 2: System Registration Quota */}
      <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/20 p-6 sm:p-8 space-y-6 shadow-sm">
        <div>
          <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">系统运行与人数配额配置</h3>
          <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">控制全站注册学员人数上限与新用户注册准入开关</p>
        </div>

        <div className="space-y-5 pt-2">
          <div>
            <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-1">
              全站学员人数上限 (人)
            </label>
            <input
              type="number"
              min={0}
              value={settings.maxStudentsLimit}
              onChange={(e) => onChangeSettings({ ...settings, maxStudentsLimit: parseInt(e.target.value, 10) || 0 })}
              className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-sm font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
            />
            <p className="text-[11px] text-slate-400 dark:text-zinc-500 mt-1">
              设置为 0 表示不设人数上限（无限注册）。当注册人数达到此数值时，新用户注册将被系统硬校验拦截。
            </p>
          </div>

          <div className="flex items-center justify-between p-4 bg-slate-50 dark:bg-zinc-900/60 rounded-2xl border border-slate-200 dark:border-zinc-800">
            <div>
              <h4 className="text-xs font-bold text-slate-900 dark:text-zinc-100">开放学员注册通道</h4>
              <p className="text-[11px] text-slate-500 dark:text-zinc-400 mt-0.5">
                若关闭，注册通道将被临时封锁，任何新用户均无法注册
              </p>
            </div>
            <input
              type="checkbox"
              checked={settings.registrationEnabled}
              onChange={(e) => onChangeSettings({ ...settings, registrationEnabled: e.target.checked })}
              className="w-5 h-5 text-indigo-600 dark:text-cyan-500 rounded focus:ring-indigo-500 dark:focus:ring-cyan-500 cursor-pointer"
            />
          </div>

          <div className="pt-4 flex justify-end">
            <button
              onClick={onSaveSettings}
              disabled={isSavingSettings || isSettingsClean}
              className={`px-6 py-2.5 rounded-xl text-xs font-bold flex items-center space-x-2 transition-colors ${
                isSettingsClean
                  ? "bg-slate-100 dark:bg-zinc-800 text-slate-400 dark:text-zinc-500 cursor-not-allowed border border-slate-200 dark:border-zinc-700/60"
                  : "bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 shadow-md shadow-indigo-200 dark:shadow-none"
              }`}
              title={isSettingsClean ? "当前人数上限与注册开关与云端完全一致，无需重复保存" : "保存系统配置"}
            >
              {isSavingSettings ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : isSettingsClean ? (
                <Check className="w-4 h-4 text-emerald-500" />
              ) : (
                <Save className="w-4 h-4" />
              )}
              <span>
                {isSavingSettings
                  ? "正在保存..."
                  : isSettingsClean
                  ? "✅ 配额与云端一致 (无需保存)"
                  : "保存系统配置"}
              </span>
            </button>
          </div>
        </div>
      </div>

      {/* Card 3: Client Quota Sentinel & API Health */}
      <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/20 p-6 sm:p-8 space-y-6 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 rounded-xl bg-indigo-50 dark:bg-cyan-500/10 text-indigo-600 dark:text-cyan-400 flex items-center justify-center font-bold">
                <Shield className="w-4 h-4" />
              </div>
              <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">
                客户端配额熔断哨兵与 API 健康度看板
              </h3>
              <span
                className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                  sentinelStatus.state === "OPEN"
                    ? "bg-rose-100 text-rose-700 dark:bg-rose-950/60 dark:text-rose-400 border border-rose-200 dark:border-rose-500/30 animate-pulse"
                    : "bg-emerald-100 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-500/30"
                }`}
              >
                {sentinelStatus.state === "OPEN"
                  ? `● 熔断冷静期中 (${sentinelStatus.remainingCooldown}s)`
                  : "● 正常健康运行 (CLOSED)"}
              </span>
            </div>
            <p className="text-xs text-slate-500 dark:text-zinc-400 mt-1">
              10秒滑动窗口主动削峰退避与防刷硬熔断 · 杜绝死循环消耗 Supabase 50万次免费配额
            </p>
          </div>

          <button
            onClick={onResetSentinel}
            className="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200/80 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-300 text-xs font-semibold flex items-center space-x-1.5 transition-all self-start sm:self-center"
          >
            <RefreshCw className="w-3.5 h-3.5 text-slate-500 dark:text-zinc-400" />
            <span>重置哨兵状态</span>
          </button>
        </div>

        {/* Metrics Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3.5 pt-2">
          <div className="p-4 bg-slate-50 dark:bg-zinc-900/60 rounded-2xl border border-slate-200/80 dark:border-zinc-800">
            <span className="text-[11px] font-medium text-slate-400 dark:text-zinc-500 block">今日客户端请求数</span>
            <span className="text-2xl font-bold font-mono text-slate-900 dark:text-zinc-100 mt-1 block">
              {sentinelStats.totalRequests}
            </span>
            <span className="text-[10px] text-slate-400 dark:text-zinc-500 mt-0.5 block">
              实时滑动: {sentinelStatus.recentRps} req/s
            </span>
          </div>

          <div className="p-4 bg-slate-50 dark:bg-zinc-900/60 rounded-2xl border border-slate-200/80 dark:border-zinc-800">
            <span className="text-[11px] font-medium text-slate-400 dark:text-zinc-500 block">软限排队削峰次数</span>
            <span className="text-2xl font-bold font-mono text-amber-600 dark:text-amber-400 mt-1 block">
              {sentinelStats.throttledRequests}
            </span>
            <span className="text-[10px] text-slate-400 dark:text-zinc-500 mt-0.5 block">
              10s内超12次自适应退避
            </span>
          </div>

          <div className="p-4 bg-slate-50 dark:bg-zinc-900/60 rounded-2xl border border-slate-200/80 dark:border-zinc-800">
            <span className="text-[11px] font-medium text-slate-400 dark:text-zinc-500 block">断路硬熔断触发</span>
            <span className="text-2xl font-bold font-mono text-rose-600 dark:text-rose-400 mt-1 block">
              {sentinelStats.trippedCount}
            </span>
            <span className="text-[10px] text-slate-400 dark:text-zinc-500 mt-0.5 block">
              10s内超25次紧急挂起
            </span>
          </div>

          <div className="p-4 bg-slate-50 dark:bg-zinc-900/60 rounded-2xl border border-slate-200/80 dark:border-zinc-800">
            <span className="text-[11px] font-medium text-slate-400 dark:text-zinc-500 block">熔断拦截无效请求</span>
            <span className="text-2xl font-bold font-mono text-indigo-600 dark:text-cyan-400 mt-1 block">
              {sentinelStats.blockedRequests}
            </span>
            <span className="text-[10px] text-slate-400 dark:text-zinc-500 mt-0.5 block">0 云端网络消耗</span>
          </div>
        </div>

        {/* Architecture Details Box */}
        <div className="p-4 bg-slate-50/80 dark:bg-zinc-900/40 rounded-2xl border border-slate-200/60 dark:border-zinc-800/80 text-xs text-slate-600 dark:text-zinc-400 space-y-1.5 leading-relaxed">
          <div className="font-semibold text-slate-800 dark:text-zinc-200 flex items-center space-x-1.5">
            <Sparkles className="w-3.5 h-3.5 text-indigo-500 dark:text-cyan-400" />
            <span>防护策略说明</span>
          </div>
          <p className="text-[11px]">
            • <strong>一级软限（10s &gt; 12次）</strong>：自适应延迟 300~1000ms 排队平滑流量脉冲，避免向 Supabase 瞬间迸发高频并发。<br />
            • <strong>二级断路（10s &gt; 25次）</strong>：断路器开启 30 秒冷静期，前端立即就地拦截并合成 429 响应，彻底切断物理网络消耗。<br />
            • <strong>特权豁免通道</strong>：账号安全退出（<code>/auth/v1/logout</code>）与正式考场交卷不受断路器影响，优先保障核心业务体验。
          </p>
        </div>
      </div>
    </div>
  );
}
