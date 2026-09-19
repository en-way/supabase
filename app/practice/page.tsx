"use client";

import { useState, useEffect, Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { 
  recordMistake, 
  toggleFavorite, 
  updateFavoriteNote, 
  getLocalState 
} from "@/lib/storage";
import { 
  ArrowLeft, 
  CheckCircle2, 
  XCircle, 
  Bookmark, 
  ChevronRight, 
  ChevronLeft, 
  Type, 
  Sparkles,
  Edit3
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

      const { data: questionData } = await supabase
        .from("questions")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order");
      setQuestions(questionData || []);

      const state = getLocalState();
      setFavoriteIds(new Set(state.favorites.map((f) => f.questionId)));
      const notesMap: Record<string, string> = {};
      state.favorites.forEach((f) => {
        if (f.note) notesMap[f.questionId] = f.note;
      });
      setEditingNotes(notesMap);

      setLoading(false);
    }
    loadExam();
  }, [examId]);

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

  if (!questions.length) {
    return (
      <div className="text-center py-20 bg-white rounded-2xl border border-slate-200">
        <p className="text-slate-600 mb-4">该试卷暂无题目</p>
        <Link href="/" className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-sm">
          返回试卷大厅
        </Link>
      </div>
    );
  }

  const currentQ = questions[currentIndex];
  const relatedPassage = passages.find((p) => p.id === currentQ.passage_id);
  const selectedAnswer = userAnswers[currentQ.id];
  const isAnswered = Boolean(selectedAnswer);
  const isCorrect = selectedAnswer === currentQ.correct_answer;
  const isFavorited = favoriteIds.has(currentQ.id);

  const handleSelectOption = (key: string) => {
    if (isAnswered) return;

    setUserAnswers((prev) => ({ ...prev, [currentQ.id]: key }));
    setShowExplanation((prev) => ({ ...prev, [currentQ.id]: true }));

    if (key !== currentQ.correct_answer) {
      recordMistake({
        questionId: currentQ.id,
        examId: exam.id,
        categoryId: exam.category_id,
        stem: currentQ.stem,
        options: currentQ.options,
        correctAnswer: currentQ.correct_answer,
        explanation: currentQ.explanation,
        wrongAnswer: key,
      });
    }
  };

  const handleToggleFav = () => {
    toggleFavorite({
      questionId: currentQ.id,
      examId: exam.id,
      stem: currentQ.stem,
      options: currentQ.options,
      correctAnswer: currentQ.correct_answer,
      explanation: currentQ.explanation,
      note: editingNotes[currentQ.id] || "",
    });

    setFavoriteIds((prev) => {
      const next = new Set(prev);
      if (next.has(currentQ.id)) {
        next.delete(currentQ.id);
      } else {
        next.add(currentQ.id);
      }
      return next;
    });
  };

  const handleSaveNote = (noteText: string) => {
    setEditingNotes((prev) => ({ ...prev, [currentQ.id]: noteText }));
    updateFavoriteNote(currentQ.id, noteText);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between bg-white p-4 rounded-2xl border border-slate-200/80">
        <div className="flex items-center space-x-3">
          <Link
            href="/"
            className="p-2 text-slate-500 hover:text-slate-900 hover:bg-slate-100 rounded-xl transition-colors"
          >
            <ArrowLeft className="w-5 h-5" />
          </Link>
          <div>
            <div className="flex items-center space-x-2">
              <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-50 text-indigo-700">
                随做随练模式
              </span>
              <h2 className="text-base font-bold text-slate-900 line-clamp-1">
                {exam?.title}
              </h2>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              点击选项即刻判定 · 双击生词呼出离线字典 · 做错自动归集错题本
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-3">
          <button
            onClick={() => setLargeFont(!largeFont)}
            title="字号缩放"
            className={`p-2 rounded-xl border text-xs font-semibold flex items-center space-x-1 transition-colors ${
              largeFont ? "bg-indigo-50 border-indigo-200 text-indigo-700" : "bg-white border-slate-200 text-slate-600"
            }`}
          >
            <Type className="w-4 h-4" />
            <span>{largeFont ? "标准字号" : "放大字号"}</span>
          </button>
          <div className="text-sm font-bold text-slate-700 bg-slate-100 px-3 py-1.5 rounded-xl">
            {currentIndex + 1} / {questions.length} 题
          </div>
        </div>
      </div>

      <div className={`grid gap-6 ${relatedPassage ? "lg:grid-cols-2" : "max-w-3xl mx-auto"}`}>
        {relatedPassage && (
          <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm overflow-y-auto max-h-[78vh] leading-relaxed">
            <div className="flex items-center justify-between pb-3 mb-4 border-b border-slate-100">
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-600">
                {relatedPassage.title}
              </span>
              <span className="text-[11px] text-slate-400">💡 选中文中任意单词可即刻查词</span>
            </div>
            <div className={`text-slate-800 font-serif selection:bg-indigo-100 whitespace-pre-line ${
              largeFont ? "text-lg leading-loose" : "text-base leading-relaxed"
            }`}>
              {relatedPassage.content}
            </div>
          </div>
        )}

        <div className="space-y-6">
          <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm">
            <div className="flex items-start justify-between gap-4 mb-4">
              <div className="flex items-center space-x-2">
                <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-indigo-600 text-white">
                  题号 {currentIndex + 1}
                </span>
                <span className="text-xs text-slate-500 font-medium">
                  {currentQ.q_type === "reading_item" ? "阅读理解小题" : currentQ.q_type === "cloze_item" ? "完形填空小题" : "客观选择题"} ({currentQ.points} 分)
                </span>
              </div>

              <button
                onClick={handleToggleFav}
                className={`p-2 rounded-xl border text-xs font-medium flex items-center space-x-1.5 transition-all ${
                  isFavorited 
                    ? "bg-amber-50 border-amber-200 text-amber-600" 
                    : "bg-white border-slate-200 text-slate-400 hover:text-slate-700"
                }`}
              >
                <Bookmark className={`w-4 h-4 ${isFavorited ? "fill-amber-400" : ""}`} />
                <span>{isFavorited ? "已收藏" : "收藏"}</span>
              </button>
            </div>

            <h3 className="text-base sm:text-lg font-bold text-slate-900 mb-6 leading-relaxed">
              {currentQ.stem}
            </h3>

            <div className="space-y-3">
              {currentQ.options.map((opt: any) => {
                const isSelected = selectedAnswer === opt.key;
                const isTheCorrectOne = opt.key === currentQ.correct_answer;

                let btnStyle = "bg-slate-50 border-slate-200/80 hover:bg-slate-100/80 text-slate-800";
                let badgeStyle = "bg-white border-slate-200 text-slate-700";

                if (isAnswered) {
                  if (isTheCorrectOne) {
                    btnStyle = "bg-emerald-50 border-emerald-400 text-emerald-950 font-medium shadow-sm ring-1 ring-emerald-400";
                    badgeStyle = "bg-emerald-600 text-white border-emerald-600";
                  } else if (isSelected && !isTheCorrectOne) {
                    btnStyle = "bg-rose-50 border-rose-300 text-rose-950 font-medium";
                    badgeStyle = "bg-rose-600 text-white border-rose-600";
                  } else {
                    btnStyle = "bg-slate-50/50 border-slate-200/50 text-slate-400 opacity-60";
                  }
                }

                return (
                  <button
                    key={opt.key}
                    onClick={() => handleSelectOption(opt.key)}
                    disabled={isAnswered}
                    className={`w-full p-4 rounded-xl border text-left flex items-start space-x-3.5 transition-all ${btnStyle}`}
                  >
                    <span className={`w-7 h-7 rounded-lg border font-bold text-xs flex items-center justify-center shrink-0 ${badgeStyle}`}>
                      {opt.key}
                    </span>
                    <span className="text-sm pt-0.5 leading-relaxed">{opt.text}</span>
                    {isAnswered && isTheCorrectOne && (
                      <CheckCircle2 className="w-5 h-5 text-emerald-600 ml-auto shrink-0" />
                    )}
                    {isAnswered && isSelected && !isTheCorrectOne && (
                      <XCircle className="w-5 h-5 text-rose-500 ml-auto shrink-0" />
                    )}
                  </button>
                );
              })}
            </div>

            {isAnswered && (
              <div className="mt-6 pt-5 border-t border-slate-100 animate-in fade-in duration-200 space-y-4">
                <div className={`p-4 rounded-xl border flex items-center justify-between ${
                  isCorrect ? "bg-emerald-50/70 border-emerald-200" : "bg-rose-50/70 border-rose-200"
                }`}>
                  <div className="flex items-center space-x-2">
                    {isCorrect ? (
                      <>
                        <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                        <span className="font-bold text-sm text-emerald-900">回答正确！加 {currentQ.points} 分</span>
                      </>
                    ) : (
                      <>
                        <XCircle className="w-5 h-5 text-rose-600" />
                        <span className="font-bold text-sm text-rose-900">
                          回答错误 (正确答案: {currentQ.correct_answer}) · 已自动收录错题本
                        </span>
                      </>
                    )}
                  </div>
                </div>

                <div className="p-4 rounded-xl bg-slate-50 border border-slate-200/80">
                  <div className="flex items-center space-x-2 text-indigo-700 font-bold text-xs mb-2">
                    <Sparkles className="w-4 h-4" />
                    <span>考点精析与长难句释义</span>
                  </div>
                  <p className="text-sm text-slate-700 leading-relaxed whitespace-pre-line">
                    {currentQ.explanation}
                  </p>
                </div>

                <div className="p-3 bg-amber-50/40 rounded-xl border border-amber-200/60">
                  <div className="flex items-center space-x-1.5 text-xs font-semibold text-amber-800 mb-1.5">
                    <Edit3 className="w-3.5 h-3.5" />
                    <span>个人解题心得 / 易错陷阱笔记:</span>
                  </div>
                  <input
                    type="text"
                    defaultValue={editingNotes[currentQ.id] || ""}
                    onBlur={(e) => handleSaveNote(e.target.value)}
                    placeholder="在此输入个人做题笔记，失焦自动保存..."
                    className="w-full text-xs bg-white border border-amber-200 rounded-lg px-3 py-2 text-slate-700 focus:outline-none focus:ring-1 focus:ring-amber-500"
                  />
                </div>
              </div>
            )}
          </div>

          <div className="flex items-center justify-between">
            <button
              onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
              disabled={currentIndex === 0}
              className="px-4 py-2.5 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-100 disabled:opacity-40 text-xs font-semibold flex items-center space-x-1 transition-colors"
            >
              <ChevronLeft className="w-4 h-4" />
              <span>上一题</span>
            </button>

            <button
              onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
              disabled={currentIndex === questions.length - 1}
              className="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white text-xs font-semibold shadow-sm flex items-center space-x-1 transition-colors"
            >
              <span>下一题</span>
              <ChevronRight className="w-4 h-4" />
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
