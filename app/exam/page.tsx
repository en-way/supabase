"use client";

import { useState, useEffect, useRef, Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { 
  saveExamDraft, 
  getExamDraft, 
  clearExamDraft, 
  saveExamResult, 
  recordMistake, 
  normalizeOptions,
  ExamResult 
} from "@/lib/storage";
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

  useEffect(() => {
    async function loadExam() {
      if (!examId) return;
      setLoading(true);
      const { data: examData } = await supabase
        .from("exams")
        .select("*")
        .eq("id", examId)
        .single();
      setExam(examData);

      const { data: passageData } = await supabase
        .from("passages")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order");
      if (passageData && passageData.length > 0) {
        setPassages(passageData);
        setActivePassageId(passageData[0].id);
      }

      const { data: questionData } = await supabase
        .from("questions")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order");
      if (questionData) {
        setQuestions(questionData);
      }

      // Check draft for real-time exam protection
      const draft = getExamDraft(examId);
      if (draft) {
        setAnswers(draft.answers || {});
        setRemainingSeconds(draft.remainingSeconds || (examData?.duration_minutes || 60) * 60);
      } else if (examData?.duration_minutes) {
        setRemainingSeconds(examData.duration_minutes * 60);
      }

      setLoading(false);
    }
    loadExam();
  }, [examId]);

  // Timer countdown
  useEffect(() => {
    if (loading || isSubmitted || remainingSeconds <= 0) return;

    const timer = setInterval(() => {
      setRemainingSeconds((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmit(true);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [loading, isSubmitted, remainingSeconds]);

  // Auto-save draft every 5 seconds
  useEffect(() => {
    if (!examId || isSubmitted || loading) return;
    const saveTimer = setTimeout(() => {
      saveExamDraft(examId, answers, remainingSeconds);
    }, 5000);
    return () => clearTimeout(saveTimer);
  }, [examId, answers, remainingSeconds, isSubmitted, loading]);

  // PC Keyboard Shortcuts: A/B/C/D to select, Arrow keys to navigate
  useEffect(() => {
    if (isSubmitted || questions.length === 0) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      const key = e.key.toUpperCase();
      if (["A", "B", "C", "D"].includes(key)) {
        e.preventDefault();
        const currentQ = questions[focusedIndex];
        if (currentQ) {
          handleSelectAnswer(currentQ.id, key);
        }
      } else if (e.key === "ArrowDown" || e.key === "ArrowRight") {
        e.preventDefault();
        setFocusedIndex((prev) => {
          const nextIdx = Math.min(questions.length - 1, prev + 1);
          scrollToQuestion(questions[nextIdx]?.id);
          return nextIdx;
        });
      } else if (e.key === "ArrowUp" || e.key === "ArrowLeft") {
        e.preventDefault();
        setFocusedIndex((prev) => {
          const prevIdx = Math.max(0, prev - 1);
          scrollToQuestion(questions[prevIdx]?.id);
          return prevIdx;
        });
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [questions, focusedIndex, isSubmitted, answers]);

  const scrollToQuestion = (qId?: string) => {
    if (!qId) return;
    const el = questionRefs.current[qId];
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  const handleSelectAnswer = (qId: string, optionKey: string) => {
    if (isSubmitted) return;
    setAnswers((prev) => ({
      ...prev,
      [qId]: optionKey,
    }));
  };

  const handleSubmit = (auto = false) => {
    if (!exam) return;

    if (!auto) {
      const answeredCount = Object.keys(answers).length;
      const totalCount = questions.length;
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

    let earnedRawPoints = 0;
    let totalRawPoints = 0;
    const detailAnswers: Record<string, { userAnswer: string; isCorrect: boolean }> = {};

    questions.forEach((q) => {
      const uAns = answers[q.id] || "";
      const isCorr = uAns === q.correct_answer;
      totalRawPoints += Number(q.points || 2);
      if (isCorr) {
        earnedRawPoints += Number(q.points || 2);
      } else {
        recordMistake({
          questionId: q.id,
          examId: exam.id,
          categoryId: exam.category_id,
          wrongAnswer: uAns || "未作答",
        });
      }

      detailAnswers[q.id] = {
        userAnswer: uAns,
        isCorrect: isCorr,
      };
    });

    const examTotal = Number(exam.total_score || totalRawPoints || 100);
    const passLine = Number(exam.pass_score || (examTotal * 0.6));
    const finalScore = Math.round(earnedRawPoints * 10) / 10;
    const passed = finalScore >= passLine;

    const examRes: ExamResult = {
      examId: exam.id,
      examTitle: exam.title,
      score: finalScore,
      totalScore: examTotal,
      isPassed: passed,
      durationSeconds: exam.duration_minutes * 60 - remainingSeconds,
      submittedAt: new Date().toISOString(),
      answers: detailAnswers,
    };

    saveExamResult(examRes);
    clearExamDraft(exam.id);
    setResult(examRes);
    setIsSubmitted(true);

    if (passed) {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 },
      });
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
    <div className="space-y-6 pb-20">
      {/* Top Sticky Header */}
      <div className="sticky top-16 z-30 bg-white/95 backdrop-blur-md border border-slate-200/90 p-4 sm:px-6 rounded-2xl shadow-sm flex items-center justify-between gap-4 no-print">
        <div className="flex items-center space-x-3 truncate">
          <Link
            href="/"
            className="p-2 hover:bg-slate-100 rounded-xl text-slate-500 hover:text-slate-900 transition-colors shrink-0"
            title="返回真题大厅"
          >
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div className="truncate">
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[10px] font-black uppercase bg-indigo-50 text-indigo-700">
                {exam.category_id} · {exam.year}
              </span>
              <span className="text-xs text-slate-400 hidden sm:inline font-mono">
                已答 {answeredCount} / {questions.length} 题
              </span>
            </div>
            <h2 className="text-sm sm:text-base font-black text-slate-900 truncate mt-0.5">
              {exam.title}
            </h2>
          </div>
        </div>

        {/* Timer & Submission Actions */}
        <div className="flex items-center space-x-3 shrink-0">
          {!isSubmitted ? (
            <>
              <div className={`flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl font-mono text-xs sm:text-sm font-black border ${
                remainingSeconds < 300 
                  ? "bg-rose-50 border-rose-200 text-rose-600 animate-pulse" 
                  : "bg-slate-50 border-slate-200 text-slate-800"
              }`}>
                <Clock className="w-4 h-4" />
                <span>{formatTime(remainingSeconds)}</span>
              </div>

              <button
                onClick={() => handleSubmit(false)}
                className="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-black shadow-md shadow-indigo-200 flex items-center space-x-1.5 transition-all"
              >
                <Send className="w-3.5 h-3.5" />
                <span>交卷核分</span>
              </button>
            </>
          ) : (
            <div className="flex items-center space-x-2">
              <button
                onClick={handleRetake}
                className="px-3.5 py-2 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-100 text-xs font-bold flex items-center space-x-1.5 transition-colors"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>重新测验</span>
              </button>
              <button
                onClick={() => window.print()}
                className="px-3.5 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 text-xs font-bold flex items-center space-x-1.5 transition-colors shadow-sm"
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
        <div className="bg-gradient-to-r from-slate-950 via-indigo-950 to-slate-900 text-white rounded-3xl p-6 sm:p-8 shadow-xl animate-in fade-in zoom-in-95 duration-200 no-print border border-slate-800">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="flex items-center space-x-5">
              <div className={`w-20 h-20 rounded-2xl flex items-center justify-center text-3xl font-black shadow-lg ${
                result.isPassed 
                  ? "bg-emerald-500/20 border-2 border-emerald-400 text-emerald-400" 
                  : "bg-rose-500/20 border-2 border-rose-400 text-rose-400"
              }`}>
                {result.score}
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider ${
                    result.isPassed ? "bg-emerald-400/20 text-emerald-300" : "bg-rose-400/20 text-rose-300"
                  }`}>
                    {result.isPassed ? "🎉 恭喜达到合格线" : "⚠️ 未达合格基准分 (需重点攻关)"}
                  </span>
                  <span className="text-xs text-slate-400 font-mono">满分 {result.totalScore || 100} 分 (及格线: {exam.pass_score || 30}分)</span>
                </div>
                <h3 className="text-xl font-black mt-1 font-serif">{result.examTitle} 测评报告</h3>
                <p className="text-xs text-slate-300 mt-1">
                  答题耗时: {Math.floor(result.durationSeconds / 60)} 分 {result.durationSeconds % 60} 秒 · 做错小题已自动归入“智能错题集”
                </p>
              </div>
            </div>

            <div className="flex items-center space-x-4 bg-white/10 p-3.5 rounded-2xl border border-white/10">
              <div className="text-center px-3">
                <span className="text-[11px] text-slate-300 block">答对题数</span>
                <span className="text-xl font-black text-emerald-400">
                  {Object.values(result.answers).filter(a => a.isCorrect).length} / {questions.length}
                </span>
              </div>
              <div className="h-8 w-px bg-white/20" />
              <div className="text-center px-3">
                <span className="text-[11px] text-slate-300 block">得分率</span>
                <span className="text-xl font-black text-sky-400">
                  {Math.round((Object.values(result.answers).filter(a => a.isCorrect).length / questions.length) * 100)}%
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Keyboard Shortcuts Guide Banner (PC Only) */}
      {!isSubmitted && (
        <div className="hidden lg:flex items-center justify-between px-4 py-2 bg-indigo-50/70 border border-indigo-100 rounded-xl text-xs text-indigo-900 no-print">
          <div className="flex items-center space-x-2">
            <Keyboard className="w-4 h-4 text-indigo-600" />
            <span className="font-bold">PC 端键盘极速答题已就绪：</span>
            <span className="text-indigo-700">直接敲击键盘按键 <kbd className="px-1.5 py-0.5 bg-white border border-indigo-200 rounded font-mono font-bold text-[10px]">A</kbd> <kbd className="px-1.5 py-0.5 bg-white border border-indigo-200 rounded font-mono font-bold text-[10px]">B</kbd> <kbd className="px-1.5 py-0.5 bg-white border border-indigo-200 rounded font-mono font-bold text-[10px]">C</kbd> <kbd className="px-1.5 py-0.5 bg-white border border-indigo-200 rounded font-mono font-bold text-[10px]">D</kbd> 瞬选答案，方向键 <kbd className="px-1.5 py-0.5 bg-white border border-indigo-200 rounded font-mono font-bold text-[10px]">↑</kbd> <kbd className="px-1.5 py-0.5 bg-white border border-indigo-200 rounded font-mono font-bold text-[10px]">↓</kbd> 平滑切题</span>
          </div>
          <span className="text-[11px] text-slate-400 font-mono">当前聚焦: 第 {focusedIndex + 1} 题</span>
        </div>
      )}

      {/* PC 55:45 Dual-Pane Golden Ratio Layout */}
      <div className="flex flex-col lg:flex-row gap-6 items-start">
        {/* Left Pane (55%): Warm Paper Reading Canvas */}
        {passages.length > 0 && (
          <div className="w-full lg:w-[55%] bg-[#fcfbf9] rounded-3xl border border-[#e8e4dc] shadow-sm overflow-hidden flex flex-col sticky top-36 h-[78vh] print-page">
            {/* Passage Selector Bar & Font Zoom Controls */}
            <div className="px-5 py-3 border-b border-[#e8e4dc] bg-white flex items-center justify-between shrink-0 no-print">
              <div className="flex items-center space-x-2 overflow-x-auto">
                <BookOpen className="w-4 h-4 text-indigo-600 shrink-0" />
                {passages.map((p, idx) => (
                  <button
                    key={p.id}
                    onClick={() => setActivePassageId(p.id)}
                    className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap transition-all ${
                      activePassageId === p.id 
                        ? "bg-slate-900 text-white shadow-xs" 
                        : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                    }`}
                  >
                    篇章 {idx + 1}
                  </button>
                ))}
              </div>

              {/* Font Zoom */}
              <div className="flex items-center space-x-1 text-xs text-slate-500 shrink-0">
                <span className="text-[11px] text-slate-400 hidden sm:inline">字号:</span>
                <button
                  onClick={() => setReadingFontSize((prev) => Math.max(13, prev - 1))}
                  className="p-1 border border-slate-200 rounded-md hover:bg-slate-50 text-slate-600"
                  title="缩小字号"
                >
                  <ZoomOut className="w-3.5 h-3.5" />
                </button>
                <span className="font-mono text-xs w-5 text-center">{readingFontSize}</span>
                <button
                  onClick={() => setReadingFontSize((prev) => Math.min(22, prev + 1))}
                  className="p-1 border border-slate-200 rounded-md hover:bg-slate-50 text-slate-600"
                  title="放大字号"
                >
                  <ZoomIn className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>

            {/* Reading Content Area */}
            <div className="flex-1 p-6 sm:p-7 overflow-y-auto leading-relaxed select-text font-serif text-[#1e293b]">
              {passages
                .filter((p) => p.id === activePassageId || passages.length === 1)
                .map((p) => (
                  <div key={p.id} className="space-y-4">
                    <div className="flex items-center justify-between pb-2 border-b border-[#eae6df]">
                      <h4 className="font-bold text-sm uppercase tracking-wide text-indigo-900">{p.title}</h4>
                      <span className="text-[11px] text-slate-400 no-print">双击单词即刻呼出词典查词</span>
                    </div>
                    <div 
                      style={{ fontSize: `${readingFontSize}px`, lineHeight: "1.85" }} 
                      className="whitespace-pre-line space-y-4 text-justify"
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
                className={`bg-white rounded-3xl border p-6 shadow-xs transition-all print-card cursor-pointer ${
                  isSubmitted
                    ? isQCorrect
                      ? "border-emerald-200 bg-emerald-50/20"
                      : "border-rose-200 bg-rose-50/20"
                    : isFocused
                    ? "border-indigo-500 ring-2 ring-indigo-500/20 shadow-md"
                    : isQAnswered
                    ? "border-indigo-200 bg-indigo-50/10"
                    : "border-slate-200 hover:border-slate-300"
                }`}
              >
                <div className="flex items-center justify-between mb-3.5">
                  <div className="flex items-center space-x-2">
                    <span className={`w-6 h-6 rounded-lg text-xs font-black flex items-center justify-center ${
                      isFocused ? "bg-indigo-600 text-white" : "bg-slate-900 text-white"
                    }`}>
                      {idx + 1}
                    </span>
                    <span className="text-xs text-slate-500 font-semibold">
                      分值: {q.points} 分
                    </span>
                    {isFocused && (
                      <span className="text-[10px] font-bold text-indigo-600 bg-indigo-50 px-1.5 py-0.5 rounded">
                        当前答题
                      </span>
                    )}
                  </div>

                  {isSubmitted && (
                    <div className="flex items-center space-x-1.5 text-xs font-bold no-print">
                      {isQCorrect ? (
                        <span className="text-emerald-600 flex items-center space-x-1">
                          <CheckCircle2 className="w-4 h-4" />
                          <span>正确 (+{q.points}分)</span>
                        </span>
                      ) : (
                        <span className="text-rose-600 flex items-center space-x-1">
                          <XCircle className="w-4 h-4" />
                          <span>选错 (正确: {q.correct_answer})</span>
                        </span>
                      )}
                    </div>
                  )}
                </div>

                <h4 className="text-sm sm:text-base font-black text-slate-900 mb-4 leading-relaxed">
                  {q.stem}
                </h4>

                {/* Tactile Option Buttons */}
                <div className="space-y-2.5">
                  {options.map((opt) => {
                    const isSelected = userAns === opt.key;
                    const isTheCorrectKey = opt.key === q.correct_answer;

                    let optionCls = "bg-slate-50 border-slate-200/90 text-slate-800 hover:bg-slate-100/80";
                    let badgeCls = "bg-white border-slate-200 text-slate-700";

                    if (isSubmitted) {
                      if (isTheCorrectKey) {
                        optionCls = "bg-emerald-50 border-emerald-400 text-emerald-950 font-bold ring-1 ring-emerald-400";
                        badgeCls = "bg-emerald-600 text-white border-emerald-600 font-black";
                      } else if (isSelected && !isTheCorrectKey) {
                        optionCls = "bg-rose-50 border-rose-300 text-rose-950 font-bold";
                        badgeCls = "bg-rose-600 text-white border-rose-600 font-black";
                      }
                    } else if (isSelected) {
                      optionCls = "bg-indigo-50 border-indigo-400 text-indigo-950 font-bold ring-2 ring-indigo-500/30 shadow-xs";
                      badgeCls = "bg-indigo-600 text-white border-indigo-600 font-black";
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
                        className={`w-full p-3 sm:p-3.5 rounded-2xl border text-left flex items-start space-x-3 transition-all ${optionCls}`}
                      >
                        <span className={`w-6 h-6 rounded-lg text-xs font-bold flex items-center justify-center shrink-0 border ${badgeCls}`}>
                          {opt.key}
                        </span>
                        <span className="text-xs sm:text-sm pt-0.5 flex-1 leading-relaxed">{opt.text}</span>
                        {!isSubmitted && (
                          <span className="text-[10px] text-slate-400 font-mono hidden sm:inline ml-auto pt-0.5">
                            [{opt.key}]
                          </span>
                        )}
                      </button>
                    );
                  })}
                </div>

                {/* Explanation Block */}
                {isSubmitted && q.explanation && (
                  <div className="mt-4 p-4 rounded-2xl bg-indigo-50/60 border border-indigo-100 text-xs text-indigo-950 space-y-1 no-print">
                    <div className="flex items-center space-x-1.5 font-black text-indigo-900">
                      <HelpCircle className="w-3.5 h-3.5 text-indigo-600" />
                      <span>考点精析 · 正确答案: {q.correct_answer}</span>
                    </div>
                    <p className="text-slate-700 leading-relaxed whitespace-pre-line pt-1">
                      {q.explanation}
                    </p>
                  </div>
                )}
              </div>
            );
          })}

          {/* Quick Answer Sheet Matrix (答题卡矩阵速览) */}
          <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-3 no-print">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-slate-800">答题卡总览 ({answeredCount} / {questions.length})</span>
              <span className="text-slate-400">点击题号快速定位</span>
            </div>
            <div className="grid grid-cols-8 sm:grid-cols-10 gap-1.5">
              {questions.map((q, idx) => {
                const uAns = answers[q.id];
                const isAns = Boolean(uAns);
                const isFocus = idx === focusedIndex;

                let btnStyle = "bg-slate-100 text-slate-600 hover:bg-slate-200";
                if (isSubmitted) {
                  btnStyle = uAns === q.correct_answer 
                    ? "bg-emerald-600 text-white" 
                    : "bg-rose-500 text-white";
                } else if (isFocus) {
                  btnStyle = "bg-indigo-600 text-white ring-2 ring-indigo-300 font-black";
                } else if (isAns) {
                  btnStyle = "bg-indigo-100 text-indigo-800 font-bold";
                }

                return (
                  <button
                    key={q.id}
                    onClick={() => {
                      setFocusedIndex(idx);
                      scrollToQuestion(q.id);
                    }}
                    className={`py-1.5 rounded-lg text-xs font-mono transition-all ${btnStyle}`}
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
