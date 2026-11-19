import { useState } from "react";
import {
  Activity,
  Crown,
  KeyRound,
  Radio,
  RefreshCw,
  Search,
  Sparkles,
  UserCheck,
  Users,
  UserX,
} from "lucide-react";
import type { AnalyticsSnapshot } from "@/lib/analyticsSnapshot";
import { WidgetErrorBoundary } from "@/components/WidgetErrorBoundary";
import type { UserProfile } from "@/types/user";
import { formatRelativeTime, isUserOnline } from "./types";

interface AdminUsersTabProps {
  userList: UserProfile[];
  onlineCount: number;
  maxStudentsLimit: number;
  pendingPasswordCount: number;
  analyticsSnapshot: AnalyticsSnapshot | null;
  isRefreshingSnapshot: boolean;
  onRefreshSnapshot: () => void;
  onOpenPwdApprovals: () => void;
  onSetRole: (targetUser: UserProfile, newRole: "student" | "admin") => void;
}

export function AdminUsersTab({
  userList,
  onlineCount,
  maxStudentsLimit,
  pendingPasswordCount,
  analyticsSnapshot,
  isRefreshingSnapshot,
  onRefreshSnapshot,
  onOpenPwdApprovals,
  onSetRole,
}: AdminUsersTabProps) {
  const [userSortOrder, setUserSortOrder] = useState<"active_desc" | "created_desc">("active_desc");
  const [userSearchTerm, setUserSearchTerm] = useState("");

  const sortedUsers = [...userList].sort((a, b) => {
    const aOnline = isUserOnline(a);
    const bOnline = isUserOnline(b);
    if (userSortOrder === "active_desc") {
      if (aOnline && !bOnline) return -1;
      if (!aOnline && bOnline) return 1;
      const aTime = a.last_active_at ? new Date(a.last_active_at).getTime() : 0;
      const bTime = b.last_active_at ? new Date(b.last_active_at).getTime() : 0;
      return bTime - aTime;
    }
    const aCreated = a.created_at ? new Date(a.created_at).getTime() : 0;
    const bCreated = b.created_at ? new Date(b.created_at).getTime() : 0;
    return bCreated - aCreated;
  });

  const filteredUsers = sortedUsers.filter((u) => {
    if (!userSearchTerm.trim()) return true;
    const term = userSearchTerm.trim().toLowerCase();
    const matchUsername = u.username?.toLowerCase().includes(term);
    const matchNickname = u.nickname?.toLowerCase().includes(term);
    return matchUsername || matchNickname;
  });

  return (
    <div className="space-y-5">
      {/* Top Monitoring Cards (Presence & Storage Analytics Snapshot) */}
      <WidgetErrorBoundary fallbackTitle="实时在场与存储快照监控组件异常">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          {/* Card 1: Live Presence (0 DB writes) */}
          <div className="bg-gradient-to-br from-emerald-500/10 via-emerald-500/5 to-transparent dark:from-emerald-500/20 dark:to-transparent p-4 rounded-2xl border border-emerald-200 dark:border-emerald-500/30 flex items-center justify-between shadow-xs">
            <div className="space-y-1">
              <div className="flex items-center space-x-1.5">
                <span className="relative flex h-2.5 w-2.5">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                </span>
                <span className="text-xs font-bold text-emerald-800 dark:text-emerald-300">当前实时在场</span>
              </div>
              <div className="text-2xl font-black text-slate-900 dark:text-white font-mono tracking-tight">
                {onlineCount || userList.filter(isUserOnline).length}{" "}
                <span className="text-xs font-medium text-slate-500 dark:text-zinc-400 font-sans">人活跃在线</span>
              </div>
              <p className="text-[10px] text-emerald-700/80 dark:text-emerald-400/80">
                ⚡ 5分钟轻量活跃打点 · 0 长连接消耗 (0/200)
              </p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold">
              <Radio className="w-5 h-5 animate-pulse" />
            </div>
          </div>

          {/* Card 2: Registered Students */}
          <div className="bg-white dark:bg-[#11131a] p-4 rounded-2xl border border-slate-200 dark:border-cyan-500/20 flex items-center justify-between shadow-xs">
            <div className="space-y-1">
              <span className="text-xs font-bold text-slate-500 dark:text-zinc-400">已注册学员</span>
              <div className="text-2xl font-black text-slate-900 dark:text-white font-mono tracking-tight">
                {userList.filter((u) => u.role === "student").length}
                {maxStudentsLimit > 0 && (
                  <span className="text-xs font-normal text-slate-400 dark:text-zinc-500 font-sans">
                    {" "}
                    / {maxStudentsLimit} 限额
                  </span>
                )}
              </div>
              <p className="text-[10px] text-slate-400 dark:text-zinc-500">
                全站总账号: {userList.length} 人 (含管理特权席位)
              </p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-indigo-50 dark:bg-cyan-500/10 text-indigo-600 dark:text-cyan-400 flex items-center justify-center font-bold">
              <Users className="w-5 h-5" />
            </div>
          </div>

          {/* Card 3: Storage Snapshot Offload (0 DB CPU) */}
          <div className="bg-white dark:bg-[#11131a] p-4 rounded-2xl border border-slate-200 dark:border-cyan-500/20 flex items-center justify-between shadow-xs">
            <div className="space-y-1">
              <div className="flex items-center space-x-1.5">
                <Activity className="w-3.5 h-3.5 text-indigo-600 dark:text-cyan-400" />
                <span className="text-xs font-bold text-slate-700 dark:text-zinc-300">1GB Storage 预计算快照</span>
              </div>
              <div className="text-xs font-medium text-slate-600 dark:text-zinc-300">
                {analyticsSnapshot ? (
                  <span>
                    {analyticsSnapshot.totalExams} 套试卷 · {analyticsSnapshot.totalBackups} 份云快照
                  </span>
                ) : (
                  <span>直接读取静态快照 (0 数据库计算)</span>
                )}
              </div>
              <button
                onClick={onRefreshSnapshot}
                disabled={isRefreshingSnapshot}
                className="inline-flex items-center space-x-1 text-[10px] font-bold text-indigo-600 hover:text-indigo-700 dark:text-cyan-400 dark:hover:text-cyan-300 transition-colors"
              >
                <RefreshCw className={`w-3 h-3 ${isRefreshingSnapshot ? "animate-spin" : ""}`} />
                <span>{isRefreshingSnapshot ? "更新中..." : "重新聚合生成云端快照"}</span>
              </button>
            </div>
            <div className="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-950/40 text-amber-600 dark:text-amber-400 flex items-center justify-center font-bold">
              <Sparkles className="w-5 h-5" />
            </div>
          </div>
        </div>
      </WidgetErrorBoundary>

      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-2">
        <div>
          <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">学员账号与权限管理</h3>
          <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
            支持查看全员实时在线/上次在线时间、任命普通管理员、重置单人密码及一键批量重置学员密码
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          {/* Search Box */}
          <div className="relative flex-1 min-w-[200px] sm:w-64">
            <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 dark:text-zinc-500" />
            <input
              type="text"
              value={userSearchTerm}
              onChange={(e) => setUserSearchTerm(e.target.value)}
              placeholder="搜索学号 / 用户名 / 昵称..."
              className="w-full pl-8 pr-3 py-1.5 text-xs rounded-xl bg-slate-100 dark:bg-zinc-800/80 border border-slate-200 dark:border-zinc-700/60 text-slate-900 dark:text-zinc-100 placeholder-slate-400 dark:placeholder-zinc-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 dark:focus:ring-cyan-500"
            />
          </div>

          {/* Sort Order Selector */}
          <div className="flex items-center bg-slate-100 dark:bg-zinc-800/80 p-1 rounded-xl text-xs font-medium">
            <button
              onClick={() => setUserSortOrder("active_desc")}
              className={`px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all ${
                userSortOrder === "active_desc"
                  ? "bg-white dark:bg-cyan-500 text-slate-900 dark:text-zinc-950 shadow-xs"
                  : "text-slate-500 dark:text-zinc-400"
              }`}
            >
              按在线时间
            </button>
            <button
              onClick={() => setUserSortOrder("created_desc")}
              className={`px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all ${
                userSortOrder === "created_desc"
                  ? "bg-white dark:bg-cyan-500 text-slate-900 dark:text-zinc-950 shadow-xs"
                  : "text-slate-500 dark:text-zinc-400"
              }`}
            >
              按注册时间
            </button>
          </div>

          {/* Password Approval Shortcut Button */}
          <button
            onClick={onOpenPwdApprovals}
            className="px-3.5 py-2 bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-500/30 hover:bg-amber-100 dark:hover:bg-amber-950/60 text-amber-800 dark:text-amber-300 rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-xs transition-colors"
          >
            <KeyRound className="w-3.5 h-3.5" />
            <span>密码审批工作台</span>
            {pendingPasswordCount > 0 && (
              <span className="px-1.5 py-0.2 bg-amber-500 text-white text-[10px] font-bold rounded-full">
                {pendingPasswordCount}
              </span>
            )}
          </button>
        </div>
      </div>

      <WidgetErrorBoundary fallbackTitle="学员与考务人员列表加载异常">
        <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-cyan-500/20 overflow-hidden shadow-sm">
          {/* Desktop Table View */}
          <div className="hidden md:block overflow-x-auto">
            <table className="w-full text-left text-xs text-slate-700 dark:text-zinc-300">
              <thead className="bg-slate-50 dark:bg-zinc-900/80 border-b border-slate-200 dark:border-zinc-800 text-slate-500 dark:text-zinc-400 font-semibold">
                <tr>
                  <th className="p-4">用户名 / 学号</th>
                  <th className="p-4">昵称</th>
                  <th className="p-4">权限角色</th>
                  <th className="p-4">在线状态</th>
                  <th className="p-4">上次在线时间</th>
                  <th className="p-4">注册时间</th>
                  <th className="p-4 text-right">角色调整</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 dark:divide-zinc-800">
                {filteredUsers.length === 0 ? (
                  <tr>
                    <td colSpan={7} className="p-8 text-center text-xs text-slate-400 dark:text-zinc-500">
                      {userSearchTerm.trim()
                        ? `未找到与 "${userSearchTerm}" 匹配的学员或考务人员`
                        : "暂无人员记录"}
                    </td>
                  </tr>
                ) : (
                  filteredUsers.map((u) => {
                    const isSuper = u.role === "super_admin";
                    const isAdmin = u.role === "admin";
                    const isOnline = isUserOnline(u);

                    return (
                      <tr key={u.id} className="hover:bg-slate-50/60 dark:hover:bg-zinc-800/40 transition-colors">
                        <td className="p-4 font-mono font-bold text-slate-900 dark:text-zinc-100">{u.username}</td>
                        <td className="p-4">{u.nickname || "--"}</td>
                        <td className="p-4">
                          {isSuper ? (
                            <span className="px-2.5 py-1 rounded-full font-black text-[10px] bg-gradient-to-r from-amber-500/15 via-purple-500/15 to-indigo-500/15 text-amber-900 dark:text-amber-300 border border-amber-300/80 dark:border-amber-500/30 inline-flex items-center space-x-1 shadow-xs">
                              <Crown className="w-3 h-3 text-amber-600 dark:text-amber-400 fill-amber-400" />
                              <span>👑 超级管理员</span>
                            </span>
                          ) : isAdmin ? (
                            <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-indigo-100 dark:bg-cyan-500/20 text-indigo-800 dark:text-cyan-300 border border-transparent dark:border-cyan-500/30">
                              🛡️ 普通管理员
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400">
                              🎓 学员
                            </span>
                          )}
                        </td>
                        {/* Live Online Presence Indicator */}
                        <td className="p-4">
                          {isOnline ? (
                            <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-emerald-100 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 border border-emerald-300/80 dark:border-emerald-500/30 inline-flex items-center space-x-1.5 shadow-xs">
                              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                              <span>在线 (5分钟内活跃)</span>
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-full font-medium text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400 inline-flex items-center space-x-1">
                              <span className="w-1.5 h-1.5 rounded-full bg-slate-400" />
                              <span>离线</span>
                            </span>
                          )}
                        </td>
                        {/* Last Active At Relative Time with Tooltip */}
                        <td
                          className="p-4 font-mono font-medium text-slate-700 dark:text-zinc-300"
                          title={u.last_active_at ? new Date(u.last_active_at).toLocaleString() : "暂无在线记录"}
                        >
                          {formatRelativeTime(u.last_active_at)}
                        </td>
                        <td className="p-4 text-slate-400 dark:text-zinc-500 font-mono">
                          {u.created_at ? new Date(u.created_at).toLocaleDateString() : "--"}
                        </td>
                        <td className="p-4 text-right">
                          {isSuper ? (
                            <span className="text-[11px] text-slate-400 dark:text-zinc-500 italic">全站独占最高席位</span>
                          ) : isAdmin ? (
                            <div className="flex items-center justify-end space-x-1.5">
                              <button
                                onClick={() => onSetRole(u, "student")}
                                className="px-2.5 py-1 text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 dark:hover:bg-rose-950/50 border border-transparent dark:border-rose-500/20 rounded-lg text-xs font-semibold inline-flex items-center space-x-1 transition-colors"
                              >
                                <UserX className="w-3 h-3" />
                                <span>降为学员</span>
                              </button>
                            </div>
                          ) : (
                            <button
                              onClick={() => onSetRole(u, "admin")}
                              className="px-2.5 py-1 text-indigo-600 dark:text-cyan-300 bg-indigo-50 dark:bg-cyan-500/10 hover:bg-indigo-100 dark:hover:bg-cyan-500/20 border border-transparent dark:border-cyan-500/20 rounded-lg text-xs font-semibold inline-flex items-center space-x-1 transition-colors"
                            >
                              <UserCheck className="w-3 h-3" />
                              <span>设为管理员</span>
                            </button>
                          )}
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>

          {/* Mobile User Card List */}
          <div className="md:hidden divide-y divide-slate-100 dark:divide-zinc-800/80">
            {filteredUsers.length === 0 ? (
              <div className="p-8 text-center text-xs text-slate-400 dark:text-zinc-500">
                {userSearchTerm.trim()
                  ? `未找到与 "${userSearchTerm}" 匹配的学员或考务人员`
                  : "暂无人员记录"}
              </div>
            ) : (
              filteredUsers.map((u) => {
                const isSuper = u.role === "super_admin";
                const isAdmin = u.role === "admin";
                const isOnline = isUserOnline(u);

                return (
                  <div key={u.id} className="p-4 space-y-3">
                    <div className="flex items-start justify-between gap-2">
                      <div>
                        <div className="font-mono font-bold text-sm text-slate-900 dark:text-zinc-100">
                          {u.username}
                        </div>
                        {u.nickname && (
                          <div className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">{u.nickname}</div>
                        )}
                      </div>
                      <div>
                        {isSuper ? (
                          <span className="px-2.5 py-1 rounded-full font-black text-[10px] bg-gradient-to-r from-amber-500/15 via-purple-500/15 to-indigo-500/15 text-amber-900 dark:text-amber-300 border border-amber-300/80 dark:border-amber-500/30 inline-flex items-center space-x-1 shadow-xs">
                            <Crown className="w-3 h-3 text-amber-600 dark:text-amber-400 fill-amber-400" />
                            <span>👑 超管</span>
                          </span>
                        ) : isAdmin ? (
                          <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-indigo-100 dark:bg-cyan-500/20 text-indigo-800 dark:text-cyan-300 border border-transparent dark:border-cyan-500/30">
                            🛡️ 管理员
                          </span>
                        ) : (
                          <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400">
                            🎓 学员
                          </span>
                        )}
                      </div>
                    </div>

                    <div className="flex flex-wrap items-center gap-3 text-[11px]">
                      {isOnline ? (
                        <span className="inline-flex items-center space-x-1 text-emerald-600 dark:text-emerald-400 font-bold">
                          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                          <span>在线</span>
                        </span>
                      ) : (
                        <span className="inline-flex items-center space-x-1 text-slate-400 dark:text-zinc-500">
                          <span className="w-1.5 h-1.5 rounded-full bg-slate-400" />
                          <span>离线</span>
                        </span>
                      )}
                      <span className="text-slate-400 dark:text-zinc-500">
                        活动: {formatRelativeTime(u.last_active_at)}
                      </span>
                      <span className="text-slate-400 dark:text-zinc-500">
                        注册: {u.created_at ? new Date(u.created_at).toLocaleDateString() : "--"}
                      </span>
                    </div>

                    <div className="flex items-center gap-2 pt-2 border-t border-slate-100 dark:border-zinc-800/60">
                      {isSuper ? (
                        <span className="text-xs text-slate-400 dark:text-zinc-500 italic py-1">全站最高席位</span>
                      ) : isAdmin ? (
                        <button
                          onClick={() => onSetRole(u, "student")}
                          className="flex-1 py-1.5 px-2 text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 rounded-lg text-xs font-semibold inline-flex items-center justify-center space-x-1"
                        >
                          <UserX className="w-3 h-3" />
                          <span>降为学员</span>
                        </button>
                      ) : (
                        <button
                          onClick={() => onSetRole(u, "admin")}
                          className="flex-1 py-1.5 px-2 text-indigo-600 dark:text-cyan-300 bg-indigo-50 dark:bg-cyan-500/10 hover:bg-indigo-100 rounded-lg text-xs font-semibold inline-flex items-center justify-center space-x-1"
                        >
                          <UserCheck className="w-3 h-3" />
                          <span>设为管理员</span>
                        </button>
                      )}
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>
      </WidgetErrorBoundary>
    </div>
  );
}
