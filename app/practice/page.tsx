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
  RotateCcw,
  BookOpen,
  HelpCircle,
  ListOrdered,
  Award,
  Target,
  X,
  Maximize2,
  Minimize2,
  Keyboard
} from "lucide-react";
import SplitPane from "@/components/SplitPane";
import KeyboardShortcutsModal from "@/components/KeyboardShortcutsModal";
import PassageHighlighter from "@/components/PassageHighlighter";

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
  const [practiceMobileTab, setPracticeMobileTab] = useState<"question" | "passage">("question");
  const [showAnswerSheet, setShowAnswerSheet] = useState(false);
  const [showPassageSheet, setShowPassageSheet] = useState(false);
  const [isZenMode, setIsZenMode] = useState(false);
  const [showShortcutsModal, setShowShortcutsModal] = useState(false);
  const passageContainerRef = useRef<HTMLDivElement | null>(null);
  const touchStartRef = useRef<{ x: number; y: number } | null>(null);

  // Sync body class for Zen Mode
  useEffect(() => {
    document.body.classList.toggle("enway-zen-mode", isZenMode);
    return () => {
      document.body.classList.remove("enway-zen-mode");
    };
  }, [isZenMode]);

  const handleTouchStart = (e: React.TouchEvent) => {
    // Only detect single touch gestures
    if (e.touches.length === 1) {
      touchStartRef.current = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    }
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (!touchStartRef.current) return;
    const deltaX = e.changedTouches[0].clientX - touchStartRef.current.x;
    const deltaY = e.changedTouches[0].clientY - touchStartRef.current.y;
    touchStartRef.current = null;

    // Do not trigger question swipe if any drawer/modal is active or user is selecting text
    if (showAnswerSheet || showPassageSheet || showShortcutsModal) return;
    if (typeof window !== "undefined" && window.getSelection()?.toString().trim()) return;

    // Minimum 48px horizontal displacement with >1.8 ratio against vertical scroll to prevent false triggers
    if (Math.abs(deltaX) > 48 && Math.abs(deltaX) > Math.abs(deltaY) * 1.8) {
      if (deltaX < 0) {
        // Swipe Left -> Next question
        if (currentIndex < questions.length - 1) {
          navigateTo(currentIndex + 1);
        }
      } else {
        // Swipe Right -> Previous question
        if (currentIndex > 0) {
          navigateTo(currentIndex - 1);
        }
      }
    }
  };

  // Mobile drawer body scroll lock & overscroll containment
  useEffect(() => {
    if (showAnswerSheet || showPassageSheet || showShortcutsModal) {
      const originalOverflow = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      return () => {
        document.body.style.overflow = originalOverflow;
      };
    }
  }, [showAnswerSheet, showPassageSheet, showShortcutsModal]);

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

  const persistDraft = (answers: Record<string, string>, targetIdx: number) => {
    if (!examId) return;
    let aCount = 0;
    let cCount = 0;
    let score = 0;
    questions.forEach((q) => {
      const ans = answers[q.id];
      if (ans) {
        aCount++;
        if (ans === q.correct_answer) {
          cCount++;
          score += Number(q.points || 2);
        }
      }
    });
    savePracticeDraft(examId, answers, targetIdx, {
      score,
      correctCount: cCount,
      totalQuestions: questions.length,
      answeredCount: aCount,
    });
  };

  const navigateTo = (newIdx: number) => {
    const safeIdx = Math.max(0, Math.min(questions.length - 1, newIdx));
    setCurrentIndex(safeIdx);
    persistDraft(userAnswers, safeIdx);

    // Smooth scroll reading passage to top if switching questions
    if (passageContainerRef.current) {
      passageContainerRef.current.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  const handleJumpToQuestion = (targetIdx: number) => {
    navigateTo(targetIdx);
    setShowAnswerSheet(false);
    setPracticeMobileTab("question");
  };

  const handleJumpToFirstUnanswered = () => {
    const firstUnansweredIdx = questions.findIndex((q) => !userAnswers[q.id]);
    if (firstUnansweredIdx >= 0) {
      handleJumpToQuestion(firstUnansweredIdx);
    } else {
      setShowAnswerSheet(false);
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

  const practiceStateRef = useRef({ currentIndex, questions, userAnswers, examId, exam });
  practiceStateRef.current = { currentIndex, questions, userAnswers, examId, exam };

  const handleSelectOption = (key: string, targetIndex?: number) => {
    const { currentIndex: curIdx, questions: qs, userAnswers: uAns, examId: eId, exam: curExam } = practiceStateRef.current;
    const idx = typeof targetIndex === "number" ? targetIndex : curIdx;
    const q = qs[idx] || qs[0];
    if (!q) return;
    const isAns = Boolean(uAns[q.id]);
    if (isAns) return;

    const nextAnswers = { ...uAns, [q.id]: key };
    setUserAnswers(nextAnswers);
    setShowExplanation((prev) => ({ ...prev, [q.id]: true }));

    // Instant LocalStorage save with stats calculation
    if (eId) {
      persistDraft(nextAnswers, idx);
    }

    if (key !== q.correct_answer) {
      recordMistake({
        questionId: q.id,
        examId: curExam?.id,
        categoryId: curExam?.category_id,
        wrongAnswer: key,
      });
    }
  };

  // BeforeUnload Exit Protection: sync latest draft on tab close
  useEffect(() => {
    if (!examId || loading) return;

    const handleBeforeUnload = () => {
      const { userAnswers: uAns, currentIndex: cIdx } = practiceStateRef.current;
      if (Object.keys(uAns).length > 0) {
        persistDraft(uAns, cIdx);
      }
    };

    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [examId, loading, questions]);

  // Physical keyboard shortcuts (A/B/C/D to answer, Arrows/J/K to navigate, Z for Zen, M for sheet, ? for help)
  useEffect(() => {
    if (loading || questions.length === 0) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement | null;
      if (
        e.isComposing ||
        target instanceof HTMLInputElement ||
        target instanceof HTMLTextAreaElement ||
        target?.isContentEditable ||
        target?.closest?.("input, textarea, [contenteditable='true']")
      ) {
        return;
      }

      const { currentIndex: cIdx, questions: qs } = practiceStateRef.current;
      const targetQ = qs[cIdx];
      const validKeys = targetQ
        ? normalizeOptions(targetQ.options).map((o) => o.key.toUpperCase())
        : ["A", "B", "C", "D"];
      const key = e.key.toUpperCase();

      if (e.key === "Escape") {
        setShowShortcutsModal(false);
        setShowAnswerSheet(false);
        setShowPassageSheet(false);
        setIsZenMode(false);
        return;
      }

      if (e.key === "?" || key === "H") {
        e.preventDefault();
        setShowShortcutsModal((prev) => !prev);
        return;
      }

      if (key === "Z") {
        e.preventDefault();
        setIsZenMode((prev) => !prev);
        return;
      }

      if (key === "M" || e.key === "Tab") {
        e.preventDefault();
        setShowAnswerSheet((prev) => !prev);
        return;
      }

      if (key === "F") {
        e.preventDefault();
        handleToggleFav();
        return;
      }

      if (validKeys.includes(key)) {
        e.preventDefault();
        handleSelectOption(key, cIdx);
      } else if (e.key === "ArrowLeft" || key === "J") {
        e.preventDefault();
        navigateTo(cIdx - 1);
      } else if (e.key === "ArrowRight" || key === "K") {
        e.preventDefault();
        navigateTo(cIdx + 1);
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
  }, [loading, questions.length]);

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

  const currentOptions = normalizeOptions(currentQ.options);
  const optionKeys = currentOptions.map((o) => o.key.toUpperCase());
  const optionKeyLabel = optionKeys.length > 4 && optionKeys.includes("G")
    ? "[A~G]"
    : optionKeys.length === 2 && optionKeys.includes("T") && optionKeys.includes("F")
      ? "[T/F]"
      : `[${optionKeys.join("/") || "A/B/C/D"}]`;

  // Live statistics calculation
  const totalQuestions = questions.length;
  let answeredCount = 0;
  let correctCount = 0;
  let currentScore = 0;
  questions.forEach((q) => {
    const ans = userAnswers[q.id];
    if (ans) {
      answeredCount++;
      if (ans === q.correct_answer) {
        correctCount++;
        currentScore += Number(q.points || 2);
      }
    }
  });
  const accuracy = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
  const progressPercent = totalQuestions > 0 ? Math.round((answeredCount / totalQuestions) * 100) : 0;

  // Question sections for answer sheet
  const section1 = questions.slice(0, 20); // 完形填空 (1-20)
  const section2 = questions.slice(20, 40); // 传统阅读 Part A (21-40)
  const section3 = questions.slice(40); // 新题型 Part B (41-45, 如有)

  const renderSheetButton = (q: any, overallIdx: number) => {
    const ans = userAnswers[q.id];
    const isAns = Boolean(ans);
    const isCorr = isAns && ans === q.correct_answer;
    const isCurr = overallIdx === currentIndex;

    let btnStyle = "bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 hover:bg-stone-200 dark:hover:bg-zinc-700 border border-transparent";
    if (isAns) {
      btnStyle = isCorr 
        ? "bg-emerald-600 text-white font-bold shadow-xs hover:bg-emerald-700" 
        : "bg-rose-600 text-white font-bold shadow-xs hover:bg-rose-700";
    }

    const ringStyle = isCurr 
      ? "ring-2 ring-offset-2 ring-emerald-600 dark:ring-cyber-400 dark:ring-offset-[#11131a] scale-105 z-10" 
      : "";

    return (
      <button
        key={q.id}
        type="button"
        onClick={() => handleJumpToQuestion(overallIdx)}
        className={`h-9 rounded-xl text-xs font-mono font-bold transition-all duration-150 flex items-center justify-center relative ${btnStyle} ${ringStyle}`}
        title={`第 ${overallIdx + 1} 题 ${isAns ? (isCorr ? "(正确)" : `(错误，选 ${ans})`) : "(未答)"}`}
      >
        <span>{overallIdx + 1}</span>
      </button>
    );
  };

  return (
    <div 
      onTouchStart={handleTouchStart}
      onTouchEnd={handleTouchEnd}
      className="space-y-6 animate-in fade-in duration-200 pb-20 lg:pb-0"
    >
      {/* Top Header Bar */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-white/85 dark:bg-[#11131a]/85 backdrop-blur-xl p-3.5 sm:p-4 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card transition-colors duration-300">
        <div className="flex items-center space-x-3">
          <Link
            href="/"
            className="p-2 text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-100 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-xl transition-colors shrink-0"
            title="返回真题大厅"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="min-w-0">
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 border border-black/[0.04] dark:border-cyan-500/20 font-mono tracking-wide shrink-0">
                精读逐题练
              </span>
              <h2 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100 truncate">
                {exam?.title}
              </h2>
            </div>
            
            {/* Live Progress, Score & Accuracy Status Pills */}
            <div className="flex flex-wrap items-center gap-2 mt-1.5 text-xs font-mono">
              {/* Progress */}
              <div className="flex items-center space-x-1.5 px-2 py-0.5 rounded-md bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 border border-black/[0.04] dark:border-cyan-500/15">
                <Target className="w-3 h-3 text-emerald-600 dark:text-cyber-400" />
                <span>已练: <strong className="text-stone-900 dark:text-zinc-100">{answeredCount}</strong>/{totalQuestions} ({progressPercent}%)</span>
                <div className="w-12 h-1.5 rounded-full bg-stone-200 dark:bg-zinc-700 overflow-hidden ml-1 hidden sm:block">
                  <div 
                    className="h-full bg-emerald-600 dark:bg-cyber-400 rounded-full transition-all duration-300" 
                    style={{ width: `${progressPercent}%` }} 
                  />
                </div>
              </div>

              {/* Score */}
              <div className="flex items-center space-x-1 px-2 py-0.5 rounded-md bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-amber-200/60 dark:border-amber-500/20">
                <Award className="w-3 h-3 text-amber-600 dark:text-amber-400" />
                <span>得分: <strong className="font-bold">{currentScore}</strong>分</span>
              </div>

              {/* Accuracy */}
              <div className="flex items-center space-x-1 px-2 py-0.5 rounded-md bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border border-emerald-200/60 dark:border-emerald-500/20">
                <CheckCircle2 className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />
                <span>正确率: <strong className="font-bold">{accuracy}%</strong></span>
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons & Answer Sheet Trigger */}
        <div className="flex items-center space-x-2 self-end sm:self-center shrink-0">
          {/* Zen Focus Mode Toggle (PC & Mobile) */}
          <button
            type="button"
            onClick={() => setIsZenMode(!isZenMode)}
            title="专注全屏模式 (快捷键 Z)"
            className={`px-2.5 py-1.5 rounded-xl border text-xs font-semibold flex items-center space-x-1.5 transition-all duration-150 active:scale-[0.98] ${
              isZenMode 
                ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] border-emerald-700 dark:border-cyber-400 shadow-subtle dark:shadow-glow-cyan" 
                : "bg-white dark:bg-zinc-800 border-black/[0.06] dark:border-cyan-500/20 text-stone-600 dark:text-zinc-300 hover:text-stone-950 dark:hover:text-white hover:bg-stone-50 dark:hover:bg-zinc-700 shadow-subtle"
            }`}
          >
            {isZenMode ? <Minimize2 className="w-3.5 h-3.5" /> : <Maximize2 className="w-3.5 h-3.5" />}
            <span className="hidden sm:inline">{isZenMode ? "退出专注" : "专注模式"}</span>
            <kbd className="hidden lg:inline-block px-1 py-0.2 rounded bg-black/10 dark:bg-white/10 text-[9px] font-mono">Z</kbd>
          </button>

          {/* Keyboard Shortcuts Cheat Sheet Button */}
          <button
            type="button"
            onClick={() => setShowShortcutsModal(true)}
            title="PC 快捷键速查表 (快捷键 ? 或 H)"
            className="p-2 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-100 hover:bg-stone-50 dark:hover:bg-zinc-700 transition-colors shadow-subtle hidden sm:flex items-center justify-center"
          >
            <Keyboard className="w-3.5 h-3.5" />
          </button>

          {/* Answer Sheet Quick Button */}
          <button
            onClick={() => setShowAnswerSheet(true)}
            title="打开全卷答题卡快速跳转 (快捷键 M)"
            className="px-3 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-stone-100 dark:bg-zinc-800 hover:bg-stone-200/80 dark:hover:bg-zinc-700 text-stone-800 dark:text-zinc-200 text-xs font-bold flex items-center space-x-1.5 transition-all shadow-subtle active:scale-[0.98]"
          >
            <ListOrdered className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
            <span>答题卡</span>
            <span className="font-mono text-[10px] px-1.5 py-0.2 rounded-full bg-stone-200 dark:bg-zinc-700 text-stone-700 dark:text-zinc-300 font-bold">
              {answeredCount}/{totalQuestions}
            </span>
            <kbd className="hidden lg:inline-block px-1 py-0.2 rounded bg-black/10 dark:bg-white/10 text-[9px] font-mono">M</kbd>
          </button>

          {Object.keys(userAnswers).length > 0 && (
            <button
              onClick={handleResetPractice}
              title="清空当前做题记录重新开始"
              className="px-2.5 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 text-stone-500 dark:text-zinc-400 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 text-xs font-semibold flex items-center space-x-1 transition-all shadow-subtle"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">重做</span>
            </button>
          )}

          <button
            onClick={() => setLargeFont(!largeFont)}
            title="字号缩放"
            className={`px-2.5 py-1.5 rounded-xl border text-xs font-semibold flex items-center space-x-1 transition-all duration-150 active:scale-[0.98] ${
              largeFont 
                ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] border-emerald-700 dark:border-cyber-400 shadow-subtle dark:shadow-glow-cyan" 
                : "bg-white dark:bg-zinc-800 border-black/[0.06] dark:border-cyan-500/20 text-stone-600 dark:text-zinc-300 hover:text-stone-950 dark:hover:text-white hover:bg-stone-50 dark:hover:bg-zinc-700 shadow-subtle"
            }`}
          >
            <Type className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">{largeFont ? "标准字号" : "大字号"}</span>
          </button>

          <div className="text-xs font-bold text-stone-800 dark:text-cyber-300 bg-stone-100 dark:bg-zinc-800 px-3 py-1.5 rounded-xl font-mono">
            {currentIndex + 1} / {questions.length} 题
          </div>
        </div>
      </div>

      {/* Zen Mode Floating Top Bar (Active when in Zen Mode) */}
      {isZenMode && (
        <div className="sticky top-2 z-50 bg-stone-900/90 dark:bg-zinc-900/95 backdrop-blur-md text-white px-4 py-2 rounded-2xl shadow-2xl border border-white/10 dark:border-cyan-500/30 flex items-center justify-between gap-4 animate-in slide-in-from-top duration-200 no-print">
          <div className="flex items-center space-x-3 truncate">
            <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0">
              专注模式
            </span>
            <span className="text-xs font-bold truncate max-w-sm hidden sm:inline">{exam?.title}</span>
            <span className="text-xs font-mono text-stone-300 shrink-0">
              题号 {currentIndex + 1} / {questions.length} · 正确率 {accuracy}%
            </span>
          </div>

          <div className="flex items-center space-x-2 shrink-0">
            <button
              onClick={() => setShowShortcutsModal(true)}
              className="p-1.5 rounded-xl bg-white/10 hover:bg-white/20 text-white text-xs flex items-center space-x-1"
              title="快捷键速查 (?)"
            >
              <Keyboard className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={() => setIsZenMode(false)}
              className="px-3 py-1 rounded-xl bg-white/20 hover:bg-white/30 text-white text-xs font-bold flex items-center space-x-1 transition-all"
            >
              <Minimize2 className="w-3.5 h-3.5" />
              <span>退出专注 (Esc)</span>
            </button>
          </div>
        </div>
      )}

      {/* Mobile View Switcher (Sticky below header) */}
      {relatedPassage && (
        <div className="lg:hidden sticky top-[4.5rem] z-20 flex items-center bg-stone-100/95 dark:bg-zinc-900/95 backdrop-blur-md p-1 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 shadow-sm no-print">
          <button
            type="button"
            onClick={() => setPracticeMobileTab("passage")}
            className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center space-x-1.5 transition-all ${
              practiceMobileTab === "passage"
                ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-sm"
                : "text-stone-600 dark:text-zinc-400"
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>阅读篇章材料</span>
          </button>
          <button
            type="button"
            onClick={() => setPracticeMobileTab("question")}
            className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center space-x-1.5 transition-all ${
              practiceMobileTab === "question"
                ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-sm"
                : "text-stone-600 dark:text-zinc-400"
            }`}
          >
            <HelpCircle className="w-3.5 h-3.5" />
            <span>本题研习 ({currentIndex + 1}/{questions.length})</span>
          </button>
        </div>
      )}

      {/* Main Dual-Column Split Reading Experience (PC SplitPane / Mobile Tabs) */}
      {(() => {
        const leftPane = relatedPassage ? (
          <div 
            ref={passageContainerRef} 
            className={`${practiceMobileTab === "passage" ? "block" : "hidden"} lg:block bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-5 sm:p-7 shadow-card overflow-y-auto max-h-[75vh] lg:max-h-[82vh] leading-relaxed select-text transition-colors duration-300`}
          >
            <div className="flex items-center justify-between pb-3.5 mb-4 border-b border-stone-100 dark:border-zinc-800">
              <span className="text-xs font-bold font-sans uppercase tracking-wider text-stone-900 dark:text-zinc-100 truncate pr-2">
                {relatedPassage.title}
              </span>
              <span className="text-[11px] text-stone-400 dark:text-zinc-500 font-sans shrink-0">
                💡 双击查词 · 划选高亮
              </span>
            </div>

            <PassageHighlighter
              passageId={relatedPassage.id}
              content={relatedPassage.content}
              largeFont={largeFont}
            />

            {/* Mobile Return to Question Button */}
            <div className="lg:hidden mt-6 pt-4 border-t border-stone-100 dark:border-zinc-800 flex justify-end">
              <button
                type="button"
                onClick={() => setPracticeMobileTab("question")}
                className="px-4 py-2 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] text-xs font-bold flex items-center space-x-1.5 shadow-subtle active:scale-95"
              >
                <span>查看题目作答 ({currentIndex + 1}/{questions.length}) &rarr;</span>
              </button>
            </div>
          </div>
        ) : null;

        const rightPane = (
          <div className={`${practiceMobileTab === "question" ? "block" : "hidden"} lg:block space-y-5`}>
            <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-5 sm:p-7 shadow-card space-y-5 transition-colors duration-300">
              <div className="flex items-start justify-between gap-4">
                <div className="flex items-center space-x-2">
                  <span className="px-2.5 py-0.5 rounded-md text-xs font-bold bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] font-mono shadow-subtle dark:shadow-glow-cyan">
                    题号 {currentIndex + 1}
                  </span>
                  <span className="text-xs text-stone-400 dark:text-zinc-500 font-medium">
                    {currentQ.q_type === "reading_item" ? "阅读小题" : currentQ.q_type === "cloze_item" ? "完形小题" : "客观题"} ({currentQ.points} 分)
                  </span>
                </div>

                <div className="flex items-center space-x-1.5">
                  {relatedPassage && (
                    <button
                      type="button"
                      onClick={() => setShowPassageSheet(true)}
                      className="lg:hidden px-2.5 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border border-emerald-200/60 dark:border-emerald-500/25 text-xs font-bold flex items-center space-x-1 active:scale-95 shadow-subtle"
                      title="在当前页面升起材料抽屉速查线索句"
                    >
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>速查材料</span>
                    </button>
                  )}

                  <button
                    onClick={handleToggleFav}
                    title="收藏本题 (快捷键 F)"
                    className={`px-2.5 py-1 rounded-lg border text-xs font-medium flex items-center space-x-1.5 transition-all duration-150 ${
                      isFavorited 
                        ? "bg-amber-50 dark:bg-amber-950/50 border-amber-200 dark:border-amber-500/30 text-amber-700 dark:text-amber-300 font-semibold" 
                        : "bg-white dark:bg-zinc-800 border-black/[0.06] dark:border-cyan-500/20 text-stone-400 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200 shadow-subtle"
                    }`}
                  >
                    <Bookmark className={`w-3.5 h-3.5 ${isFavorited ? "fill-amber-400" : ""}`} />
                    <span>{isFavorited ? "已收藏" : "收藏"}</span>
                    <kbd className="hidden lg:inline-block px-1 py-0.2 rounded bg-black/10 dark:bg-white/10 text-[9px] font-mono">F</kbd>
                  </button>
                </div>
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

            {/* Bottom Nav Stepper Buttons */}
            <div className="flex items-center justify-between gap-3 pt-2">
              <button
                onClick={() => navigateTo(currentIndex - 1)}
                disabled={currentIndex === 0}
                className="flex-1 sm:flex-none px-4 py-2.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 hover:text-stone-950 dark:hover:text-white hover:bg-stone-50 dark:hover:bg-zinc-700 disabled:opacity-30 text-xs font-bold flex items-center justify-center space-x-1.5 transition-all shadow-subtle active:scale-[0.98]"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>上一题</span>
                <kbd className="hidden lg:inline-block px-1 py-0.2 rounded bg-stone-100 dark:bg-zinc-700 text-[9px] font-mono opacity-60">←</kbd>
              </button>

              <span className="text-xs font-mono font-bold text-stone-500 dark:text-zinc-400 sm:hidden">
                {currentIndex + 1} / {questions.length}
              </span>

              <button
                onClick={() => navigateTo(currentIndex + 1)}
                disabled={currentIndex === questions.length - 1}
                className="flex-1 sm:flex-none px-5 py-2.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 disabled:opacity-30 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle hover:shadow-card dark:shadow-glow-cyan flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
              >
                <span>下一题</span>
                <kbd className="hidden lg:inline-block px-1 py-0.2 rounded bg-white/20 text-[9px] font-mono">→</kbd>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        );

        return relatedPassage ? (
          <SplitPane
            storageKey="enway_split_ratio_practice"
            defaultRatio={60}
            isZenMode={isZenMode}
            leftPane={leftPane}
            rightPane={rightPane}
          />
        ) : (
          <div className="max-w-3xl mx-auto">
            {rightPane}
          </div>
        );
      })()}

      {/* Mobile Fixed Bottom Dock for Immersive Practice (SafeArea Aware) */}
      <div className="lg:hidden fixed bottom-0 left-0 right-0 z-30 bg-white/95 dark:bg-[#0e1017]/95 backdrop-blur-xl border-t border-black/[0.08] dark:border-cyan-500/20 px-3.5 py-2 pb-[max(0.75rem,env(safe-area-inset-bottom))] shadow-lg flex items-center justify-between gap-2.5 no-print">
        <button
          type="button"
          onClick={() => navigateTo(currentIndex - 1)}
          disabled={currentIndex === 0}
          className="px-3.5 py-2 rounded-xl bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 disabled:opacity-30 text-xs font-bold flex items-center space-x-1 active:scale-95 transition-transform"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>上一题</span>
        </button>

        <button
          type="button"
          onClick={() => setShowAnswerSheet(true)}
          className="flex-1 py-2 rounded-xl bg-stone-100 dark:bg-zinc-800 hover:bg-stone-200 dark:hover:bg-zinc-700 text-stone-900 dark:text-zinc-100 font-mono text-xs font-bold flex items-center justify-center space-x-1.5 border border-black/[0.05] dark:border-cyan-500/20 active:scale-98 transition-all"
        >
          <ListOrdered className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
          <span>答题卡 ({currentIndex + 1}/{totalQuestions})</span>
        </button>

        <button
          type="button"
          onClick={() => navigateTo(currentIndex + 1)}
          disabled={currentIndex === questions.length - 1}
          className="px-4 py-2 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] disabled:opacity-30 text-xs font-bold flex items-center space-x-1 active:scale-95 transition-transform"
        >
          <span>下一题</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* Floating Answer Sheet Capsule for PC Only (Bottom-Right FAB) */}
      <div className="hidden lg:block fixed bottom-6 right-6 z-40 no-print">
        <button
          type="button"
          onClick={() => setShowAnswerSheet(true)}
          className="flex items-center space-x-2 px-4 py-2.5 rounded-full bg-stone-900/90 dark:bg-zinc-800/95 hover:bg-black dark:hover:bg-zinc-700 text-white shadow-xl border border-white/10 dark:border-cyan-500/30 backdrop-blur-md transition-all duration-200 active:scale-95 group"
          title="展开全卷答题卡，快速跳选任意题目"
        >
          <ListOrdered className="w-4 h-4 text-emerald-400 dark:text-cyber-400 group-hover:rotate-6 transition-transform" />
          <span className="text-xs font-bold font-sans">答题卡</span>
          <span className="px-1.5 py-0.5 rounded-full bg-white/20 text-[10px] font-mono font-bold">
            {answeredCount}/{totalQuestions}
          </span>
        </button>
      </div>

      {/* Mobile Floating Passage Peek Sheet */}
      {showPassageSheet && relatedPassage && (
        <div 
          className="lg:hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex flex-col justify-end animate-in fade-in duration-150"
          onClick={(e) => {
            if (e.target === e.currentTarget) setShowPassageSheet(false);
          }}
        >
          <div className="bg-white dark:bg-[#11131a] rounded-t-3xl border-t border-black/[0.08] dark:border-cyan-500/25 p-5 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-2xl max-h-[85vh] max-h-[85dvh] flex flex-col animate-in slide-in-from-bottom duration-200">
            <div className="flex items-center justify-between pb-3 border-b border-stone-100 dark:border-zinc-800">
              <div className="flex items-center space-x-2 truncate pr-2">
                <BookOpen className="w-4 h-4 text-emerald-600 dark:text-cyber-400 shrink-0" />
                <span className="text-xs font-bold text-stone-900 dark:text-zinc-100 truncate">
                  {relatedPassage.title}
                </span>
              </div>
              <div className="flex items-center space-x-1.5 shrink-0">
                <button
                  type="button"
                  onClick={() => setLargeFont(!largeFont)}
                  className="p-1.5 rounded-lg text-xs text-stone-500 hover:text-stone-900 dark:text-zinc-400 dark:hover:text-zinc-100 hover:bg-stone-100 dark:hover:bg-zinc-800"
                  title="字号缩放"
                >
                  <Type className="w-4 h-4" />
                </button>
                <button
                  type="button"
                  onClick={() => setShowPassageSheet(false)}
                  className="p-1.5 rounded-full bg-stone-100 dark:bg-zinc-800 text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-100"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
            </div>
            <div className="flex-1 overflow-y-auto overscroll-contain py-3 leading-relaxed text-stone-800 dark:text-zinc-200 font-serif whitespace-pre-line selection:bg-emerald-100/70 dark:selection:bg-cyan-500/30">
              <div className={largeFont ? "text-lg leading-[2.1]" : "text-[15px] leading-[1.85]"}>
                {relatedPassage.content}
              </div>
            </div>
            <div className="pt-2 border-t border-stone-100 dark:border-zinc-800 flex justify-between items-center text-xs text-stone-400 dark:text-zinc-500">
              <span>💡 双击词汇即呼词典</span>
              <button
                type="button"
                onClick={() => setShowPassageSheet(false)}
                className="px-3.5 py-1.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle active:scale-95"
              >
                返回作答 (第 {currentIndex + 1} 题)
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Interactive Answer Sheet Modal / Bottom Sheet Drawer */}
      {showAnswerSheet && (
        <div 
          className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4 animate-in fade-in duration-150"
          onClick={(e) => {
            if (e.target === e.currentTarget) setShowAnswerSheet(false);
          }}
        >
          <div className="bg-white dark:bg-[#11131a] rounded-t-3xl sm:rounded-3xl border-t sm:border border-black/[0.08] dark:border-cyan-500/25 p-5 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-2xl max-w-xl w-full max-h-[85vh] max-h-[85dvh] flex flex-col animate-in slide-in-from-bottom duration-200">
            {/* Header */}
            <div className="flex items-center justify-between pb-3.5 border-b border-stone-100 dark:border-zinc-800">
              <div>
                <div className="flex items-center space-x-2">
                  <ListOrdered className="w-4 h-4 text-emerald-600 dark:text-cyber-400" />
                  <h3 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100">
                    全卷答题卡速览
                  </h3>
                </div>
                <div className="flex items-center space-x-2.5 mt-1 text-xs text-stone-500 dark:text-zinc-400 font-mono">
                  <span>已练: <strong className="text-stone-800 dark:text-zinc-200">{answeredCount}</strong>/{totalQuestions}</span>
                  <span>·</span>
                  <span>得分: <strong className="text-amber-600 dark:text-amber-400">{currentScore}</strong>分</span>
                  <span>·</span>
                  <span>正确率: <strong className="text-emerald-600 dark:text-emerald-400">{accuracy}%</strong></span>
                </div>
              </div>
              <button
                onClick={() => setShowAnswerSheet(false)}
                className="p-1.5 rounded-full bg-stone-100 dark:bg-zinc-800 text-stone-400 hover:text-stone-700 dark:hover:text-zinc-200 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Sheet Content: Categorized Sections */}
            <div className="flex-1 overflow-y-auto overscroll-contain py-4 space-y-4 pr-1">
              {/* Section 1: Use of English */}
              {section1.length > 0 && (
                <div>
                  <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                    <span>Section I 英语知识运用 (完形填空 1 - 20)</span>
                    <span className="font-mono text-[10px]">
                      {section1.filter(q => userAnswers[q.id]).length}/{section1.length}
                    </span>
                  </div>
                  <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                    {section1.map((q, sIdx) => renderSheetButton(q, sIdx))}
                  </div>
                </div>
              )}

              {/* Section 2: Reading Part A */}
              {section2.length > 0 && (
                <div>
                  <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                    <span>Section II 阅读理解 Part A (传统阅读 21 - 40)</span>
                    <span className="font-mono text-[10px]">
                      {section2.filter(q => userAnswers[q.id]).length}/{section2.length}
                    </span>
                  </div>
                  <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                    {section2.map((q, sIdx) => renderSheetButton(q, 20 + sIdx))}
                  </div>
                </div>
              )}

              {/* Section 3: Reading Part B */}
              {section3.length > 0 && (
                <div>
                  <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                    <span>Section II 阅读理解 Part B (新题型 41 - {totalQuestions})</span>
                    <span className="font-mono text-[10px]">
                      {section3.filter(q => userAnswers[q.id]).length}/{section3.length}
                    </span>
                  </div>
                  <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                    {section3.map((q, sIdx) => renderSheetButton(q, 40 + sIdx))}
                  </div>
                </div>
              )}
            </div>

            {/* Footer & Legend */}
            <div className="pt-3.5 border-t border-stone-100 dark:border-zinc-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
              <div className="flex items-center space-x-3 text-[11px] text-stone-500 dark:text-zinc-400">
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-600 inline-block" />
                  <span>正确</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full bg-rose-600 inline-block" />
                  <span>错误</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full bg-stone-200 dark:bg-zinc-700 inline-block" />
                  <span>未答</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full ring-2 ring-emerald-500 inline-block" />
                  <span>当前题</span>
                </span>
              </div>

              <div className="flex items-center space-x-2 w-full sm:w-auto">
                {answeredCount < totalQuestions && (
                  <button
                    onClick={handleJumpToFirstUnanswered}
                    className="flex-1 sm:flex-none px-3 py-1.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/30 font-semibold hover:bg-emerald-100 text-xs transition-colors"
                  >
                    定位首道未答题
                  </button>
                )}
                <button
                  onClick={() => setShowAnswerSheet(false)}
                  className="flex-1 sm:flex-none px-3.5 py-1.5 rounded-xl bg-stone-900 dark:bg-zinc-800 text-white font-semibold hover:bg-stone-800 text-xs transition-colors"
                >
                  返回做题
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Keyboard Shortcuts Cheat Sheet Modal */}
      <KeyboardShortcutsModal 
        isOpen={showShortcutsModal} 
        onClose={() => setShowShortcutsModal(false)} 
      />
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
