"use client";

import { useState, useEffect, useRef, Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { 
  saveExamDraft, 
  getExamDraft, 
  clearExamDraft, 
  saveExamResult, 
  recordMistake, 
  normalizeOptions,
  ExamResult 
} from "@/lib/storage";
import { enqueueSubmissionTask } from "@/lib/submissionQueue";
import { fetchExamDetailWithFallback } from "@/lib/examLoader";
import confetti from "canvas-confetti";
import { 
  ArrowLeft, 
  Clock, 
  Send, 
  CheckCircle2, 
  XCircle, 
  RotateCcw, 
  Printer, 
  FileCheck, 
  HelpCircle,
  ZoomIn,
  ZoomOut,
  Sparkles,
  BookOpen,
  Keyboard,
  FileText,
  ListOrdered,
  X,
  Award,
  Target,
  Maximize2,
  Minimize2
} from "lucide-react";
import SplitPane from "@/components/SplitPane";
import KeyboardShortcutsModal from "@/components/KeyboardShortcutsModal";
import PassageHighlighter from "@/components/PassageHighlighter";

function ExamContent() {
  const searchParams = useSearchParams();
  const examId = searchParams.get("id");

  const [exam, setExam] = useState<any>(null);
  const [passages, setPassages] = useState<any[]>([]);
  const [questions, setQuestions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [remainingSeconds, setRemainingSeconds] = useState<number>(3600);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [result, setResult] = useState<ExamResult | null>(null);
  const [activePassageId, setActivePassageId] = useState<string>("");

  // PC Typography & Keyboard navigation state
  const [readingFontSize, setReadingFontSize] = useState<number>(15);
  const [focusedIndex, setFocusedIndex] = useState<number>(0);

  // Mobile responsive & Zen state
  const [mobileTab, setMobileTab] = useState<"questions" | "passage">("questions");
  const [showMobileAnswerSheet, setShowMobileAnswerSheet] = useState<boolean>(false);
  const [showSubmitReviewSheet, setShowSubmitReviewSheet] = useState<boolean>(false);
  const [isZenMode, setIsZenMode] = useState<boolean>(false);
  const [showShortcutsModal, setShowShortcutsModal] = useState<boolean>(false);

  // Sync body class for Zen Mode
  useEffect(() => {
    document.body.classList.toggle("enway-zen-mode", isZenMode);
    return () => {
      document.body.classList.remove("enway-zen-mode");
    };
  }, [isZenMode]);

  const questionRefs = useRef<Record<string, HTMLDivElement | null>>({});
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
        const examData = detail?.exam || null;
        const passageData = detail?.passages || [];
        const questionData = detail?.questions || [];

        setExam(examData);

        if (passageData.length > 0) {
          setPassages(passageData);
          setActivePassageId(passageData[0].id);
        } else {
          setPassages([]);
          setActivePassageId("");
        }

        setQuestions(questionData);

        // Check draft for real-time exam protection
        const draft = getExamDraft(examId);
        if (draft) {
          setAnswers(draft.answers || {});
          const restoredSec = typeof draft.remainingSeconds === "number"
            ? draft.remainingSeconds
            : (examData?.duration_minutes || 60) * 60;
          setRemainingSeconds(restoredSec);
          if (typeof draft.focusedIndex === "number" && draft.focusedIndex >= 0 && draft.focusedIndex < questionData.length) {
            setFocusedIndex(draft.focusedIndex);
          }
        } else if (examData?.duration_minutes) {
          setRemainingSeconds(examData.duration_minutes * 60);
        }
      } catch (err) {
        console.error("Failed to load exam data:", err);
      } finally {
        setLoading(false);
      }
    }
    loadExam();
  }, [examId]);

  const latestRef = useRef({
    exam,
    questions,
    answers,
    remainingSeconds,
    focusedIndex,
    isSubmitted,
  });
  latestRef.current = { exam, questions, answers, remainingSeconds, focusedIndex, isSubmitted };

  const isSubmittingRef = useRef(false);
  // Tracks the jitter setTimeout for auto-submit so manual submit can cancel it
  const autoSubmitTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // 1. Timer countdown (decoupled from remainingSeconds to prevent 1-second interval thrashing)
  useEffect(() => {
    if (loading || isSubmitted) return;

    const timer = setInterval(() => {
      setRemainingSeconds((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          // 🛡️ 500-Concurrency Dirac Pulse Armor: Inject 0 ~ 12s Uniform Jitter
          // Flattens the 400 req/s Dirac impulse into a smooth <= 41.6 req/s stream
          const jitterMs = Math.floor(Math.random() * 12000);
          autoSubmitTimerRef.current = setTimeout(() => {
            autoSubmitTimerRef.current = null;
            handleSubmit(true);
          }, jitterMs);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => {
      clearInterval(timer);
      // Clean up any pending jitter auto-submit timer on unmount/re-run
      if (autoSubmitTimerRef.current) {
        clearTimeout(autoSubmitTimerRef.current);
        autoSubmitTimerRef.current = null;
      }
    };
  }, [loading, isSubmitted]);

  // 2. Periodic draft background sync every 5 seconds (reliably fires from ref)
  useEffect(() => {
    if (!examId || isSubmitted || loading) return;

    const draftInterval = setInterval(() => {
      const { answers: curAns, remainingSeconds: curSec, focusedIndex: curIdx } = latestRef.current;
      if (examId && Object.keys(curAns).length > 0) {
        saveExamDraft(examId, curAns, curSec, curIdx);
      }
    }, 5000);

    return () => clearInterval(draftInterval);
  }, [examId, isSubmitted, loading]);

  // 3. BeforeUnload Exit Protection: Guarantee instant flush and prevent accidental tab closes
  useEffect(() => {
    if (!examId || isSubmitted || loading) return;

    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      const { answers: curAns, remainingSeconds: curSec, focusedIndex: curIdx } = latestRef.current;
      if (examId) {
        saveExamDraft(examId, curAns, curSec, curIdx);
      }
      if (Object.keys(curAns).length > 0) {
        e.preventDefault();
        e.returnValue = "";
      }
    };

    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [examId, isSubmitted, loading]);

  // 4. PC Keyboard Shortcuts: decoupled with ref to avoid re-binding on each answer
  const keydownRef = useRef({ questions, focusedIndex });
  useEffect(() => {
    keydownRef.current = { questions, focusedIndex };
  });

  useEffect(() => {
    if (isSubmitted || loading) return;

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

      const { questions: qs, focusedIndex: fIdx } = keydownRef.current;
      if (!qs || qs.length === 0) return;

      const key = e.key.toUpperCase();
      const currentQ = qs[fIdx];
      const validKeys = currentQ
        ? normalizeOptions(currentQ.options).map((o) => o.key)
        : ["A", "B", "C", "D"];

      if (e.key === "Escape") {
        setShowShortcutsModal(false);
        setShowMobileAnswerSheet(false);
        setShowSubmitReviewSheet(false);
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
        setShowMobileAnswerSheet((prev) => !prev);
        return;
      }

      if (validKeys.includes(key)) {
        e.preventDefault();
        if (currentQ) {
          handleSelectAnswer(currentQ.id, key);
        }
      } else if (e.key === "ArrowRight" || key === "K") {
        e.preventDefault();
        setFocusedIndex((prev) => {
          const nextIdx = Math.min(qs.length - 1, prev + 1);
          scrollToQuestion(qs[nextIdx]?.id);
          return nextIdx;
        });
      } else if (e.key === "ArrowLeft" || key === "J") {
        e.preventDefault();
        setFocusedIndex((prev) => {
          const prevIdx = Math.max(0, prev - 1);
          scrollToQuestion(qs[prevIdx]?.id);
          return prevIdx;
        });
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
  }, [isSubmitted, loading]);

  const scrollToQuestion = (qId?: string) => {
    if (!qId) return;
    const el = questionRefs.current[qId];
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  const handleBlankClick = (blankNum: number) => {
    const qIdx = blankNum - 1;
    if (qIdx >= 0 && qIdx < questions.length) {
      setFocusedIndex(qIdx);
      scrollToQuestion(questions[qIdx]?.id);
      if (mobileTab === "passage") {
        setMobileTab("questions");
      }
    }
  };

  // Two-way auto-synchronization: switch left reading canvas when question changes
  useEffect(() => {
    if (questions.length === 0 || passages.length === 0) return;
    const currentQ = questions[focusedIndex];
    if (currentQ?.passage_id && currentQ.passage_id !== activePassageId) {
      setActivePassageId(currentQ.passage_id);
    }
    // If Cloze, smooth scroll to corresponding blank
    const curP = passages.find((p) => p.id === (currentQ?.passage_id || activePassageId));
    const isCloze = curP && (curP.title.includes("Use of English") || curP.title.includes("完型") || curP.content.includes("[1]"));
    if (isCloze && focusedIndex < 20) {
      setTimeout(() => {
        const blankEl = document.getElementById(`cloze-blank-${focusedIndex + 1}`);
        if (blankEl) {
          blankEl.scrollIntoView({ behavior: "smooth", block: "center" });
        }
      }, 50);
    }
  }, [focusedIndex, questions, passages]);

  // Mobile drawer body scroll lock & overscroll containment
  useEffect(() => {
    if (showMobileAnswerSheet || showSubmitReviewSheet) {
      const originalOverflow = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      return () => {
        document.body.style.overflow = originalOverflow;
      };
    }
  }, [showMobileAnswerSheet, showSubmitReviewSheet]);

  const handleSelectAnswer = (qId: string, optionKey: string) => {
    if (isSubmitted) return;
    const { remainingSeconds: curSec, focusedIndex: curIdx } = latestRef.current;
    setAnswers((prev) => {
      const next = {
        ...prev,
        [qId]: optionKey,
      };
      if (examId) {
        saveExamDraft(examId, next, curSec, curIdx);
      }
      return next;
    });
  };

  const requestSubmit = () => {
    if (isSubmittingRef.current || isSubmitted) return;
    setShowSubmitReviewSheet(true);
  };

  const executeSubmit = (auto = false) => {
    if (isSubmittingRef.current) return;
    const { exam: curExam, questions: curQuestions, answers: curAnswers, remainingSeconds: curSec } = latestRef.current;
    if (!curExam) return;

    isSubmittingRef.current = true;
    setShowSubmitReviewSheet(false);
    setShowMobileAnswerSheet(false);

    // Cancel pending jitter auto-submit timer (if user submitted manually before timer fired)
    if (autoSubmitTimerRef.current) {
      clearTimeout(autoSubmitTimerRef.current);
      autoSubmitTimerRef.current = null;
    }

    let earnedRawPoints = 0;
    let totalRawPoints = 0;
    const detailAnswers: Record<string, { userAnswer: string; isCorrect: boolean }> = {};

    curQuestions.forEach((q) => {
      const uAns = curAnswers[q.id] || "";
      const isCorr = uAns === q.correct_answer;
      totalRawPoints += Number(q.points || 2);
      if (isCorr) {
        earnedRawPoints += Number(q.points || 2);
      } else {
        recordMistake({
          questionId: q.id,
          examId: curExam.id,
          categoryId: curExam.category_id,
          wrongAnswer: uAns || "未作答",
        });
      }

      detailAnswers[q.id] = {
        userAnswer: uAns,
        isCorrect: isCorr,
      };
    });

    const examTotal = Number(totalRawPoints > 0 ? totalRawPoints : (curExam.total_score || 60));
    const passLine = Number(
      curExam.pass_score && curExam.total_score === examTotal
        ? curExam.pass_score
        : Math.round(examTotal * 0.6)
    );
    const finalScore = Math.round(earnedRawPoints * 10) / 10;
    const passed = finalScore >= passLine;

    const examDuration = Number(curExam?.duration_minutes || 60);
    const examRes: ExamResult = {
      examId: curExam.id,
      examTitle: curExam.title,
      score: finalScore,
      totalScore: examTotal,
      isPassed: passed,
      durationSeconds: Math.max(0, examDuration * 60 - curSec),
      submittedAt: new Date().toISOString(),
      answers: detailAnswers,
    };

    saveExamResult(examRes);
    // 🛡️ Durable Zero-Loss Queue: Enqueue submission task before clearing draft
    enqueueSubmissionTask("exam_result", { examId: curExam.id, score: finalScore });
    clearExamDraft(curExam.id);
    setResult(examRes);
    setIsSubmitted(true);

    if (passed) {
      try {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 },
        });
      } catch (err) {
        console.warn("Confetti effect skipped:", err);
      }
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleSubmit = (auto = false) => {
    if (auto) {
      executeSubmit(true);
    } else {
      requestSubmit();
    }
  };

  const handleRetake = () => {
    if (window.confirm("重新测验将清空本次作答，重新进入考场计时。确定重做吗？")) {
      setAnswers({});
      setIsSubmitted(false);
      setResult(null);
      setRemainingSeconds((exam?.duration_minutes || 60) * 60);
      setFocusedIndex(0);
      isSubmittingRef.current = false; // 🐛 Bug Fix: Release submission lock so retake can be submitted
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
  };

  if (loading) {
    return (
      <div className="py-24 text-center">
        <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-500 font-semibold text-sm">正在加载全真考卷数据与答题卡...</p>
      </div>
    );
  }

  if (!exam) {
    return (
      <div className="py-20 text-center">
        <p className="text-rose-500 font-bold">考卷不存在或已被下架</p>
        <Link href="/" className="inline-block mt-4 text-indigo-600 text-sm font-semibold">
          返回真题大厅
        </Link>
      </div>
    );
  }

  const answeredCount = Object.keys(answers).length;
  const totalExamQuestions = questions.length;
  let examCorrectCount = 0;
  if (isSubmitted && result?.answers) {
    Object.values(result.answers).forEach((a) => {
      if (a?.isCorrect) examCorrectCount++;
    });
  }
  const examAccuracy = totalExamQuestions > 0 && isSubmitted
    ? Math.round((examCorrectCount / totalExamQuestions) * 100)
    : 0;

  const unansweredQuestions = questions
    .map((q, idx) => ({ id: q.id, num: idx + 1, idx }))
    .filter((item) => !answers[item.id]);
  const unansweredCount = unansweredQuestions.length;

  // Question sections for answer sheet
  const examSection1 = questions.slice(0, 20); // 完形填空 (1-20)
  const examSection2 = questions.slice(20, 40); // 传统阅读 Part A (21-40)
  const examSection3 = questions.slice(40); // 新题型 Part B (41-45, 如有)

  const scrollToFirstUnanswered = () => {
    const targetQ = questions.find((q) => !answers[q.id]);
    if (targetQ) {
      const targetIdx = questions.findIndex((q) => q.id === targetQ.id);
      if (targetIdx >= 0) setFocusedIndex(targetIdx);
      scrollToQuestion(targetQ.id);
      setShowMobileAnswerSheet(false);
    }
  };

  const renderExamSheetButton = (q: any, overallIdx: number, isDrawer = false) => {
    const uAns = answers[q.id];
    const isAns = Boolean(uAns);
    const isFocus = overallIdx === focusedIndex;

    let btnStyle = "bg-stone-100 dark:bg-zinc-800 text-stone-600 dark:text-zinc-400 hover:bg-stone-200/80 dark:hover:bg-zinc-700";
    if (isSubmitted) {
      btnStyle = uAns === q.correct_answer 
        ? "bg-emerald-600 text-white font-bold" 
        : "bg-rose-500 text-white font-bold";
    } else if (isFocus) {
      btnStyle = "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] font-bold shadow-subtle dark:shadow-glow-cyan ring-2 ring-offset-2 ring-emerald-600 dark:ring-cyber-400 dark:ring-offset-[#11131a]";
    } else if (isAns) {
      btnStyle = "bg-emerald-50 dark:bg-cyan-950/80 text-emerald-800 dark:text-cyber-300 font-semibold border border-emerald-200/50 dark:border-cyan-500/30";
    }

    return (
      <button
        key={q.id}
        type="button"
        onClick={() => {
          setFocusedIndex(overallIdx);
          if (isDrawer) {
            setMobileTab("questions");
            setShowMobileAnswerSheet(false);
            setTimeout(() => scrollToQuestion(q.id), 50);
          } else {
            scrollToQuestion(q.id);
          }
        }}
        className={`${isDrawer ? "py-2 rounded-xl" : "py-1.5 rounded-lg"} text-xs font-mono font-bold transition-all duration-150 ${btnStyle}`}
        title={`第 ${overallIdx + 1} 题 ${isAns ? (isSubmitted ? (uAns === q.correct_answer ? "(正确)" : `(错误，选 ${uAns})`) : `(已作答: ${uAns})`) : "(未答)"}`}
      >
        {overallIdx + 1}
      </button>
    );
  };

  return (
    <div className="space-y-6 pb-20 animate-in fade-in duration-200">
      {/* Top Sticky Header */}
      <div className="sticky top-16 z-30 bg-white/85 dark:bg-[#11131a]/85 backdrop-blur-xl border border-black/[0.06] dark:border-cyan-500/20 p-3.5 sm:px-6 rounded-2xl shadow-card flex items-center justify-between gap-4 no-print transition-colors duration-300">
        <div className="flex items-center space-x-3 truncate">
          <Link
            href="/"
            className="p-2 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-xl text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-100 transition-colors shrink-0"
            title="返回真题大厅"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="truncate">
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 font-mono tracking-wider shrink-0">
                {exam.category_id} · {exam.year}
              </span>
              
              {/* Progress & Live Scores */}
              {isSubmitted && result ? (
                <div className="flex items-center space-x-2 font-mono">
                  <span className="px-2 py-0.5 rounded text-xs font-bold bg-amber-50 dark:bg-amber-950/50 text-amber-800 dark:text-amber-300 border border-amber-200/60 dark:border-amber-500/30 flex items-center space-x-1">
                    <Award className="w-3 h-3 text-amber-600 dark:text-amber-400" />
                    <span>得分: {result.score} / {result.totalScore}分</span>
                  </span>
                  <span className={`px-2 py-0.5 rounded text-xs font-bold border ${
                    result.isPassed 
                      ? "bg-emerald-50 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 border-emerald-200/60 dark:border-emerald-500/30" 
                      : "bg-rose-50 dark:bg-rose-950/50 text-rose-800 dark:text-rose-300 border-rose-200/60 dark:border-rose-500/30"
                  }`}>
                    正确率: {examAccuracy}%
                  </span>
                </div>
              ) : (
                <div className="flex items-center space-x-1.5 text-xs text-stone-600 dark:text-zinc-400 font-mono">
                  <span className="font-bold">已答 {answeredCount} / {totalExamQuestions} 题</span>
                  <span className="text-[11px] text-stone-400 dark:text-zinc-500 hidden sm:inline">
                    ({totalExamQuestions - answeredCount > 0 ? `待答 ${totalExamQuestions - answeredCount} 题` : "已全答"})
                  </span>
                </div>
              )}

              {!isSubmitted && (
                <span className="hidden lg:inline-flex items-center space-x-1 px-2 py-0.5 rounded text-[10px] font-medium bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-400 border border-emerald-200/60 dark:border-emerald-500/20">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                  <span>实时草稿保全</span>
                </span>
              )}
            </div>
            <h2 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100 truncate mt-0.5">
              {exam.title}
            </h2>
          </div>
        </div>

        {/* Timer & Submission Actions */}
        <div className="flex items-center space-x-2 shrink-0">
          {/* Zen Focus Mode Toggle */}
          <button
            type="button"
            onClick={() => setIsZenMode(!isZenMode)}
            title="专注考场模式 (快捷键 Z)"
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

          {!isSubmitted ? (
            <>
              <div className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-xl font-mono text-xs sm:text-sm font-bold border ${
                remainingSeconds < 300 
                  ? "bg-rose-50 dark:bg-rose-950/50 border-rose-200 dark:border-rose-500/30 text-rose-600 dark:text-rose-400 animate-pulse" 
                  : "bg-stone-100 dark:bg-zinc-800 border-black/[0.04] dark:border-cyan-500/20 text-stone-900 dark:text-cyber-300"
              }`}>
                <Clock className="w-3.5 h-3.5" />
                <span>{formatTime(remainingSeconds)}</span>
              </div>

              <button
                onClick={() => handleSubmit(false)}
                className="px-4 py-2 rounded-xl bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle hover:shadow-card dark:shadow-glow-cyan flex items-center space-x-1.5 transition-all active:scale-[0.98]"
              >
                <Send className="w-3.5 h-3.5" />
                <span>交卷核分</span>
              </button>
            </>
          ) : (
            <div className="flex items-center space-x-2">
              <button
                onClick={handleRetake}
                className="px-3.5 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 text-stone-700 dark:text-zinc-300 hover:bg-stone-100 dark:hover:bg-zinc-800 text-xs font-bold flex items-center space-x-1.5 transition-all shadow-subtle"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>重新测验</span>
              </button>
              <button
                onClick={() => window.print()}
                className="px-3.5 py-1.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] hover:bg-emerald-800 dark:hover:bg-cyber-400 text-xs font-bold flex items-center space-x-1.5 transition-all shadow-subtle"
              >
                <Printer className="w-3.5 h-3.5" />
                <span>纸质打印试卷</span>
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Zen Mode Floating Top Bar (Active when in Zen Mode) */}
      {isZenMode && (
        <div className="sticky top-2 z-50 bg-stone-900/90 dark:bg-zinc-900/95 backdrop-blur-md text-white px-4 py-2 rounded-2xl shadow-2xl border border-white/10 dark:border-cyan-500/30 flex items-center justify-between gap-4 animate-in slide-in-from-top duration-200 no-print">
          <div className="flex items-center space-x-3 truncate">
            <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0">
              专注考场
            </span>
            <span className="text-xs font-bold truncate max-w-sm hidden sm:inline">{exam?.title}</span>
            <div className="flex items-center space-x-1.5 text-xs font-mono shrink-0">
              <Clock className="w-3.5 h-3.5 text-amber-400" />
              <span>{formatTime(remainingSeconds)}</span>
              <span className="text-stone-400">· 已答 {answeredCount}/{questions.length} 题</span>
            </div>
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

      {/* Score Result Card */}
      {isSubmitted && result && (
        <div className="bg-white dark:bg-[#11131a] rounded-2xl p-6 sm:p-8 shadow-card border border-black/[0.06] dark:border-cyan-500/25 text-stone-900 dark:text-zinc-100 animate-in fade-in zoom-in-95 duration-200 no-print transition-colors duration-300">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="flex items-center space-x-5">
              <div className={`w-18 h-18 rounded-2xl flex items-center justify-center text-3xl font-black shadow-subtle ${
                result.isPassed 
                  ? "bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-300 dark:border-emerald-500/40 text-emerald-700 dark:text-emerald-300" 
                  : "bg-rose-50 dark:bg-rose-950/50 border border-rose-300 dark:border-rose-500/40 text-rose-700 dark:text-rose-300"
              }`}>
                {result.score}
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <span className={`px-2.5 py-0.5 rounded-md text-xs font-bold uppercase tracking-wider ${
                    result.isPassed ? "bg-emerald-100 dark:bg-emerald-900/60 text-emerald-800 dark:text-emerald-200" : "bg-rose-100 dark:bg-rose-900/60 text-rose-800 dark:text-rose-200"
                  }`}>
                    {result.isPassed ? "🎉 恭喜达到合格线" : "⚠️ 未达合格基准分 (需重点攻关)"}
                  </span>
                  <span className="text-xs text-stone-400 dark:text-zinc-500 font-mono">满分 {result.totalScore || 60} 分 (及格线: {exam.pass_score || Math.round((result.totalScore || 60) * 0.6)}分)</span>
                </div>
                <h3 className="text-lg font-bold mt-1 text-stone-900 dark:text-zinc-100">{result.examTitle} 测评报告</h3>
                <p className="text-xs text-stone-400 dark:text-zinc-500 mt-1">
                  答题耗时: {Math.floor(result.durationSeconds / 60)} 分 {result.durationSeconds % 60} 秒 · 做错小题已自动归入“智能错题集”
                </p>
              </div>
            </div>

            <div className="flex items-center space-x-4 bg-stone-50 dark:bg-zinc-900 p-3.5 rounded-xl border border-black/[0.04] dark:border-cyan-500/20">
              <div className="text-center px-3">
                <span className="text-[11px] text-stone-400 dark:text-zinc-500 block">答对题数</span>
                <span className="text-xl font-bold text-stone-900 dark:text-cyber-300">
                  {Object.values(result.answers).filter(a => a.isCorrect).length} / {questions.length}
                </span>
              </div>
              <div className="h-8 w-px bg-stone-200 dark:bg-zinc-800" />
              <div className="text-center px-3">
                <span className="text-[11px] text-stone-400 dark:text-zinc-500 block">得分率</span>
                <span className="text-xl font-bold text-stone-900 dark:text-cyber-300">
                  {Math.round((Object.values(result.answers).filter(a => a.isCorrect).length / questions.length) * 100)}%
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Keyboard Shortcuts Guide Banner (PC Only) */}
      {!isSubmitted && (
        <div className="hidden lg:flex items-center justify-between px-3.5 py-2 bg-stone-100/80 dark:bg-zinc-900/80 border border-black/[0.04] dark:border-cyan-500/20 rounded-xl text-xs text-stone-700 dark:text-zinc-300 no-print">
          <div className="flex items-center space-x-2">
            <Keyboard className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400" />
            <span className="font-semibold text-stone-900 dark:text-zinc-100">键盘快捷键：</span>
            <span>键入 <kbd className="px-1.5 py-0.5 bg-white dark:bg-zinc-800 border border-black/[0.08] dark:border-cyan-500/25 rounded font-mono font-bold text-[10px] shadow-subtle text-stone-800 dark:text-zinc-200">A</kbd> <kbd className="px-1.5 py-0.5 bg-white dark:bg-zinc-800 border border-black/[0.08] dark:border-cyan-500/25 rounded font-mono font-bold text-[10px] shadow-subtle text-stone-800 dark:text-zinc-200">B</kbd> <kbd className="px-1.5 py-0.5 bg-white dark:bg-zinc-800 border border-black/[0.08] dark:border-cyan-500/25 rounded font-mono font-bold text-[10px] shadow-subtle text-stone-800 dark:text-zinc-200">C</kbd> <kbd className="px-1.5 py-0.5 bg-white dark:bg-zinc-800 border border-black/[0.08] dark:border-cyan-500/25 rounded font-mono font-bold text-[10px] shadow-subtle text-stone-800 dark:text-zinc-200">D</kbd> 瞬选答案，方向键 <kbd className="px-1.5 py-0.5 bg-white dark:bg-zinc-800 border border-black/[0.08] dark:border-cyan-500/25 rounded font-mono font-bold text-[10px] shadow-subtle text-stone-800 dark:text-zinc-200">↑</kbd> <kbd className="px-1.5 py-0.5 bg-white dark:bg-zinc-800 border border-black/[0.08] dark:border-cyan-500/25 rounded font-mono font-bold text-[10px] shadow-subtle text-stone-800 dark:text-zinc-200">↓</kbd> 翻题</span>
          </div>
          <span className="text-[11px] text-stone-400 dark:text-zinc-500 font-mono">当前聚焦: 第 {focusedIndex + 1} 题</span>
        </div>
      )}

      {/* Mobile View Switcher (Sticky Segmented Control below header) */}
      {passages.length > 0 && !isSubmitted && (
        <div className="lg:hidden sticky top-[4.5rem] z-20 flex items-center bg-stone-100/95 dark:bg-zinc-900/95 backdrop-blur-md p-1 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 shadow-sm no-print">
          <button
            type="button"
            onClick={() => setMobileTab("passage")}
            className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center space-x-1.5 transition-all ${
              mobileTab === "passage"
                ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-sm"
                : "text-stone-600 dark:text-zinc-400"
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>阅读材料 ({passages.length})</span>
          </button>
          <button
            type="button"
            onClick={() => setMobileTab("questions")}
            className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center space-x-1.5 transition-all ${
              mobileTab === "questions"
                ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-sm"
                : "text-stone-600 dark:text-zinc-400"
            }`}
          >
            <FileText className="w-3.5 h-3.5" />
            <span>试卷作答 ({answeredCount}/{questions.length})</span>
          </button>
        </div>
      )}

      {/* PC Dual-Pane Layout (Mobile Tabbed / SplitPane) */}
      {(() => {
        const leftPane = passages.length > 0 ? (
          <div className={`${mobileTab === "passage" || isSubmitted ? "flex" : "hidden"} lg:flex w-full bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card overflow-hidden flex-col lg:sticky lg:top-36 h-[calc(100dvh-12rem)] min-h-[360px] lg:h-[78vh] print-page transition-colors duration-300`}>
            {/* Passage Selector Bar & Font Zoom Controls */}
            <div className="px-5 py-2.5 border-b border-stone-100 dark:border-zinc-800 bg-stone-50/70 dark:bg-zinc-900/70 flex items-center justify-between shrink-0 no-print">
              <div className="flex items-center space-x-1.5 overflow-x-auto no-scrollbar">
                <BookOpen className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400 shrink-0" />
                {passages.map((p, idx) => {
                  const label = (() => {
                    const t = p.title || "";
                    if (t.includes("Use of English") || t.includes("完型")) return "完型填空";
                    if (t.includes("Text 1")) return "Text 1";
                    if (t.includes("Text 2")) return "Text 2";
                    if (t.includes("Text 3")) return "Text 3";
                    if (t.includes("Text 4")) return "Text 4";
                    if (t.includes("Part B") || t.includes("新题型") || t.includes("多项") || t.includes("小标题") || t.includes("排序")) return "新题型";
                    return `篇章 ${idx + 1}`;
                  })();
                  return (
                    <button
                      key={p.id}
                      onClick={() => setActivePassageId(p.id)}
                      className={`px-3 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition-all duration-150 ${
                        activePassageId === p.id 
                          ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle dark:shadow-glow-cyan" 
                          : "bg-white dark:bg-zinc-800 text-stone-600 dark:text-zinc-300 hover:bg-stone-100 dark:hover:bg-zinc-700 border border-black/[0.04] dark:border-cyan-500/20"
                      }`}
                    >
                      {label}
                    </button>
                  );
                })}
              </div>

              {/* Font Zoom */}
              <div className="flex items-center space-x-1 text-xs text-stone-500 dark:text-zinc-400 shrink-0">
                <span className="text-[11px] text-stone-400 dark:text-zinc-500 hidden sm:inline">字号:</span>
                <button
                  onClick={() => setReadingFontSize((prev) => Math.max(13, prev - 1))}
                  className="p-1 border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 rounded-md hover:bg-stone-50 dark:hover:bg-zinc-700 text-stone-600 dark:text-zinc-300 shadow-subtle"
                  title="缩小字号"
                >
                  <ZoomOut className="w-3.5 h-3.5" />
                </button>
                <span className="font-mono text-xs w-5 text-center text-stone-700 dark:text-zinc-300">{readingFontSize}</span>
                <button
                  onClick={() => setReadingFontSize((prev) => Math.min(22, prev + 1))}
                  className="p-1 border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-zinc-800 rounded-md hover:bg-stone-50 dark:hover:bg-zinc-700 text-stone-600 dark:text-zinc-300 shadow-subtle"
                  title="放大字号"
                >
                  <ZoomIn className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>

            {/* Reading Content Area */}
            <div ref={passageContainerRef} className="flex-1 p-6 sm:p-7 overflow-y-auto leading-relaxed select-text font-serif text-stone-800 dark:text-zinc-200">
              {(passages.filter((p) => p.id === activePassageId).length > 0
                ? passages.filter((p) => p.id === activePassageId)
                : passages.slice(0, 1)
              ).map((p) => {
                const isCloze = p.title.includes("Use of English") || p.title.includes("完型") || p.content.includes("[1]");
                const paras = p.content.split(/\n\s*\n/).filter((x: string) => x.trim().length > 0);

                return (
                  <div key={p.id} className="space-y-4">
                    <div className="flex items-center justify-between pb-2 border-b border-stone-100 dark:border-zinc-800">
                      <h4 className="font-bold text-sm tracking-wide text-stone-900 dark:text-zinc-100 font-sans">
                        {p.title}
                      </h4>
                      <span className="text-[11px] text-stone-400 dark:text-zinc-500 no-print font-sans">
                        双击单词即刻离线查词
                      </span>
                    </div>

                    <div 
                      style={{ fontSize: `${readingFontSize}px`, lineHeight: "1.9" }} 
                      className="text-justify select-text font-serif text-stone-800 dark:text-zinc-200"
                    >
                      {isCloze ? (
                        <div className="space-y-4">
                          {paras.map((paraText: string, pIdx: number) => {
                            const tokens = paraText.split(/(\[\s*\d+\s*\])/g);
                            return (
                              <p key={pIdx} className="leading-loose">
                                {tokens.map((token: string, tIdx: number) => {
                                  const match = token.match(/\[\s*(\d+)\s*\]/);
                                  if (match) {
                                    const blankNum = parseInt(match[1], 10);
                                    const qIdx = blankNum - 1;
                                    const targetQ = questions[qIdx];
                                    const qId = targetQ?.id;
                                    const userAns = qId ? answers[qId] : undefined;
                                    const isFocused = focusedIndex === qIdx;
                                    const isCorrect = isSubmitted && userAns && userAns === targetQ?.correct_answer;
                                    const isWrong = isSubmitted && userAns && userAns !== targetQ?.correct_answer;

                                    return (
                                      <button
                                        type="button"
                                        key={`b-${tIdx}`}
                                        id={`cloze-blank-${blankNum}`}
                                        onClick={() => handleBlankClick(blankNum)}
                                        title={`点击定位作答第 ${blankNum} 题`}
                                        className={`inline-flex items-center justify-center font-mono font-bold mx-1 px-2 py-0.5 rounded-lg text-xs transition-all duration-150 cursor-pointer select-none active:scale-95 ${
                                          isSubmitted
                                            ? isCorrect
                                              ? "bg-emerald-100 dark:bg-emerald-950/80 text-emerald-800 dark:text-emerald-300 border border-emerald-400 dark:border-emerald-600 ring-1 ring-emerald-400 font-bold"
                                              : isWrong
                                              ? "bg-rose-100 dark:bg-rose-950/80 text-rose-800 dark:text-rose-300 border border-rose-400 dark:border-rose-600 ring-1 ring-rose-400 font-bold"
                                              : "bg-stone-100 dark:bg-zinc-800 text-stone-500 border border-stone-300"
                                            : isFocused
                                            ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] ring-2 ring-emerald-500 dark:ring-cyber-300 shadow-md scale-105"
                                            : userAns
                                            ? "bg-emerald-50 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-700 hover:bg-emerald-100 dark:hover:bg-emerald-900/40"
                                            : "bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 border border-black/10 dark:border-cyan-500/20 hover:border-emerald-500 dark:hover:border-cyber-400"
                                        }`}
                                      >
                                        [{blankNum}{userAns ? `: ${userAns}` : ""}]
                                      </button>
                                    );
                                  }
                                  return <span key={`t-${tIdx}`}>{token}</span>;
                                })}
                              </p>
                            );
                          })}
                        </div>
                      ) : (
                        <div className="space-y-4">
                          <PassageHighlighter
                            passageId={p.id}
                            content={p.content}
                            className="text-justify"
                          />
                        </div>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Mobile Return to Questions Bar */}
            <div className="lg:hidden p-3 border-t border-stone-100 dark:border-zinc-800 bg-stone-50/90 dark:bg-zinc-900/90 flex justify-between items-center shrink-0 no-print">
              <span className="text-xs text-stone-500 dark:text-zinc-400">阅读完毕？随时返回作答</span>
              <button
                type="button"
                onClick={() => setMobileTab("questions")}
                className="px-4 py-1.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle flex items-center space-x-1.5 active:scale-95"
              >
                <span>返回答卷 ({answeredCount}/{questions.length})</span>
                <FileText className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        ) : null;

        const rightPane = (
          <div className={`${mobileTab === "questions" || isSubmitted ? "block" : "hidden"} lg:block w-full space-y-6 pb-28 lg:pb-0`}>
          {questions.map((q, idx) => {
            const userAns = answers[q.id];
            const isQAnswered = Boolean(userAns);
            const isQCorrect = userAns === q.correct_answer;
            const isFocused = idx === focusedIndex;
            const options = normalizeOptions(q.options);

            return (
              <div
                key={q.id}
                ref={(el) => { questionRefs.current[q.id] = el; }}
                onClick={() => setFocusedIndex(idx)}
                className={`bg-white dark:bg-[#11131a] rounded-2xl border p-5 sm:p-6 shadow-card transition-all duration-150 print-card cursor-pointer ${
                  isSubmitted
                    ? isQCorrect
                      ? "border-emerald-200 dark:border-emerald-500/40 bg-emerald-50/20 dark:bg-emerald-950/20"
                      : "border-rose-200 dark:border-rose-500/40 bg-rose-50/20 dark:bg-rose-950/20"
                    : isFocused
                    ? "border-emerald-700 dark:border-cyber-400 ring-1 ring-emerald-700 dark:ring-cyber-400 dark:shadow-glow-cyan"
                    : isQAnswered
                    ? "border-stone-200 dark:border-zinc-800 bg-stone-50/30 dark:bg-zinc-900/30"
                    : "border-black/[0.06] dark:border-cyan-500/15 hover:border-black/[0.14] dark:hover:border-cyan-500/35"
                }`}
              >
                <div className="flex items-center justify-between mb-3.5">
                  <div className="flex items-center space-x-2">
                    <span className={`w-6 h-6 rounded-lg text-xs font-bold font-mono flex items-center justify-center ${
                      isFocused ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f]" : "bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300"
                    }`}>
                      {idx + 1}
                    </span>
                    <span className="text-xs text-stone-400 dark:text-zinc-500 font-medium">
                      分值: {q.points} 分
                    </span>
                    {isFocused && (
                      <span className="text-[10px] font-bold text-emerald-800 dark:text-cyber-300 bg-emerald-50 dark:bg-zinc-800 px-1.5 py-0.5 rounded font-mono">
                        当前答题
                      </span>
                    )}
                  </div>

                  {q.passage_id && passages.length > 0 && !isSubmitted && (
                    <button
                      type="button"
                      onClick={(e) => {
                        e.stopPropagation();
                        setActivePassageId(q.passage_id);
                        setMobileTab("passage");
                      }}
                      className="lg:hidden text-[11px] font-semibold text-emerald-700 dark:text-cyber-400 bg-emerald-50/80 dark:bg-cyan-950/60 border border-emerald-200/50 dark:border-cyan-500/30 px-2 py-0.5 rounded-md flex items-center space-x-1 active:scale-95"
                    >
                      <BookOpen className="w-3 h-3" />
                      <span>查阅篇章</span>
                    </button>
                  )}

                  {isSubmitted && (
                    <div className="flex items-center space-x-1.5 text-xs font-bold no-print">
                      {isQCorrect ? (
                        <span className="text-emerald-600 dark:text-emerald-400 flex items-center space-x-1">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>正确 (+{q.points}分)</span>
                        </span>
                      ) : (
                        <span className="text-rose-600 dark:text-rose-400 flex items-center space-x-1">
                          <XCircle className="w-3.5 h-3.5" />
                          <span>选错 (正确: {q.correct_answer})</span>
                        </span>
                      )}
                    </div>
                  )}
                </div>

                <h4 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100 mb-4 leading-relaxed">
                  {q.stem}
                </h4>

                {/* Tactile Option Buttons */}
                <div className={options.length > 5 ? "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2" : "space-y-2.5"}>
                  {options.map((opt) => {
                    const isSelected = userAns === opt.key;
                    const isTheCorrectKey = opt.key === q.correct_answer;
                    const isGrid = options.length > 5;

                    let optionCls = "bg-stone-50/70 dark:bg-zinc-900/70 border-black/[0.06] dark:border-cyan-500/20 text-stone-800 dark:text-zinc-200 hover:bg-stone-100/70 dark:hover:bg-zinc-800/70";
                    let badgeCls = "bg-white dark:bg-zinc-800 border-black/[0.08] dark:border-cyan-500/25 text-stone-700 dark:text-zinc-300";

                    if (isSubmitted) {
                      if (isTheCorrectKey) {
                        optionCls = "bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-500/50 text-emerald-950 dark:text-emerald-200 font-bold ring-1 ring-emerald-300 dark:ring-emerald-500/50";
                        badgeCls = "bg-emerald-600 text-white border-emerald-600 font-bold";
                      } else if (isSelected && !isTheCorrectKey) {
                        optionCls = "bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-500/50 text-rose-950 dark:text-rose-200 font-bold";
                        badgeCls = "bg-rose-600 text-white border-rose-600 font-bold";
                      }
                    } else if (isSelected) {
                      optionCls = "bg-emerald-700 dark:bg-cyber-500 border-emerald-700 dark:border-cyber-400 text-white dark:text-[#090a0f] font-bold shadow-subtle dark:shadow-glow-cyan";
                      badgeCls = "bg-white text-emerald-800 dark:text-[#090a0f] border-white font-bold";
                    }

                    return (
                      <button
                        key={opt.key}
                        onClick={(e) => {
                          e.stopPropagation();
                          setFocusedIndex(idx);
                          handleSelectAnswer(q.id, opt.key);
                        }}
                        disabled={isSubmitted}
                        className={isGrid
                          ? `min-h-[44px] p-2 sm:p-2.5 rounded-xl border text-left flex items-center space-x-2 transition-all duration-150 active:scale-[0.98] ${optionCls}`
                          : `w-full min-h-[44px] p-3 sm:p-3.5 rounded-xl border text-left flex items-start space-x-3 transition-all duration-150 active:scale-[0.99] ${optionCls}`}
                        title={opt.text}
                      >
                        <span className={`w-6 h-6 rounded-lg text-xs font-bold font-mono flex items-center justify-center shrink-0 border ${badgeCls}`}>
                          {opt.key}
                        </span>
                        <span className={`text-xs ${isGrid ? "truncate font-medium" : "sm:text-sm pt-0.5 leading-relaxed"} flex-1`}>
                          {opt.text}
                        </span>
                        {!isSubmitted && !isGrid && (
                          <span className={`text-[10px] font-mono hidden sm:inline ml-auto pt-0.5 ${isSelected ? "text-emerald-100 dark:text-[#090a0f]/80" : "text-stone-400 dark:text-zinc-500"}`}>
                            [{opt.key}]
                          </span>
                        )}
                      </button>
                    );
                  })}
                </div>

                {/* Explanation Block */}
                {isSubmitted && q.explanation && (
                  <div className="mt-4 p-4 rounded-xl bg-stone-50/80 dark:bg-zinc-900/80 border border-black/[0.04] dark:border-cyan-500/20 text-xs text-stone-800 dark:text-zinc-200 space-y-1 no-print">
                    <div className="flex items-center space-x-1.5 font-bold text-stone-900 dark:text-zinc-100">
                      <HelpCircle className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
                      <span>考点精析 · 正确答案: {q.correct_answer}</span>
                    </div>
                    <p className="text-stone-600 dark:text-zinc-300 leading-relaxed whitespace-pre-line pt-1">
                      {q.explanation}
                    </p>
                  </div>
                )}
              </div>
            );
          })}

          {/* Quick Answer Sheet Matrix (答题卡分题型矩阵速览) */}
          <div className="bg-white dark:bg-[#11131a] p-5 sm:p-6 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card space-y-5 no-print transition-colors duration-300">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-stone-100 dark:border-zinc-800 text-xs">
              <div>
                <span className="font-bold text-sm text-stone-900 dark:text-zinc-100">答题卡总览 ({answeredCount} / {questions.length})</span>
                <span className="text-stone-400 dark:text-zinc-500 ml-2">点击题号快速定位到对应试题</span>
              </div>
              {!isSubmitted && answeredCount < questions.length && (
                <button
                  type="button"
                  onClick={scrollToFirstUnanswered}
                  className="px-3 py-1.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/30 font-semibold hover:bg-emerald-100 text-xs transition-colors self-start sm:self-auto"
                >
                  定位首道未答题
                </button>
              )}
            </div>

            {/* Section I */}
            {examSection1.length > 0 && (
              <div>
                <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                  <span>Section I 英语知识运用 (完形填空 1 - 20)</span>
                  <span className="font-mono text-[10px]">
                    {examSection1.filter(q => answers[q.id]).length}/{examSection1.length}
                  </span>
                </div>
                <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                  {examSection1.map((q, sIdx) => renderExamSheetButton(q, sIdx))}
                </div>
              </div>
            )}

            {/* Section II Part A */}
            {examSection2.length > 0 && (
              <div>
                <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                  <span>Section II 阅读理解 Part A (传统阅读 21 - 40)</span>
                  <span className="font-mono text-[10px]">
                    {examSection2.filter(q => answers[q.id]).length}/{examSection2.length}
                  </span>
                </div>
                <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                  {examSection2.map((q, sIdx) => renderExamSheetButton(q, 20 + sIdx))}
                </div>
              </div>
            )}

            {/* Section II Part B */}
            {examSection3.length > 0 && (
              <div>
                <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                  <span>Section II 阅读理解 Part B (新题型 41 - {questions.length})</span>
                  <span className="font-mono text-[10px]">
                    {examSection3.filter(q => answers[q.id]).length}/{examSection3.length}
                  </span>
                </div>
                <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                  {examSection3.map((q, sIdx) => renderExamSheetButton(q, 40 + sIdx))}
                </div>
              </div>
            )}

            <div className="pt-2 border-t border-stone-100 dark:border-zinc-800 flex items-center space-x-4 text-[11px] text-stone-500 dark:text-zinc-400">
              {isSubmitted ? (
                <>
                  <span className="flex items-center space-x-1">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-600 inline-block" />
                    <span>回答正确</span>
                  </span>
                  <span className="flex items-center space-x-1">
                    <span className="w-2.5 h-2.5 rounded-full bg-rose-500 inline-block" />
                    <span>回答错误</span>
                  </span>
                </>
              ) : (
                <>
                  <span className="flex items-center space-x-1">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block" />
                    <span>已作答</span>
                  </span>
                  <span className="flex items-center space-x-1">
                    <span className="w-2.5 h-2.5 rounded-full bg-stone-300 dark:bg-zinc-700 inline-block" />
                    <span>未作答</span>
                  </span>
                  <span className="flex items-center space-x-1">
                    <span className="w-2.5 h-2.5 rounded-full ring-2 ring-emerald-500 inline-block" />
                    <span>当前聚焦</span>
                  </span>
                </>
              )}
            </div>
          </div>
        </div>
      );

      return passages.length > 0 ? (
          <SplitPane
            storageKey="enway_split_ratio_exam"
            defaultRatio={55}
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

      {/* Mobile Bottom Exam Action Bar (Sticky Floating Dock) */}
      {!isSubmitted && (
        <div className="lg:hidden fixed bottom-0 left-0 right-0 z-30 bg-white/95 dark:bg-[#0e1017]/95 backdrop-blur-xl border-t border-black/[0.08] dark:border-cyan-500/20 px-4 py-2.5 pb-[max(0.75rem,env(safe-area-inset-bottom))] shadow-lg flex items-center justify-between gap-3 no-print">
          <button
            type="button"
            onClick={() => setShowMobileAnswerSheet(true)}
            className="px-3 py-2 rounded-xl bg-stone-100 dark:bg-zinc-800 text-stone-800 dark:text-zinc-200 border border-black/[0.05] dark:border-cyan-500/20 text-xs font-bold flex items-center space-x-1.5 active:scale-95 transition-transform"
          >
            <ListOrdered className="w-4 h-4 text-emerald-600 dark:text-cyber-400" />
            <span>答题卡 ({answeredCount}/{questions.length})</span>
          </button>

          <div className="flex items-center space-x-2">
            {passages.length > 0 && (
              <button
                type="button"
                onClick={() => setMobileTab(mobileTab === "questions" ? "passage" : "questions")}
                className="px-3 py-2 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-stone-50 dark:bg-zinc-900 text-stone-700 dark:text-zinc-300 text-xs font-semibold flex items-center space-x-1 active:scale-95"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>{mobileTab === "questions" ? "看原文" : "看试题"}</span>
              </button>
            )}

            <button
              type="button"
              onClick={() => handleSubmit(false)}
              className="px-4 py-2 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle dark:shadow-glow-cyan flex items-center space-x-1.5 active:scale-95 transition-transform"
            >
              <Send className="w-3.5 h-3.5" />
              <span>交卷</span>
            </button>
          </div>
        </div>
      )}

      {/* Floating Answer Sheet Capsule for Exam (Bottom-Right FAB) */}
      {!isSubmitted && (
        <div className="hidden lg:block fixed bottom-6 right-6 z-40 no-print">
          <button
            type="button"
            onClick={() => setShowMobileAnswerSheet(true)}
            className="flex items-center space-x-2 px-4 py-2.5 rounded-full bg-stone-900/90 dark:bg-zinc-800/95 hover:bg-black dark:hover:bg-zinc-700 text-white shadow-xl border border-white/10 dark:border-cyan-500/30 backdrop-blur-md transition-all duration-200 active:scale-95 group"
            title="展开全真答题卡，快速跳选任意题目"
          >
            <ListOrdered className="w-4 h-4 text-emerald-400 dark:text-cyber-400 group-hover:rotate-6 transition-transform" />
            <span className="text-xs font-bold font-sans">答题卡</span>
            <span className="px-1.5 py-0.5 rounded-full bg-white/20 text-[10px] font-mono font-bold">
              {answeredCount}/{questions.length}
            </span>
          </button>
        </div>
      )}

      {/* Answer Sheet Drawer (Mobile & Quick Overlay) */}
      {showMobileAnswerSheet && (
        <div 
          className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4 animate-in fade-in duration-150"
          onClick={(e) => {
            if (e.target === e.currentTarget) setShowMobileAnswerSheet(false);
          }}
        >
          <div 
            className="bg-white dark:bg-[#11131a] rounded-t-3xl sm:rounded-3xl border-t sm:border border-black/[0.08] dark:border-cyan-500/25 p-5 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-2xl max-h-[85vh] max-h-[85dvh] w-full max-w-xl flex flex-col animate-in slide-in-from-bottom duration-200"
          >
            <div className="flex items-center justify-between pb-3 border-b border-stone-100 dark:border-zinc-800">
              <div>
                <h4 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100 flex items-center space-x-2">
                  <ListOrdered className="w-4 h-4 text-emerald-600 dark:text-cyber-400" />
                  <span>答题卡总览 ({answeredCount} / {questions.length})</span>
                </h4>
                <span className="text-[11px] text-stone-400 dark:text-zinc-500">点击题号快速定位到对应试题</span>
              </div>
              <button
                type="button"
                onClick={() => setShowMobileAnswerSheet(false)}
                className="p-1.5 rounded-full bg-stone-100 dark:bg-zinc-800 text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-100"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="flex-1 overflow-y-auto overscroll-contain py-4 space-y-4 pr-1">
              {examSection1.length > 0 && (
                <div>
                  <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                    <span>Section I 英语知识运用 (完形填空 1 - 20)</span>
                    <span className="font-mono text-[10px]">
                      {examSection1.filter(q => answers[q.id]).length}/{examSection1.length}
                    </span>
                  </div>
                  <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                    {examSection1.map((q, sIdx) => renderExamSheetButton(q, sIdx, true))}
                  </div>
                </div>
              )}

              {examSection2.length > 0 && (
                <div>
                  <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                    <span>Section II 阅读理解 Part A (传统阅读 21 - 40)</span>
                    <span className="font-mono text-[10px]">
                      {examSection2.filter(q => answers[q.id]).length}/{examSection2.length}
                    </span>
                  </div>
                  <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                    {examSection2.map((q, sIdx) => renderExamSheetButton(q, 20 + sIdx, true))}
                  </div>
                </div>
              )}

              {examSection3.length > 0 && (
                <div>
                  <div className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 mb-2 uppercase tracking-wider flex items-center justify-between">
                    <span>Section II 阅读理解 Part B (新题型 41 - {questions.length})</span>
                    <span className="font-mono text-[10px]">
                      {examSection3.filter(q => answers[q.id]).length}/{examSection3.length}
                    </span>
                  </div>
                  <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
                    {examSection3.map((q, sIdx) => renderExamSheetButton(q, 40 + sIdx, true))}
                  </div>
                </div>
              )}
            </div>

            <div className="pt-3 border-t border-stone-100 dark:border-zinc-800 flex flex-col sm:flex-row justify-between items-center gap-3 text-xs text-stone-500 dark:text-zinc-400">
              <div className="flex items-center space-x-3">
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block" />
                  <span>已答</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full bg-stone-300 dark:bg-zinc-700 inline-block" />
                  <span>未答</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="w-2.5 h-2.5 rounded-full ring-2 ring-emerald-500 inline-block" />
                  <span>当前聚焦</span>
                </span>
              </div>
              <div className="flex items-center space-x-2 w-full sm:w-auto">
                {!isSubmitted && answeredCount < questions.length && (
                  <button
                    type="button"
                    onClick={scrollToFirstUnanswered}
                    className="flex-1 sm:flex-none px-3 py-1.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/30 font-semibold hover:bg-emerald-100 text-xs transition-colors"
                  >
                    定位首道未答题
                  </button>
                )}
                {!isSubmitted && (
                  <button
                    type="button"
                    onClick={() => {
                      setShowMobileAnswerSheet(false);
                      handleSubmit(false);
                    }}
                    className="flex-1 sm:flex-none px-4 py-1.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] font-bold text-xs"
                  >
                    立即交卷
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Exam Submission Review Bottom Sheet (Professional Proctor-Grade Review) */}
      {showSubmitReviewSheet && (
        <div 
          className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4 animate-in fade-in duration-150"
          onClick={(e) => {
            if (e.target === e.currentTarget) setShowSubmitReviewSheet(false);
          }}
        >
          <div className="bg-white dark:bg-[#11131a] rounded-t-3xl sm:rounded-3xl border-t sm:border border-black/[0.08] dark:border-cyan-500/25 p-5 sm:p-6 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-2xl max-h-[85vh] max-h-[85dvh] w-full max-w-lg flex flex-col animate-in slide-in-from-bottom duration-200">
            {/* Header */}
            <div className="flex items-center justify-between pb-3.5 border-b border-stone-100 dark:border-zinc-800">
              <div className="flex items-center space-x-2">
                <FileCheck className="w-5 h-5 text-emerald-600 dark:text-cyber-400" />
                <h3 className="font-bold text-base text-stone-900 dark:text-zinc-100">考卷作答核验与交卷</h3>
              </div>
              <button 
                onClick={() => setShowSubmitReviewSheet(false)} 
                className="p-1.5 rounded-full bg-stone-100 dark:bg-zinc-800 text-stone-400 hover:text-stone-700 dark:hover:text-zinc-200"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Content: Summary Stats & Unanswered list */}
            <div className="py-4 space-y-4 overflow-y-auto overscroll-contain">
              <div className="grid grid-cols-2 gap-3">
                <div className="p-3.5 rounded-2xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-500/30">
                  <span className="text-[11px] font-medium text-emerald-700 dark:text-emerald-400">已作答试题</span>
                  <div className="text-2xl font-bold font-mono text-emerald-900 dark:text-emerald-200 mt-0.5">
                    {answeredCount} <span className="text-xs font-normal">/ {questions.length} 题</span>
                  </div>
                </div>
                <div className={`p-3.5 rounded-2xl border ${
                  unansweredCount > 0 
                    ? "bg-amber-50 dark:bg-amber-950/40 border-amber-200 dark:border-amber-500/30 text-amber-900 dark:text-amber-200" 
                    : "bg-stone-50 dark:bg-zinc-900 border-black/[0.04] text-stone-600 dark:text-zinc-400"
                }`}>
                  <span className="text-[11px] font-medium">尚未作答</span>
                  <div className="text-2xl font-bold font-mono mt-0.5">
                    {unansweredCount} <span className="text-xs font-normal">题</span>
                  </div>
                </div>
              </div>

              {unansweredCount > 0 ? (
                <div className="p-3.5 rounded-2xl bg-amber-50/60 dark:bg-amber-950/20 border border-amber-200/60 dark:border-amber-500/20 space-y-2">
                  <div className="flex items-center justify-between text-xs font-semibold text-amber-800 dark:text-amber-300">
                    <span>待补答试题（点击快速直达补答）：</span>
                    <span className="font-mono text-[11px]">{unansweredCount} 题待答</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5 max-h-36 overflow-y-auto pt-1 pr-1">
                    {unansweredQuestions.map(({ id, num, idx }) => (
                      <button
                        key={id}
                        type="button"
                        onClick={() => {
                          setShowSubmitReviewSheet(false);
                          setFocusedIndex(idx);
                          setMobileTab("questions");
                          setTimeout(() => scrollToQuestion(id), 50);
                        }}
                        className="px-2.5 py-1.5 rounded-xl text-xs font-mono font-bold bg-white dark:bg-zinc-800 text-amber-900 dark:text-amber-200 border border-amber-300/80 dark:border-amber-500/40 hover:scale-105 active:scale-95 transition-all shadow-subtle"
                        title={`点击快速跳转至第 ${num} 题进行作答`}
                      >
                        第 {num} 题
                      </button>
                    ))}
                  </div>
                </div>
              ) : (
                <div className="p-4 rounded-2xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200/80 dark:border-emerald-500/30 flex items-center space-x-3">
                  <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                  <div className="text-xs text-emerald-900 dark:text-emerald-200">
                    <p className="font-bold">所有题目均已完成作答！</p>
                    <p className="text-[11px] text-emerald-700 dark:text-emerald-400 mt-0.5">确认交卷后系统将即时生成全真考卷成绩报告与逐题解析。</p>
                  </div>
                </div>
              )}
            </div>

            {/* Footer Buttons */}
            <div className="pt-3.5 border-t border-stone-100 dark:border-zinc-800 flex items-center space-x-3">
              <button
                type="button"
                onClick={() => setShowSubmitReviewSheet(false)}
                className="flex-1 py-2.5 rounded-xl border border-stone-200 dark:border-zinc-700 hover:bg-stone-50 dark:hover:bg-zinc-800 text-stone-700 dark:text-zinc-300 text-xs font-bold transition-colors active:scale-98"
              >
                返回继续作答
              </button>
              <button
                type="button"
                onClick={() => executeSubmit(false)}
                className="flex-1 py-2.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] text-xs font-bold shadow-subtle transition-all active:scale-98"
              >
                确认交卷核分
              </button>
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

export default function ExamPage() {
  return (
    <Suspense fallback={
      <div className="py-24 text-center">
        <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-slate-500 font-semibold text-sm">正在载入全真考场环境...</p>
      </div>
    }>
      <ExamContent />
    </Suspense>
  );
}
