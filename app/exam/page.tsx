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
  Keyboard
} from "lucide-react";

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
          setTimeout(() => handleSubmit(true), jitterMs);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
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
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      const { questions: qs, focusedIndex: fIdx } = keydownRef.current;
      if (!qs || qs.length === 0) return;

      const key = e.key.toUpperCase();
      const currentQ = qs[fIdx];
      const validKeys = currentQ
        ? normalizeOptions(currentQ.options).map((o) => o.key)
        : ["A", "B", "C", "D"];

      if (validKeys.includes(key)) {
        e.preventDefault();
        if (currentQ) {
          handleSelectAnswer(currentQ.id, key);
        }
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        setFocusedIndex((prev) => {
          const nextIdx = Math.min(qs.length - 1, prev + 1);
          scrollToQuestion(qs[nextIdx]?.id);
          return nextIdx;
        });
      } else if (e.key === "ArrowLeft") {
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

  const handleSubmit = (auto = false) => {
    if (isSubmittingRef.current) return;
    const { exam: curExam, questions: curQuestions, answers: curAnswers, remainingSeconds: curSec } = latestRef.current;
    if (!curExam) return;

    if (!auto) {
      const answeredCount = Object.keys(curAnswers).length;
      const totalCount = curQuestions.length;
      if (answeredCount < totalCount) {
        if (!window.confirm(`当前共有 ${totalCount} 道试题，您已完成 ${answeredCount} 道，尚有 ${totalCount - answeredCount} 道未作答。\n确定现在交卷核分吗？`)) {
          return;
        }
      } else {
        if (!window.confirm("所有题目均已作答完毕，确认立即交卷并生成成绩报告吗？")) {
          return;
        }
      }
    }

    isSubmittingRef.current = true;

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

    const examTotal = Number(curExam.total_score || totalRawPoints || 100);
    const passLine = Number(curExam.pass_score || (examTotal * 0.6));
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

  const handleRetake = () => {
    if (window.confirm("重新测验将清空本次作答，重新进入考场计时。确定重做吗？")) {
      setAnswers({});
      setIsSubmitted(false);
      setResult(null);
      setRemainingSeconds((exam?.duration_minutes || 60) * 60);
      setFocusedIndex(0);
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
              <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 font-mono tracking-wider">
                {exam.category_id} · {exam.year}
              </span>
              <span className="text-xs text-stone-400 dark:text-zinc-500 hidden sm:inline font-mono">
                已答 {answeredCount} / {questions.length} 题
              </span>
              <span className="hidden md:inline-flex items-center space-x-1 px-2 py-0.5 rounded text-[10px] font-medium bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-400 border border-emerald-200/60 dark:border-emerald-500/20">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                <span>实时草稿保全</span>
              </span>
            </div>
            <h2 className="text-sm sm:text-base font-bold text-stone-900 dark:text-zinc-100 truncate mt-0.5">
              {exam.title}
            </h2>
          </div>
        </div>

        {/* Timer & Submission Actions */}
        <div className="flex items-center space-x-2.5 shrink-0">
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
                  <span className="text-xs text-stone-400 dark:text-zinc-500 font-mono">满分 {result.totalScore || 100} 分 (及格线: {exam.pass_score || 30}分)</span>
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

      {/* PC 55:45 Dual-Pane Layout */}
      <div className="flex flex-col lg:flex-row gap-6 items-start">
        {/* Left Pane (55%): Reading Canvas */}
        {passages.length > 0 && (
          <div className="w-full lg:w-[55%] bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card overflow-hidden flex flex-col sticky top-36 h-[78vh] print-page transition-colors duration-300">
            {/* Passage Selector Bar & Font Zoom Controls */}
            <div className="px-5 py-2.5 border-b border-stone-100 dark:border-zinc-800 bg-stone-50/70 dark:bg-zinc-900/70 flex items-center justify-between shrink-0 no-print">
              <div className="flex items-center space-x-1.5 overflow-x-auto">
                <BookOpen className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400 shrink-0" />
                {passages.map((p, idx) => (
                  <button
                    key={p.id}
                    onClick={() => setActivePassageId(p.id)}
                    className={`px-3 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition-all duration-150 ${
                      activePassageId === p.id 
                        ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle dark:shadow-glow-cyan" 
                        : "bg-white dark:bg-zinc-800 text-stone-600 dark:text-zinc-300 hover:bg-stone-100 dark:hover:bg-zinc-700 border border-black/[0.04] dark:border-cyan-500/20"
                    }`}
                  >
                    篇章 {idx + 1}
                  </button>
                ))}
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
              ).map((p) => (
                  <div key={p.id} className="space-y-4">
                    <div className="flex items-center justify-between pb-2 border-b border-stone-100 dark:border-zinc-800">
                      <h4 className="font-bold text-sm uppercase tracking-wide text-stone-900 dark:text-zinc-100 font-sans">{p.title}</h4>
                      <span className="text-[11px] text-stone-400 dark:text-zinc-500 no-print font-sans">双击单词即刻离线查词</span>
                    </div>
                    <div 
                      style={{ fontSize: `${readingFontSize}px`, lineHeight: "1.85" }} 
                      className="whitespace-pre-line space-y-4 text-justify selection:bg-emerald-100/70 dark:selection:bg-cyan-500/30"
                    >
                      {p.content}
                    </div>
                  </div>
                ))}
            </div>
          </div>
        )}

        {/* Right Pane (45%): Question Answering Studio */}
        <div className={`w-full ${passages.length > 0 ? "lg:w-[45%]" : "lg:max-w-3xl lg:mx-auto"} space-y-6`}>
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
                className={`bg-white dark:bg-[#11131a] rounded-2xl border p-6 shadow-card transition-all duration-150 print-card cursor-pointer ${
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
                          ? `p-2 sm:p-2.5 rounded-xl border text-left flex items-center space-x-2 transition-all duration-150 active:scale-[0.98] ${optionCls}`
                          : `w-full p-3 sm:p-3.5 rounded-xl border text-left flex items-start space-x-3 transition-all duration-150 active:scale-[0.99] ${optionCls}`}
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

          {/* Quick Answer Sheet Matrix (答题卡矩阵速览) */}
          <div className="bg-white dark:bg-[#11131a] p-5 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card space-y-3 no-print transition-colors duration-300">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-stone-900 dark:text-zinc-100">答题卡总览 ({answeredCount} / {questions.length})</span>
              <span className="text-stone-400 dark:text-zinc-500">点击题号快速定位</span>
            </div>
            <div className="grid grid-cols-8 sm:grid-cols-10 gap-1.5">
              {questions.map((q, idx) => {
                const uAns = answers[q.id];
                const isAns = Boolean(uAns);
                const isFocus = idx === focusedIndex;

                let btnStyle = "bg-stone-100 dark:bg-zinc-800 text-stone-600 dark:text-zinc-400 hover:bg-stone-200/80 dark:hover:bg-zinc-700";
                if (isSubmitted) {
                  btnStyle = uAns === q.correct_answer 
                    ? "bg-emerald-600 text-white" 
                    : "bg-rose-500 text-white";
                } else if (isFocus) {
                  btnStyle = "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] font-bold shadow-subtle dark:shadow-glow-cyan";
                } else if (isAns) {
                  btnStyle = "bg-emerald-50 dark:bg-cyan-950/80 text-emerald-800 dark:text-cyber-300 font-semibold border border-emerald-200/50 dark:border-cyan-500/30";
                }

                return (
                  <button
                    key={q.id}
                    onClick={() => {
                      setFocusedIndex(idx);
                      scrollToQuestion(q.id);
                    }}
                    className={`py-1.5 rounded-lg text-xs font-mono transition-all duration-150 ${btnStyle}`}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      </div>
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
