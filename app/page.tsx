"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { supabase } from "@/lib/supabase";
import { getLocalState, LocalLearningState } from "@/lib/storage";
import { 
  BookOpen, 
  Clock, 
  Award, 
  Play, 
  CheckCircle2, 
  HelpCircle, 
  Flame, 
  AlertCircle, 
  Bookmark, 
  Printer
} from "lucide-react";

export default function HomePage() {
  const [exams, setExams] = useState<any[]>([]);
  const [categories, setCategories] = useState<any[]>([]);
  const [activeCat, setActiveCat] = useState<string>("all");
  const [loading, setLoading] = useState(true);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);

  useEffect(() => {
    async function loadData() {
      setLoading(true);
      // Fetch categories
      const { data: cats } = await supabase
        .from("categories")
        .select("*")
        .order("sort_order");
      if (cats) setCategories(cats);

      // Fetch exams with question counts
      const { data: examList } = await supabase
        .from("exams")
        .select(`
          *,
          questions(count),
          passages(count)
        `)
        .eq("is_published", true)
        .order("year", { ascending: false });
      if (examList) setExams(examList);

      // Read local learning state
      setLocalState(getLocalState());
      setLoading(false);
    }
    loadData();
  }, []);

  const filteredExams = activeCat === "all" 
    ? exams 
    : exams.filter((e) => e.category_id === activeCat);

  return (
    <div className="space-y-8 animate-in fade-in duration-200">
      {/* Hero / Learning Overview Card */}
      <div className="bg-gradient-to-r from-indigo-900 via-indigo-800 to-indigo-950 rounded-3xl p-6 sm:p-8 text-white shadow-xl relative overflow-hidden">
        <div className="absolute right-0 top-0 -mt-8 -mr-8 w-64 h-64 bg-indigo-500/20 rounded-full blur-3xl pointer-events-none" />
        
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/30 border border-indigo-400/30 text-indigo-200 text-xs font-medium mb-3">
            <Flame className="w-3.5 h-3.5 text-amber-400" />
            <span>大学英语四六级 · 考研英语权威真题在线模考</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
            精准测评 · 随练随学 · 本地无感存盘
          </h1>
          <p className="mt-2 text-sm text-indigo-200 leading-relaxed">
            支持真题长篇阅读与完形填空，选择答案即刻反馈解析；双击词汇随时呼出离线生词卡片，全真模考 100 分制实时测评。
          </p>

          {/* Quick Learning Stats */}
          {localState && (
            <div className="mt-6 pt-5 border-t border-indigo-800/80 grid grid-cols-3 gap-4 max-w-md">
              <div className="bg-indigo-800/40 p-3 rounded-xl border border-indigo-700/40">
                <span className="text-[11px] text-indigo-300 block">待复习错题</span>
                <span className="text-xl font-bold text-amber-300">
                  {localState.mistakes.filter(m => !m.isMastered).length}
                </span>
              </div>
              <div className="bg-indigo-800/40 p-3 rounded-xl border border-indigo-700/40">
                <span className="text-[11px] text-indigo-300 block">已存生词</span>
                <span className="text-xl font-bold text-emerald-300">
                  {localState.vocabulary.length}
                </span>
              </div>
              <div className="bg-indigo-800/40 p-3 rounded-xl border border-indigo-700/40">
                <span className="text-[11px] text-indigo-300 block">已完赛模考</span>
                <span className="text-xl font-bold text-sky-300">
                  {Object.keys(localState.examResults).length}
                </span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Category Tabs */}
      <div className="flex items-center space-x-2 overflow-x-auto pb-1 border-b border-slate-200">
        <button
          onClick={() => setActiveCat("all")}
          className={`px-4 py-2 rounded-xl text-sm font-semibold whitespace-nowrap transition-all ${
            activeCat === "all"
              ? "bg-indigo-600 text-white shadow-sm"
              : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
          }`}
        >
          全部科目试卷
        </button>
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setActiveCat(cat.id)}
            className={`px-4 py-2 rounded-xl text-sm font-semibold whitespace-nowrap transition-all ${
              activeCat === cat.id
                ? "bg-indigo-600 text-white shadow-sm"
                : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
            }`}
          >
            {cat.name}
          </button>
        ))}
      </div>

      {/* Exam Cards Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {[1, 2].map((i) => (
            <div key={i} className="h-48 bg-slate-100 animate-pulse rounded-2xl" />
          ))}
        </div>
      ) : filteredExams.length === 0 ? (
        <div className="text-center py-16 bg-white rounded-2xl border border-dashed border-slate-300">
          <BookOpen className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <p className="text-slate-500 font-medium">当前分类暂无试卷发布</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {filteredExams.map((exam) => {
            const pastResult = localState?.examResults?.[exam.id];
            const draft = localState?.examDrafts?.[exam.id];
            const qCount = exam.questions?.[0]?.count || 0;

            return (
              <div
                key={exam.id}
                className="bg-white rounded-2xl border border-slate-200/90 hover:border-indigo-200 hover:shadow-lg transition-all p-6 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-start justify-between gap-3 mb-2">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-indigo-50 text-indigo-700">
                      {exam.category_id.toUpperCase()} · {exam.year} 年
                    </span>
                    {pastResult ? (
                      <div className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-bold ${
                        pastResult.isPassed ? "bg-emerald-50 text-emerald-700" : "bg-rose-50 text-rose-700"
                      }`}>
                        <Award className="w-3.5 h-3.5" />
                        <span>最近成绩: {pastResult.score}分 ({pastResult.isPassed ? "及格" : "未达标"})</span>
                      </div>
                    ) : draft ? (
                      <span className="px-2.5 py-1 rounded-lg text-xs font-medium bg-amber-50 text-amber-700">
                        作答草稿暂存中
                      </span>
                    ) : null}
                  </div>

                  <h3 className="text-lg font-bold text-slate-900 leading-snug hover:text-indigo-600 transition-colors">
                    {exam.title}
                  </h3>

                  <div className="mt-4 flex items-center space-x-4 text-xs text-slate-500">
                    <span className="flex items-center space-x-1">
                      <Clock className="w-3.5 h-3.5" />
                      <span>{exam.duration_minutes} 分钟</span>
                    </span>
                    <span className="flex items-center space-x-1">
                      <HelpCircle className="w-3.5 h-3.5" />
                      <span>满分 {exam.total_score} 分 (及格 {exam.pass_score} 分)</span>
                    </span>
                    <span>共 {qCount} 道客观题</span>
                  </div>
                </div>

                {/* Card Action Buttons */}
                <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between gap-3">
                  <div className="flex items-center space-x-2">
                    {/* Practice Mode (随做随练) */}
                    <Link
                      href={`/practice?id=${exam.id}`}
                      className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-indigo-50 text-indigo-700 hover:bg-indigo-100 transition-colors flex items-center space-x-1.5"
                    >
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>随做随练</span>
                    </Link>

                    {/* Mock Exam Mode (全真模考) */}
                    <Link
                      href={`/exam?id=${exam.id}`}
                      className="px-4 py-2 rounded-xl text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm shadow-indigo-200 transition-colors flex items-center space-x-1.5"
                    >
                      <Play className="w-3.5 h-3.5 fill-current" />
                      <span>{draft ? "继续全真模考" : "开始全真模考"}</span>
                    </Link>
                  </div>

                  {/* Print / Export Link */}
                  <Link
                    href={`/exam?id=${exam.id}&mode=print`}
                    title="导出/打印纸质试卷"
                    className="p-2 text-slate-400 hover:text-slate-700 hover:bg-slate-100 rounded-xl transition-colors"
                  >
                    <Printer className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
