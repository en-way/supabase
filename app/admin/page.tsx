"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import dynamic from "next/dynamic";
import Link from "next/link";
import { useRouter } from "next/navigation";
import type { User as AuthUser } from "@supabase/supabase-js";
import { AlertCircle, CheckCircle2, KeyRound, Shield } from "lucide-react";
import { supabase } from "@/lib/supabase";
import {
  fetchAnalyticsSnapshot,
  refreshAnalyticsSnapshot,
  type AnalyticsSnapshot,
} from "@/lib/analyticsSnapshot";
import {
  getCircuitBreakerState,
  getSentinelStats,
  resetSentinelState,
  type SentinelStats,
} from "@/lib/quotaSentinel";
import type { ExamRecord } from "@/types/exam";
import type {
  PasswordResetRequestRecord,
  SystemAnnouncementRow,
  UserProfile,
  UserRole,
} from "@/types/user";
import { AdminExamsTab } from "@/components/admin/AdminExamsTab";
import {
  getAdminErrorMessage,
  normalizeAnnouncementType,
  type AdminAnnouncementState,
  type AdminNotice,
  type AdminSettingsState,
  type AdminTab,
  type ExamApprovalActionType,
} from "@/components/admin/types";

const AdminTabLoadingFallback = () => (
  <div className="py-12 text-center text-xs text-slate-400 dark:text-zinc-500">
    正在加载控制台模块...
  </div>
);

const AdminApprovalsTab = dynamic(
  () => import("@/components/admin/AdminApprovalsTab").then((m) => m.AdminApprovalsTab),
  { ssr: false, loading: AdminTabLoadingFallback }
);
const AdminPasswordApprovalsTab = dynamic(
  () =>
    import("@/components/admin/AdminPasswordApprovalsTab").then(
      (m) => m.AdminPasswordApprovalsTab
    ),
  { ssr: false, loading: AdminTabLoadingFallback }
);
const AdminImportTab = dynamic(
  () => import("@/components/admin/AdminImportTab").then((m) => m.AdminImportTab),
  { ssr: false, loading: AdminTabLoadingFallback }
);
const AdminUsersTab = dynamic(
  () => import("@/components/admin/AdminUsersTab").then((m) => m.AdminUsersTab),
  { ssr: false, loading: AdminTabLoadingFallback }
);
const AdminSettingsTab = dynamic(
  () => import("@/components/admin/AdminSettingsTab").then((m) => m.AdminSettingsTab),
  { ssr: false, loading: AdminTabLoadingFallback }
);
const AdminExamEditModal = dynamic(
  () => import("@/components/admin/AdminExamEditModal").then((m) => m.AdminExamEditModal),
  { ssr: false, loading: () => null }
);

const DEFAULT_SETTINGS: AdminSettingsState = {
  maxStudentsLimit: 0,
  registrationEnabled: true,
};

const DEFAULT_ANNOUNCEMENT: AdminAnnouncementState = {
  enabled: false,
  text: "",
  type: "info",
  linkText: "",
  linkUrl: "",
  updatedAt: "",
};

export default function AdminPage() {
  const router = useRouter();
  const [currentUser, setCurrentUser] = useState<AuthUser | null>(null);
  const [currentRole, setCurrentRole] = useState<UserRole | null>(null);
  const [activeTab, setActiveTab] = useState<AdminTab>("exams");

  const [analyticsSnapshot, setAnalyticsSnapshot] = useState<AnalyticsSnapshot | null>(null);
  const [isRefreshingSnapshot, setIsRefreshingSnapshot] = useState(false);

  const [exams, setExams] = useState<ExamRecord[]>([]);
  const [userList, setUserList] = useState<UserProfile[]>([]);
  const [pendingExams, setPendingExams] = useState<ExamRecord[]>([]);
  const [onlineCount, setOnlineCount] = useState<number>(0);

  const [serverSettings, setServerSettings] = useState<AdminSettingsState>(DEFAULT_SETTINGS);
  const [serverAnnouncement, setServerAnnouncement] =
    useState<AdminAnnouncementState>(DEFAULT_ANNOUNCEMENT);
  const [settings, setSettings] = useState<AdminSettingsState>(DEFAULT_SETTINGS);
  const [isSavingSettings, setIsSavingSettings] = useState(false);

  const [announcementSettings, setAnnouncementSettings] =
    useState<AdminAnnouncementState>(DEFAULT_ANNOUNCEMENT);
  const [isSavingAnnouncement, setIsSavingAnnouncement] = useState(false);

  const isSettingsClean =
    settings.maxStudentsLimit === serverSettings.maxStudentsLimit &&
    settings.registrationEnabled === serverSettings.registrationEnabled;

  const isAnnouncementClean =
    announcementSettings.enabled === serverAnnouncement.enabled &&
    announcementSettings.text.trim() === serverAnnouncement.text.trim() &&
    announcementSettings.type === serverAnnouncement.type &&
    announcementSettings.linkText.trim() === serverAnnouncement.linkText.trim() &&
    announcementSettings.linkUrl.trim() === serverAnnouncement.linkUrl.trim();

  const [passwordRequests, setPasswordRequests] = useState<PasswordResetRequestRecord[]>([]);
  const [loadingPwdRequests, setLoadingPwdRequests] = useState(false);
  const [reviewNotes, setReviewNotes] = useState<Record<string, string>>({});
  const [processingRequestId, setProcessingRequestId] = useState<string | null>(null);
  const pendingPasswordRequests = passwordRequests.filter((r) => r.status === "pending");

  const [notice, setNotice] = useState<AdminNotice | null>(null);
  const noticeTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const [sentinelStats, setSentinelStats] = useState<SentinelStats>(() => getSentinelStats());
  const [sentinelStatus, setSentinelStatus] = useState(() => getCircuitBreakerState());

  const [editingExam, setEditingExam] = useState<ExamRecord | null>(null);
  const mountedRef = useRef(true);

  const showNotification = useCallback((type: "success" | "error", text: string) => {
    setNotice({ type, text });
    if (noticeTimerRef.current) {
      clearTimeout(noticeTimerRef.current);
    }
    noticeTimerRef.current = setTimeout(() => {
      if (mountedRef.current) {
        setNotice(null);
      }
      noticeTimerRef.current = null;
    }, 3000);
  }, []);

  useEffect(() => {
    const handleSentinelAlert = (e: Event) => {
      const detail = (e as CustomEvent<{ stats?: SentinelStats }>).detail;
      if (detail?.stats) {
        setSentinelStats(detail.stats);
      }
      setSentinelStatus(getCircuitBreakerState());
    };
    window.addEventListener("enway_sentinel_alert", handleSentinelAlert);
    return () => window.removeEventListener("enway_sentinel_alert", handleSentinelAlert);
  }, []);

  const handleResetSentinel = () => {
    resetSentinelState();
    setSentinelStats(getSentinelStats());
    setSentinelStatus(getCircuitBreakerState());
  };

  const loadExams = useCallback(async () => {
    const { data } = await supabase
      .from("exams")
      .select(
        "id, category_id, title, year, exam_type, duration_minutes, total_score, pass_score, is_published, approval_status, created_at, questions(count), passages(count)"
      )
      .order("created_at", { ascending: false });
    if (data && mountedRef.current) {
      const rows = data as ExamRecord[];
      setExams(rows);
      setPendingExams(
        rows.filter((e) => e.approval_status === "pending_upload" || e.approval_status === "pending_delete")
      );
    }
  }, []);

  const loadUsers = useCallback(async () => {
    const activeWindowAgo = new Date(Date.now() - 20 * 60 * 1000).toISOString();
    const [usersRes, onlineRes] = await Promise.all([
      supabase
        .from("profiles")
        .select("id, username, nickname, role, last_active_at, created_at")
        .order("last_active_at", { ascending: false, nullsFirst: false })
        .limit(100),
      supabase
        .from("profiles")
        .select("id", { count: "exact", head: true })
        .gte("last_active_at", activeWindowAgo),
    ]);
    if (!mountedRef.current) return;
    if (usersRes.data) setUserList(usersRes.data as UserProfile[]);
    if (typeof onlineRes.count === "number") setOnlineCount(onlineRes.count);
  }, []);

  const loadPasswordRequests = useCallback(async () => {
    setLoadingPwdRequests(true);
    try {
      const { data, error } = await supabase
        .from("password_reset_requests")
        .select("id, user_id, username, nickname, role, status, created_at, reviewed_at, review_note")
        .order("created_at", { ascending: false });
      if (error) throw error;
      if (mountedRef.current) {
        setPasswordRequests((data as PasswordResetRequestRecord[] | null) || []);
      }
    } catch (err: unknown) {
      console.warn("Load password reset requests failed:", err);
    } finally {
      if (mountedRef.current) {
        setLoadingPwdRequests(false);
      }
    }
  }, []);

  const loadSettings = useCallback(async () => {
    const { data } = await supabase
      .from("system_settings")
      .select(
        "max_students_limit, registration_enabled, announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at"
      )
      .eq("id", 1)
      .maybeSingle();
    if (data && mountedRef.current) {
      const row = data as SystemAnnouncementRow & {
        max_students_limit?: number | null;
        registration_enabled?: boolean | null;
      };
      const s: AdminSettingsState = {
        maxStudentsLimit: Number(row.max_students_limit || 0),
        registrationEnabled: Boolean(row.registration_enabled),
      };
      setSettings(s);
      setServerSettings(s);

      const a: AdminAnnouncementState = {
        enabled: Boolean(row.announcement_enabled),
        text: row.announcement_text || "",
        type: normalizeAnnouncementType(row.announcement_type),
        linkText: row.announcement_link_text || "",
        linkUrl: row.announcement_link_url || "",
        updatedAt: row.announcement_updated_at || "",
      };
      setAnnouncementSettings(a);
      setServerAnnouncement(a);
    }
  }, []);

  useEffect(() => {
    mountedRef.current = true;

    async function checkRole() {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      const user = session?.user || null;
      if (!user) {
        router.replace("/login");
        return;
      }
      if (!mountedRef.current) return;
      setCurrentUser(user);

      const { data } = await supabase
        .from("profiles")
        .select("role")
        .eq("id", user.id)
        .single();
      if (!mountedRef.current) return;

      const profileRole = (data as { role?: UserRole } | null)?.role;
      if (profileRole === "super_admin" || profileRole === "admin") {
        setCurrentRole(profileRole);
        if (profileRole === "super_admin") {
          await Promise.all([loadExams(), loadUsers(), loadSettings(), loadPasswordRequests()]);
        } else {
          await loadExams();
        }
      } else {
        setCurrentRole("student");
      }
    }

    checkRole();
    return () => {
      mountedRef.current = false;
      if (noticeTimerRef.current) {
        clearTimeout(noticeTimerRef.current);
        noticeTimerRef.current = null;
      }
    };
  }, [router, loadExams, loadUsers, loadSettings, loadPasswordRequests]);

  // Load pre-rendered analytics snapshot from Storage Bucket (0 DB CPU) for Super Admin
  useEffect(() => {
    if (currentRole !== "super_admin") return;

    fetchAnalyticsSnapshot().then(({ snapshot }) => {
      if (snapshot && mountedRef.current) setAnalyticsSnapshot(snapshot);
    });
  }, [currentRole]);

  const handleRefreshSnapshot = async () => {
    setIsRefreshingSnapshot(true);
    try {
      const snap = await refreshAnalyticsSnapshot();
      if (snap) {
        setAnalyticsSnapshot(snap);
        showNotification("success", "统计大盘快照已成功刷新至云端 Storage 桶！");
      }
    } catch (err: unknown) {
      showNotification("error", "刷新快照失败: " + getAdminErrorMessage(err, "未知错误"));
    } finally {
      setIsRefreshingSnapshot(false);
    }
  };

  const handleTogglePublish = async (exam: ExamRecord) => {
    const nextState = !exam.is_published;
    const { error } = await supabase.from("exams").update({ is_published: nextState }).eq("id", exam.id);
    if (!error) {
      loadExams();
      showNotification("success", nextState ? "试卷已公开上架" : "试卷已下架隐藏");
    } else {
      showNotification("error", error.message);
    }
  };

  const handleDeleteExam = async (exam: ExamRecord) => {
    if (currentRole === "super_admin") {
      if (!window.confirm(`确定要彻底删除试卷 "${exam.title}" 及其所有篇章和题目吗？`)) return;
      const { error } = await supabase.from("exams").delete().eq("id", exam.id);
      if (!error) {
        loadExams();
        showNotification("success", "试卷已彻底删除");
      } else {
        showNotification("error", error.message);
      }
    } else {
      if (!window.confirm(`确定要申请删除试卷 "${exam.title}" 吗？该操作需超级管理员批准后生效。`)) return;
      const { error } = await supabase
        .from("exams")
        .update({ approval_status: "pending_delete" })
        .eq("id", exam.id);
      if (!error) {
        loadExams();
        showNotification("success", "已提交删除申请，请等待超级管理员审批");
      } else {
        showNotification("error", error.message);
      }
    }
  };

  const handleApprovalAction = async (examId: string, actionType: ExamApprovalActionType) => {
    try {
      const { error } = await supabase.rpc("super_admin_handle_approval", {
        exam_id: examId,
        action_type: actionType,
      });
      if (error) throw error;
      loadExams();
      showNotification("success", "审批处理完成！");
    } catch (err: unknown) {
      showNotification("error", `审批失败: ${getAdminErrorMessage(err, "未知错误")}`);
    }
  };

  const handleSetRole = async (targetUser: UserProfile, newRole: "student" | "admin") => {
    const roleName = newRole === "admin" ? "普通管理员" : "学员";
    if (!window.confirm(`确定将用户 ${targetUser.username} 的权限调整为【${roleName}】吗？`)) return;

    try {
      const { error } = await supabase.rpc("super_admin_set_user_role", {
        target_user_id: targetUser.id,
        new_role: newRole,
      });
      if (error) throw error;
      loadUsers();
      showNotification("success", `已将 ${targetUser.username} 的身份设为 ${roleName}`);
    } catch (err: unknown) {
      showNotification("error", `角色修改失败: ${getAdminErrorMessage(err, "未知错误")}`);
    }
  };

  const handleReviewPassword = async (requestId: string, approve: boolean) => {
    const defaultNote = approve ? "超级管理员审批通过" : "管理员驳回申请";
    const note = reviewNotes[requestId]?.trim() || defaultNote;
    setProcessingRequestId(requestId);
    try {
      const { data, error } = await supabase.rpc("super_admin_review_password_reset", {
        request_id: requestId,
        approve,
        note,
      });
      if (error) throw error;
      const rpcRes = (data as { message?: string } | null) ?? null;
      showNotification(
        "success",
        rpcRes?.message || (approve ? "已成功批准改密申请，新密码即刻生效！" : "已驳回该改密申请。")
      );
      await loadPasswordRequests();
    } catch (err: unknown) {
      showNotification("error", `审批处理失败: ${getAdminErrorMessage(err, "未知错误")}`);
    } finally {
      setProcessingRequestId(null);
    }
  };

  const handleSaveSettings = async () => {
    if (isSettingsClean) {
      showNotification("success", "当前考务配额设置与云端一致，无需重复保存！");
      return;
    }
    setIsSavingSettings(true);
    try {
      const { error } = await supabase.rpc("super_admin_update_settings", {
        new_limit: settings.maxStudentsLimit,
        is_enabled: settings.registrationEnabled,
      });
      if (error) throw error;
      showNotification("success", "系统配额与注册设置已成功保存！");
      await loadSettings();
    } catch (err: unknown) {
      showNotification("error", `保存失败: ${getAdminErrorMessage(err, "未知错误")}`);
    } finally {
      setIsSavingSettings(false);
    }
  };

  const handleClearAnnouncement = async () => {
    if (!window.confirm("确定要一键清空并下架全站公告吗？\n下架后前台将立即清除置顶横幅及导航栏小喇叭提示。")) {
      return;
    }
    setIsSavingAnnouncement(true);
    try {
      const { error } = await supabase.rpc("super_admin_update_announcement", {
        p_enabled: false,
        p_text: "",
        p_type: "info",
        p_link_text: "",
        p_link_url: "",
      });
      if (error) throw error;
      setAnnouncementSettings(DEFAULT_ANNOUNCEMENT);
      showNotification("success", "全站公告已成功清空并下架！");
      loadSettings();
      window.dispatchEvent(new CustomEvent("enway_announcement_updated"));
    } catch (err: unknown) {
      showNotification("error", `清空下架失败: ${getAdminErrorMessage(err, "未知错误")}`);
    } finally {
      setIsSavingAnnouncement(false);
    }
  };

  const handleSaveAnnouncement = async () => {
    if (isAnnouncementClean) {
      showNotification("success", "当前全站公告与云端一致，无需重复发布！");
      return;
    }
    if (announcementSettings.enabled && !announcementSettings.text.trim()) {
      showNotification("error", "公告正文不能为空！无法发布开启中的全站公告。若需清空下架，请点击【一键清空并下架】。");
      return;
    }
    setIsSavingAnnouncement(true);
    try {
      const { error } = await supabase.rpc("super_admin_update_announcement", {
        p_enabled: announcementSettings.enabled,
        p_text: announcementSettings.text.trim(),
        p_type: announcementSettings.type,
        p_link_text: announcementSettings.linkText.trim(),
        p_link_url: announcementSettings.linkUrl.trim(),
      });
      if (error) throw error;
      showNotification("success", "全站公告已成功保存并同步！");
      await loadSettings();
      window.dispatchEvent(new CustomEvent("enway_announcement_updated"));
      if (announcementSettings.enabled && announcementSettings.text.trim()) {
        window.dispatchEvent(new CustomEvent("enway_reopen_announcement"));
      }
    } catch (err: unknown) {
      showNotification("error", `公告保存失败: ${getAdminErrorMessage(err, "未知错误")}`);
    } finally {
      setIsSavingAnnouncement(false);
    }
  };

  if (currentRole === null) {
    return (
      <div className="py-20 text-center">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-500 font-medium text-sm">正在验证管理权限...</p>
      </div>
    );
  }

  if (currentRole === "student") {
    return (
      <div className="max-w-md mx-auto py-16 text-center bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.08] dark:border-cyan-500/20 shadow-card p-8">
        <div className="w-12 h-12 rounded-xl bg-rose-50 dark:bg-rose-500/10 border border-rose-200/60 dark:border-rose-500/20 flex items-center justify-center mx-auto mb-3.5">
          <Shield className="w-6 h-6 text-rose-600 dark:text-rose-400" />
        </div>
        <h2 className="text-base font-bold text-zinc-900 dark:text-zinc-100 mb-1.5">访问受限</h2>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 mb-6">当前账号不是管理员，无法访问管理控制台。</p>
        <Link
          href="/"
          className="px-4 py-2 bg-zinc-900 hover:bg-zinc-800 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 rounded-xl text-xs font-bold transition-all shadow-sm"
        >
          返回试卷大厅
        </Link>
      </div>
    );
  }

  const isSuperAdmin = currentRole === "super_admin";

  return (
    <div className="space-y-6 animate-in fade-in duration-150">
      {/* Notice Banner */}
      {notice && (
        <div
          className={`p-3.5 rounded-xl border text-xs font-medium flex items-center space-x-2 ${
            notice.type === "success"
              ? "bg-emerald-50/80 border-emerald-200/80 text-emerald-800"
              : "bg-rose-50/80 border-rose-200/80 text-rose-800"
          }`}
        >
          {notice.type === "success" ? (
            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
          ) : (
            <AlertCircle className="w-4 h-4 text-rose-600 shrink-0" />
          )}
          <span>{notice.text}</span>
        </div>
      )}

      {/* Admin Header */}
      <div className="bg-zinc-950 text-white p-6 sm:p-7 rounded-2xl border border-zinc-800/80 dark:border-cyan-500/25 dark:shadow-glow-cyan shadow-subtle flex flex-col lg:flex-row lg:items-center justify-between gap-5 transition-all duration-300">
        <div className="flex items-center space-x-4">
          <div className="w-11 h-11 rounded-xl bg-zinc-900 border border-zinc-800 dark:border-cyan-500/30 flex items-center justify-center font-bold">
            <Shield className="w-5 h-5 text-emerald-400 dark:text-cyber-400" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[10px] font-medium bg-zinc-800 text-zinc-300 border border-zinc-700/60 dark:border-cyan-500/30 dark:text-cyber-300">
                {isSuperAdmin ? "👑 超级管理中心" : "🛡️ 普通管理员工作台"}
              </span>
            </div>
            <h1 className="text-xl font-bold tracking-tight mt-1 text-white">Enway 考务与真题题库控制台</h1>
            <p className="text-xs text-zinc-400 mt-0.5">
              {isSuperAdmin
                ? "最高权限决策 · 试卷发布审批 · 学员密码统一维护 · 人数配额与考务授权"
                : "真题录入与试题维护 · 试卷公开上架需超级管理员审批确认"}
            </p>
          </div>
        </div>

        {/* Tab Controls */}
        <div className="flex items-center gap-1 p-1 bg-zinc-900/90 border border-zinc-800 dark:border-cyan-500/20 rounded-xl overflow-x-auto no-scrollbar max-w-full">
          <button
            onClick={() => setActiveTab("exams")}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap shrink-0 transition-all ${
              activeTab === "exams"
                ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm"
                : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            真题试卷 ({exams.length})
          </button>

          {isSuperAdmin && (
            <>
              <button
                onClick={() => setActiveTab("approvals")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap shrink-0 transition-all flex items-center space-x-1.5 ${
                  activeTab === "approvals"
                    ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm"
                    : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                <span>考务审批</span>
                {pendingExams.length > 0 && (
                  <span className="px-1.5 py-0.2 bg-rose-500 text-white text-[10px] font-bold rounded-full">
                    {pendingExams.length}
                  </span>
                )}
              </button>

              <button
                onClick={() => setActiveTab("pwdApprovals")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap shrink-0 transition-all flex items-center space-x-1.5 ${
                  activeTab === "pwdApprovals"
                    ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm"
                    : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                <KeyRound className="w-3.5 h-3.5" />
                <span>密码审批</span>
                {pendingPasswordRequests.length > 0 && (
                  <span className="px-1.5 py-0.2 bg-amber-500 text-white text-[10px] font-bold rounded-full">
                    {pendingPasswordRequests.length}
                  </span>
                )}
              </button>
            </>
          )}

          <button
            onClick={() => setActiveTab("import")}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap shrink-0 transition-all ${
              activeTab === "import"
                ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm"
                : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            结构化导入
          </button>

          {isSuperAdmin && (
            <>
              <button
                onClick={() => setActiveTab("users")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap shrink-0 transition-all ${
                  activeTab === "users"
                    ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm"
                    : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                学员与考务 ({userList.length})
              </button>

              <button
                onClick={() => setActiveTab("settings")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap shrink-0 transition-all ${
                  activeTab === "settings"
                    ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm"
                    : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                考务配置与配额
              </button>
            </>
          )}
        </div>
      </div>

      {activeTab === "exams" && (
        <AdminExamsTab
          exams={exams}
          isSuperAdmin={isSuperAdmin}
          onOpenEdit={(exam) => setEditingExam(exam)}
          onTogglePublish={handleTogglePublish}
          onDeleteExam={handleDeleteExam}
          onSwitchToImport={() => setActiveTab("import")}
        />
      )}

      {isSuperAdmin && activeTab === "approvals" && (
        <AdminApprovalsTab
          pendingExams={pendingExams}
          onRefresh={loadExams}
          onApprovalAction={handleApprovalAction}
        />
      )}

      {isSuperAdmin && activeTab === "pwdApprovals" && (
        <AdminPasswordApprovalsTab
          passwordRequests={passwordRequests}
          loadingPwdRequests={loadingPwdRequests}
          reviewNotes={reviewNotes}
          processingRequestId={processingRequestId}
          onRefresh={loadPasswordRequests}
          onChangeReviewNote={(requestId, note) =>
            setReviewNotes((prev) => ({ ...prev, [requestId]: note }))
          }
          onReviewPassword={handleReviewPassword}
        />
      )}

      {activeTab === "import" && (
        <AdminImportTab
          currentRole={currentRole}
          currentUserId={currentUser?.id}
          onImported={loadExams}
          onNotify={showNotification}
        />
      )}

      {isSuperAdmin && activeTab === "users" && (
        <AdminUsersTab
          userList={userList}
          onlineCount={onlineCount}
          maxStudentsLimit={settings.maxStudentsLimit}
          pendingPasswordCount={pendingPasswordRequests.length}
          analyticsSnapshot={analyticsSnapshot}
          isRefreshingSnapshot={isRefreshingSnapshot}
          onRefreshSnapshot={handleRefreshSnapshot}
          onOpenPwdApprovals={() => setActiveTab("pwdApprovals")}
          onSetRole={handleSetRole}
        />
      )}

      {isSuperAdmin && activeTab === "settings" && (
        <AdminSettingsTab
          totalUsersCount={userList.length}
          settings={settings}
          isSettingsClean={isSettingsClean}
          isSavingSettings={isSavingSettings}
          onChangeSettings={setSettings}
          onSaveSettings={handleSaveSettings}
          announcementSettings={announcementSettings}
          isAnnouncementClean={isAnnouncementClean}
          isSavingAnnouncement={isSavingAnnouncement}
          onChangeAnnouncement={setAnnouncementSettings}
          onSaveAnnouncement={handleSaveAnnouncement}
          onClearAnnouncement={handleClearAnnouncement}
          sentinelStats={sentinelStats}
          sentinelStatus={sentinelStatus}
          onResetSentinel={handleResetSentinel}
        />
      )}

      {editingExam && (
        <AdminExamEditModal
          exam={editingExam}
          currentRole={currentRole}
          onClose={() => setEditingExam(null)}
          onSaved={loadExams}
          onNotify={showNotification}
        />
      )}
    </div>
  );
}
