import { useState } from "react";
import { Download, Upload } from "lucide-react";
import { supabase } from "@/lib/supabase";
import type { RawQuestionOptions } from "@/types/exam";
import type { UserRole } from "@/types/user";
import {
  getAdminErrorMessage,
  type ImportExamInput,
  type ImportPassageInput,
  type ImportQuestionInput,
} from "./types";

interface ImportQuestionRow {
  exam_id: string;
  passage_id: string;
  category_id: string;
  q_type: string;
  stem: string;
  options: RawQuestionOptions;
  correct_answer: string;
  explanation: string;
  points: number;
  sort_order: number;
}

interface AdminImportTabProps {
  currentRole: UserRole | null;
  currentUserId?: string;
  onImported: () => void;
  onNotify: (type: "success" | "error", text: string) => void;
}

export function AdminImportTab({
  currentRole,
  currentUserId,
  onImported,
  onNotify,
}: AdminImportTabProps) {
  const [jsonText, setJsonText] = useState("");
  const [importStatus, setImportStatus] = useState<string>("");
  const isSuperAdmin = currentRole === "super_admin";

  const handleDownloadTemplate = () => {
    const template = {
      title: "2025年全国硕士研究生招生考试英语（一）真题精解(示例)",
      category_id: "ky1",
      year: 2025,
      exam_type: "mock",
      duration_minutes: 75,
      total_score: 60,
      pass_score: 36,
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
                { key: "D", text: "Guarantees lower electricity prices" },
              ],
              correct_answer: "B",
              explanation: "【考点点拨】细节事实题。根据第二段可知闭环水培极大节约了土地与水资源。",
              points: 2.0,
            },
          ],
        },
      ],
    };

    const blob = new Blob([JSON.stringify(template, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "enway_exam_import_template.json";
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleBatchImport = async () => {
    setImportStatus("正在解析 JSON...");
    try {
      const parsedRaw: unknown = JSON.parse(jsonText);
      if (!parsedRaw || typeof parsedRaw !== "object" || Array.isArray(parsedRaw)) {
        throw new Error("JSON 格式不符合规范，缺少必要字段 (title, category_id, passages)");
      }
      const data = parsedRaw as ImportExamInput;
      if (!data.title || !data.category_id || !Array.isArray(data.passages)) {
        throw new Error("JSON 格式不符合规范，缺少必要字段 (title, category_id, passages)");
      }

      const categoryId = data.category_id;
      const passagesInput = data.passages;

      setImportStatus("正在写入试卷主表...");
      const isSuper = currentRole === "super_admin";
      const approvalStatus = isSuper ? "approved" : "pending_upload";
      const isPublished = isSuper;

      const { data: examData, error: examErr } = await supabase
        .from("exams")
        .insert({
          title: data.title,
          category_id: categoryId,
          year: data.year || new Date().getFullYear(),
          exam_type: data.exam_type || "real",
          duration_minutes: data.duration_minutes || 75,
          total_score: data.total_score || 60,
          pass_score: data.pass_score ?? 36,
          is_published: isPublished,
          approval_status: approvalStatus,
          created_by: currentUserId,
        })
        .select("id")
        .single();

      if (examErr || !examData) throw examErr || new Error("创建试卷失败");
      const createdExamId = (examData as { id: string }).id;

      setImportStatus("正在写入篇章与题目...");
      if (passagesInput.length > 0) {
        const passagePayloads = passagesInput.map((p: ImportPassageInput, i: number) => ({
          exam_id: createdExamId,
          category_id: categoryId,
          section_type: p.section_type || "reading",
          title: p.title || `Passage ${i + 1}`,
          content: p.content || "",
          sort_order: i + 1,
        }));

        const { data: insertedPassages, error: pErr } = await supabase
          .from("passages")
          .insert(passagePayloads)
          .select("id");

        if (pErr) throw pErr;

        const questionRows: ImportQuestionRow[] = [];
        (insertedPassages as Array<{ id: string }> | null)?.forEach((passageData, i) => {
          const p = passagesInput[i];
          if (Array.isArray(p?.questions)) {
            p.questions.forEach((q: ImportQuestionInput, qIdx: number) => {
              questionRows.push({
                exam_id: createdExamId,
                passage_id: passageData.id,
                category_id: categoryId,
                q_type: q.q_type || "reading_item",
                stem: q.stem || "",
                options: q.options ?? [],
                correct_answer: q.correct_answer || "",
                explanation: q.explanation || "暂无详细解析",
                points: q.points !== undefined && q.points !== null ? Number(q.points) : 2.0,
                sort_order: qIdx + 1,
              });
            });
          }
        });

        if (questionRows.length > 0) {
          const { error: qErr } = await supabase.from("questions").insert(questionRows);
          if (qErr) throw qErr;
        }
      }

      if (isSuper) {
        setImportStatus("✅ 试卷与题目导入成功！已由超级管理员直接发布。");
        onNotify("success", "试卷导入并自动发布成功！");
      } else {
        setImportStatus("⏳ 试卷与题目上传成功！已标记为待审核，待超级管理员批准后即可发布上架。");
        onNotify("success", "试卷上传成功，请等待超级管理员审批！");
      }

      setJsonText("");
      onImported();
    } catch (err: unknown) {
      setImportStatus(`❌ 导入失败: ${getAdminErrorMessage(err, "未知错误")}`);
    }
  };

  return (
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
  );
}
