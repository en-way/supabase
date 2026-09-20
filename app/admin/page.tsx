"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { 
  Shield, 
  FileText, 
  Upload, 
  Users, 
  KeyRound, 
  CheckCircle2, 
  AlertCircle, 
  Trash2, 
  Plus, 
  Download,
  Eye,
  EyeOff,
  Check,
  X,
  Sliders,
  Sparkles,
  Lock,
  UserCheck,
  UserX,
  RefreshCw,
  Loader2,
  Clock,
  Crown,
  ArrowRightLeft,
  Megaphone,
  Info,
  AlertTriangle,
  ExternalLink,
  ChevronRight
} from "lucide-react";

export default function AdminPage() {
  const router = useRouter();
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [currentRole, setCurrentRole] = useState<"super_admin" | "admin" | "student" | null>(null);
  const [activeTab, setActiveTab] = useState<"exams" | "approvals" | "import" | "users" | "settings">("exams");

  // Exams list
  const [exams, setExams] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  // Users list
  const [userList, setUserList] = useState<any[]>([]);
  // Approvals list (exams pending upload or delete)
  const [pendingExams, setPendingExams] = useState<any[]>([]);

  // System settings
  const [settings, setSettings] = useState<{
    maxStudentsLimit: number;
    registrationEnabled: boolean;
  }>({ maxStudentsLimit: 0, registrationEnabled: true });
  const [isSavingSettings, setIsSavingSettings] = useState(false);

  // Sitewide Announcement settings
  const [announcementSettings, setAnnouncementSettings] = useState<{
    enabled: boolean;
    text: string;
    type: "info" | "warning" | "alert";
    linkText: string;
    linkUrl: string;
    updatedAt: string;
  }>({
    enabled: false,
    text: "",
    type: "info",
    linkText: "",
    linkUrl: "",
    updatedAt: "",
  });
  const [isSavingAnnouncement, setIsSavingAnnouncement] = useState(false);

  // JSON batch import
  const [jsonText, setJsonText] = useState("");
  const [importStatus, setImportStatus] = useState<string>("");

  // Single User Password reset modal
  const [resetTargetUser, setResetTargetUser] = useState<any>(null);
  const [newPassword, setNewPassword] = useState("");
  const [resetNotice, setResetNotice] = useState<string>("");

  // Batch Reset All Students Password modal
  const [showBatchResetModal, setShowBatchResetModal] = useState(false);
  const [batchDefaultPassword, setBatchDefaultPassword] = useState("123456");
  const [isBatchResetting, setIsBatchResetting] = useState(false);

  // Global notice banner
  const [notice, setNotice] = useState<{ type: "success" | "error"; text: string } | null>(null);

  const checkRole = async () => {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.replace("/login");
      return;
    }
    setCurrentUser(user);

    const { data } = await supabase
      .from("profiles")
      .select("role")
      .eq("id", user.id)
      .single();

    if (data?.role === "super_admin" || data?.role === "admin") {
      setCurrentRole(data.role);
      loadExams();
      if (data.role === "super_admin") {
        loadUsers();
        loadSettings();
        loadPendingExams();
      }
    } else {
      setCurrentRole("student");
    }
  };

  useEffect(() => {
    checkRole();
  }, [router]);

  const loadExams = async () => {
    const { data } = await supabase
      .from("exams")
      .select("*, questions(count), passages(count)")
      .order("created_at", { ascending: false });
    if (data) {
      setExams(data);
      setPendingExams(data.filter((e) => e.approval_status === "pending_upload" || e.approval_status === "pending_delete"));
    }
  };

  const loadPendingExams = async () => {
    const { data } = await supabase
      .from("exams")
      .select("*, questions(count), passages(count)")
      .in("approval_status", ["pending_upload", "pending_delete"])
      .order("created_at", { ascending: false });
    if (data) setPendingExams(data);
  };

  const loadUsers = async () => {
    const { data } = await supabase
      .from("profiles")
      .select("*")
      .order("created_at", { ascending: false });
    if (data) setUserList(data);
  };

  const loadSettings = async () => {
    const { data } = await supabase
      .from("system_settings")
      .select("max_students_limit, registration_enabled, announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at")
      .eq("id", 1)
      .maybeSingle();
    if (data) {
      setSettings({
        maxStudentsLimit: Number(data.max_students_limit || 0),
        registrationEnabled: Boolean(data.registration_enabled),
      });
      setAnnouncementSettings({
        enabled: Boolean(data.announcement_enabled),
        text: data.announcement_text || "",
        type: (data.announcement_type as any) || "info",
        linkText: data.announcement_link_text || "",
        linkUrl: data.announcement_link_url || "",
        updatedAt: data.announcement_updated_at || "",
      });
    }
  };

  const showNotification = (type: "success" | "error", text: string) => {
    setNotice({ type, text });
    setTimeout(() => setNotice(null), 3000);
  };

  // Toggle Publish / Unpublish (Direct for Super Admin)
  const handleTogglePublish = async (exam: any) => {
    const nextState = !exam.is_published;
    const { error } = await supabase
      .from("exams")
      .update({ is_published: nextState })
      .eq("id", exam.id);
    if (!error) {
      loadExams();
      showNotification("success", nextState ? "试卷已公开上架" : "试卷已下架隐藏");
    } else {
      showNotification("error", error.message);
    }
  };

  // Delete Exam (Super admin physically deletes; normal admin requests deletion)
  const handleDeleteExam = async (exam: any) => {
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
      // Normal admin: request deletion for super admin approval
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

  // Super Admin: Handle Approval (Approve / Reject)
  const handleApprovalAction = async (examId: string, actionType: "approve_upload" | "reject_upload" | "approve_delete" | "reject_delete") => {
    try {
      const { error } = await supabase.rpc("super_admin_handle_approval", {
        exam_id: examId,
        action_type: actionType,
      });
      if (error) throw error;
      loadExams();
      loadPendingExams();
      showNotification("success", "审批处理完成！");
    } catch (err: any) {
      showNotification("error", `审批失败: ${err.message}`);
    }
  };

  // Super Admin: Set User Role (Assign or Revoke Admin)
  const handleSetRole = async (targetUser: any, newRole: "student" | "admin") => {
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
    } catch (err: any) {
      showNotification("error", `角色修改失败: ${err.message}`);
    }
  };

  // Super Admin: Transfer Single-Seat Ownership
  const handleTransferSuperAdmin = async (targetUser: any) => {
    if (!isSuperAdmin) {
      alert("权限不足：仅当前超级管理员可执行所有权转让。");
      return;
    }
    const promptText = `⚠️ 极高危安全操作确认：\n\n您即将把全站唯一的【超级管理员】身份完整转让给：\n用户: ${targetUser.username} (${targetUser.nickname || "无昵称"})\n\n转让生效后：\n1. 该用户将成为系统唯一的超级管理员；\n2. 您的身份将自动变更为【普通管理员】。\n\n如确认转让，请在下方输入目标用户名 "${targetUser.username}" 进行二次校验：`;
    const input = window.prompt(promptText);
    if (input !== targetUser.username) {
      if (input !== null) alert("输入用户名不匹配，转让操作已终止。");
      return;
    }

    try {
      const { data, error } = await supabase.rpc("super_admin_transfer_ownership", {
        target_admin_id: targetUser.id,
      });
      if (error) throw error;
      showNotification("success", `超级管理员所有权已成功转交至 ${targetUser.username}！您当前已转为普通管理员。`);
      await checkRole();
      loadUsers();
    } catch (err: any) {
      showNotification("error", `超管转让失败: ${err.message}`);
    }
  };

  // Super Admin: Batch Reset All Students Password
  const handleBatchResetPasswords = async () => {
    if (!batchDefaultPassword || batchDefaultPassword.length < 6) {
      alert("批量重置密码至少需 6 位长度");
      return;
    }
    if (!window.confirm(`⚠️ 高危操作确认：\n将把全站所有学员的密码统一重置为: "${batchDefaultPassword}"。\n确定要执行吗？`)) {
      return;
    }

    setIsBatchResetting(true);
    try {
      const { data, error } = await supabase.rpc("super_admin_batch_reset_student_passwords", {
        default_password: batchDefaultPassword,
      });
      if (error) throw error;
      setShowBatchResetModal(false);
      showNotification("success", `一键重置成功！已将全站 ${data || 0} 位学员的密码统一重置。`);
    } catch (err: any) {
      showNotification("error", `批量重置失败: ${err.message}`);
    } finally {
      setIsBatchResetting(false);
    }
  };

  // Super Admin: Save System Quota & Registration Toggle
  const handleSaveSettings = async () => {
    setIsSavingSettings(true);
    try {
      const { error } = await supabase.rpc("super_admin_update_settings", {
        new_limit: settings.maxStudentsLimit,
        is_enabled: settings.registrationEnabled,
      });
      if (error) throw error;
      showNotification("success", "系统配额与注册设置已成功保存！");
    } catch (err: any) {
      showNotification("error", `保存失败: ${err.message}`);
    } finally {
      setIsSavingSettings(false);
    }
  };

  // Super Admin: Clear and take down announcement
  const handleClearAnnouncement = async () => {
    if (!window.confirm("确定要一键清空并下架全站公告吗？\n下架后前台将立即清除置顶横幅及导航栏小喇叭提示。")) {
      return;
    }
    setIsSavingAnnouncement(true);
    try {
      const cleared = {
        enabled: false,
        text: "",
        type: "info" as const,
        linkText: "",
        linkUrl: "",
        updatedAt: "",
      };
      const { error } = await supabase.rpc("super_admin_update_announcement", {
        p_enabled: false,
        p_text: "",
        p_type: "info",
        p_link_text: "",
        p_link_url: "",
      });
      if (error) throw error;
      setAnnouncementSettings(cleared);
      showNotification("success", "全站公告已成功清空并下架！");
      loadSettings();
      window.dispatchEvent(new CustomEvent("enway_announcement_updated"));
    } catch (err: any) {
      showNotification("error", `清空下架失败: ${err.message}`);
    } finally {
      setIsSavingAnnouncement(false);
    }
  };

  // Super Admin: Save Sitewide Announcement
  const handleSaveAnnouncement = async () => {
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
      loadSettings();
      window.dispatchEvent(new CustomEvent("enway_announcement_updated"));
      if (announcementSettings.enabled && announcementSettings.text.trim()) {
        window.dispatchEvent(new CustomEvent("enway_reopen_announcement"));
      }
    } catch (err: any) {
      showNotification("error", `公告保存失败: ${err.message}`);
    } finally {
      setIsSavingAnnouncement(false);
    }
  };

  // Standard JSON Template Download
  const handleDownloadTemplate = () => {
    const template = {
      title: "2025年大学英语四级真题模拟卷(示例)",
      category_id: "cet4",
      year: 2025,
      exam_type: "mock",
      duration_minutes: 60,
      total_score: 100,
      pass_score: 60,
      passages: [
        {
          section_type: "reading",
          title: "Section C: Reading Comprehension",
          content: "Technological innovations in sustainable agriculture are transforming...",
          questions: [
            {
              q_type: "reading_item",
              stem: "What is the primary benefit of modern vertical farming?",
              options: [
                { key: "A", text: "Requires zero energy" },
                { key: "B", text: "Significantly conserves water and land" },
                { key: "C", text: "Completely eliminates the need for seeds" },
                { key: "D", text: "Guarantees lower electricity prices" }
              ],
              correct_answer: "B",
              explanation: "【考点点拨】细节事实题。根据第二段可知闭环水培极大节约了土地与水资源。",
              points: 20
            }
          ]
        }
      ]
    };

    const blob = new Blob([JSON.stringify(template, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "enway_exam_import_template.json";
    a.click();
    URL.revokeObjectURL(url);
  };

  // Batch JSON Import Execution
  const handleBatchImport = async () => {
    setImportStatus("正在解析 JSON...");
    try {
      const data = JSON.parse(jsonText);
      if (!data.title || !data.category_id || !Array.isArray(data.passages)) {
        throw new Error("JSON 格式不符合规范，缺少必要字段 (title, category_id, passages)");
      }

      setImportStatus("正在写入试卷主表...");
      // For super admin: auto-approve; For normal admin: pending_upload
      const isSuper = currentRole === "super_admin";
      const approvalStatus = isSuper ? "approved" : "pending_upload";
      const isPublished = isSuper;

      const { data: examData, error: examErr } = await supabase
        .from("exams")
        .insert({
          title: data.title,
          category_id: data.category_id,
          year: data.year || new Date().getFullYear(),
          exam_type: data.exam_type || "real",
          duration_minutes: data.duration_minutes || 60,
          total_score: data.total_score || 100,
          pass_score: data.pass_score || 60,
          is_published: isPublished,
          approval_status: approvalStatus,
          created_by: currentUser?.id,
        })
        .select()
        .single();

      if (examErr) throw examErr;

      setImportStatus("正在写入篇章与题目...");
      for (let i = 0; i < data.passages.length; i++) {
        const p = data.passages[i];
        const { data: passageData, error: pErr } = await supabase
          .from("passages")
          .insert({
            exam_id: examData.id,
            category_id: data.category_id,
            section_type: p.section_type || "reading",
            title: p.title || `Passage ${i + 1}`,
            content: p.content || "",
            sort_order: i + 1,
          })
          .select()
          .single();

        if (pErr) throw pErr;

        if (Array.isArray(p.questions)) {
          const questionRows = p.questions.map((q: any, qIdx: number) => ({
            exam_id: examData.id,
            passage_id: passageData.id,
            category_id: data.category_id,
            q_type: q.q_type || "reading_item",
            stem: q.stem,
            options: q.options,
            correct_answer: q.correct_answer,
            explanation: q.explanation || "暂无详细解析",
            points: q.points || 20,
            sort_order: qIdx + 1,
          }));

          const { error: qErr } = await supabase.from("questions").insert(questionRows);
          if (qErr) throw qErr;
        }
      }

      if (isSuper) {
        setImportStatus("✅ 试卷与题目导入成功！已由超级管理员直接发布。");
        showNotification("success", "试卷导入并自动发布成功！");
      } else {
        setImportStatus("⏳ 试卷与题目上传成功！已标记为待审核，待超级管理员批准后即可发布上架。");
        showNotification("success", "试卷上传成功，请等待超级管理员审批！");
      }

      setJsonText("");
      loadExams();
    } catch (err: any) {
      setImportStatus(`❌ 导入失败: ${err.message}`);
    }
  };

  // Reset Single Student Password
  const handleExecuteResetPassword = async () => {
    if (!resetTargetUser || newPassword.length < 6) {
      setResetNotice("密码长度至少需 6 位");
      return;
    }

    try {
      const { error } = await supabase.rpc("admin_reset_user_password", {
        target_user_id: resetTargetUser.id,
        new_plain_password: newPassword,
      });

      if (error) throw error;

      setResetNotice("密码修改成功！");
      setTimeout(() => {
        setResetTargetUser(null);
        setNewPassword("");
        setResetNotice("");
        showNotification("success", `已成功重置学员 ${resetTargetUser.username} 的密码！`);
      }, 1000);
    } catch (err: any) {
      setResetNotice(`修改失败: ${err.message}`);
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
      <div className="max-w-md mx-auto py-16 text-center bg-white rounded-2xl border border-black/[0.08] shadow-card p-8">
        <div className="w-12 h-12 rounded-xl bg-rose-50 border border-rose-200/60 flex items-center justify-center mx-auto mb-3.5">
          <Shield className="w-6 h-6 text-rose-600" />
        </div>
        <h2 className="text-base font-bold text-zinc-900 mb-1.5">访问受限</h2>
        <p className="text-xs text-zinc-500 mb-6">
          当前账号不是管理员，无法访问管理控制台。
        </p>
        <Link href="/" className="px-4 py-2 bg-zinc-900 hover:bg-zinc-800 text-white rounded-xl text-xs font-medium transition-all shadow-sm">
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
        <div className={`p-3.5 rounded-xl border text-xs font-medium flex items-center space-x-2 ${
          notice.type === "success" 
            ? "bg-emerald-50/80 border-emerald-200/80 text-emerald-800" 
            : "bg-rose-50/80 border-rose-200/80 text-rose-800"
        }`}>
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
            <h1 className="text-xl font-bold tracking-tight mt-1 text-white">
              Enway 考务与真题题库控制台
            </h1>
            <p className="text-xs text-zinc-400 mt-0.5">
              {isSuperAdmin 
                ? "最高权限决策 · 试卷发布审批 · 学员密码统一维护 · 人数配额与考务授权" 
                : "真题录入与试题维护 · 试卷公开上架需超级管理员审批确认"}
            </p>
          </div>
        </div>

        {/* Tab Controls */}
        <div className="flex flex-wrap items-center gap-1 p-1 bg-zinc-900/90 border border-zinc-800 dark:border-cyan-500/20 rounded-xl">
          <button
            onClick={() => setActiveTab("exams")}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === "exams" ? "bg-white text-zinc-900 shadow-sm" : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            真题试卷 ({exams.length})
          </button>

          {isSuperAdmin && (
            <button
              onClick={() => setActiveTab("approvals")}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center space-x-1.5 ${
                activeTab === "approvals" ? "bg-white text-zinc-900 shadow-sm" : "text-zinc-400 hover:text-zinc-200"
              }`}
            >
              <span>考务审批</span>
              {pendingExams.length > 0 && (
                <span className="px-1.5 py-0.2 bg-rose-500 text-white text-[10px] font-bold rounded-full">
                  {pendingExams.length}
                </span>
              )}
            </button>
          )}

          <button
            onClick={() => setActiveTab("import")}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === "import" ? "bg-white text-zinc-900 shadow-sm" : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            结构化导入
          </button>

          {isSuperAdmin && (
            <>
              <button
                onClick={() => setActiveTab("users")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  activeTab === "users" ? "bg-white text-zinc-900 shadow-sm" : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                学员与考务 ({userList.length})
              </button>

              <button
                onClick={() => setActiveTab("settings")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  activeTab === "settings" ? "bg-white text-zinc-900 shadow-sm" : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                考务配置与配额
              </button>
            </>
          )}
        </div>
      </div>

      {/* ========================================================================= */}
      {/* Tab 1: Exams Management                                                   */}
      {/* ========================================================================= */}
      {activeTab === "exams" && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-slate-900">题库试卷总览</h3>
            <button
              onClick={() => setActiveTab("import")}
              className="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold flex items-center space-x-1.5 shadow-sm"
            >
              <Plus className="w-3.5 h-3.5" />
              <span>导入新试卷</span>
            </button>
          </div>

          <div className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-700">
                <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
                  <tr>
                    <th className="p-4">试卷标题</th>
                    <th className="p-4">科目</th>
                    <th className="p-4">篇章 / 题数</th>
                    <th className="p-4">满分 / 及格</th>
                    <th className="p-4">审核状态</th>
                    <th className="p-4">上架状态</th>
                    <th className="p-4 text-right">操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {exams.map((e) => {
                    const isPendingUpload = e.approval_status === "pending_upload";
                    const isPendingDelete = e.approval_status === "pending_delete";
                    const isRejected = e.approval_status === "rejected";

                    return (
                      <tr key={e.id} className="hover:bg-slate-50/60 transition-colors">
                        <td className="p-4 font-bold text-slate-900 max-w-xs truncate">{e.title}</td>
                        <td className="p-4 uppercase font-semibold text-indigo-600">{e.category_id}</td>
                        <td className="p-4 text-slate-500">
                          {e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题
                        </td>
                        <td className="p-4">{e.total_score}分 / {e.pass_score}分</td>
                        <td className="p-4">
                          {isPendingUpload ? (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-amber-100 text-amber-800 flex items-center w-fit space-x-1">
                              <Clock className="w-3 h-3" />
                              <span>待超管审批</span>
                            </span>
                          ) : isPendingDelete ? (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-rose-100 text-rose-800 flex items-center w-fit space-x-1">
                              <Trash2 className="w-3 h-3" />
                              <span>申请删除中</span>
                            </span>
                          ) : isRejected ? (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-slate-100 text-slate-500">
                              已驳回
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-emerald-100 text-emerald-800">
                              已通过
                            </span>
                          )}
                        </td>
                        <td className="p-4">
                          <span className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                            e.is_published ? "bg-emerald-100 text-emerald-700" : "bg-slate-100 text-slate-500"
                          }`}>
                            {e.is_published ? "公开可见" : "隐藏未发布"}
                          </span>
                        </td>
                        <td className="p-4 text-right space-x-2">
                          {isSuperAdmin && (
                            <button
                              onClick={() => handleTogglePublish(e)}
                              title={e.is_published ? "点击下架隐藏" : "点击上架公开"}
                              className="p-1.5 text-slate-400 hover:text-indigo-600 rounded-lg"
                            >
                              {e.is_published ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                            </button>
                          )}
                          <button
                            onClick={() => handleDeleteExam(e)}
                            title={isSuperAdmin ? "彻底物理删除" : "申请删除(需超管审批)"}
                            className="p-1.5 text-slate-400 hover:text-rose-600 rounded-lg"
                          >
                            <Trash2 className="w-4 h-4" />
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* Tab 2: Super Admin Approvals Queue                                        */}
      {/* ========================================================================= */}
      {isSuperAdmin && activeTab === "approvals" && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-base font-bold text-slate-900">试卷待审批大厅</h3>
              <p className="text-xs text-slate-500 mt-0.5">
                普通管理员提交的新试卷与删除申请，需在此由超级管理员核准
              </p>
            </div>
            <button
              onClick={loadPendingExams}
              className="p-2 text-slate-500 hover:bg-slate-100 rounded-xl"
              title="刷新待审列表"
            >
              <RefreshCw className="w-4 h-4" />
            </button>
          </div>

          {pendingExams.length === 0 ? (
            <div className="text-center py-16 bg-white rounded-2xl border border-dashed border-slate-300">
              <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
              <p className="text-slate-600 font-bold text-sm">当前暂无待审批的试卷申请</p>
              <p className="text-xs text-slate-400 mt-1">普通管理员提交的上传或删除将会实时出现在这里</p>
            </div>
          ) : (
            <div className="grid gap-4">
              {pendingExams.map((item) => {
                const isUpload = item.approval_status === "pending_upload";
                return (
                  <div
                    key={item.id}
                    className="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4"
                  >
                    <div className="space-y-1.5">
                      <div className="flex items-center space-x-2">
                        <span className={`px-2.5 py-0.5 rounded-md text-[10px] font-bold ${
                          isUpload ? "bg-amber-100 text-amber-800" : "bg-rose-100 text-rose-800"
                        }`}>
                          {isUpload ? "📤 新试卷上传待审" : "🗑️ 申请删除试卷待审"}
                        </span>
                        <span className="text-xs font-mono font-bold text-indigo-600 uppercase">
                          {item.category_id}
                        </span>
                        <span className="text-xs text-slate-400">
                          年份: {item.year}
                        </span>
                      </div>
                      <h4 className="text-sm font-bold text-slate-900">{item.title}</h4>
                      <p className="text-xs text-slate-500">
                        篇章: {item.passages?.[0]?.count || 0} 篇 · 包含客观题: {item.questions?.[0]?.count || 0} 道 · 提交时间: {new Date(item.created_at).toLocaleString()}
                      </p>
                    </div>

                    <div className="flex items-center space-x-2 shrink-0">
                      {isUpload ? (
                        <>
                          <button
                            onClick={() => handleApprovalAction(item.id, "approve_upload")}
                            className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm"
                          >
                            <Check className="w-3.5 h-3.5" />
                            <span>批准发布上架</span>
                          </button>
                          <button
                            onClick={() => handleApprovalAction(item.id, "reject_upload")}
                            className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-semibold flex items-center space-x-1.5"
                          >
                            <X className="w-3.5 h-3.5" />
                            <span>驳回上传</span>
                          </button>
                        </>
                      ) : (
                        <>
                          <button
                            onClick={() => handleApprovalAction(item.id, "approve_delete")}
                            className="px-3.5 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm"
                          >
                            <Trash2 className="w-3.5 h-3.5" />
                            <span>批准彻底删除</span>
                          </button>
                          <button
                            onClick={() => handleApprovalAction(item.id, "reject_delete")}
                            className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-semibold flex items-center space-x-1.5"
                          >
                            <X className="w-3.5 h-3.5" />
                            <span>驳回删除申请</span>
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* ========================================================================= */}
      {/* Tab 3: Standard JSON Batch Import                                         */}
      {/* ========================================================================= */}
      {activeTab === "import" && (
        <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 space-y-6 shadow-sm">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100">
            <div>
              <h3 className="text-base font-bold text-slate-900">标准 JSON 结构化整卷导入</h3>
              <p className="text-xs text-slate-500 mt-0.5">
                一次性批量导入长篇阅读材料、完形填空、单选题干、选项与详细解析
              </p>
            </div>
            <button
              onClick={handleDownloadTemplate}
              className="px-3.5 py-2 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 text-xs font-semibold flex items-center space-x-1.5"
            >
              <Download className="w-3.5 h-3.5 text-slate-500" />
              <span>下载标准 JSON 示例模版</span>
            </button>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-2">
              在此粘贴整套试卷 JSON 内容:
            </label>
            <textarea
              rows={14}
              value={jsonText}
              onChange={(e) => setJsonText(e.target.value)}
              placeholder="请粘贴符合规范的标准 JSON 内容..."
              className="w-full font-mono text-xs p-4 bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          {importStatus && (
            <div className="p-3 bg-slate-100 rounded-xl text-xs font-mono font-medium text-slate-800">
              {importStatus}
            </div>
          )}

          <div className="flex justify-between items-center">
            <span className="text-xs text-slate-400">
              {isSuperAdmin ? "超级管理员导入将直接上架" : "普通管理员导入将自动提交超管审批"}
            </span>
            <button
              onClick={handleBatchImport}
              disabled={!jsonText.trim()}
              className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white text-xs font-bold rounded-xl shadow-md shadow-indigo-200 flex items-center space-x-2 transition-all"
            >
              <Upload className="w-4 h-4" />
              <span>开始整卷导入</span>
            </button>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* Tab 4: Users & Roles (Super Admin Exclusive)                              */}
      {/* ========================================================================= */}
      {isSuperAdmin && activeTab === "users" && (
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h3 className="text-base font-bold text-slate-900">学员账号与权限管理</h3>
              <p className="text-xs text-slate-500 mt-0.5">
                支持任命/降职普通管理员、重置单人密码及一键批量重置所有学员密码
              </p>
            </div>
            
            {/* Batch Reset All Students Button */}
            <button
              onClick={() => setShowBatchResetModal(true)}
              className="px-4 py-2 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-700 hover:to-amber-700 text-white rounded-xl text-xs font-bold flex items-center space-x-2 shadow-sm"
            >
              <KeyRound className="w-3.5 h-3.5" />
              <span>🔥 一键重置所有学员密码</span>
            </button>
          </div>

          <div className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-700">
                <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-semibold">
                  <tr>
                    <th className="p-4">用户名 / 学号</th>
                    <th className="p-4">昵称</th>
                    <th className="p-4">权限角色</th>
                    <th className="p-4">注册时间</th>
                    <th className="p-4 text-right">角色调整</th>
                    <th className="p-4 text-right">密码操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {userList.map((u) => {
                    const isSuper = u.role === "super_admin";
                    const isAdmin = u.role === "admin";
                    const isStudent = u.role === "student";

                    return (
                      <tr key={u.id} className="hover:bg-slate-50/60 transition-colors">
                        <td className="p-4 font-mono font-bold text-slate-900">{u.username}</td>
                        <td className="p-4">{u.nickname || "--"}</td>
                        <td className="p-4">
                          {isSuper ? (
                            <span className="px-2.5 py-1 rounded-full font-black text-[10px] bg-gradient-to-r from-amber-500/15 via-purple-500/15 to-indigo-500/15 text-amber-900 border border-amber-300/80 inline-flex items-center space-x-1 shadow-xs">
                              <Crown className="w-3 h-3 text-amber-600 fill-amber-400" />
                              <span>👑 超级管理员 (全站独占)</span>
                            </span>
                          ) : isAdmin ? (
                            <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-indigo-100 text-indigo-800">
                              🛡️ 普通管理员
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-full font-bold text-[10px] bg-slate-100 text-slate-600">
                              🎓 学员
                            </span>
                          )}
                        </td>
                        <td className="p-4 text-slate-400 font-mono">
                          {new Date(u.created_at).toLocaleDateString()}
                        </td>
                        <td className="p-4 text-right">
                          {isSuper ? (
                            <span className="text-[11px] text-slate-400 italic">全站独占最高席位</span>
                          ) : isAdmin ? (
                            <div className="flex items-center justify-end space-x-1.5">
                              {isSuperAdmin && (
                                <button
                                  onClick={() => handleTransferSuperAdmin(u)}
                                  className="px-2 py-1 text-amber-700 bg-amber-50 hover:bg-amber-100 border border-amber-200/80 rounded-lg text-xs font-bold inline-flex items-center space-x-1 transition-all"
                                  title="将全站唯一的超级管理员所有权安全转让给该管理员"
                                >
                                  <ArrowRightLeft className="w-3 h-3 text-amber-600" />
                                  <span>转让超管</span>
                                </button>
                              )}
                              <button
                                onClick={() => handleSetRole(u, "student")}
                                className="px-2.5 py-1 text-rose-600 bg-rose-50 hover:bg-rose-100 rounded-lg text-xs font-semibold inline-flex items-center space-x-1"
                              >
                                <UserX className="w-3 h-3" />
                                <span>降为学员</span>
                              </button>
                            </div>
                          ) : (
                            <button
                              onClick={() => handleSetRole(u, "admin")}
                              className="px-2.5 py-1 text-indigo-600 bg-indigo-50 hover:bg-indigo-100 rounded-lg text-xs font-semibold inline-flex items-center space-x-1"
                            >
                              <UserCheck className="w-3 h-3" />
                              <span>设为管理员</span>
                            </button>
                          )}
                        </td>
                        <td className="p-4 text-right">
                          <button
                            onClick={() => {
                              setResetTargetUser(u);
                              setNewPassword("");
                              setResetNotice("");
                            }}
                            className="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-semibold inline-flex items-center space-x-1"
                          >
                            <KeyRound className="w-3 h-3 text-indigo-600" />
                            <span>改密</span>
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* Tab 5: Settings & Quota (Super Admin Exclusive)                           */}
      {/* ========================================================================= */}
      {isSuperAdmin && activeTab === "settings" && (
        <div className="space-y-6 max-w-3xl">
          {/* Card 1: Sitewide Announcement */}
          <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 space-y-6 shadow-sm">
            <div className="flex items-center justify-between border-b border-slate-100 pb-4">
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold shadow-xs">
                  <Megaphone className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-bold text-slate-900">全站置顶公告管理</h3>
                  <p className="text-xs text-slate-500 mt-0.5">
                    发布置顶全站横幅，关闭后自动收纳至导航栏小喇叭，零数据库写消耗
                  </p>
                </div>
              </div>

              <label className="flex items-center space-x-2 cursor-pointer bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-100 transition-colors">
                <span className="text-xs font-bold text-slate-700">启用置顶</span>
                <input
                  type="checkbox"
                  checked={announcementSettings.enabled}
                  onChange={(e) => setAnnouncementSettings({ ...announcementSettings, enabled: e.target.checked })}
                  className="w-4 h-4 text-indigo-600 rounded focus:ring-indigo-500 cursor-pointer"
                />
              </label>
            </div>

            <div className="space-y-4">
              {/* Theme style selector */}
              <div>
                <label className="block text-xs font-bold text-slate-800 mb-2">公告主题风格</label>
                <div className="grid grid-cols-3 gap-3">
                  <button
                    type="button"
                    onClick={() => setAnnouncementSettings({ ...announcementSettings, type: "info" })}
                    className={`p-3 rounded-2xl border text-xs font-bold flex items-center justify-center space-x-2 transition-all ${
                      announcementSettings.type === "info"
                        ? "bg-blue-50 border-blue-500 text-blue-800 ring-2 ring-blue-400/20 shadow-xs"
                        : "bg-slate-50 border-slate-200 text-slate-600 hover:bg-slate-100"
                    }`}
                  >
                    <Info className="w-4 h-4 text-blue-600" />
                    <span>信息蓝 (日常通知)</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => setAnnouncementSettings({ ...announcementSettings, type: "warning" })}
                    className={`p-3 rounded-2xl border text-xs font-bold flex items-center justify-center space-x-2 transition-all ${
                      announcementSettings.type === "warning"
                        ? "bg-amber-50 border-amber-500 text-amber-800 ring-2 ring-amber-400/20 shadow-xs"
                        : "bg-slate-50 border-slate-200 text-slate-600 hover:bg-slate-100"
                    }`}
                  >
                    <AlertTriangle className="w-4 h-4 text-amber-600" />
                    <span>警示黄 (维护/提醒)</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => setAnnouncementSettings({ ...announcementSettings, type: "alert" })}
                    className={`p-3 rounded-2xl border text-xs font-bold flex items-center justify-center space-x-2 transition-all ${
                      announcementSettings.type === "alert"
                        ? "bg-rose-50 border-rose-500 text-rose-800 ring-2 ring-rose-400/20 shadow-xs"
                        : "bg-slate-50 border-slate-200 text-slate-600 hover:bg-slate-100"
                    }`}
                  >
                    <AlertCircle className="w-4 h-4 text-rose-600" />
                    <span>紧急红 (重大事项)</span>
                  </button>
                </div>
              </div>

              {/* Textarea */}
              <div>
                <label className="block text-xs font-bold text-slate-800 mb-1">公告正文文案</label>
                <textarea
                  rows={3}
                  value={announcementSettings.text}
                  onChange={(e) => setAnnouncementSettings({ ...announcementSettings, text: e.target.value })}
                  placeholder="请输入面向全站考生的公告通知内容（例如：2024考研真题已更新，支持查词与左右键换题...）"
                  className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-2xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
              </div>

              {/* Action Button & Link */}
              <div className="grid sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-bold text-slate-800 mb-1">附带跳转按钮文字 (可选)</label>
                  <input
                    type="text"
                    value={announcementSettings.linkText}
                    onChange={(e) => setAnnouncementSettings({ ...announcementSettings, linkText: e.target.value })}
                    placeholder="例如: 立即前往做题"
                    className="w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-800 mb-1">跳转目标路由或链接 (可选)</label>
                  <input
                    type="text"
                    value={announcementSettings.linkUrl}
                    onChange={(e) => setAnnouncementSettings({ ...announcementSettings, linkUrl: e.target.value })}
                    placeholder="例如: /practice?id=xxx 或 https://..."
                    className="w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>
              </div>

              {/* Live Preview */}
              <div>
                <label className="block text-xs font-bold text-slate-400 mb-1.5">所见即所得前台实时预览</label>
                <div className={`p-3 rounded-2xl border flex items-center justify-between gap-3 text-xs ${
                  announcementSettings.type === "info"
                    ? "bg-blue-50 border-blue-200 text-blue-950"
                    : announcementSettings.type === "warning"
                    ? "bg-amber-50 border-amber-200 text-amber-950"
                    : "bg-rose-50 border-rose-200 text-rose-950"
                }`}>
                  <div className="flex items-center space-x-2 flex-1 min-w-0">
                    <Megaphone className="w-4 h-4 shrink-0 text-indigo-600" />
                    <span className="font-semibold truncate">
                      {announcementSettings.text || "公告内容将在此实时预览呈现..."}
                    </span>
                    {announcementSettings.linkText && (
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-slate-900 text-white shrink-0">
                        {announcementSettings.linkText} →
                      </span>
                    )}
                  </div>
                  <div className="text-slate-400 text-[10px] shrink-0 font-mono">
                    {announcementSettings.enabled ? "● 开启展示" : "○ 未开启"}
                  </div>
                </div>
              </div>

              {/* Actions: Clear & Save */}
              <div className="pt-2 flex flex-wrap items-center justify-between gap-3">
                <button
                  type="button"
                  onClick={handleClearAnnouncement}
                  disabled={isSavingAnnouncement || (!announcementSettings.text && !announcementSettings.enabled)}
                  className="px-4 py-2.5 bg-rose-50 hover:bg-rose-100 disabled:opacity-40 disabled:cursor-not-allowed text-rose-700 border border-rose-200 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition-all"
                  title="一键清空文案并关闭全站公告"
                >
                  <Trash2 className="w-4 h-4" />
                  <span>一键清空并下架公告</span>
                </button>

                <button
                  onClick={handleSaveAnnouncement}
                  disabled={isSavingAnnouncement}
                  className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white rounded-xl text-xs font-bold shadow-md shadow-indigo-200 flex items-center space-x-2 transition-all"
                >
                  {isSavingAnnouncement ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <Sparkles className="w-4 h-4" />
                  )}
                  <span>保存并全站发布公告</span>
                </button>
              </div>
            </div>
          </div>

          {/* Card 2: System Registration Quota */}
          <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 space-y-6 shadow-sm">
            <div>
              <h3 className="text-base font-bold text-slate-900">系统运行与人数配额配置</h3>
              <p className="text-xs text-slate-500 mt-0.5">
                控制全站注册学员人数上限与新用户注册准入开关
              </p>
            </div>

            <div className="space-y-5 pt-2">
              <div>
                <label className="block text-xs font-bold text-slate-800 mb-1">
                  全站学员人数上限 (人)
                </label>
                <input
                  type="number"
                  min={0}
                  value={settings.maxStudentsLimit}
                  onChange={(e) => setSettings({ ...settings, maxStudentsLimit: parseInt(e.target.value) || 0 })}
                  className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
                <p className="text-[11px] text-slate-400 mt-1">
                  设置为 0 表示不设人数上限（无限注册）。当注册人数达到此数值时，新用户注册将被系统硬校验拦截。
                </p>
              </div>

              <div className="flex items-center justify-between p-4 bg-slate-50 rounded-2xl border border-slate-200">
                <div>
                  <h4 className="text-xs font-bold text-slate-900">开放学员注册通道</h4>
                  <p className="text-[11px] text-slate-500 mt-0.5">
                    若关闭，注册通道将被临时封锁，任何新用户均无法注册
                  </p>
                </div>
                <input
                  type="checkbox"
                  checked={settings.registrationEnabled}
                  onChange={(e) => setSettings({ ...settings, registrationEnabled: e.target.checked })}
                  className="w-5 h-5 text-indigo-600 rounded focus:ring-indigo-500 cursor-pointer"
                />
              </div>

              <div className="pt-4 flex justify-end">
                <button
                  onClick={handleSaveSettings}
                  disabled={isSavingSettings}
                  className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white rounded-xl text-xs font-bold shadow-md shadow-indigo-200 flex items-center space-x-2"
                >
                  {isSavingSettings ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <span>保存系统配置</span>
                  )}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* Modal 1: Single User Password Reset                                       */}
      {/* ========================================================================= */}
      {resetTargetUser && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl max-w-sm w-full p-6 shadow-2xl space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-2 text-indigo-600">
              <KeyRound className="w-5 h-5" />
              <h3 className="font-bold text-slate-900 text-base">重置密码</h3>
            </div>

            <p className="text-xs text-slate-500">
              正在为用户 <strong className="text-slate-800">{resetTargetUser.username}</strong> ({resetTargetUser.nickname}) 设置新密码。
            </p>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                新密码 (至少 6 位)
              </label>
              <input
                type="text"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                placeholder="输入新密码..."
                className="w-full px-3 py-2 border border-slate-200 rounded-xl text-xs font-mono focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
            </div>

            {resetNotice && (
              <div className="text-xs font-bold text-indigo-700 bg-indigo-50 p-2 rounded-lg">
                {resetNotice}
              </div>
            )}

            <div className="flex justify-end space-x-2 pt-2">
              <button
                type="button"
                onClick={() => setResetTargetUser(null)}
                className="px-3 py-2 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded-xl"
              >
                取消
              </button>
              <button
                type="button"
                onClick={handleExecuteResetPassword}
                disabled={newPassword.length < 6}
                className="px-4 py-2 text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white rounded-xl shadow-sm"
              >
                确认重置
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* Modal 2: Batch Reset All Students Password (Super Admin Exclusive)        */}
      {/* ========================================================================= */}
      {showBatchResetModal && (
        <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-2.5 text-rose-600">
              <div className="p-2 bg-rose-50 rounded-xl">
                <KeyRound className="w-5 h-5" />
              </div>
              <div>
                <h3 className="font-bold text-slate-900 text-base">一键重置全员学员密码</h3>
                <p className="text-[11px] text-slate-400">超级管理员专享全局操作</p>
              </div>
            </div>

            <div className="p-3 bg-amber-50 border border-amber-200 rounded-2xl text-xs text-amber-800 leading-relaxed">
              ⚠️ <strong>注意</strong>：该操作将把全站<strong>所有普通学员 (student)</strong> 的登录密码一次性重置为下方设置的统一初始密码。管理员密码不受影响。
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                统一默认密码 (至少 6 位)
              </label>
              <input
                type="text"
                value={batchDefaultPassword}
                onChange={(e) => setBatchDefaultPassword(e.target.value)}
                placeholder="例如 123456"
                className="w-full px-3.5 py-2.5 border border-slate-200 rounded-xl text-xs font-mono font-bold focus:outline-none focus:ring-2 focus:ring-rose-500"
              />
            </div>

            <div className="flex justify-end space-x-2 pt-2">
              <button
                type="button"
                onClick={() => setShowBatchResetModal(false)}
                disabled={isBatchResetting}
                className="px-4 py-2.5 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded-xl"
              >
                取消
              </button>
              <button
                type="button"
                onClick={handleBatchResetPasswords}
                disabled={isBatchResetting || batchDefaultPassword.length < 6}
                className="px-5 py-2.5 text-xs font-bold bg-rose-600 hover:bg-rose-700 disabled:opacity-40 text-white rounded-xl shadow-sm flex items-center space-x-2"
              >
                {isBatchResetting ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <span>确认执行全员重置</span>
                )}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
