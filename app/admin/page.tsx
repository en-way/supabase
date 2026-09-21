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
  ChevronRight,
  FileEdit,
  Code2,
  Save,
  Radio,
  Activity
} from "lucide-react";
import { fetchAnalyticsSnapshot, refreshAnalyticsSnapshot, AnalyticsSnapshot } from "@/lib/analyticsSnapshot";
import { WidgetErrorBoundary } from "@/components/WidgetErrorBoundary";

export default function AdminPage() {
  const router = useRouter();
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [currentRole, setCurrentRole] = useState<"super_admin" | "admin" | "student" | null>(null);
  const [activeTab, setActiveTab] = useState<"exams" | "approvals" | "import" | "users" | "settings">("exams");

  // 0-WebSocket architecture: 5-minute activity window detection (0/200 concurrent connection quota consumed)
  const isUserOnline = (u: any) => {
    if (!u?.last_active_at) return false;
    const diff = Date.now() - new Date(u.last_active_at).getTime();
    return diff >= 0 && diff <= 5 * 60 * 1000;
  };
  const [analyticsSnapshot, setAnalyticsSnapshot] = useState<AnalyticsSnapshot | null>(null);
  const [isRefreshingSnapshot, setIsRefreshingSnapshot] = useState(false);
  const [userSortOrder, setUserSortOrder] = useState<"active_desc" | "created_desc">("active_desc");

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

  // Exam Edit / Material & File Modification Modal (Available to Admin & Super Admin)
  const [editingExam, setEditingExam] = useState<any | null>(null);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [editTab, setEditTab] = useState<"form" | "json">("form");
  const [editLoading, setEditLoading] = useState(false);
  const [isSavingEdit, setIsSavingEdit] = useState(false);
  const [jsonSyntaxError, setJsonSyntaxError] = useState<string | null>(null);

  const [editFormData, setEditFormData] = useState<{
    id: string;
    title: string;
    category_id: string;
    year: number;
    exam_type: string;
    duration_minutes: number;
    total_score: number;
    pass_score: number;
    passages: Array<{
      id?: string;
      title: string;
      section_type: string;
      content: string;
      sort_order: number;
    }>;
  }>({
    id: "",
    title: "",
    category_id: "cet4",
    year: 2024,
    exam_type: "real",
    duration_minutes: 60,
    total_score: 100,
    pass_score: 60,
    passages: [],
  });
  const [editJsonText, setEditJsonText] = useState("");

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

  // Load pre-rendered analytics snapshot from Storage Bucket (0 DB CPU) for Super Admin
  useEffect(() => {
    if (currentRole !== "super_admin") return;

    fetchAnalyticsSnapshot().then(({ snapshot }) => {
      if (snapshot) setAnalyticsSnapshot(snapshot);
    });
  }, [currentRole]);

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
      .order("last_active_at", { ascending: false, nullsFirst: false });
    if (data) setUserList(data);
  };

  const handleRefreshSnapshot = async () => {
    setIsRefreshingSnapshot(true);
    try {
      const snap = await refreshAnalyticsSnapshot();
      if (snap) {
        setAnalyticsSnapshot(snap);
        showNotification("success", "统计大盘快照已成功刷新至云端 Storage 桶！");
      }
    } catch (err: any) {
      showNotification("error", "刷新快照失败: " + err.message);
    } finally {
      setIsRefreshingSnapshot(false);
    }
  };

  const formatRelativeTime = (isoString?: string | null) => {
    if (!isoString) return "从未在线";
    const date = new Date(isoString);
    const diffMs = Date.now() - date.getTime();
    if (diffMs < 0 || isNaN(diffMs)) return "刚刚 (在线)";
    const diffSec = Math.floor(diffMs / 1000);
    if (diffSec < 60) return "刚刚 (在线)";
    const diffMin = Math.floor(diffSec / 60);
    if (diffMin <= 5) return "刚刚 (在线)";
    if (diffMin < 60) return `${diffMin}分钟前`;
    const diffHour = Math.floor(diffMin / 60);
    if (diffHour < 24) return `${diffHour}小时前`;
    const diffDay = Math.floor(diffHour / 24);
    if (diffDay < 30) return `${diffDay}天前`;
    return date.toLocaleDateString();
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

  // Open Exam & Material Edit Modal (Fetches full passages and questions)
  const handleOpenEditModal = async (exam: any) => {
    setEditingExam(exam);
    setIsEditModalOpen(true);
    setEditLoading(true);
    setEditTab("form");
    setJsonSyntaxError(null);

    try {
      const { data: fullExam, error: examErr } = await supabase
        .from("exams")
        .select("*")
        .eq("id", exam.id)
        .single();
      if (examErr) throw examErr;

      const { data: passagesData, error: passErr } = await supabase
        .from("passages")
        .select("*")
        .eq("exam_id", exam.id)
        .order("sort_order", { ascending: true });
      if (passErr) throw passErr;

      const { data: questionsData, error: qErr } = await supabase
        .from("questions")
        .select("*")
        .eq("exam_id", exam.id)
        .order("sort_order", { ascending: true });
      if (qErr) throw qErr;

      const passages = (passagesData || []).map((p: any) => ({
        id: p.id,
        title: p.title || "",
        section_type: p.section_type || "reading",
        content: p.content || "",
        sort_order: p.sort_order || 1,
      }));

      setEditFormData({
        id: fullExam.id,
        title: fullExam.title || "",
        category_id: fullExam.category_id || "cet4",
        year: fullExam.year || 2024,
        exam_type: fullExam.exam_type || "real",
        duration_minutes: fullExam.duration_minutes || 60,
        total_score: fullExam.total_score || 100,
        pass_score: fullExam.pass_score || 60,
        passages,
      });

      // Construct complete full exam object (identical to static json structure)
      const fullExamJson = {
        id: fullExam.id,
        title: fullExam.title,
        category_id: fullExam.category_id,
        year: fullExam.year,
        exam_type: fullExam.exam_type,
        duration_minutes: fullExam.duration_minutes,
        total_score: fullExam.total_score,
        pass_score: fullExam.pass_score,
        is_published: fullExam.is_published,
        passages: (passagesData || []).map((p: any) => {
          const pQuestions = (questionsData || [])
            .filter((q: any) => q.passage_id === p.id)
            .map((q: any) => ({
              id: q.id,
              q_type: q.q_type,
              stem: q.stem,
              options: q.options,
              correct_answer: q.correct_answer,
              explanation: q.explanation,
              points: q.points,
              sort_order: q.sort_order,
            }));
          return {
            id: p.id,
            section_type: p.section_type,
            title: p.title,
            content: p.content,
            sort_order: p.sort_order,
            questions: pQuestions,
          };
        }),
      };

      setEditJsonText(JSON.stringify(fullExamJson, null, 2));
    } catch (err: any) {
      showNotification("error", `获取试卷材料失败: ${err.message}`);
    } finally {
      setEditLoading(false);
    }
  };

  // Save Form Edits (Exam metadata and passage materials)
  const handleSaveFormEdit = async () => {
    if (!editingExam) return;
    setIsSavingEdit(true);
    try {
      const { error: examErr } = await supabase
        .from("exams")
        .update({
          title: editFormData.title.trim(),
          category_id: editFormData.category_id,
          year: Number(editFormData.year),
          exam_type: editFormData.exam_type,
          duration_minutes: Number(editFormData.duration_minutes),
          total_score: Number(editFormData.total_score),
          pass_score: Number(editFormData.pass_score),
        })
        .eq("id", editFormData.id);
      if (examErr) throw examErr;

      for (const p of editFormData.passages) {
        if (p.id) {
          const { error: passErr } = await supabase
            .from("passages")
            .update({
              title: p.title.trim(),
              content: p.content,
            })
            .eq("id", p.id);
          if (passErr) throw passErr;
        }
      }

      showNotification("success", "试卷与篇章材料已成功保存更新！");
      setIsEditModalOpen(false);
      loadExams();
    } catch (err: any) {
      showNotification("error", `保存失败: ${err.message}`);
    } finally {
      setIsSavingEdit(false);
    }
  };

  // Save Raw JSON Edits (Full exam, passages, questions update)
  const handleSaveJsonEdit = async () => {
    if (!editingExam) return;
    setIsSavingEdit(true);
    setJsonSyntaxError(null);

    try {
      let parsed: any;
      try {
        parsed = JSON.parse(editJsonText);
      } catch (parseErr: any) {
        setJsonSyntaxError(`JSON 语法解析错误: ${parseErr.message}`);
        throw new Error("JSON 语法格式有误，请修正后再保存");
      }

      if (!parsed.title || !parsed.category_id || !Array.isArray(parsed.passages)) {
        throw new Error("JSON 缺少必要结构字段 (title, category_id, passages)");
      }

      const examId = editingExam.id;

      // 1. Update exams main table
      const { error: examErr } = await supabase
        .from("exams")
        .update({
          title: parsed.title,
          category_id: parsed.category_id,
          year: parsed.year || editingExam.year,
          exam_type: parsed.exam_type || "real",
          duration_minutes: parsed.duration_minutes || 60,
          total_score: parsed.total_score || 100,
          pass_score: parsed.pass_score || 60,
        })
        .eq("id", examId);
      if (examErr) throw examErr;

      // 2. Clear old questions to avoid orphan references
      const { error: delQErr } = await supabase
        .from("questions")
        .delete()
        .eq("exam_id", examId);
      if (delQErr) throw delQErr;

      // 3. Clear old passages
      const { error: delPErr } = await supabase
        .from("passages")
        .delete()
        .eq("exam_id", examId);
      if (delPErr) throw delPErr;

      // 4. Re-insert passages and their questions cleanly
      for (let i = 0; i < parsed.passages.length; i++) {
        const p = parsed.passages[i];
        const { data: newP, error: pInsErr } = await supabase
          .from("passages")
          .insert({
            exam_id: examId,
            category_id: parsed.category_id,
            section_type: p.section_type || "reading",
            title: p.title || `Passage ${i + 1}`,
            content: p.content || "",
            sort_order: p.sort_order || i + 1,
          })
          .select()
          .single();
        if (pInsErr) throw pInsErr;

        if (Array.isArray(p.questions) && p.questions.length > 0) {
          const questionRows = p.questions.map((q: any, qIdx: number) => ({
            exam_id: examId,
            passage_id: newP.id,
            category_id: parsed.category_id,
            q_type: q.q_type || "reading_item",
            stem: q.stem,
            options: q.options,
            correct_answer: q.correct_answer,
            explanation: q.explanation || "暂无详细解析",
            points: q.points || 20,
            sort_order: q.sort_order || qIdx + 1,
          }));

          const { error: qInsErr } = await supabase.from("questions").insert(questionRows);
          if (qInsErr) throw qInsErr;
        }
      }

      showNotification("success", "试卷材料、题目与完整 JSON 已成功同步保存至数据库！");
      setIsEditModalOpen(false);
      loadExams();
    } catch (err: any) {
      showNotification("error", err.message);
    } finally {
      setIsSavingEdit(false);
    }
  };

  const handleFormatJson = () => {
    try {
      const parsed = JSON.parse(editJsonText);
      setEditJsonText(JSON.stringify(parsed, null, 2));
      setJsonSyntaxError(null);
    } catch (err: any) {
      setJsonSyntaxError(`无法格式化，JSON 语法有误: ${err.message}`);
    }
  };

  const handleDownloadCurrentJson = () => {
    try {
      const blob = new Blob([editJsonText], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      const safeTitle = (editingExam?.title || "exam").replace(/[^a-zA-Z0-9_\u4e00-\u9fa5-]/g, "_");
      a.download = `${safeTitle}.json`;
      a.click();
      URL.revokeObjectURL(url);
    } catch (err: any) {
      showNotification("error", `下载失败: ${err.message}`);
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
      <div className="max-w-md mx-auto py-16 text-center bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.08] dark:border-cyan-500/20 shadow-card p-8">
        <div className="w-12 h-12 rounded-xl bg-rose-50 dark:bg-rose-500/10 border border-rose-200/60 dark:border-rose-500/20 flex items-center justify-center mx-auto mb-3.5">
          <Shield className="w-6 h-6 text-rose-600 dark:text-rose-400" />
        </div>
        <h2 className="text-base font-bold text-zinc-900 dark:text-zinc-100 mb-1.5">访问受限</h2>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 mb-6">
          当前账号不是管理员，无法访问管理控制台。
        </p>
        <Link href="/" className="px-4 py-2 bg-zinc-900 hover:bg-zinc-800 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 rounded-xl text-xs font-bold transition-all shadow-sm">
          返回试卷大厅
        </Link>
      </div>
    );
  }

  const isSuperAdmin = currentRole === "super_admin";

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
    return new Date(b.created_at).getTime() - new Date(a.created_at).getTime();
  });

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
              activeTab === "exams" ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm" : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            真题试卷 ({exams.length})
          </button>

          {isSuperAdmin && (
            <button
              onClick={() => setActiveTab("approvals")}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center space-x-1.5 ${
                activeTab === "approvals" ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm" : "text-zinc-400 hover:text-zinc-200"
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
              activeTab === "import" ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm" : "text-zinc-400 hover:text-zinc-200"
            }`}
          >
            结构化导入
          </button>

          {isSuperAdmin && (
            <>
              <button
                onClick={() => setActiveTab("users")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  activeTab === "users" ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm" : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                学员与考务 ({userList.length})
              </button>

              <button
                onClick={() => setActiveTab("settings")}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  activeTab === "settings" ? "bg-white dark:bg-cyan-500 text-zinc-900 dark:text-zinc-950 font-bold shadow-sm" : "text-zinc-400 hover:text-zinc-200"
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
            <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">题库试卷总览</h3>
            <button
              onClick={() => setActiveTab("import")}
              className="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 text-xs font-bold flex items-center space-x-1.5 shadow-sm"
            >
              <Plus className="w-3.5 h-3.5" />
              <span>导入新试卷</span>
            </button>
          </div>

          <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-cyan-500/20 overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-700 dark:text-zinc-300">
                <thead className="bg-slate-50 dark:bg-zinc-900/80 border-b border-slate-200 dark:border-zinc-800 text-slate-500 dark:text-zinc-400 font-semibold">
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
                <tbody className="divide-y divide-slate-100 dark:divide-zinc-800">
                  {exams.map((e) => {
                    const isPendingUpload = e.approval_status === "pending_upload";
                    const isPendingDelete = e.approval_status === "pending_delete";
                    const isRejected = e.approval_status === "rejected";

                    return (
                      <tr key={e.id} className="hover:bg-slate-50/60 dark:hover:bg-zinc-800/40 transition-colors">
                        <td className="p-4 font-bold text-slate-900 dark:text-zinc-100 max-w-xs truncate">{e.title}</td>
                        <td className="p-4 uppercase font-semibold text-indigo-600 dark:text-cyan-400">{e.category_id}</td>
                        <td className="p-4 text-slate-500 dark:text-zinc-400">
                          {e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题
                        </td>
                        <td className="p-4">{e.total_score}分 / {e.pass_score}分</td>
                        <td className="p-4">
                          {isPendingUpload ? (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-amber-100 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-transparent dark:border-amber-500/30 flex items-center w-fit space-x-1">
                              <Clock className="w-3 h-3" />
                              <span>待超管审批</span>
                            </span>
                          ) : isPendingDelete ? (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-rose-100 dark:bg-rose-950/40 text-rose-800 dark:text-rose-300 border border-transparent dark:border-rose-500/30 flex items-center w-fit space-x-1">
                              <Trash2 className="w-3 h-3" />
                              <span>申请删除中</span>
                            </span>
                          ) : isRejected ? (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400">
                              已驳回
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-emerald-100 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border border-transparent dark:border-emerald-500/30">
                              已通过
                            </span>
                          )}
                        </td>
                        <td className="p-4">
                          <span className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                            e.is_published 
                              ? "bg-emerald-100 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-transparent dark:border-emerald-500/30" 
                              : "bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400"
                          }`}>
                            {e.is_published ? "公开可见" : "隐藏未发布"}
                          </span>
                        </td>
                        <td className="p-4 text-right space-x-2 whitespace-nowrap">
                          <button
                            onClick={() => handleOpenEditModal(e)}
                            title="修改材料、题目与完整 JSON 文件"
                            className="inline-flex items-center space-x-1 px-2.5 py-1 text-xs font-semibold text-indigo-600 dark:text-cyan-400 bg-indigo-50 dark:bg-cyan-950/40 hover:bg-indigo-100 dark:hover:bg-cyan-900/50 rounded-lg border border-indigo-200/50 dark:border-cyan-500/30 transition-colors"
                          >
                            <FileEdit className="w-3.5 h-3.5" />
                            <span>修改材料/JSON</span>
                          </button>
                          {isSuperAdmin && (
                            <button
                              onClick={() => handleTogglePublish(e)}
                              title={e.is_published ? "点击下架隐藏" : "点击上架公开"}
                              className="p-1.5 text-slate-400 dark:text-zinc-500 hover:text-indigo-600 dark:hover:text-cyan-400 rounded-lg transition-colors"
                            >
                              {e.is_published ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                            </button>
                          )}
                          <button
                            onClick={() => handleDeleteExam(e)}
                            title={isSuperAdmin ? "彻底物理删除" : "申请删除(需超管审批)"}
                            className="p-1.5 text-slate-400 dark:text-zinc-500 hover:text-rose-600 dark:hover:text-rose-400 rounded-lg transition-colors"
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
              <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">试卷待审批大厅</h3>
              <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
                普通管理员提交的新试卷与删除申请，需在此由超级管理员核准
              </p>
            </div>
            <button
              onClick={loadPendingExams}
              className="p-2 text-slate-500 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
              title="刷新待审列表"
            >
              <RefreshCw className="w-4 h-4" />
            </button>
          </div>

          {pendingExams.length === 0 ? (
            <div className="text-center py-16 bg-white dark:bg-[#11131a] rounded-2xl border border-dashed border-slate-300 dark:border-zinc-800">
              <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
              <p className="text-slate-600 dark:text-zinc-300 font-bold text-sm">当前暂无待审批的试卷申请</p>
              <p className="text-xs text-slate-400 dark:text-zinc-500 mt-1">普通管理员提交的上传或删除将会实时出现在这里</p>
            </div>
          ) : (
            <div className="grid gap-4">
              {pendingExams.map((item) => {
                const isUpload = item.approval_status === "pending_upload";
                return (
                  <div
                    key={item.id}
                    className="p-5 bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-cyan-500/20 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4"
                  >
                    <div className="space-y-1.5">
                      <div className="flex items-center space-x-2">
                        <span className={`px-2.5 py-0.5 rounded-md text-[10px] font-bold ${
                          isUpload 
                            ? "bg-amber-100 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-transparent dark:border-amber-500/30" 
                            : "bg-rose-100 dark:bg-rose-950/40 text-rose-800 dark:text-rose-300 border border-transparent dark:border-rose-500/30"
                        }`}>
                          {isUpload ? "📤 新试卷上传待审" : "🗑️ 申请删除试卷待审"}
                        </span>
                        <span className="text-xs font-mono font-bold text-indigo-600 dark:text-cyan-400 uppercase">
                          {item.category_id}
                        </span>
                        <span className="text-xs text-slate-400 dark:text-zinc-500">
                          年份: {item.year}
                        </span>
                      </div>
                      <h4 className="text-sm font-bold text-slate-900 dark:text-zinc-100">{item.title}</h4>
                      <p className="text-xs text-slate-500 dark:text-zinc-400">
                        篇章: {item.passages?.[0]?.count || 0} 篇 · 包含客观题: {item.questions?.[0]?.count || 0} 道 · 提交时间: {new Date(item.created_at).toLocaleString()}
                      </p>
                    </div>

                    <div className="flex items-center space-x-2 shrink-0">
                      {isUpload ? (
                        <>
                          <button
                            onClick={() => handleApprovalAction(item.id, "approve_upload")}
                            className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-colors"
                          >
                            <Check className="w-3.5 h-3.5" />
                            <span>批准发布上架</span>
                          </button>
                          <button
                            onClick={() => handleApprovalAction(item.id, "reject_upload")}
                            className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-200 rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition-colors"
                          >
                            <X className="w-3.5 h-3.5" />
                            <span>驳回上传</span>
                          </button>
                        </>
                      ) : (
                        <>
                          <button
                            onClick={() => handleApprovalAction(item.id, "approve_delete")}
                            className="px-3.5 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-colors"
                          >
                            <Trash2 className="w-3.5 h-3.5" />
                            <span>批准彻底删除</span>
                          </button>
                          <button
                            onClick={() => handleApprovalAction(item.id, "reject_delete")}
                            className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-200 rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition-colors"
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
        <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/20 p-6 sm:p-8 space-y-6 shadow-sm">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100 dark:border-zinc-800">
            <div>
              <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">标准 JSON 结构化整卷导入</h3>
              <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
                一次性批量导入长篇阅读材料、完形填空、单选题干、选项与详细解析
              </p>
            </div>
            <button
              onClick={handleDownloadTemplate}
              className="px-3.5 py-2 rounded-xl border border-slate-200 dark:border-zinc-700 text-slate-700 dark:text-zinc-300 hover:bg-slate-50 dark:hover:bg-zinc-800 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
            >
              <Download className="w-3.5 h-3.5 text-slate-500 dark:text-zinc-400" />
              <span>下载标准 JSON 示例模版</span>
            </button>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 dark:text-zinc-300 mb-2">
              在此粘贴整套试卷 JSON 内容:
            </label>
            <textarea
              rows={14}
              value={jsonText}
              onChange={(e) => setJsonText(e.target.value)}
              placeholder="请粘贴符合规范的标准 JSON 内容..."
              className="w-full font-mono text-xs p-4 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-2xl focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
            />
          </div>

          {importStatus && (
            <div className="p-3 bg-slate-100 dark:bg-zinc-800/80 text-slate-800 dark:text-zinc-200 border border-transparent dark:border-zinc-700 rounded-xl text-xs font-mono font-medium">
              {importStatus}
            </div>
          )}

          <div className="flex justify-between items-center">
            <span className="text-xs text-slate-400 dark:text-zinc-500">
              {isSuperAdmin ? "超级管理员导入将直接上架" : "普通管理员导入将自动提交超管审批"}
            </span>
            <button
              onClick={handleBatchImport}
              disabled={!jsonText.trim()}
              className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 disabled:opacity-40 text-white dark:text-zinc-950 text-xs font-bold rounded-xl shadow-md shadow-indigo-200 dark:shadow-none flex items-center space-x-2 transition-all"
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
                    {userList.filter(isUserOnline).length} <span className="text-xs font-medium text-slate-500 dark:text-zinc-400 font-sans">人活跃在线</span>
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
                    {userList.filter(u => u.role === "student").length}
                    {settings.maxStudentsLimit > 0 && (
                      <span className="text-xs font-normal text-slate-400 dark:text-zinc-500 font-sans">
                        {" "}/ {settings.maxStudentsLimit} 限额
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
                      <span>{analyticsSnapshot.totalExams} 套试卷 · {analyticsSnapshot.totalBackups} 份云快照</span>
                    ) : (
                      <span>直接读取静态快照 (0 数据库计算)</span>
                    )}
                  </div>
                  <button
                    onClick={handleRefreshSnapshot}
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
            
            <div className="flex items-center space-x-2">
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
                  按在线时间排序
                </button>
                <button
                  onClick={() => setUserSortOrder("created_desc")}
                  className={`px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all ${
                    userSortOrder === "created_desc" 
                      ? "bg-white dark:bg-cyan-500 text-slate-900 dark:text-zinc-950 shadow-xs" 
                      : "text-slate-500 dark:text-zinc-400"
                  }`}
                >
                  按注册时间排序
                </button>
              </div>

              {/* Batch Reset All Students Button */}
              <button
                onClick={() => setShowBatchResetModal(true)}
                className="px-3.5 py-2 bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-700 hover:to-amber-700 text-white rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm"
              >
                <KeyRound className="w-3.5 h-3.5" />
                <span>🔥 批量重置学员密码</span>
              </button>
            </div>
          </div>

          <WidgetErrorBoundary fallbackTitle="学员与考务人员列表加载异常">
            <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-cyan-500/20 overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
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
                    <th className="p-4 text-right">密码操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 dark:divide-zinc-800">
                  {sortedUsers.map((u) => {
                    const isSuper = u.role === "super_admin";
                    const isAdmin = u.role === "admin";
                    const isStudent = u.role === "student";
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
                          {new Date(u.created_at).toLocaleDateString()}
                        </td>
                        <td className="p-4 text-right">
                          {isSuper ? (
                            <span className="text-[11px] text-slate-400 dark:text-zinc-500 italic">全站独占最高席位</span>
                          ) : isAdmin ? (
                            <div className="flex items-center justify-end space-x-1.5">
                              {isSuperAdmin && (
                                <button
                                  onClick={() => handleTransferSuperAdmin(u)}
                                  className="px-2 py-1 text-amber-700 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/30 hover:bg-amber-100 dark:hover:bg-amber-950/50 border border-amber-200/80 dark:border-amber-500/20 rounded-lg text-xs font-bold inline-flex items-center space-x-1 transition-all"
                                  title="将全站唯一的超级管理员所有权安全转让给该管理员"
                                >
                                  <ArrowRightLeft className="w-3 h-3 text-amber-600 dark:text-amber-400" />
                                  <span>转让超管</span>
                                </button>
                              )}
                              <button
                                onClick={() => handleSetRole(u, "student")}
                                className="px-2.5 py-1 text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 dark:hover:bg-rose-950/50 border border-transparent dark:border-rose-500/20 rounded-lg text-xs font-semibold inline-flex items-center space-x-1 transition-colors"
                              >
                                <UserX className="w-3 h-3" />
                                <span>降为学员</span>
                              </button>
                            </div>
                          ) : (
                            <button
                              onClick={() => handleSetRole(u, "admin")}
                              className="px-2.5 py-1 text-indigo-600 dark:text-cyan-300 bg-indigo-50 dark:bg-cyan-500/10 hover:bg-indigo-100 dark:hover:bg-cyan-500/20 border border-transparent dark:border-cyan-500/20 rounded-lg text-xs font-semibold inline-flex items-center space-x-1 transition-colors"
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
                            className="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-200 rounded-lg text-xs font-semibold inline-flex items-center space-x-1 transition-colors"
                          >
                            <KeyRound className="w-3 h-3 text-indigo-600 dark:text-cyan-400" />
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
          </WidgetErrorBoundary>
        </div>
      )}

      {/* ========================================================================= */}
      {/* Tab 5: Settings & Quota (Super Admin Exclusive)                           */}
      {/* ========================================================================= */}
      {isSuperAdmin && activeTab === "settings" && (
        <div className="space-y-6 max-w-3xl">
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
                  onChange={(e) => setAnnouncementSettings({ ...announcementSettings, enabled: e.target.checked })}
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
                    onClick={() => setAnnouncementSettings({ ...announcementSettings, type: "info" })}
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
                    onClick={() => setAnnouncementSettings({ ...announcementSettings, type: "warning" })}
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
                    onClick={() => setAnnouncementSettings({ ...announcementSettings, type: "alert" })}
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
                  onChange={(e) => setAnnouncementSettings({ ...announcementSettings, text: e.target.value })}
                  placeholder="请输入面向全站考生的公告通知内容（例如：2024考研真题已更新，支持查词与左右键换题...）"
                  className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-2xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                />
              </div>

              {/* Action Button & Link */}
              <div className="grid sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-1">附带跳转按钮文字 (可选)</label>
                  <input
                    type="text"
                    value={announcementSettings.linkText}
                    onChange={(e) => setAnnouncementSettings({ ...announcementSettings, linkText: e.target.value })}
                    placeholder="例如: 立即前往做题"
                    className="w-full px-4 py-2 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-xl text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-800 dark:text-zinc-200 mb-1">跳转目标路由或链接 (可选)</label>
                  <input
                    type="text"
                    value={announcementSettings.linkUrl}
                    onChange={(e) => setAnnouncementSettings({ ...announcementSettings, linkUrl: e.target.value })}
                    placeholder="例如: /practice?id=xxx 或 https://..."
                    className="w-full px-4 py-2 bg-slate-50 dark:bg-[#090a0f] border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 placeholder:text-slate-400 dark:placeholder:text-zinc-600 rounded-xl text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                  />
                </div>
              </div>

              {/* Live Preview */}
              <div>
                <label className="block text-xs font-bold text-slate-400 dark:text-zinc-500 mb-1.5">所见即所得前台实时预览</label>
                <div className={`p-3 rounded-2xl border flex items-center justify-between gap-3 text-xs ${
                  announcementSettings.type === "info"
                    ? "bg-blue-50 dark:bg-blue-950/40 border-blue-200 dark:border-blue-500/30 text-blue-950 dark:text-blue-200"
                    : announcementSettings.type === "warning"
                    ? "bg-amber-50 dark:bg-amber-950/40 border-amber-200 dark:border-amber-500/30 text-amber-950 dark:text-amber-200"
                    : "bg-rose-50 dark:bg-rose-950/40 border-rose-200 dark:border-rose-500/30 text-rose-950 dark:text-rose-200"
                }`}>
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
                  onClick={handleClearAnnouncement}
                  disabled={isSavingAnnouncement || (!announcementSettings.text && !announcementSettings.enabled)}
                  className="px-4 py-2.5 bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 dark:hover:bg-rose-950/50 disabled:opacity-40 disabled:cursor-not-allowed text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-500/20 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition-all"
                  title="一键清空文案并关闭全站公告"
                >
                  <Trash2 className="w-4 h-4" />
                  <span>一键清空并下架公告</span>
                </button>

                <button
                  onClick={handleSaveAnnouncement}
                  disabled={isSavingAnnouncement}
                  className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 disabled:opacity-50 text-white dark:text-zinc-950 rounded-xl text-xs font-bold shadow-md shadow-indigo-200 dark:shadow-none flex items-center space-x-2 transition-all"
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
          <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/20 p-6 sm:p-8 space-y-6 shadow-sm">
            <div>
              <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">系统运行与人数配额配置</h3>
              <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
                控制全站注册学员人数上限与新用户注册准入开关
              </p>
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
                  onChange={(e) => setSettings({ ...settings, maxStudentsLimit: parseInt(e.target.value) || 0 })}
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
                  onChange={(e) => setSettings({ ...settings, registrationEnabled: e.target.checked })}
                  className="w-5 h-5 text-indigo-600 dark:text-cyan-500 rounded focus:ring-indigo-500 dark:focus:ring-cyan-500 cursor-pointer"
                />
              </div>

              <div className="pt-4 flex justify-end">
                <button
                  onClick={handleSaveSettings}
                  disabled={isSavingSettings}
                  className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 disabled:opacity-50 text-white dark:text-zinc-950 rounded-xl text-xs font-bold shadow-md shadow-indigo-200 dark:shadow-none flex items-center space-x-2 transition-colors"
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
          <div className="bg-white dark:bg-[#11131a] rounded-2xl max-w-sm w-full p-6 shadow-2xl border border-transparent dark:border-cyan-500/25 space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-2 text-indigo-600 dark:text-cyan-400">
              <KeyRound className="w-5 h-5" />
              <h3 className="font-bold text-slate-900 dark:text-zinc-100 text-base">重置密码</h3>
            </div>

            <p className="text-xs text-slate-500 dark:text-zinc-400">
              正在为用户 <strong className="text-slate-800 dark:text-zinc-200">{resetTargetUser.username}</strong> ({resetTargetUser.nickname}) 设置新密码。
            </p>

            <div>
              <label className="block text-xs font-semibold text-slate-700 dark:text-zinc-300 mb-1.5">
                新密码 (至少 6 位)
              </label>
              <input
                type="text"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                placeholder="输入新密码..."
                className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 rounded-xl text-xs font-mono focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
              />
            </div>

            {resetNotice && (
              <div className="text-xs font-bold text-indigo-700 dark:text-cyan-300 bg-indigo-50 dark:bg-cyan-500/10 p-2 rounded-lg border border-transparent dark:border-cyan-500/20">
                {resetNotice}
              </div>
            )}

            <div className="flex justify-end space-x-2 pt-2">
              <button
                type="button"
                onClick={() => setResetTargetUser(null)}
                className="px-3 py-2 text-xs font-semibold text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
              >
                取消
              </button>
              <button
                type="button"
                onClick={handleExecuteResetPassword}
                disabled={newPassword.length < 6}
                className="px-4 py-2 text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 disabled:opacity-40 text-white dark:text-zinc-950 font-bold rounded-xl shadow-sm transition-colors"
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
          <div className="bg-white dark:bg-[#11131a] rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 dark:border-cyan-500/25 space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-2.5 text-rose-600 dark:text-rose-400">
              <div className="p-2 bg-rose-50 dark:bg-rose-950/30 rounded-xl border border-transparent dark:border-rose-500/20">
                <KeyRound className="w-5 h-5" />
              </div>
              <div>
                <h3 className="font-bold text-slate-900 dark:text-zinc-100 text-base">一键重置全员学员密码</h3>
                <p className="text-[11px] text-slate-400 dark:text-zinc-500">超级管理员专享全局操作</p>
              </div>
            </div>

            <div className="p-3 bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-500/30 rounded-2xl text-xs text-amber-800 dark:text-amber-300 leading-relaxed">
              ⚠️ <strong>注意</strong>：该操作将把全站<strong>所有普通学员 (student)</strong> 的登录密码一次性重置为下方设置的统一初始密码。管理员密码不受影响。
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1.5">
                统一默认密码 (至少 6 位)
              </label>
              <input
                type="text"
                value={batchDefaultPassword}
                onChange={(e) => setBatchDefaultPassword(e.target.value)}
                placeholder="例如 123456"
                className="w-full px-3.5 py-2.5 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 rounded-xl text-xs font-mono font-bold focus:outline-none focus:ring-2 focus:ring-rose-500"
              />
            </div>

            <div className="flex justify-end space-x-2 pt-2">
              <button
                type="button"
                onClick={() => setShowBatchResetModal(false)}
                disabled={isBatchResetting}
                className="px-4 py-2.5 text-xs font-semibold text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
              >
                取消
              </button>
              <button
                type="button"
                onClick={handleBatchResetPasswords}
                disabled={isBatchResetting || batchDefaultPassword.length < 6}
                className="px-5 py-2.5 text-xs font-bold bg-rose-600 hover:bg-rose-700 disabled:opacity-40 text-white rounded-xl shadow-sm flex items-center space-x-2 transition-colors"
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

      {/* ========================================================================= */}
      {/* Modal 3: Exam & Material Edit Modal (Admin & Super Admin Full Access)     */}
      {/* ========================================================================= */}
      {isEditModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
          <div className="bg-white dark:bg-[#11131a] rounded-3xl max-w-4xl w-full max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 dark:border-cyan-500/25 animate-in fade-in zoom-in-95 duration-150 overflow-hidden">
            {/* Header */}
            <div className="p-4 sm:p-5 border-b border-slate-100 dark:border-zinc-800 flex items-center justify-between shrink-0 bg-slate-50/50 dark:bg-zinc-900/40">
              <div className="flex items-center space-x-3">
                <div className="p-2.5 bg-indigo-50 dark:bg-cyan-950/40 text-indigo-600 dark:text-cyan-400 rounded-2xl border border-indigo-100 dark:border-cyan-500/30">
                  <FileEdit className="w-5 h-5" />
                </div>
                <div>
                  <div className="flex items-center space-x-2">
                    <h3 className="font-bold text-slate-900 dark:text-zinc-100 text-base">
                      编辑试卷材料与完整数据
                    </h3>
                    <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-emerald-100 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300">
                      管理员后台
                    </span>
                  </div>
                  <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5 truncate max-w-md">
                    {editingExam?.title || "正在加载试卷信息..."}
                  </p>
                </div>
              </div>

              <button
                onClick={() => setIsEditModalOpen(false)}
                className="p-2 rounded-xl text-slate-400 dark:text-zinc-500 hover:text-slate-700 dark:hover:text-zinc-300 hover:bg-slate-100 dark:hover:bg-zinc-800 transition-colors"
                title="关闭窗口"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Sub-Header Tabs */}
            <div className="flex items-center justify-between px-5 pt-3 pb-2 border-b border-slate-100 dark:border-zinc-800 shrink-0 bg-white dark:bg-[#11131a]">
              <div className="flex items-center space-x-2">
                <button
                  type="button"
                  onClick={() => setEditTab("form")}
                  className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 ${
                    editTab === "form"
                      ? "bg-indigo-600 dark:bg-cyan-500 text-white dark:text-zinc-950 shadow-sm"
                      : "text-slate-500 dark:text-zinc-400 hover:text-slate-800 dark:hover:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-800/60"
                  }`}
                >
                  <FileText className="w-3.5 h-3.5" />
                  <span>基础信息与篇章材料</span>
                </button>

                <button
                  type="button"
                  onClick={() => setEditTab("json")}
                  className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 ${
                    editTab === "json"
                      ? "bg-indigo-600 dark:bg-cyan-500 text-white dark:text-zinc-950 shadow-sm"
                      : "text-slate-500 dark:text-zinc-400 hover:text-slate-800 dark:hover:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-800/60"
                  }`}
                >
                  <Code2 className="w-3.5 h-3.5" />
                  <span>完整 JSON / 试题与文件修改</span>
                </button>
              </div>

              {editTab === "json" && (
                <div className="flex items-center space-x-2">
                  <button
                    type="button"
                    onClick={handleFormatJson}
                    className="px-2.5 py-1 text-xs font-semibold text-slate-600 dark:text-zinc-300 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-lg transition-colors flex items-center space-x-1"
                    title="格式化 JSON 缩进"
                  >
                    <Sparkles className="w-3.5 h-3.5 text-amber-500" />
                    <span>格式化</span>
                  </button>
                  <button
                    type="button"
                    onClick={handleDownloadCurrentJson}
                    className="px-2.5 py-1 text-xs font-semibold text-indigo-600 dark:text-cyan-400 hover:bg-indigo-50 dark:hover:bg-cyan-950/40 rounded-lg transition-colors flex items-center space-x-1"
                    title="下载当前试卷完整 JSON 文件到本地"
                  >
                    <Download className="w-3.5 h-3.5" />
                    <span>下载文件</span>
                  </button>
                </div>
              )}
            </div>

            {/* Modal Body */}
            <div className="p-5 flex-1 overflow-y-auto space-y-4">
              {editLoading ? (
                <div className="flex flex-col items-center justify-center py-20 space-y-3">
                  <Loader2 className="w-7 h-7 text-indigo-600 dark:text-cyan-400 animate-spin" />
                  <p className="text-xs text-slate-400 dark:text-zinc-500">
                    正在同步加载试卷全部篇章与试题数据...
                  </p>
                </div>
              ) : editTab === "form" ? (
                /* Tab 1: Form View */
                <div className="space-y-5">
                  {/* Basic Metadata Grid */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3.5 bg-slate-50 dark:bg-zinc-900/50 p-4 rounded-2xl border border-slate-100 dark:border-zinc-800">
                    <div className="sm:col-span-2">
                      <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">
                        试卷标题
                      </label>
                      <input
                        type="text"
                        value={editFormData.title}
                        onChange={(e) => setEditFormData({ ...editFormData, title: e.target.value })}
                        className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">
                        科目分类
                      </label>
                      <select
                        value={editFormData.category_id}
                        onChange={(e) => setEditFormData({ ...editFormData, category_id: e.target.value })}
                        className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                      >
                        <option value="cet4">大学英语四级 (CET-4)</option>
                        <option value="cet6">大学英语六级 (CET-6)</option>
                        <option value="ky1">考研英语一 (KY-1)</option>
                        <option value="ky2">考研英语二 (KY-2)</option>
                      </select>
                    </div>

                    <div>
                      <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">
                        考试年份
                      </label>
                      <input
                        type="number"
                        value={editFormData.year}
                        onChange={(e) => setEditFormData({ ...editFormData, year: Number(e.target.value) })}
                        className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">
                        考试时长 (分钟)
                      </label>
                      <input
                        type="number"
                        value={editFormData.duration_minutes}
                        onChange={(e) => setEditFormData({ ...editFormData, duration_minutes: Number(e.target.value) })}
                        className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">
                        满分 / 及格分 (分)
                      </label>
                      <div className="flex items-center space-x-1.5">
                        <input
                          type="number"
                          value={editFormData.total_score}
                          onChange={(e) => setEditFormData({ ...editFormData, total_score: Number(e.target.value) })}
                          placeholder="满分"
                          className="w-1/2 px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                        />
                        <span className="text-slate-400 text-xs">/</span>
                        <input
                          type="number"
                          value={editFormData.pass_score}
                          onChange={(e) => setEditFormData({ ...editFormData, pass_score: Number(e.target.value) })}
                          placeholder="及格"
                          className="w-1/2 px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                        />
                      </div>
                    </div>
                  </div>

                  {/* Passages List */}
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <h4 className="text-xs font-bold text-slate-800 dark:text-zinc-200">
                        篇章材料列表 ({editFormData.passages.length} 篇)
                      </h4>
                      <span className="text-[11px] text-slate-400 dark:text-zinc-500">
                        管理员可在此直接校对与修改阅读材料原文
                      </span>
                    </div>

                    {editFormData.passages.map((p, pIdx) => (
                      <div
                        key={p.id || pIdx}
                        className="p-4 bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-zinc-800 space-y-2.5 shadow-sm"
                      >
                        <div className="flex items-center justify-between">
                          <div className="flex items-center space-x-2">
                            <span className="px-2 py-0.5 rounded-md font-mono font-bold text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300">
                              Passage #{pIdx + 1}
                            </span>
                            <span className="text-[10px] uppercase font-semibold text-slate-400">
                              {p.section_type}
                            </span>
                          </div>
                          <span className="text-[10px] text-slate-400">
                            {p.content?.length || 0} 字符
                          </span>
                        </div>

                        <div>
                          <label className="block text-[11px] font-semibold text-slate-600 dark:text-zinc-400 mb-1">
                            材料标题 / 描述
                          </label>
                          <input
                            type="text"
                            value={p.title}
                            onChange={(e) => {
                              const updated = [...editFormData.passages];
                              updated[pIdx].title = e.target.value;
                              setEditFormData({ ...editFormData, passages: updated });
                            }}
                            className="w-full px-3 py-1.5 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                          />
                        </div>

                        <div>
                          <label className="block text-[11px] font-semibold text-slate-600 dark:text-zinc-400 mb-1">
                            篇章材料正文 (支持改错与微调)
                          </label>
                          <textarea
                            rows={5}
                            value={p.content}
                            onChange={(e) => {
                              const updated = [...editFormData.passages];
                              updated[pIdx].content = e.target.value;
                              setEditFormData({ ...editFormData, passages: updated });
                            }}
                            className="w-full px-3 py-2 bg-slate-50 dark:bg-zinc-900/80 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-mono leading-relaxed focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                          />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ) : (
                /* Tab 2: Raw JSON Editor */
                <div className="space-y-3">
                  <div className="p-3 bg-indigo-50/60 dark:bg-cyan-950/30 border border-indigo-100 dark:border-cyan-500/20 rounded-2xl text-xs text-indigo-900 dark:text-cyan-200 flex items-start space-x-2">
                    <Info className="w-4 h-4 shrink-0 mt-0.5 text-indigo-600 dark:text-cyan-400" />
                    <p className="leading-relaxed">
                      <strong>试卷完整 JSON 代码编辑器</strong>：普通管理员可在此直接对试卷元数据、篇章、以及所有试题题目、选项、标准答案、解析等进行任意修改。点击右上方可随时<strong>下载该 JSON 文件</strong>或<strong>格式化</strong>。保存时系统将自动校验语法并更新数据库。
                    </p>
                  </div>

                  {jsonSyntaxError && (
                    <div className="p-3 bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-500/30 rounded-2xl text-xs text-rose-700 dark:text-rose-300 flex items-center space-x-2">
                      <AlertCircle className="w-4 h-4 shrink-0" />
                      <span>{jsonSyntaxError}</span>
                    </div>
                  )}

                  <div className="relative rounded-2xl overflow-hidden border border-slate-300 dark:border-zinc-700 shadow-inner">
                    <textarea
                      rows={20}
                      value={editJsonText}
                      onChange={(e) => {
                        setEditJsonText(e.target.value);
                        if (jsonSyntaxError) setJsonSyntaxError(null);
                      }}
                      className="w-full p-4 bg-slate-950 text-emerald-300 font-mono text-xs leading-relaxed focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500 resize-y"
                      placeholder={'{\n  "title": ...\n}'}
                    />
                  </div>
                </div>
              )}
            </div>

            {/* Footer */}
            <div className="p-4 sm:p-5 border-t border-slate-100 dark:border-zinc-800 flex items-center justify-between shrink-0 bg-slate-50/50 dark:bg-zinc-900/40">
              <button
                type="button"
                onClick={() => setIsEditModalOpen(false)}
                className="px-4 py-2 text-xs font-semibold text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
              >
                取消
              </button>

              <div className="flex items-center space-x-2">
                {editTab === "form" ? (
                  <button
                    type="button"
                    onClick={handleSaveFormEdit}
                    disabled={isSavingEdit || !editFormData.title.trim()}
                    className="px-5 py-2.5 text-xs font-bold bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 rounded-xl shadow-sm flex items-center space-x-1.5 transition-colors disabled:opacity-50"
                  >
                    {isSavingEdit ? (
                      <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                      <Save className="w-4 h-4" />
                    )}
                    <span>保存基础与篇章材料修改</span>
                  </button>
                ) : (
                  <button
                    type="button"
                    onClick={handleSaveJsonEdit}
                    disabled={isSavingEdit || !editJsonText.trim()}
                    className="px-5 py-2.5 text-xs font-bold bg-emerald-600 hover:bg-emerald-700 dark:bg-cyber-500 dark:hover:bg-cyber-400 text-white dark:text-zinc-950 rounded-xl shadow-sm flex items-center space-x-1.5 transition-colors disabled:opacity-50"
                  >
                    {isSavingEdit ? (
                      <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                      <Save className="w-4 h-4" />
                    )}
                    <span>保存并同步更新试题与材料</span>
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
