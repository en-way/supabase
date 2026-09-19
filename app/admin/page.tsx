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
  EyeOff
} from "lucide-react";

export default function AdminPage() {
  const router = useRouter();
  const [isAdmin, setIsAdmin] = useState<boolean | null>(null);
  const [activeTab, setActiveTab] = useState<"exams" | "import" | "users">("exams");

  // Exams list
  const [exams, setExams] = useState<any[]>([]);
  // Users list
  const [userList, setUserList] = useState<any[]>([]);

  // JSON batch import
  const [jsonText, setJsonText] = useState("");
  const [importStatus, setImportStatus] = useState<string>("");

  // Password reset modal
  const [resetTargetUser, setResetTargetUser] = useState<any>(null);
  const [newPassword, setNewPassword] = useState("");
  const [resetNotice, setResetNotice] = useState<string>("");

  // Global notice
  const [notice, setNotice] = useState<{ type: "success" | "error"; text: string } | null>(null);

  useEffect(() => {
    async function checkRole() {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) {
        router.replace("/login");
        return;
      }
      const { data } = await supabase
        .from("profiles")
        .select("role")
        .eq("id", user.id)
        .single();

      if (data?.role === "admin") {
        setIsAdmin(true);
        loadExams();
        loadUsers();
      } else {
        setIsAdmin(false);
      }
    }
    checkRole();
  }, [router]);

  const loadExams = async () => {
    const { data } = await supabase
      .from("exams")
      .select("*, questions(count), passages(count)")
      .order("created_at", { ascending: false });
    if (data) setExams(data);
  };

  const loadUsers = async () => {
    const { data } = await supabase
      .from("profiles")
      .select("*")
      .order("created_at", { ascending: false });
    if (data) setUserList(data);
  };

  const handleTogglePublish = async (exam: any) => {
    const nextState = !exam.is_published;
    const { error } = await supabase
      .from("exams")
      .update({ is_published: nextState })
      .eq("id", exam.id);
    if (!error) {
      loadExams();
      setNotice({ type: "success", text: nextState ? "试卷已公开上架" : "试卷已下架隐藏" });
      setTimeout(() => setNotice(null), 2500);
    }
  };

  const handleDeleteExam = async (examId: string, title: string) => {
    if (!window.confirm(`确定要彻底删除试卷 "${title}" 及其所有题目吗？`)) return;
    const { error } = await supabase.from("exams").delete().eq("id", examId);
    if (!error) {
      loadExams();
      setNotice({ type: "success", text: "试卷已删除" });
      setTimeout(() => setNotice(null), 2500);
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
          is_published: true,
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

      setImportStatus("✅ 试卷与题目导入成功！已自动发布到题库。");
      setJsonText("");
      loadExams();
      setNotice({ type: "success", text: "整卷导入成功！" });
      setTimeout(() => setNotice(null), 3000);
    } catch (err: any) {
      setImportStatus(`❌ 导入失败: ${err.message}`);
    }
  };

  // Reset Student Password
  const handleExecuteResetPassword = async () => {
    if (!resetTargetUser || newPassword.length < 6) {
      setResetNotice("密码长度至少需 6 位");
      return;
    }

    try {
      const { data, error } = await supabase.rpc("admin_reset_user_password", {
        target_user_id: resetTargetUser.id,
        new_plain_password: newPassword,
      });

      if (error) throw error;

      setResetNotice("密码修改成功！");
      setTimeout(() => {
        setResetTargetUser(null);
        setNewPassword("");
        setResetNotice("");
        setNotice({ type: "success", text: `已成功将学员 ${resetTargetUser.username} 的密码重置！` });
      }, 1200);
    } catch (err: any) {
      setResetNotice(`修改失败: ${err.message}`);
    }
  };

  if (isAdmin === null) {
    return (
      <div className="py-20 text-center">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-500 font-medium text-sm">正在验证管理员权限...</p>
      </div>
    );
  }

  if (isAdmin === false) {
    return (
      <div className="max-w-md mx-auto py-20 text-center bg-white rounded-3xl border border-slate-200 p-8">
        <Shield className="w-12 h-12 text-rose-500 mx-auto mb-3" />
        <h2 className="text-lg font-bold text-slate-900 mb-2">访问受限</h2>
        <p className="text-xs text-slate-500 mb-6">
          当前账号不是系统管理员，无权进入管理控制台。
        </p>
        <Link href="/" className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
          返回试卷大厅
        </Link>
      </div>
    );
  }

  return (
    <div className="space-y-8 animate-in fade-in duration-150">
      {/* Notice Banner */}
      {notice && (
        <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold flex items-center space-x-2">
          <CheckCircle2 className="w-4 h-4 text-emerald-600" />
          <span>{notice.text}</span>
        </div>
      )}

      {/* Admin Header */}
      <div className="bg-gradient-to-r from-purple-900 via-indigo-900 to-slate-900 text-white p-6 sm:p-8 rounded-3xl shadow-xl flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-center space-x-4">
          <div className="w-12 h-12 rounded-2xl bg-white/10 border border-white/20 flex items-center justify-center font-black">
            <Shield className="w-6 h-6 text-purple-300" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-400/20 text-purple-200">
                超级管理控制台
              </span>
            </div>
            <h1 className="text-2xl font-black tracking-tight mt-0.5">
              Enway 题库与系统管理中心
            </h1>
          </div>
        </div>

        {/* Tab Controls */}
        <div className="flex items-center space-x-1 p-1 bg-white/10 rounded-xl">
          <button
            onClick={() => setActiveTab("exams")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
              activeTab === "exams" ? "bg-white text-slate-900 shadow-sm" : "text-white/80 hover:text-white"
            }`}
          >
            试卷管理 ({exams.length})
          </button>
          <button
            onClick={() => setActiveTab("import")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
              activeTab === "import" ? "bg-white text-slate-900 shadow-sm" : "text-white/80 hover:text-white"
            }`}
          >
            JSON 批量导入
          </button>
          <button
            onClick={() => setActiveTab("users")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
              activeTab === "users" ? "bg-white text-slate-900 shadow-sm" : "text-white/80 hover:text-white"
            }`}
          >
            学员管理 ({userList.length})
          </button>
        </div>
      </div>

      {/* Tab 1: Exams Management */}
      {activeTab === "exams" && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-slate-900">当前已发布与管理的试卷</h3>
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
                    <th className="p-4">科目分类</th>
                    <th className="p-4">年份</th>
                    <th className="p-4">篇章数 / 题数</th>
                    <th className="p-4">满分 / 及格</th>
                    <th className="p-4">状态</th>
                    <th className="p-4 text-right">操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {exams.map((e) => (
                    <tr key={e.id} className="hover:bg-slate-50/60 transition-colors">
                      <td className="p-4 font-bold text-slate-900 max-w-xs truncate">{e.title}</td>
                      <td className="p-4 uppercase font-semibold text-indigo-600">{e.category_id}</td>
                      <td className="p-4">{e.year}</td>
                      <td className="p-4 text-slate-500">
                        {e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题
                      </td>
                      <td className="p-4">{e.total_score}分 / {e.pass_score}分</td>
                      <td className="p-4">
                        <span className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                          e.is_published ? "bg-emerald-100 text-emerald-700" : "bg-slate-100 text-slate-500"
                        }`}>
                          {e.is_published ? "已上架" : "已隐藏"}
                        </span>
                      </td>
                      <td className="p-4 text-right space-x-2">
                        <button
                          onClick={() => handleTogglePublish(e)}
                          title={e.is_published ? "点击隐藏" : "点击上架"}
                          className="p-1.5 text-slate-400 hover:text-indigo-600 rounded-lg"
                        >
                          {e.is_published ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                        </button>
                        <button
                          onClick={() => handleDeleteExam(e.id, e.title)}
                          title="删除试卷"
                          className="p-1.5 text-slate-400 hover:text-rose-600 rounded-lg"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* Tab 2: Standard JSON Batch Import */}
      {activeTab === "import" && (
        <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 space-y-6 shadow-sm">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100">
            <div>
              <h3 className="text-base font-bold text-slate-900">标准 JSON 结构化整卷导入</h3>
              <p className="text-xs text-slate-500 mt-0.5">
                一次性批量载入长篇阅读材料、完型填空、单选题干、选项与详细解析
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

          <div className="flex justify-end">
            <button
              onClick={handleBatchImport}
              disabled={!jsonText.trim()}
              className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white text-xs font-bold rounded-xl shadow-md shadow-indigo-200 flex items-center space-x-2 transition-all"
            >
              <Upload className="w-4 h-4" />
              <span>开始整卷批量导入</span>
            </button>
          </div>
        </div>
      )}

      {/* Tab 3: Users & Password Reset */}
      {activeTab === "users" && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-slate-900">已注册学员与账号管理</h3>
            <span className="text-xs text-slate-400">支持查看所有学员并一键重置学员密码</span>
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
                    <th className="p-4 text-right">管理操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {userList.map((u) => (
                    <tr key={u.id} className="hover:bg-slate-50/60 transition-colors">
                      <td className="p-4 font-mono font-bold text-slate-900">{u.username}</td>
                      <td className="p-4">{u.nickname || "--"}</td>
                      <td className="p-4">
                        <span className={`px-2 py-0.5 rounded-full font-bold text-[10px] ${
                          u.role === "admin" ? "bg-purple-100 text-purple-700" : "bg-slate-100 text-slate-600"
                        }`}>
                          {u.role === "admin" ? "👑 超级管理员" : "🎓 学员"}
                        </span>
                      </td>
                      <td className="p-4 text-slate-400 font-mono">
                        {new Date(u.created_at).toLocaleDateString()}
                      </td>
                      <td className="p-4 text-right">
                        <button
                          onClick={() => {
                            setResetTargetUser(u);
                            setNewPassword("");
                            setResetNotice("");
                          }}
                          className="px-2.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-semibold inline-flex items-center space-x-1"
                        >
                          <KeyRound className="w-3.5 h-3.5 text-indigo-600" />
                          <span>重置密码</span>
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* Password Reset Modal */}
      {resetTargetUser && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl max-w-sm w-full p-6 shadow-2xl space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-2 text-indigo-600">
              <KeyRound className="w-5 h-5" />
              <h3 className="font-bold text-slate-900 text-base">重置学员密码</h3>
            </div>

            <p className="text-xs text-slate-500">
              正在重置学员 <strong className="text-slate-800">{resetTargetUser.username}</strong> ({resetTargetUser.nickname}) 的登录密码。
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
    </div>
  );
}
