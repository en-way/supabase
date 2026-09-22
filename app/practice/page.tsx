"use client";

import { useState, useEffect, useRef, Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { 
  recordMistake, 
  toggleFavorite, 
  updateFavoriteNote, 
  getLocalState,
  normalizeOptions,
  savePracticeDraft,
  getPracticeDraft,
  clearPracticeDraft
} from "@/lib/storage";
import { fetchExamDetailWithFallback } from "@/lib/examLoader";
import { 
  ArrowLeft, 
  CheckCircle2, 
  XCircle, 
  Bookmark, 
  ChevronRight, 
  ChevronLeft, 
  Type, 
  Sparkles,
  Edit3,
  RotateCcw
} from "lucide-react";

function PracticeContent() {
  const searchParams = useSearchParams();
  const examId = searchParams.get("id");

  const [exam, setExam] = useState<any>(null);
  const [passages, setPassages] = useState<any[]>([]);
  const [questions, setQuestions] = useState<any[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);

  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [showExplanation, setShowExplanation] = useState<Record<string, boolean>>({});
  const [favoriteIds, setFavoriteIds] = useState<Set<string>>(new Set());
  const [editingNotes, setEditingNotes] = useState<Record<string, string>>({});
  const [largeFont, setLargeFont] = useState(false);
  const passageContainerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    async function loadExam() {
      if (!examId) {
        setLoading(false);
        return;
      }
      setLoading(true);
      try {
        const detail = await fetchExamDetailWithFallback(examId);
        if (detail) {
          setExam(detail.exam || null);
          setPassages(detail.passages || []);
          setQuestions(detail.questions || []);
        }

        const state = getLocalState();
        const favs = Array.isArray(state?.favorites) ? state.favorites : [];
        setFavoriteIds(new Set(favs.map((f) => f?.questionId).filter(Boolean)));
        const notesMap: Record<string, string> = {};
        favs.forEach((f) => {
          if (f && f.questionId && f.note) notesMap[f.questionId] = f.note;
        });
        setEditingNotes(notesMap);

        // Smart Practice Resume: Restore previous draft progress if exists
        const draft = getPracticeDraft(examId);
        if (draft) {
          setUserAnswers(draft.answers || {});
          if (typeof draft.currentIndex === "number" && draft.currentIndex >= 0 && draft.currentIndex < (detail?.questions || []).length) {
            setCurrentIndex(draft.currentIndex);
          }
          const expMap: Record<string, boolean> = {};
          Object.keys(draft.answers || {}).forEach((qId) => {
            expMap[qId] = true;
          });
          setShowExplanation(expMap);
        }
      } catch (err) {
        console.error("Failed to load practice data:", err);
      } finally {
        setLoading(false);
      }
    }
    loadExam();
  }, [examId]);

  const navigateTo = (newIdx: number) => {
    const safeIdx = Math.max(0, Math.min(questions.length - 1, newIdx));
    setCurrentIndex(safeIdx);
    if (examId) {
      savePracticeDraft(examId, userAnswers, safeIdx);
    }
  };

  const handleResetPractice = () => {
    if (!window.confirm("确定要重新开始本卷练习吗？当前已作答的选项与解析进度将被重置。")) return;
    if (examId) {
      clearPracticeDraft(examId);
    }
    setUserAnswers({});
    setShowExplanation({});
    setCurrentIndex(0);
  };

  const handleSelectOption = (key: string) => {
    const q = questions[currentIndex] || questions[0];
    if (!q) return;
    const isAns = Boolean(userAnswers[q.id]);
    if (isAns) return;

    const nextAnswers = { ...userAnswers, [q.id]: key };
    setUserAnswers(nextAnswers);
    setShowExplanation((prev) => ({ ...prev, [q.id]: true }));

    // Instant LocalStorage save with zero delay
    if (examId) {
      savePracticeDraft(examId, nextAnswers, currentIndex);
    }

    if (key !== q.correct_answer) {
      recordMistake({
        questionId: q.id,
        examId: exam?.id,
        categoryId: exam?.category_id,
        stem: q.stem,
        options: normalizeOptions(q.options),
        correctAnswer: q.correct_answer,
        explanation: q.explanation,
        wrongAnswer: key,
      });
    }
  };

  // BeforeUnload Exit Protection: sync latest draft on tab close
  useEffect(() => {
    if (!examId || loading) return;

    const handleBeforeUnload = () => {
      if (Object.keys(userAnswers).length > 0) {
        savePracticeDraft(examId, userAnswers, currentIndex);
      }
    };

    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [examId, userAnswers, currentIndex, loading]);

  // Physical keyboard shortcuts (A/B/C/D to answer, Left/Right arrow to navigate)
  // Must be called unconditionally before any early returns
  useEffect(() => {
    if (loading || questions.length === 0) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      const key = e.key.toUpperCase();
      if (["A", "B", "C", "D"].includes(key)) {
        e.preventDefault();
        handleSelectOption(key);
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        navigateTo(currentIndex - 1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        navigateTo(currentIndex + 1);
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        passageContainerRef.current?.scrollBy({ top: -140, behavior: "smooth" });
      } else if (e.key === "ArrowDown") {
        e.preventDefault();
        passageContainerRef.current?.scrollBy({ top: 140, behavior: "smooth" });
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [currentIndex, questions, userAnswers, loading]);

  const handleToggleFav = () => {
    const q = questions[currentIndex] || questions[0];
    if (!q) return;
    toggleFavorite({
      questionId: q.id,
      examId: exam?.id || "",
      stem: q.stem,
      options: normalizeOptions(q.options),
      correctAnswer: q.correct_answer,
      explanation: q.explanation,
      note: editingNotes[q.id] || "",
    });

    setFavoriteIds((prev) => {
      const next = new Set(prev);
      if (next.has(q.id)) {
        next.delete(q.id);
      } else {
        next.add(q.id);
      }
      return next;
    });
  };

  const handleSaveNote = (noteText: string) => {
    const q = questions[currentIndex] || questions[0];
    if (!q) return;
    setEditingNotes((prev) => ({ ...prev, [q.id]: noteText }));
    updateFavoriteNote(q.id, noteText);
  };

  // Conditional early returns placed strictly AFTER all Hooks
  if (!examId) {
    return (
      <div className="py-20 text-center">
        <p className="text-slate-500 mb-4">缺少试卷 ID 参数</p>
        <Link href="/" className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
          返回试卷大厅
        </Link>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="py-20 text-center">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-500 font-medium text-sm">正在加载随做随练题库...</p>
      </div>
    );
  }

  const currentQ = questions[currentIndex] || questions[0];

  if (!questions.length || !currentQ) {
    return (
      <div className="text-center py-20 bg-white rounded-2xl border border-slate-200">
        <p className="text-slate-600 mb-4">该试卷暂无题目</p>
        <Link href="/" className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-sm">
          返回试卷大厅
        </Link>
      </div>
    );
  }

  const relatedPassage = currentQ.passage_id 
    ? passages.find((p) => p.id === currentQ.passage_id) || passages[0] || null
    : passages[0] || null;
  const selectedAnswer = userAnswers[currentQ.id];
  const isAnswered = Boolean(selectedAnswer);
  const isCorrect = selectedAnswer === currentQ.correct_answer;
  const isFavorited = favoriteIds.has(currentQ.id);

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      {/* Top Header Bar */}
      <div className="flex items-center justify-between bg-white/85 dark:bg-[#11131a]/85 backdrop-blur-xl p-3.5 sm:p-4 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card transition-colors duration-300">
        <div className="flex items-center space-x-3">
          <Link
            href="/"
            className="p-2 text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-100 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 border border-black/[0.04] dark:border-cyan-500/20 font-mono tracking-wide">
                随做随练 · 真题精研
              </span>
              <h2 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100 line-clamp-1">
                {exam?.title}
              </h2>
            </div>
            <p className="text-[11px] text-stone-400 dark:text-zinc-500 mt-0.5 hidden sm:block">
              键选即时核对 · 双击生词即呼词典 · 错题自动归集智能错题本
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2.5">
          <span className="hidden md:inline-flex items-center space-x-1 px-2 py-0.5 rounded text-[10px] font-medium bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-400 border border-emerald-200/60 dark:border-emerald-500/20">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
            <span>实时进度保全</span>
          </span>

          {Object.keys(userAnswers).length > 0 && (
            <button
              onClick={handleResetPractice}
              title="清空当前做题记录重新开始"
              className="px-2.5 py-1.5 rounded-lg border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 text-stone-500 dark:text-zinc-400 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 text-xs font-semibold flex items-center space-x-1 transition-all shadow-subtle"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">重做本卷</span>
            </button>
          )}

          {/* Keyboard shortcut reminder pill */}
          <div className="hidden lg:flex items-center space-x-1.5 text-xs text-stone-500 dark:text-zinc-400 bg-stone-50 dark:bg-zinc-900 border border-black/[0.05] dark:border-cyan-500/20 px-2.5 py-1 rounded-lg font-mono">
            <span className="text-stone-700 dark:text-zinc-300 font-bold text-[11px]">快捷键:</span>
            <span className="bg-white dark:bg-zinc-800 px-1.5 py-0.5 rounded border border-black/[0.06] dark:border-cyan-500/20 text-[11px] font-semibold text-stone-800 dark:text-zinc-200">[A/B/C/D]</span>
            <span className="bg-white dark:bg-zinc-800 px-1.5 py-0.5 rounded border border-black/[0.06] dark:border-cyan-500/20 text-[11px] font-semibold text-stone-800 dark:text-zinc-200">[←/→] 翻题</span>
            <span className="bg-white dark:bg-zinc-800 px-1.5 py-0.5 rounded border border-black/[0.06] dark:border-cyan-500/20 text-[11px] font-semibold text-stone-800 dark:text-zinc-200">[↑/↓] 滚文</span>
          </div>

          <button
            onClick={() => setLargeFont(!largeFont)}
            title="字号缩放"
            className={`px-2.5 py-1.5 rounded-lg border text-xs font-semibold flex items-center space-x-1 transition-all duration-150 active:scale-[0.98] ${
              largeFont 
                ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] border-emerald-700 dark:border-cyber-400 shadow-subtle dark:shadow-glow-cyan" 
                : "bg-white dark:bg-zinc-800 border-black/[0.06] dark:border-cyan-500/20 text-stone-600 dark:text-zinc-300 hover:text-stone-950 dark:hover:text-white hover:bg-stone-50 dark:hover:bg-zinc-700 shadow-subtle"
            }`}
          >
            <Type className="w-3.5 h-3.5" />
            <span>{largeFont ? "标准字号" : "大字号"}</span>
          </button>

          <div className="text-xs font-bold text-stone-800 dark:text-cyber-300 bg-stone-100 dark:bg-zinc-800 px-3 py-1.5 rounded-lg font-mono">
            {currentIndex + 1} / {questions.length} 题
          </div>
        </div>
      </div>

      {/* Main Dual-Column Split Reading Experience */}
      <div className={`grid gap-6 ${relatedPassage ? "lg:grid-cols-12" : "max-w-3xl mx-auto"}`}>
        {/* Left Column: Reading Passage */}
        {relatedPassage && (
          <div 
            ref={passageContainerRef} 
            className="lg:col-span-7 bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-7 sm:p-8 shadow-card overflow-y-auto max-h-[82vh] leading-relaxed select-text transition-colors duration-300"
          >
            <div className="flex items-center justify-between pb-3.5 mb-5 border-b border-stone-100 dark:border-zinc-800">
              <span className="text-xs font-bold font-sans uppercase tracking-wider text-stone-900 dark:text-zinc-100">
                {relatedPassage.title}
              </span>
              <span className="text-[11px] text-stone-400 dark:text-zinc-500 font-sans">💡 双击文中单词即刻离线查词</span>
            </div>
            <div className={`text-stone-800 dark:text-zinc-200 font-serif selection:bg-emerald-100/70 dark:selection:bg-cyan-500/30 whitespace-pre-line tracking-wide ${
              largeFont ? "text-lg leading-[2.1]" : "text-[15px] sm:text-base leading-[1.85]"
            }`}>
              {relatedPassage.content}
            </div>
          </div>
        )}

        {/* Right Column: Question Card & Options */}
        <div className={`space-y-5 ${relatedPassage ? "lg:col-span-5" : ""}`}>
          <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-6 sm:p-7 shadow-card space-y-5 transition-colors duration-300">
            <div className="flex items-start justify-between gap-4">
              <div className="flex items-center space-x-2">
                <span className="px-2.5 py-0.5 rounded-md text-xs font-bold bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] font-mono shadow-subtle dark:shadow-glow-cyan">
                  题号 {currentIndex + 1}
                </span>
                <span className="text-xs text-stone-400 dark:text-zinc-500 font-medium">
                  {currentQ.q_type === "reading_item" ? "阅读小题" : currentQ.q_type === "cloze_item" ? "完形小题" : "客观题"} ({currentQ.points} 分)
                </span>
              </div>

              <button
                onClick={handleToggleFav}
                className={`px-2.5 py-1 rounded-lg border text-xs font-medium flex items-center space-x-1.5 transition-all duration-150 ${
                  isFavorited 
                    ? "bg-amber-50 dark:bg-amber-950/50 border-amber-200 dark:border-amber-500/30 text-amber-700 dark:text-amber-300 font-semibold" 
                    : "bg-white dark:bg-zinc-800 border-black/[0.06] dark:border-cyan-500/20 text-stone-400 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200 shadow-subtle"
                }`}
              >
                <Bookmark className={`w-3.5 h-3.5 ${isFavorited ? "fill-amber-400" : ""}`} />
                <span>{isFavorited ? "已收藏" : "收藏"}</span>
              </button>
            </div>

            <h3 className="text-base font-bold text-stone-900 dark:text-zinc-100 leading-relaxed">
              {currentQ.stem}
            </h3>

            {/* Tactile Capsule Options */}
            {(() => {
              const opts = normalizeOptions(currentQ.options);
              const isGrid = opts.length > 5;
              return (
                <div className={isGrid ? "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2" : "space-y-2.5"}>
                  {opts.map((opt) => {
                    const isSelected = selectedAnswer === opt.key;
                    const isTheCorrectOne = opt.key === currentQ.correct_answer;

                    let btnStyle = "bg-stone-50/70 dark:bg-zinc-900/70 border-black/[0.06] dark:border-cyan-500/20 hover:bg-stone-100/70 dark:hover:bg-zinc-800/70 hover:border-emerald-600/30 dark:hover:border-cyan-400/40 text-stone-800 dark:text-zinc-200 hover:-translate-y-[1px]";
                    let badgeStyle = "bg-white dark:bg-zinc-800 border-black/[0.08] dark:border-cyan-500/25 text-stone-700 dark:text-zinc-300";

                    if (isAnswered) {
                      if (isTheCorrectOne) {
                        btnStyle = "bg-emerald-50/80 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-500/50 text-emerald-950 dark:text-emerald-200 font-semibold shadow-subtle ring-1 ring-emerald-300 dark:ring-emerald-500/50";
                        badgeStyle = "bg-emerald-600 text-white border-emerald-600";
                      } else if (isSelected && !isTheCorrectOne) {
                        btnStyle = "bg-rose-50/80 dark:bg-rose-950/40 border-rose-300 dark:border-rose-500/50 text-rose-950 dark:text-rose-200 font-semibold";
                        badgeStyle = "bg-rose-600 text-white border-rose-600";
                      } else {
                        btnStyle = "bg-stone-50/40 dark:bg-zinc-900/40 border-black/[0.03] dark:border-cyan-500/10 text-stone-400 dark:text-zinc-600 opacity-60";
                        badgeStyle = "bg-stone-100 dark:bg-zinc-800 border-black/[0.04] dark:border-cyan-500/10 text-stone-400 dark:text-zinc-600";
                      }
                    }

                    return (
                      <button
                        key={opt.key}
                        onClick={() => handleSelectOption(opt.key)}
                        disabled={isAnswered}
                        className={isGrid
                          ? `p-2 sm:p-2.5 rounded-xl border text-left flex items-center space-x-2 transition-all duration-150 active:scale-[0.98] ${btnStyle}`
                          : `w-full p-3.5 rounded-xl border text-left flex items-start space-x-3 transition-all duration-150 ease-spring shadow-subtle ${btnStyle}`}
                        title={opt.text}
                      >
                        <span className={`w-6 h-6 rounded-lg border font-bold text-xs font-mono flex items-center justify-center shrink-0 ${badgeStyle}`}>
                          {opt.key}
                        </span>
                        <span className={`text-xs ${isGrid ? "truncate font-medium" : "sm:text-sm pt-0.5 leading-relaxed"} flex-1`}>
                          {opt.text}
                        </span>
                        {!isAnswered && !isGrid && (
                          <span className="text-[10px] text-stone-400 dark:text-zinc-500 font-mono self-center hidden sm:inline">
                            [{opt.key}]
                          </span>
                        )}
                        {isAnswered && isTheCorrectOne && (
                          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 ml-auto shrink-0" />
                        )}
                        {isAnswered && isSelected && !isTheCorrectOne && (
                          <XCircle className="w-3.5 h-3.5 text-rose-600 dark:text-rose-400 ml-auto shrink-0" />
                        )}
                      </button>
                    );
                  })}
                </div>
              );
            })()}

            {/* Answer Result & Explanation Panel */}
            {isAnswered && (
              <div className="pt-4 border-t border-stone-100 dark:border-zinc-800 animate-in fade-in duration-200 space-y-3.5">
                <div className={`p-3.5 rounded-xl border flex items-center justify-between ${
                  isCorrect 
                    ? "bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200/80 dark:border-emerald-500/30 text-emerald-950 dark:text-emerald-200" 
                    : "bg-rose-50/70 dark:bg-rose-950/40 border-rose-200/80 dark:border-rose-500/30 text-rose-950 dark:text-rose-200"
                }`}>
                  <div className="flex items-center space-x-2">
                    {isCorrect ? (
                      <>
                        <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                        <span className="font-bold text-xs">回答正确！加 {currentQ.points} 分</span>
                      </>
                    ) : (
                      <>
                        <XCircle className="w-4 h-4 text-rose-600 dark:text-rose-400" />
                        <span className="font-bold text-xs">
                          回答错误 (正确答案: {currentQ.correct_answer}) · 已入错题本
                        </span>
                      </>
                    )}
                  </div>
                </div>

                <div className="p-4 rounded-xl bg-stone-50/80 dark:bg-zinc-900/80 border border-black/[0.04] dark:border-cyan-500/20">
                  <div className="flex items-center space-x-1.5 text-stone-900 dark:text-zinc-100 font-bold text-xs mb-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
                    <span>考点精析与释义</span>
                  </div>
                  <p className="text-xs text-stone-600 dark:text-zinc-300 leading-relaxed whitespace-pre-line">
                    {currentQ.explanation}
                  </p>
                </div>

                <div className="p-3 bg-amber-50/40 dark:bg-amber-950/20 rounded-xl border border-amber-200/60 dark:border-amber-500/20">
                  <div className="flex items-center space-x-1.5 text-xs font-semibold text-amber-800 dark:text-amber-300 mb-1.5">
                    <Edit3 className="w-3.5 h-3.5" />
                    <span>个人做题笔记心得:</span>
                  </div>
                  <input
                    type="text"
                    defaultValue={editingNotes[currentQ.id] || ""}
                    onBlur={(e) => handleSaveNote(e.target.value)}
                    placeholder="在此输入个人做题笔记，失焦自动保存..."
                    className="w-full text-xs bg-white dark:bg-zinc-900 border border-amber-200 dark:border-amber-500/30 rounded-lg px-3 py-1.5 text-stone-800 dark:text-zinc-200 focus:outline-none focus:ring-1 focus:ring-amber-500 shadow-subtle"
                  />
                </div>
              </div>
            )}
          </div>

          {/* Bottom Nav Buttons */}
          <div className="flex items-center justify-between">
            <button
              onClick={() => navigateTo(currentIndex - 1)}
              disabled={currentIndex === 0}
              className="px-4 py-2 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 hover:text-stone-950 dark:hover:text-white hover:bg-stone-50 dark:hover:bg-zinc-700 disabled:opacity-40 text-xs font-semibold flex items-center space-x-1.5 transition-all shadow-subtle active:scale-[0.98]"
            >
              <ChevronLeft className="w-3.5 h-3.5" />
              <span>上一题 (←)</span>
            </button>

            <button
              onClick={() => navigateTo(currentIndex + 1)}
              disabled={currentIndex === questions.length - 1}
              className="px-5 py-2 rounded-xl bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 disabled:opacity-40 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle hover:shadow-card dark:shadow-glow-cyan flex items-center space-x-1.5 transition-all active:scale-[0.98]"
            >
              <span>下一题 (→)</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function PracticePage() {
  return (
    <Suspense fallback={<div className="py-20 text-center text-slate-500">正在初始化...</div>}>
      <PracticeContent />
    </Suspense>
  );
}
