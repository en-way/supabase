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
  HelpCircle 
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
      setPassages(passageData || []);
      if (passageData && passageData.length > 0) {
        setActivePassageId(passageData[0].id);
      }

      const { data: questionData } = await supabase
        .from("questions")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order");
      setQuestions(questionData || []);

      const draft = getExamDraft(examId);
      if (draft) {
        setAnswers(draft.answers || {});
        setRemainingSeconds(draft.remainingSeconds || (examData?.duration_minutes || 60) * 60);
      } else if (examData) {
        setRemainingSeconds((examData.duration_minutes || 60) * 60);
      }

      setLoading(false);
    }
    loadExam();
  }, [examId]);

  useEffect(() => {
    if (loading || isSubmitted || remainingSeconds <= 0 || !examId) return;

    const timer = setInterval(() => {
      setRemainingSeconds((prev) => {
        const next = prev - 1;
        if (next <= 0) {
          clearInterval(timer);
          handleSubmit(true);
          return 0;
        }
        if (next % 10 === 0) {
          saveExamDraft(examId, answers, next);
        }
        return next;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [loading, isSubmitted, remainingSeconds, answers, examId]);

  const handleSelect = (questionId: string, optionKey: string) => {
    if (isSubmitted || !examId) return;
    const nextAnswers = { ...answers, [questionId]: optionKey };
    setAnswers(nextAnswers);
    saveExamDraft(examId, nextAnswers, remainingSeconds);
  };

  const handleSubmit = (force = false) => {
    if (isSubmitted || !examId) return;

    const answeredCount = Object.keys(answers).length;
    if (!force && answeredCount < questions.length) {
      const confirmSubmit = window.confirm(
        `你还有 ${questions.length - answeredCount} 道题未作答，确定现在提前交卷吗？`
      );
      if (!confirmSubmit) return;
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
          stem: q.stem,
          options: q.options,
          correctAnswer: q.correct_answer,
          explanation: q.explanation,
          wrongAnswer: uAns || "未作答",
        });
      }

      detailAnswers[q.id] = {
        userAnswer: uAns,
        isCorrect: isCorr,
      };
    });

    const finalScaledScore = totalRawPoints > 0 
      ? Math.round((earnedRawPoints / totalRawPoints) * 100 * 10) / 10 
      : 0;
    const isPassed = finalScaledScore >= (exam?.pass_score || 60);
    const timeSpent = (exam?.duration_minutes * 60) - remainingSeconds;

    const examResultData: ExamResult = {
      examId: exam.id,
      examTitle: exam.title,
      score: finalScaledScore,
      totalScore: 100,
      isPassed,
      durationSeconds: Math.max(1, timeSpent),
      submittedAt: new Date().toISOString(),
      answers: detailAnswers,
    };

    saveExamResult(examResultData);
    setResult(examResultData);
    setIsSubmitted(true);

    if (isPassed) {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
      });
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleRetake = () => {
    if (!examId) return;
    clearExamDraft(examId);
    setAnswers({});
    setRemainingSeconds((exam?.duration_minutes || 60) * 60);
    setIsSubmitted(false);
    setResult(null);
  };

  const formatTime = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
  };

  const scrollToQuestion = (qId: string) => {
    const el = questionRefs.current[qId];
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

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
        <p className="text-slate-500 font-medium text-sm">正在加载全真模考试卷...</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="sticky top-16 z-30 bg-white/95 backdrop-blur border border-slate-200/90 rounded-2xl p-4 shadow-sm flex items-center justify-between no-print">
        <div className="flex items-center space-x-3">
          <Link
            href="/"
            className="p-2 text-slate-500 hover:text-slate-900 hover:bg-slate-100 rounded-xl transition-colors"
          >
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-600 text-white">
                全真模考
              </span>
              <h2 className="text-base font-bold text-slate-900 line-clamp-1">
                {exam?.title}
              </h2>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              100 分满分制 · 及格线 {exam?.pass_score} 分 · 实时本地防丢保护
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-4">
          {!isSubmitted ? (
            <>
              <div className={`flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl font-mono text-sm font-bold border ${
                remainingSeconds < 300 
                  ? "bg-rose-50 border-rose-200 text-rose-600 animate-pulse" 
                  : "bg-slate-50 border-slate-200 text-slate-800"
              }`}>
                <Clock className="w-4 h-4" />
                <span>{formatTime(remainingSeconds)}</span>
              </div>

              <button
                onClick={() => handleSubmit(false)}
                className="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold shadow-md shadow-indigo-200 flex items-center space-x-1.5 transition-all"
              >
                <Send className="w-3.5 h-3.5" />
                <span>立即交卷</span>
              </button>
            </>
          ) : (
            <div className="flex items-center space-x-2">
              <button
                onClick={handleRetake}
                className="px-3.5 py-2 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-100 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>重新测验</span>
              </button>
              <button
                onClick={() => window.print()}
                className="px-3.5 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 text-xs font-semibold flex items-center space-x-1.5 transition-colors shadow-sm"
              >
                <Printer className="w-3.5 h-3.5" />
                <span>打印 / 导出 PDF</span>
              </button>
            </div>
          )}
        </div>
      </div>

      {isSubmitted && result && (
        <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl p-6 sm:p-8 shadow-xl animate-in fade-in zoom-in-95 duration-200 no-print">
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
                    {result.isPassed ? "🎉 恭喜通过及格线" : "⚠️ 未达及格线 (需复习)"}
                  </span>
                  <span className="text-xs text-slate-400">满分 100 分制</span>
                </div>
                <h3 className="text-xl font-bold mt-1">{result.examTitle} 模考成绩报告</h3>
                <p className="text-xs text-slate-300 mt-1">
                  用时: {Math.floor(result.durationSeconds / 60)} 分 {result.durationSeconds % 60} 秒 · 错题已自动收入“智能错题本”
                </p>
              </div>
            </div>

            <div className="flex items-center space-x-4 bg-white/10 p-3 rounded-2xl border border-white/10">
              <div className="text-center px-3">
                <span className="text-[11px] text-slate-300 block">正确题数</span>
                <span className="text-lg font-bold text-emerald-400">
                  {Object.values(result.answers).filter(a => a.isCorrect).length} / {questions.length}
                </span>
              </div>
              <div className="h-8 w-px bg-white/20" />
              <div className="text-center px-3">
                <span className="text-[11px] text-slate-300 block">正确率</span>
                <span className="text-lg font-bold text-sky-400">
                  {Math.round((Object.values(result.answers).filter(a => a.isCorrect).length / questions.length) * 100)}%
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Printable Heading */}
      <div className="hidden print-only text-center mb-6">
        <h1 className="text-2xl font-black mb-1">{exam?.title}</h1>
        <p className="text-xs text-slate-500">
          考试时长: {exam?.duration_minutes} 分钟 · 满分: {exam?.total_score} 分 · 及格: {exam?.pass_score} 分
        </p>
      </div>

      <div className="grid lg:grid-cols-12 gap-6 items-start">
        {passages.length > 0 && (
          <div className="lg:col-span-6 bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm overflow-y-auto max-h-[80vh] sticky top-36 print-page">
            {passages.length > 1 && (
              <div className="flex items-center space-x-2 pb-3 mb-4 border-b border-slate-100 overflow-x-auto no-print">
                {passages.map((p, idx) => (
                  <button
                    key={p.id}
                    onClick={() => setActivePassageId(p.id)}
                    className={`px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all ${
                      activePassageId === p.id 
                        ? "bg-indigo-600 text-white" 
                        : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                    }`}
                  >
                    篇章 {idx + 1}
                  </button>
                ))}
              </div>
            )}

            {passages
              .filter((p) => p.id === activePassageId || passages.length === 1)
              .map((p) => (
                <div key={p.id} className="space-y-4">
                  <div className="flex items-center justify-between pb-2 border-b border-slate-100">
                    <h4 className="font-bold text-sm uppercase text-indigo-700">{p.title}</h4>
                    <span className="text-[11px] text-slate-400 no-print">双击任意单词可查词</span>
                  </div>
                  <div className="text-slate-800 font-serif leading-relaxed whitespace-pre-line text-base selection:bg-indigo-100">
                    {p.content}
                  </div>
                </div>
              ))}
          </div>
        )}

        <div className={passages.length > 0 ? "lg:col-span-4 space-y-6" : "lg:col-span-9 space-y-6"}>
          {questions.map((q, idx) => {
            const userAns = answers[q.id];
            const isQAnswered = Boolean(userAns);
            const isQCorrect = userAns === q.correct_answer;

            return (
              <div
                key={q.id}
                ref={(el) => { questionRefs.current[q.id] = el; }}
                className={`bg-white rounded-2xl border p-6 shadow-sm transition-all print-card ${
                  isSubmitted
                    ? isQCorrect
                      ? "border-emerald-200 bg-emerald-50/20"
                      : "border-rose-200 bg-rose-50/20"
                    : isQAnswered
                    ? "border-indigo-200 shadow-indigo-50"
                    : "border-slate-200"
                }`}
              >
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center space-x-2">
                    <span className="w-6 h-6 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <span className="text-xs text-slate-500 font-medium">
                      {q.points} 分
                    </span>
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
                          <span>错误 (正确答案: {q.correct_answer})</span>
                        </span>
                      )}
                    </div>
                  )}
                </div>

                <h4 className="text-sm sm:text-base font-bold text-slate-900 mb-4 leading-relaxed">
                  {q.stem}
                </h4>

                <div className="space-y-2.5">
                  {q.options.map((opt: any) => {
                    const isSelected = userAns === opt.key;
                    const isTheCorrectKey = opt.key === q.correct_answer;

                    let optionCls = "bg-slate-50 border-slate-200/80 text-slate-700 hover:bg-slate-100";
                    let badgeCls = "bg-white border-slate-200 text-slate-700";

                    if (isSubmitted) {
                      if (isTheCorrectKey) {
                        optionCls = "bg-emerald-50 border-emerald-400 text-emerald-950 font-semibold ring-1 ring-emerald-400";
                        badgeCls = "bg-emerald-600 text-white border-emerald-600";
                      } else if (isSelected && !isTheCorrectKey) {
                        optionCls = "bg-rose-50 border-rose-300 text-rose-950 font-semibold";
                        badgeCls = "bg-rose-600 text-white border-rose-600";
                      } else {
                        optionCls = "bg-slate-50/50 border-slate-200/40 text-slate-400 opacity-60";
                      }
                    } else if (isSelected) {
                      optionCls = "bg-indigo-50 border-indigo-500 text-indigo-900 font-semibold shadow-sm ring-1 ring-indigo-500";
                      badgeCls = "bg-indigo-600 text-white border-indigo-600";
                    }

                    return (
                      <button
                        key={opt.key}
                        type="button"
                        onClick={() => handleSelect(q.id, opt.key)}
                        disabled={isSubmitted}
                        className={`w-full p-3 rounded-xl border text-left flex items-start space-x-3 transition-all ${optionCls}`}
                      >
                        <span className={`w-6 h-6 rounded-lg border font-bold text-xs flex items-center justify-center shrink-0 ${badgeCls}`}>
                          {opt.key}
                        </span>
                        <span className="text-xs sm:text-sm pt-0.5 leading-relaxed">{opt.text}</span>
                      </button>
                    );
                  })}
                </div>

                {isSubmitted && (
                  <div className="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-600 space-y-2">
                    <div className="font-bold text-indigo-700 flex items-center space-x-1">
                      <HelpCircle className="w-3.5 h-3.5" />
                      <span>解析点拨</span>
                    </div>
                    <p className="leading-relaxed bg-slate-50 p-2.5 rounded-lg border border-slate-100">
                      {q.explanation}
                    </p>
                  </div>
                )}
              </div>
            );
          })}
        </div>

        <div className={passages.length > 0 ? "lg:col-span-2 sticky top-36 no-print" : "lg:col-span-3 sticky top-36 no-print"}>
          <div className="bg-white rounded-2xl border border-slate-200/90 p-4 shadow-sm space-y-4">
            <div className="flex items-center justify-between pb-2 border-b border-slate-100">
              <span className="text-xs font-bold text-slate-900 flex items-center space-x-1">
                <FileCheck className="w-4 h-4 text-indigo-600" />
                <span>答题卡</span>
              </span>
              <span className="text-[11px] text-slate-400">
                已做 {Object.keys(answers).length} / {questions.length}
              </span>
            </div>

            <div className="grid grid-cols-4 gap-2">
              {questions.map((q, idx) => {
                const isAnswered = Boolean(answers[q.id]);
                const isCorrect = isSubmitted && answers[q.id] === q.correct_answer;

                let btnBg = "bg-slate-100 text-slate-600 hover:bg-slate-200";
                if (isSubmitted) {
                  btnBg = isCorrect 
                    ? "bg-emerald-500 text-white font-bold" 
                    : "bg-rose-500 text-white font-bold";
                } else if (isAnswered) {
                  btnBg = "bg-indigo-600 text-white font-bold shadow-sm shadow-indigo-200";
                }

                return (
                  <button
                    key={q.id}
                    onClick={() => scrollToQuestion(q.id)}
                    className={`h-8 rounded-lg text-xs font-medium flex items-center justify-center transition-all ${btnBg}`}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>

            {!isSubmitted && (
              <button
                onClick={() => handleSubmit(false)}
                className="w-full py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold rounded-xl shadow-md shadow-indigo-200 transition-all flex items-center justify-center space-x-1.5"
              >
                <Send className="w-3.5 h-3.5" />
                <span>交卷出分</span>
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default function ExamPage() {
  return (
    <Suspense fallback={<div className="py-20 text-center text-slate-500">正在初始化考场...</div>}>
      <ExamContent />
    </Suspense>
  );
}
