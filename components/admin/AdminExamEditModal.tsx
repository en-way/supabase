import { useEffect, useRef, useState } from "react";
import {
  AlertCircle,
  Code2,
  Download,
  FileEdit,
  FileText,
  Info,
  Loader2,
  Save,
  Sparkles,
  X,
} from "lucide-react";
import { supabase } from "@/lib/supabase";
import type { ExamRecord, PassageRecord, QuestionRecord } from "@/types/exam";
import type { UserRole } from "@/types/user";
import {
  getAdminErrorMessage,
  type AdminSaveExamRpcResult,
  type EditExamFormData,
  type EditPassageFormItem,
  type ImportExamInput,
  type ImportPassageInput,
  type ImportQuestionInput,
} from "./types";

interface AdminExamEditModalProps {
  exam: ExamRecord | null;
  currentRole: UserRole | null;
  onClose: () => void;
  onSaved: () => void;
  onNotify: (type: "success" | "error", text: string) => void;
}

const DEFAULT_EDIT_FORM_DATA: EditExamFormData = {
  id: "",
  title: "",
  category_id: "ky1",
  year: 2024,
  exam_type: "real",
  duration_minutes: 75,
  total_score: 60,
  pass_score: 36,
  passages: [],
};

export function AdminExamEditModal({
  exam,
  currentRole,
  onClose,
  onSaved,
  onNotify,
}: AdminExamEditModalProps) {
  const [editTab, setEditTab] = useState<"form" | "json">("form");
  const [editLoading, setEditLoading] = useState(false);
  const [isSavingEdit, setIsSavingEdit] = useState(false);
  const [jsonSyntaxError, setJsonSyntaxError] = useState<string | null>(null);
  const [editFormData, setEditFormData] = useState<EditExamFormData>(DEFAULT_EDIT_FORM_DATA);
  const [editJsonText, setEditJsonText] = useState("");

  const mountedRef = useRef(true);
  const editLoadSeqRef = useRef(0);
  const onNotifyRef = useRef(onNotify);
  onNotifyRef.current = onNotify;

  useEffect(() => {
    mountedRef.current = true;
    return () => {
      mountedRef.current = false;
    };
  }, []);

  useEffect(() => {
    if (!exam) return;
    const targetExam = exam;
    const seq = ++editLoadSeqRef.current;

    setEditLoading(true);
    setEditTab("form");
    setJsonSyntaxError(null);

    async function loadDetail() {
      try {
        const { data: fullExamRaw, error: examErr } = await supabase
          .from("exams")
          .select(
            "id, title, category_id, year, exam_type, duration_minutes, total_score, pass_score, is_published, approval_status"
          )
          .eq("id", targetExam.id)
          .single();
        if (examErr || !fullExamRaw) throw examErr || new Error("试卷详情不存在");

        const { data: passagesRaw, error: passErr } = await supabase
          .from("passages")
          .select("id, exam_id, title, content, section_type, sort_order")
          .eq("exam_id", targetExam.id)
          .order("sort_order", { ascending: true });
        if (passErr) throw passErr;

        const { data: questionsRaw, error: qErr } = await supabase
          .from("questions")
          .select(
            "id, exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order"
          )
          .eq("exam_id", targetExam.id)
          .order("sort_order", { ascending: true });
        if (qErr) throw qErr;

        if (!mountedRef.current || seq !== editLoadSeqRef.current) return;

        const fullExam = fullExamRaw as ExamRecord;
        const passagesData = (passagesRaw as PassageRecord[] | null) || [];
        const questionsData = (questionsRaw as QuestionRecord[] | null) || [];

        const passages: EditPassageFormItem[] = passagesData.map((p) => ({
          id: p.id,
          title: p.title || "",
          section_type: p.section_type || "reading",
          content: p.content || "",
          sort_order: p.sort_order || 1,
        }));

        setEditFormData({
          id: fullExam.id,
          title: fullExam.title || "",
          category_id: fullExam.category_id || "ky1",
          year: fullExam.year || 2024,
          exam_type: fullExam.exam_type || "real",
          duration_minutes: fullExam.duration_minutes || 75,
          total_score: fullExam.total_score || 60,
          pass_score: fullExam.pass_score ?? 36,
          passages,
        });

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
          passages: passagesData.map((p) => {
            const pQuestions = questionsData
              .filter((q) => q.passage_id === p.id)
              .map((q) => ({
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
      } catch (err: unknown) {
        if (mountedRef.current && seq === editLoadSeqRef.current) {
          onNotifyRef.current("error", `获取试卷材料失败: ${getAdminErrorMessage(err, "未知错误")}`);
        }
      } finally {
        if (mountedRef.current && seq === editLoadSeqRef.current) {
          setEditLoading(false);
        }
      }
    }

    loadDetail();
  }, [exam]);

  if (!exam) return null;

  const handleSaveFormEdit = async () => {
    if (currentRole !== "super_admin" && (exam.approval_status === "approved" || exam.is_published)) {
      onNotify("error", "已审核发布的试卷仅超级管理员可修改内容");
      return;
    }
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

      const passageUpdates = editFormData.passages
        .filter((p): p is EditPassageFormItem & { id: string } => Boolean(p.id))
        .map((p) =>
          supabase
            .from("passages")
            .update({
              title: p.title.trim(),
              content: p.content,
            })
            .eq("id", p.id)
        );
      const updateResults = await Promise.all(passageUpdates);
      const fail = updateResults.find((r) => r.error);
      if (fail?.error) throw fail.error;

      onNotify("success", "试卷与篇章材料已成功保存更新！");
      onClose();
      onSaved();
    } catch (err: unknown) {
      onNotify("error", `保存失败: ${getAdminErrorMessage(err, "未知错误")}`);
    } finally {
      setIsSavingEdit(false);
    }
  };

  const handleSaveJsonEdit = async () => {
    setIsSavingEdit(true);
    setJsonSyntaxError(null);

    try {
      if (currentRole !== "super_admin" && (exam.approval_status === "approved" || exam.is_published)) {
        throw new Error("已审核发布的试卷仅超级管理员可修改内容");
      }

      let parsedRaw: unknown;
      try {
        parsedRaw = JSON.parse(editJsonText);
      } catch (parseErr: unknown) {
        setJsonSyntaxError(`JSON 语法解析错误: ${getAdminErrorMessage(parseErr, "格式有误")}`);
        throw new Error("JSON 语法格式有误，请修正后再保存");
      }

      if (!parsedRaw || typeof parsedRaw !== "object" || Array.isArray(parsedRaw)) {
        throw new Error("JSON 顶层结构必须为对象");
      }

      const parsed = parsedRaw as ImportExamInput;
      const cleanTitle = typeof parsed.title === "string" ? parsed.title.trim() : "";
      const cleanCatId = typeof parsed.category_id === "string" ? parsed.category_id.trim() : "";
      if (!cleanTitle || !cleanCatId || !Array.isArray(parsed.passages)) {
        throw new Error("JSON 缺少必要结构字段 (title, category_id, passages)");
      }

      const normalizedPassages = parsed.passages.map((p: ImportPassageInput, pIdx: number) => ({
        id: typeof p?.id === "string" && p.id.trim() ? p.id.trim() : undefined,
        section_type: p?.section_type || "reading",
        title: typeof p?.title === "string" && p.title.trim() ? p.title : `Passage ${pIdx + 1}`,
        content: typeof p?.content === "string" ? p.content : "",
        sort_order: typeof p?.sort_order === "number" ? p.sort_order : pIdx + 1,
        questions: Array.isArray(p?.questions)
          ? p.questions.map((q: ImportQuestionInput, qIdx: number) => {
              const stem = typeof q?.stem === "string" ? q.stem.trim() : "";
              const correct = typeof q?.correct_answer === "string" ? q.correct_answer.trim() : "";
              const pts = q?.points !== undefined && q?.points !== null ? Number(q.points) : 2.0;
              if (!stem) {
                throw new Error(`第 ${pIdx + 1} 篇第 ${qIdx + 1} 题缺少题干 stem`);
              }
              if (!correct) {
                throw new Error(`第 ${pIdx + 1} 篇第 ${qIdx + 1} 题缺少正确答案 correct_answer`);
              }
              if (q?.options === undefined || q?.options === null) {
                throw new Error(`第 ${pIdx + 1} 篇第 ${qIdx + 1} 题缺少 options 选项`);
              }
              if (!Number.isFinite(pts) || pts < 0) {
                throw new Error(`第 ${pIdx + 1} 篇第 ${qIdx + 1} 题分值 points 必须为非负数字`);
              }
              return {
                id: typeof q?.id === "string" && q.id.trim() ? q.id.trim() : undefined,
                q_type: q?.q_type || "reading_item",
                stem,
                options: q.options,
                correct_answer: correct,
                explanation:
                  typeof q?.explanation === "string" && q.explanation.trim() ? q.explanation : "暂无详细解析",
                points: pts,
                sort_order: typeof q?.sort_order === "number" ? q.sort_order : qIdx + 1,
              };
            })
          : [],
      }));

      const normalizedPayload = {
        title: cleanTitle,
        category_id: cleanCatId,
        year: Number(parsed.year || exam.year),
        exam_type: parsed.exam_type || "real",
        duration_minutes: Number(parsed.duration_minutes || 75),
        total_score: Number(parsed.total_score || 60),
        pass_score:
          parsed.pass_score !== undefined && parsed.pass_score !== null ? Number(parsed.pass_score) : 36,
        passages: normalizedPassages,
      };

      const { data: rpcRaw, error: rpcErr } = await supabase.rpc("admin_save_exam_payload", {
        p_exam_id: exam.id,
        p_payload: normalizedPayload,
      });
      if (rpcErr) throw rpcErr;

      const rpcRes = (rpcRaw as AdminSaveExamRpcResult) ?? null;
      const pCount = rpcRes?.passages_count ?? normalizedPassages.length;
      const qCount =
        rpcRes?.questions_count ??
        normalizedPassages.reduce((sum, p) => sum + p.questions.length, 0);
      onNotify("success", `已事务原子保存 ${pCount} 篇材料与 ${qCount} 道试题（保留现有题目 UUID）！`);
      onClose();
      onSaved();
    } catch (err: unknown) {
      onNotify("error", getAdminErrorMessage(err, "保存失败"));
    } finally {
      setIsSavingEdit(false);
    }
  };

  const handleFormatJson = () => {
    try {
      const parsed: unknown = JSON.parse(editJsonText);
      setEditJsonText(JSON.stringify(parsed, null, 2));
      setJsonSyntaxError(null);
    } catch (err: unknown) {
      setJsonSyntaxError(`无法格式化，JSON 语法有误: ${getAdminErrorMessage(err, "格式错误")}`);
    }
  };

  const handleDownloadCurrentJson = () => {
    try {
      const blob = new Blob([editJsonText], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      const safeTitle = (exam.title || "exam").replace(/[^a-zA-Z0-9_\u4e00-\u9fa5-]/g, "_");
      a.download = `${safeTitle}.json`;
      a.click();
      URL.revokeObjectURL(url);
    } catch (err: unknown) {
      onNotify("error", `下载失败: ${getAdminErrorMessage(err, "未知错误")}`);
    }
  };

  return (
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
                <h3 className="font-bold text-slate-900 dark:text-zinc-100 text-base">编辑试卷材料与完整数据</h3>
                <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-emerald-100 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300">
                  管理员后台
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5 truncate max-w-md">
                {exam.title || "正在加载试卷信息..."}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
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
              <p className="text-xs text-slate-400 dark:text-zinc-500">正在同步加载试卷全部篇章与试题数据...</p>
            </div>
          ) : editTab === "form" ? (
            /* Tab 1: Form View */
            <div className="space-y-5">
              {/* Basic Metadata Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3.5 bg-slate-50 dark:bg-zinc-900/50 p-4 rounded-2xl border border-slate-100 dark:border-zinc-800">
                <div className="sm:col-span-2">
                  <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">试卷标题</label>
                  <input
                    type="text"
                    value={editFormData.title}
                    onChange={(e) => setEditFormData({ ...editFormData, title: e.target.value })}
                    className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                  />
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">科目分类</label>
                  <select
                    value={editFormData.category_id}
                    onChange={(e) => setEditFormData({ ...editFormData, category_id: e.target.value })}
                    className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 rounded-xl text-xs font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                  >
                    <option value="ky1">考研英语一 (KY-1)</option>
                    <option value="ky2">考研英语二 (KY-2)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-700 dark:text-zinc-300 mb-1">考试年份</label>
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
                        <span className="text-[10px] uppercase font-semibold text-slate-400">{p.section_type}</span>
                      </div>
                      <span className="text-[10px] text-slate-400">{p.content?.length || 0} 字符</span>
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 dark:text-zinc-400 mb-1">
                        材料标题 / 描述
                      </label>
                      <input
                        type="text"
                        value={p.title}
                        onChange={(e) => {
                          const updated = editFormData.passages.map((item, idx) =>
                            idx === pIdx ? { ...item, title: e.target.value } : item
                          );
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
                          const updated = editFormData.passages.map((item, idx) =>
                            idx === pIdx ? { ...item, content: e.target.value } : item
                          );
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
                  <strong>试卷完整 JSON 代码编辑器</strong>：普通管理员可在此直接对试卷元数据、篇章、以及所有试题题目、选项、标准答案、解析等进行任意修改。点击右上方可随时
                  <strong>下载该 JSON 文件</strong>或<strong>格式化</strong>。保存时系统将自动校验语法并更新数据库。
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
            onClick={onClose}
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
                {isSavingEdit ? <Loader2 className="w-4 h-4 animate-spin" /> : <Save className="w-4 h-4" />}
                <span>保存基础与篇章材料修改</span>
              </button>
            ) : (
              <button
                type="button"
                onClick={handleSaveJsonEdit}
                disabled={isSavingEdit || !editJsonText.trim()}
                className="px-5 py-2.5 text-xs font-bold bg-emerald-600 hover:bg-emerald-700 dark:bg-cyber-500 dark:hover:bg-cyber-400 text-white dark:text-zinc-950 rounded-xl shadow-sm flex items-center space-x-1.5 transition-colors disabled:opacity-50"
              >
                {isSavingEdit ? <Loader2 className="w-4 h-4 animate-spin" /> : <Save className="w-4 h-4" />}
                <span>保存并同步更新试题与材料</span>
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
