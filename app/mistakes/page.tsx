"use client";

import { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { 
  getLocalState, 
  toggleMistakeMastered, 
  removeMistake, 
  reconcileLearningState,
  normalizeOptions,
  MistakeItem 
} from "@/lib/storage";
import { supabase } from "@/lib/supabase";
import { 
  AlertCircle, 
  CheckCircle2, 
  XCircle, 
  RotateCcw, 
  Trash2, 
  Printer, 
  Download, 
  BookOpen,
  SplitSquareVertical,
  ExternalLink,
  ChevronLeft,
  ChevronRight,
  ZoomIn,
  ZoomOut,
  X,
  HelpCircle,
  Sparkles,
  Loader2
} from "lucide-react";

interface OnlineQuestionDetail {
  id: string;
  exam_id: string;
  passage_id?: string | null;
  category_id: string;
  q_type: string;
  stem: string;
  options: { key: string; text: string }[];
  correct_answer: string;
  explanation: string;
  points: number;
  sort_order: number;
  passages?: {
    id: string;
    title: string;
    content: string;
    section_type: string;
  } | null;
  exams?: {
    id: string;
    title: string;
    year: number;
  } | null;
}

// Client-side session memory cache for question details to avoid repeated network calls
const questionDetailsCache: Record<string, OnlineQuestionDetail> = {};

export default function MistakesPage() {
  const [mistakes, setMistakes] = useState<MistakeItem[]>([]);
  const [questionMap, setQuestionMap] = useState<Record<string, OnlineQuestionDetail>>({});
  const [isLoadingOnline, setIsLoadingOnline] = useState(false);
  const [activeTab, setActiveTab] = useState<"unmastered" | "mastered">("unmastered");
  const [categoryFilter, setCategoryFilter] = useState<string>("all");

  // Re-practice interactive state: { [qId]: selectedKey }
  const [retestAnswers, setRetestAnswers] = useState<Record<string, string>>({});
  // Congratulatory prompt for mastered: qId
  const [congratsId, setCongratsId] = useState<string | null>(null);
  // Reconciliation Toast alert
  const [toastMsg, setToastMsg] = useState<string | null>(null);

  // Side-by-Side "边看边写" Modal/Studio State
  const [sideBySideItem, setSideBySideItem] = useState<{
    mistake: MistakeItem;
    detail: OnlineQuestionDetail;
    index: number;
  } | null>(null);
  const [articleFontSize, setArticleFontSize] = useState<number>(15);

  // Print mode toggle
  const [printWithAnswers, setPrintWithAnswers] = useState(true);

  useEffect(() => {
    loadLocalMistakes();
  }, []);

  const loadLocalMistakes = () => {
    const state = getLocalState();
    const loadedMistakes = state.mistakes || [];
    setMistakes(loadedMistakes);
    fetchOnlineQuestionDetails(loadedMistakes);
  };

  // Quota optimization: Fetch missing questions in ONE batched request (.in('id', ids))
  const fetchOnlineQuestionDetails = async (items: MistakeItem[]) => {
    if (!items || items.length === 0) return;

    const allIds = Array.from(new Set(items.map((m) => m.questionId)));
    const missingIds = allIds.filter((id) => !questionDetailsCache[id]);

    // Update state with whatever is already in cache
    const initialMap: Record<string, OnlineQuestionDetail> = {};
    allIds.forEach((id) => {
      if (questionDetailsCache[id]) {
        initialMap[id] = questionDetailsCache[id];
      }
    });
    setQuestionMap(initialMap);

    if (missingIds.length === 0) return;

    setIsLoadingOnline(true);
    try {
      const { data, error } = await supabase
        .from("questions")
        .select(`
          id, exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order,
          passages (id, title, content, section_type),
          exams (id, title, year)
        `)
        .in("id", missingIds);

      if (error) throw error;

      if (data) {
        data.forEach((q: any) => {
          const detail: OnlineQuestionDetail = {
            id: q.id,
            exam_id: q.exam_id,
            passage_id: q.passage_id,
            category_id: q.category_id,
            q_type: q.q_type,
            stem: q.stem,
            options: normalizeOptions(q.options),
            correct_answer: q.correct_answer,
            explanation: q.explanation,
            points: Number(q.points || 2),
            sort_order: q.sort_order || 0,
            passages: q.passages,
            exams: q.exams,
          };
          questionDetailsCache[q.id] = detail;
          initialMap[q.id] = detail;
        });
        setQuestionMap({ ...initialMap });
      }

      // Execute reconciliation to prune deleted questions or auto-heal corrected answers
      const recon = await reconcileLearningState();
      if (recon.hasChanges) {
        setMistakes(getLocalState().mistakes);
        setToastMsg(recon.summaryText);
        setTimeout(() => setToastMsg(null), 3500);
      }
    } catch (err) {
      console.error("Failed to fetch questions details batch:", err);
    } finally {
      setIsLoadingOnline(false);
    }
  };

  const handleToggle = (qId: string) => {
    toggleMistakeMastered(qId);
    loadLocalMistakes();
    if (sideBySideItem && sideBySideItem.mistake.questionId === qId) {
      setSideBySideItem({
        ...sideBySideItem,
        mistake: {
          ...sideBySideItem.mistake,
          isMastered: !sideBySideItem.mistake.isMastered,
        },
      });
    }
  };

  const handleDelete = (qId: string) => {
    if (window.confirm("确定将这道错题从错题本中移除吗？")) {
      removeMistake(qId);
      if (sideBySideItem && sideBySideItem.mistake.questionId === qId) {
        setSideBySideItem(null);
      }
      loadLocalMistakes();
    }
  };

  const handleRetestOption = (questionId: string, correctAnswer: string, optionKey: string) => {
    setRetestAnswers((prev) => ({ ...prev, [questionId]: optionKey }));
    if (optionKey === correctAnswer) {
      setCongratsId(questionId);
    }
  };

  const handleConfirmMastered = (qId: string) => {
    toggleMistakeMastered(qId, true);
    setCongratsId(null);
    loadLocalMistakes();
    if (sideBySideItem && sideBySideItem.mistake.questionId === qId) {
      setSideBySideItem({
        ...sideBySideItem,
        mistake: { ...sideBySideItem.mistake, isMastered: true },
      });
    }
  };

  const filteredMistakes = useMemo(() => {
    return mistakes
      .filter((m) => (activeTab === "unmastered" ? !m.isMastered : m.isMastered))
      .filter((m) => (categoryFilter === "all" ? true : m.categoryId === categoryFilter));
  }, [mistakes, activeTab, categoryFilter]);

  // Open "边看边写" studio
  const handleOpenSideBySide = (mistake: MistakeItem, index: number) => {
    const detail = questionMap[mistake.questionId];
    if (detail) {
      setSideBySideItem({ mistake, detail, index });
    } else {
      alert("题目正在联网拉取中，请稍候点击...");
    }
  };

  // Navigate to previous/next mistake in side-by-side view
  const handleNavigateSideBySide = (direction: "prev" | "next") => {
    if (!sideBySideItem) return;
    const newIdx = direction === "prev" ? sideBySideItem.index - 1 : sideBySideItem.index + 1;
    if (newIdx >= 0 && newIdx < filteredMistakes.length) {
      const nextMistake = filteredMistakes[newIdx];
      const detail = questionMap[nextMistake.questionId];
      if (detail) {
        setSideBySideItem({ mistake: nextMistake, detail, index: newIdx });
      }
    }
  };

  // PC Keyboard Shortcuts for Side-by-Side Studio (A/B/C/D to answer, Left/Right to switch, Esc to close)
  useEffect(() => {
    if (!sideBySideItem) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      const key = e.key.toUpperCase();
      if (["A", "B", "C", "D"].includes(key)) {
        e.preventDefault();
        handleRetestOption(
          sideBySideItem.detail.id,
          sideBySideItem.detail.correct_answer,
          key
        );
      } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
        e.preventDefault();
        handleNavigateSideBySide("prev");
      } else if (e.key === "ArrowRight" || e.key === "ArrowDown") {
        e.preventDefault();
        handleNavigateSideBySide("next");
      } else if (e.key === "Escape") {
        e.preventDefault();
        setSideBySideItem(null);
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [sideBySideItem, filteredMistakes, questionMap]);

  // Export as Plain Text File (.txt)
  const handleExportTxt = () => {
    if (filteredMistakes.length === 0) {
      alert("当前列表暂无错题可导出");
      return;
    }

    let textContent = `===============================\n`;
    textContent += `Enway 英语智能错题练习集 (${new Date().toLocaleDateString()})\n`;
    textContent += `总计错题: ${filteredMistakes.length} 道\n`;
    textContent += `===============================\n\n`;

    filteredMistakes.forEach((item, idx) => {
      const detail = questionMap[item.questionId];
      const stemText = detail?.stem || item.stem || "（题目加载中）";
      const opts = detail?.options || item.options || [];
      const corr = detail?.correct_answer || item.correctAnswer || "详见系统";
      const expl = detail?.explanation || item.explanation || "详见系统";

      textContent += `【第 ${idx + 1} 题】(错误次数: ${item.wrongCount})\n`;
      if (detail?.exams?.title) {
        textContent += `[所属试卷]: ${detail.exams.title}\n`;
      }
      if (detail?.passages?.content) {
        textContent += `[篇章材料]:\n${detail.passages.content}\n\n`;
      }
      textContent += `${stemText}\n\n`;
      opts.forEach((opt) => {
        textContent += `  ${opt.key}. ${opt.text}\n`;
      });
      textContent += `\n[正确答案]: ${corr}\n`;
      textContent += `[上次选错]: ${item.wrongAnswer}\n`;
      textContent += `[考点解析]: ${expl}\n`;
      textContent += `--------------------------------------------------\n\n`;
    });

    const blob = new Blob([textContent], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `Enway_真题错题研习集_${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="space-y-6">
      {/* Floating Reconciliation Toast */}
      {toastMsg && (
        <div className="fixed top-20 right-6 z-50 p-4 bg-slate-900 text-white rounded-2xl shadow-xl border border-slate-700 flex items-center space-x-2.5 text-xs font-semibold animate-in fade-in slide-in-from-top-4 duration-200">
          <Sparkles className="w-4 h-4 text-amber-400 shrink-0" />
          <span>{toastMsg}</span>
        </div>
      )}

      {/* Header Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white dark:bg-[#11131a] p-6 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card no-print">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center font-bold">
            <AlertCircle className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h1 className="text-lg sm:text-xl font-bold text-zinc-900 dark:text-zinc-100">历年真题错题研习库</h1>
              {isLoadingOnline && (
                <span className="flex items-center text-xs text-zinc-600 dark:text-zinc-400 font-medium bg-zinc-100 dark:bg-zinc-800 px-2 py-0.5 rounded-full">
                  <Loader2 className="w-3 h-3 animate-spin mr-1" />
                  拉取篇章与考题...
                </span>
              )}
            </div>
            <p className="text-xs text-zinc-400 dark:text-zinc-500 mt-0.5">
              单项错题定向回溯文章 · 支持“边看边写”双栏研习 · 自动校准云端考题
            </p>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex items-center space-x-2">
          <button
            onClick={handleExportTxt}
            className="px-3 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-[#151923] text-zinc-700 dark:text-zinc-300 hover:bg-zinc-50 dark:hover:bg-zinc-800 text-xs font-semibold flex items-center space-x-1.5 transition-all shadow-subtle active:scale-[0.98]"
          >
            <Download className="w-3.5 h-3.5 text-zinc-500 dark:text-zinc-400" />
            <span>导出 TXT</span>
          </button>
          <button
            onClick={() => window.print()}
            className="px-3.5 py-1.5 rounded-xl bg-zinc-900 text-white hover:bg-zinc-800 dark:bg-gradient-to-r dark:from-cyan-500 dark:to-blue-600 dark:text-zinc-950 dark:font-black text-xs font-bold flex items-center space-x-1.5 shadow-subtle transition-all active:scale-[0.98]"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>打印 / 导出 PDF</span>
          </button>
        </div>
      </div>

      {/* Filter Tabs & Category Filter */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-black/[0.06] dark:border-zinc-800 pb-3 no-print">
        <div className="flex items-center space-x-1.5">
          <button
            onClick={() => setActiveTab("unmastered")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
              activeTab === "unmastered"
                ? "bg-zinc-900 text-white dark:bg-cyan-500 dark:text-zinc-950 shadow-subtle font-bold"
                : "text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800"
            }`}
          >
            待复习 ({mistakes.filter((m) => !m.isMastered).length})
          </button>
          <button
            onClick={() => setActiveTab("mastered")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
              activeTab === "mastered"
                ? "bg-zinc-900 text-white dark:bg-cyan-500 dark:text-zinc-950 shadow-subtle font-bold"
                : "text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800"
            }`}
          >
            已掌握归档 ({mistakes.filter((m) => m.isMastered).length})
          </button>
        </div>

        {/* Category Filter & Print Options */}
        <div className="flex items-center space-x-3 text-xs text-zinc-600 dark:text-zinc-400">
          <div className="flex items-center space-x-1.5">
            <span className="text-zinc-400 dark:text-zinc-500">分类:</span>
            <select
              value={categoryFilter}
              onChange={(e) => setCategoryFilter(e.target.value)}
              className="text-xs bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/20 rounded-lg px-2.5 py-1 text-zinc-800 dark:text-zinc-200 outline-none shadow-subtle"
            >
              <option value="all">全部分类</option>
              <option value="cet4">大学英语四级 (CET-4)</option>
              <option value="cet6">大学英语六级 (CET-6)</option>
              <option value="ky1">考研英语一 (KY-1)</option>
              <option value="ky2">考研英语二 (KY-2)</option>
            </select>
          </div>

          <div className="flex items-center space-x-1.5">
            <span className="text-zinc-400 dark:text-zinc-500">打印视图:</span>
            <button
              onClick={() => setPrintWithAnswers(!printWithAnswers)}
              className={`px-2.5 py-1 rounded-lg border text-xs font-medium transition-all ${
                printWithAnswers 
                  ? "bg-zinc-100 dark:bg-zinc-800 border-zinc-300 dark:border-zinc-700 text-zinc-900 dark:text-zinc-100 font-semibold" 
                  : "bg-white dark:bg-[#11131a] border-black/[0.06] dark:border-cyan-500/20 text-zinc-600 dark:text-zinc-400 shadow-subtle"
              }`}
            >
              {printWithAnswers ? "含答案与解析" : "仅题目(做题卷)"}
            </button>
          </div>
        </div>
      </div>

      {/* Printable Heading (Only visible in Print) */}
      <div className="hidden print-only text-center mb-6">
        <h1 className="text-2xl font-black mb-1">Enway 英语重点错题复习卷</h1>
        <p className="text-xs text-slate-500">
          打印时间: {new Date().toLocaleDateString()} · 共 {filteredMistakes.length} 道错题
        </p>
      </div>

      {/* Mistakes List */}
      {filteredMistakes.length === 0 ? (
        <div className="text-center py-20 bg-white dark:bg-[#11131a] rounded-2xl border border-dashed border-slate-300 dark:border-zinc-800 no-print">
          <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
          <p className="text-slate-600 dark:text-zinc-300 font-medium">太棒了！当前分类下没有待复习错题</p>
          <Link href="/" className="inline-block mt-4 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 text-xs font-bold rounded-xl transition-colors">
            前往试卷大厅刷题
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          {filteredMistakes.map((item, idx) => {
            const detail = questionMap[item.questionId];
            const retestAns = retestAnswers[item.questionId];
            const isRetested = Boolean(retestAns);
            const corrAnswer = detail?.correct_answer || item.correctAnswer || "";
            const isRetestCorrect = isRetested && retestAns === corrAnswer;
            const isShowCongrats = congratsId === item.questionId;
            const hasPassage = Boolean(detail?.passages?.content);

            const options = normalizeOptions(detail?.options || item.options || []);
            const stem = detail?.stem || item.stem || "（题目正在加载中...）";
            const explanation = detail?.explanation || item.explanation || "（解析加载中...）";

            return (
              <div
                key={item.questionId}
                className="bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200/90 dark:border-cyan-500/20 p-6 shadow-sm print-card space-y-4 transition-all hover:border-slate-300 dark:hover:border-cyan-400/40"
              >
                {/* Header info */}
                <div className="flex items-center justify-between flex-wrap gap-2">
                  <div className="flex items-center space-x-2 flex-wrap gap-y-1">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-900 dark:bg-cyan-500/20 dark:border dark:border-cyan-500/40 dark:text-cyan-300 text-white">
                      错题 #{idx + 1}
                    </span>
                    {detail?.exams?.title && (
                      <span className="px-2.5 py-0.5 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300">
                        {detail.exams.title}
                      </span>
                    )}
                    <span className="text-xs text-rose-600 dark:text-rose-400 font-semibold bg-rose-50 dark:bg-rose-950/30 px-2 py-0.5 rounded border border-transparent dark:border-rose-500/20">
                      做错 {item.wrongCount} 次
                    </span>
                    <span className="text-xs text-slate-400 dark:text-zinc-500">
                      上次选错: <strong className="text-rose-600 dark:text-rose-400">{item.wrongAnswer}</strong>
                    </span>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center space-x-2 no-print">
                    {/* Side-by-side reading button */}
                    {hasPassage && (
                      <button
                        onClick={() => handleOpenSideBySide(item, idx)}
                        className="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-50 dark:bg-cyan-500/10 border border-indigo-200 dark:border-cyan-500/30 text-indigo-700 dark:text-cyan-300 hover:bg-indigo-100 dark:hover:bg-cyan-500/20 flex items-center space-x-1.5 transition-all"
                        title="打开双栏对照窗口，边读文章边写题"
                      >
                        <SplitSquareVertical className="w-3.5 h-3.5" />
                        <span>边看边写 (对照文章)</span>
                      </button>
                    )}

                    <button
                      onClick={() => handleToggle(item.questionId)}
                      className={`px-3 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                        item.isMastered
                          ? "bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 dark:hover:bg-zinc-700 border-slate-200 dark:border-zinc-700"
                          : "bg-emerald-50 dark:bg-emerald-500/10 border-emerald-200 dark:border-emerald-500/30 text-emerald-700 dark:text-emerald-400 hover:bg-emerald-100 dark:hover:bg-emerald-500/20"
                      }`}
                    >
                      {item.isMastered ? "撤销已掌握" : "标记已掌握"}
                    </button>
                    <button
                      onClick={() => handleDelete(item.questionId)}
                      title="彻底删除"
                      className="p-1.5 text-slate-400 dark:text-zinc-500 hover:text-rose-600 dark:hover:text-rose-400 rounded-lg hover:bg-rose-50 dark:hover:bg-rose-950/30 transition-colors"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>

                {/* Printable Passage Content if printing and has passage */}
                {detail?.passages?.content && (
                  <div className="hidden print-only p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs leading-relaxed space-y-2">
                    <h4 className="font-bold text-slate-900">{detail.passages.title}</h4>
                    <p className="whitespace-pre-line text-slate-700">{detail.passages.content}</p>
                  </div>
                )}

                {/* Question Stem */}
                <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100 leading-relaxed">
                  {stem}
                </h3>

                {/* Options (Interactive for retesting) */}
                <div className="space-y-2">
                  {options.map((opt) => {
                    const isSelected = retestAns === opt.key;
                    const isTheCorrect = opt.key === corrAnswer;

                    let optStyle = "bg-slate-50 dark:bg-zinc-900/60 border-slate-200 dark:border-zinc-800 text-slate-800 dark:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-800/80";
                    if (isRetested) {
                      if (isTheCorrect) {
                        optStyle = "bg-emerald-50 dark:bg-emerald-950/30 border-emerald-400 dark:border-emerald-500/50 text-emerald-950 dark:text-emerald-300 font-bold";
                      } else if (isSelected) {
                        optStyle = "bg-rose-50 dark:bg-rose-950/30 border-rose-300 dark:border-rose-500/50 text-rose-950 dark:text-rose-300 font-bold";
                      }
                    }

                    return (
                      <button
                        key={opt.key}
                        onClick={() => handleRetestOption(item.questionId, corrAnswer, opt.key)}
                        className={`w-full p-3 rounded-xl border text-left flex items-start space-x-3 transition-all ${optStyle}`}
                      >
                        <span className="w-6 h-6 rounded-lg bg-white dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700 text-zinc-900 dark:text-zinc-200 text-xs font-bold flex items-center justify-center shrink-0">
                          {opt.key}
                        </span>
                        <span className="text-xs sm:text-sm pt-0.5">{opt.text}</span>
                      </button>
                    );
                  })}
                </div>

                {/* Retest Success Notification */}
                {isShowCongrats && (
                  <div className="p-3 bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-500/30 rounded-xl flex items-center justify-between text-xs text-emerald-800 dark:text-emerald-300 animate-in fade-in duration-150 no-print">
                    <span className="font-bold">🎉 重做答对了！该题已攻克，是否移入“已掌握”？</span>
                    <button
                      onClick={() => handleConfirmMastered(item.questionId)}
                      className="px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-lg shadow-sm"
                    >
                      移入已掌握
                    </button>
                  </div>
                )}

                {/* Explanation Block */}
                {(printWithAnswers || isRetested) && (
                  <div className={`p-4 rounded-xl bg-slate-50 dark:bg-zinc-900/80 border border-slate-200/80 dark:border-cyan-500/20 text-xs space-y-1.5 ${!printWithAnswers ? 'no-print' : ''}`}>
                    <div className="flex items-center space-x-2 font-bold text-indigo-700 dark:text-cyan-400">
                      <HelpCircle className="w-3.5 h-3.5" />
                      <span>正确答案: {corrAnswer} · 考点精析</span>
                    </div>
                    <p className="text-slate-700 dark:text-zinc-300 leading-relaxed whitespace-pre-line">
                      {explanation}
                    </p>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* ========================================================================= */}
      {/* "边看边写" (Side-by-Side Dual-Pane Review Studio Modal)                    */}
      {/* ========================================================================= */}
      {sideBySideItem && (
        <div className="fixed inset-0 z-50 bg-slate-950/70 backdrop-blur-sm flex items-center justify-center p-2 sm:p-4 animate-in fade-in duration-150">
          <div className="bg-white dark:bg-[#0d0e15] w-full max-w-[96vw] xl:max-w-7xl h-[95vh] rounded-3xl shadow-2xl flex flex-col overflow-hidden border border-slate-300 dark:border-cyan-500/25">
            {/* Studio Header */}
            <div className="px-6 py-3.5 bg-slate-900 dark:bg-[#11131a] text-white flex items-center justify-between shrink-0 border-b border-slate-800 dark:border-cyan-500/20">
              <div className="flex items-center space-x-3">
                <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/40 flex items-center justify-center font-bold text-sm">
                  📖
                </div>
                <div>
                  <h2 className="text-sm font-bold text-white flex items-center space-x-2">
                    <span>边看边写 · 错题精研工作台</span>
                    <span className="text-[11px] px-2 py-0.5 bg-indigo-500/30 dark:bg-cyan-500/20 text-indigo-200 dark:text-cyan-300 rounded-full font-mono">
                      第 {sideBySideItem.index + 1} / {filteredMistakes.length} 题
                    </span>
                  </h2>
                  <p className="text-xs text-slate-300 dark:text-zinc-400 truncate max-w-md">
                    {sideBySideItem.detail.exams?.title || "历年真题研习"}
                  </p>
                </div>
              </div>

              {/* Central shortcuts guide banner */}
              <div className="hidden md:flex items-center space-x-2 text-[11px] text-slate-300 dark:text-zinc-300 bg-slate-800/80 dark:bg-zinc-900 px-3 py-1.5 rounded-xl border border-slate-700 dark:border-zinc-800">
                <span className="text-amber-400 font-semibold">物理快捷键:</span>
                <span>[A / B / C / D] 作答</span>
                <span className="text-slate-500">|</span>
                <span>[← / →] 切换错题</span>
                <span className="text-slate-500">|</span>
                <span>[Esc] 退出</span>
              </div>

              {/* Navigation & Controls */}
              <div className="flex items-center space-x-2">
                <div className="flex items-center space-x-1 bg-slate-800 dark:bg-zinc-800/80 p-1 rounded-xl">
                  <button
                    onClick={() => handleNavigateSideBySide("prev")}
                    disabled={sideBySideItem.index <= 0}
                    className="px-2 py-1 text-slate-300 hover:text-white disabled:text-slate-600 rounded-lg hover:bg-slate-700/50 transition-colors text-xs flex items-center space-x-1"
                    title="上一题 (快捷键: ←)"
                  >
                    <ChevronLeft className="w-4 h-4" />
                    <span className="hidden sm:inline">上一题</span>
                  </button>
                  <button
                    onClick={() => handleNavigateSideBySide("next")}
                    disabled={sideBySideItem.index >= filteredMistakes.length - 1}
                    className="px-2 py-1 text-slate-300 hover:text-white disabled:text-slate-600 rounded-lg hover:bg-slate-700/50 transition-colors text-xs flex items-center space-x-1"
                    title="下一题 (快捷键: →)"
                  >
                    <span className="hidden sm:inline">下一题</span>
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>

                <button
                  onClick={() => setSideBySideItem(null)}
                  className="p-2 text-slate-400 hover:text-white rounded-xl hover:bg-slate-800 dark:hover:bg-zinc-800 transition-colors"
                  title="关闭 (快捷键: Esc)"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Split Screen Workspace: 55% Left, 45% Right */}
            <div className="flex-1 flex flex-col lg:flex-row overflow-hidden">
              {/* Left Pane: Golden 55% Reading Canvas */}
              {sideBySideItem.detail.passages?.content ? (
                <div className="lg:w-[55%] border-r border-stone-200/90 dark:border-cyan-500/20 flex flex-col bg-[#fcfbf9] dark:bg-[#090a0f] h-full overflow-hidden">
                  <div className="px-5 py-3 border-b border-stone-200/80 dark:border-cyan-500/20 bg-[#f8f6f0] dark:bg-[#11131a] flex items-center justify-between shrink-0">
                    <div className="flex items-center space-x-2">
                      <BookOpen className="w-4 h-4 text-amber-700 dark:text-amber-400" />
                      <span className="text-xs font-bold text-stone-800 dark:text-zinc-200 tracking-wide font-serif">
                        {sideBySideItem.detail.passages.title || "阅读篇章原文"}
                      </span>
                    </div>
                    {/* Font Zoom Controls */}
                    <div className="flex items-center space-x-1.5 text-xs text-stone-600 dark:text-zinc-400">
                      <span className="text-stone-500 dark:text-zinc-500 text-[11px]">字号:</span>
                      <button
                        onClick={() => setArticleFontSize((prev) => Math.max(14, prev - 1))}
                        className="px-2 py-0.5 border border-stone-300 dark:border-zinc-700 rounded bg-white dark:bg-zinc-800 hover:bg-stone-100 dark:hover:bg-zinc-700 text-stone-700 dark:text-zinc-200 font-serif font-bold text-xs"
                        title="缩小文字"
                      >
                        A-
                      </button>
                      <span className="font-mono text-xs w-6 text-center text-stone-800 dark:text-zinc-200">{articleFontSize}px</span>
                      <button
                        onClick={() => setArticleFontSize((prev) => Math.min(22, prev + 1))}
                        className="px-2 py-0.5 border border-stone-300 dark:border-zinc-700 rounded bg-white dark:bg-zinc-800 hover:bg-stone-100 dark:hover:bg-zinc-700 text-stone-700 dark:text-zinc-200 font-serif font-bold text-xs"
                        title="放大文字"
                      >
                        A+
                      </button>
                    </div>
                  </div>

                  {/* Passage Text Content (Paper reading canvas) */}
                  <div className="flex-1 p-6 sm:p-8 overflow-y-auto font-serif text-[#2c3e50] dark:text-zinc-200 leading-[1.85] tracking-wide select-text">
                    <div 
                      style={{ fontSize: `${articleFontSize}px` }} 
                      className="whitespace-pre-line space-y-4 max-w-prose"
                    >
                      {sideBySideItem.detail.passages.content}
                    </div>
                    <div className="mt-8 pt-4 border-t border-stone-200/80 dark:border-zinc-800 text-xs text-stone-500 dark:text-zinc-500 flex items-center space-x-2">
                      <Sparkles className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
                      <span>提示：双击文中任意生词，即可唤醒离线词典查词并收录至生词本。</span>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="hidden lg:flex lg:w-[55%] border-r border-stone-200 dark:border-cyan-500/20 bg-[#fcfbf9] dark:bg-[#090a0f] p-8 flex-col items-center justify-center text-center">
                  <div className="w-14 h-14 rounded-2xl bg-amber-50 dark:bg-amber-500/10 border border-amber-200/60 dark:border-amber-500/20 flex items-center justify-center text-amber-600 dark:text-amber-400 mb-3 font-serif text-2xl font-bold">
                    §
                  </div>
                  <p className="text-sm font-bold text-stone-700 dark:text-zinc-200">独立单项题研习</p>
                  <p className="text-xs text-stone-500 dark:text-zinc-400 mt-1.5 max-w-sm">
                    本题无需对照篇章材料，请在右侧研析题干、重新作答或查看考点精析。
                  </p>
                </div>
              )}

              {/* Right Pane: Golden 45% Answering Canvas */}
              <div className="flex-1 lg:w-[45%] flex flex-col bg-white dark:bg-[#11131a] h-full overflow-hidden">
                <div className="px-6 py-3 border-b border-slate-200 dark:border-cyan-500/20 flex items-center justify-between shrink-0 bg-slate-50/50 dark:bg-zinc-900/60">
                  <div className="flex items-center space-x-2">
                    <span className="text-xs font-bold bg-amber-100 dark:bg-amber-950/40 text-amber-900 dark:text-amber-300 px-2 py-0.5 rounded border border-transparent dark:border-amber-500/20">
                      做错 {sideBySideItem.mistake.wrongCount} 次
                    </span>
                    <span className="text-xs text-slate-500 dark:text-zinc-400">
                      上次选错: <strong className="text-rose-600 dark:text-rose-400 font-mono">{sideBySideItem.mistake.wrongAnswer}</strong>
                    </span>
                  </div>

                  <button
                    onClick={() => handleToggle(sideBySideItem.mistake.questionId)}
                    className={`px-3 py-1 rounded-lg text-xs font-bold border transition-colors ${
                      sideBySideItem.mistake.isMastered
                        ? "bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 border-slate-200 dark:border-zinc-700"
                        : "bg-emerald-50 dark:bg-emerald-500/10 border-emerald-300 dark:border-emerald-500/30 text-emerald-700 dark:text-emerald-400 hover:bg-emerald-100 dark:hover:bg-emerald-500/20"
                    }`}
                  >
                    {sideBySideItem.mistake.isMastered ? "撤销已掌握" : "标为已掌握"}
                  </button>
                </div>

                {/* Right Scrollable Area */}
                <div className="flex-1 p-6 overflow-y-auto space-y-6">
                  {/* Stem */}
                  <div>
                    <h3 className="text-base sm:text-lg font-bold text-slate-900 dark:text-zinc-100 leading-relaxed font-serif">
                      {sideBySideItem.detail.stem}
                    </h3>
                  </div>

                  {/* Options with normalizeOptions support */}
                  <div className="space-y-3">
                    {normalizeOptions(sideBySideItem.detail.options).map((opt) => {
                      const retestAns = retestAnswers[sideBySideItem.detail.id];
                      const isRetested = Boolean(retestAns);
                      const isTheCorrect = opt.key === sideBySideItem.detail.correct_answer;
                      const isSelected = retestAns === opt.key;

                      let btnStyle = "bg-slate-50 dark:bg-zinc-900/70 border-slate-200/80 dark:border-zinc-800 text-slate-800 dark:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-800/80";
                      let badgeStyle = "bg-white dark:bg-zinc-800 border-slate-300 dark:border-zinc-700 text-slate-700 dark:text-zinc-200";

                      if (isRetested) {
                        if (isTheCorrect) {
                          btnStyle = "bg-emerald-50 dark:bg-emerald-950/40 border-emerald-400 dark:border-emerald-500 text-emerald-950 dark:text-emerald-300 font-bold ring-1 ring-emerald-400";
                          badgeStyle = "bg-emerald-600 text-white border-emerald-600";
                        } else if (isSelected) {
                          btnStyle = "bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-500 text-rose-950 dark:text-rose-300 font-bold ring-1 ring-rose-300";
                          badgeStyle = "bg-rose-600 text-white border-rose-600";
                        }
                      }

                      return (
                        <button
                          key={opt.key}
                          onClick={() =>
                            handleRetestOption(
                              sideBySideItem.detail.id,
                              sideBySideItem.detail.correct_answer,
                              opt.key
                            )
                          }
                          className={`w-full p-4 rounded-xl border text-left flex items-start space-x-3.5 transition-all shadow-xs ${btnStyle}`}
                        >
                          <span className={`w-7 h-7 rounded-lg border text-xs font-bold font-mono flex items-center justify-center shrink-0 ${badgeStyle}`}>
                            {opt.key}
                          </span>
                          <span className="text-sm pt-0.5 leading-relaxed flex-1">{opt.text}</span>
                          <span className="text-[10px] text-slate-400 dark:text-zinc-500 font-mono self-center hidden sm:inline">
                            [键入 {opt.key}]
                          </span>
                        </button>
                      );
                    })}
                  </div>

                  {/* Retest Success Alert */}
                  {congratsId === sideBySideItem.detail.id && (
                    <div className="p-4 bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-500/30 rounded-2xl flex items-center justify-between text-xs text-emerald-800 dark:text-emerald-300 animate-in fade-in duration-150 shadow-xs">
                      <div className="flex items-center space-x-2">
                        <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
                        <span className="font-bold">恭喜！重做答对，该考点已被攻克！</span>
                      </div>
                      <button
                        onClick={() => handleConfirmMastered(sideBySideItem.detail.id)}
                        className="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl shadow-sm transition-colors"
                      >
                        移入已掌握
                      </button>
                    </div>
                  )}

                  {/* Explanation Block */}
                  {(Boolean(retestAnswers[sideBySideItem.detail.id]) || sideBySideItem.mistake.isMastered) && (
                    <div className="p-5 rounded-2xl bg-indigo-50/70 dark:bg-zinc-900/80 border border-indigo-100 dark:border-cyan-500/20 text-xs space-y-2">
                      <div className="flex items-center space-x-2 font-bold text-indigo-950 dark:text-cyan-300">
                        <HelpCircle className="w-4 h-4 text-indigo-600 dark:text-cyan-400" />
                        <span>考点精析 · 正确答案: {sideBySideItem.detail.correct_answer}</span>
                      </div>
                      <p className="text-slate-700 dark:text-zinc-300 leading-relaxed whitespace-pre-line text-sm">
                        {sideBySideItem.detail.explanation}
                      </p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
