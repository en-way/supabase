"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { supabase } from "@/lib/supabase";
import { getLocalState, LocalLearningState } from "@/lib/storage";
import { fetchExamLobbyData } from "@/lib/examLoader";
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
  Printer,
  RefreshCw,
  Sparkles,
  ShieldCheck
} from "lucide-react";

export default function HomePage() {
  const [exams, setExams] = useState<any[]>([]);
  const [categories, setCategories] = useState<any[]>([]);
  const [activeCat, setActiveCat] = useState<string>("all");
  const [loading, setLoading] = useState(true);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);

  const loadData = async (forceRefresh = false) => {
    setLoading(true);
    const now = Date.now();

    if (!forceRefresh) {
      try {
        const cachedCats = sessionStorage.getItem("enway_cache_cats");
        const cachedExams = sessionStorage.getItem("enway_cache_exams");
        const cacheTime = sessionStorage.getItem("enway_cache_time");

        if (cachedCats && cachedExams && cacheTime && now - Number(cacheTime) < 5 * 60 * 1000) {
          setCategories(JSON.parse(cachedCats));
          setExams(JSON.parse(cachedExams));
          setLocalState(getLocalState());
          setLoading(false);
          return;
        }
      } catch {}
    }

    try {
      if (!forceRefresh) {
        const { categories: cats, exams: examList } = await fetchExamLobbyData();
        if (cats && cats.length > 0) setCategories(cats);
        if (examList && examList.length > 0) setExams(examList);
      } else {
        // Force refresh queries Supabase directly
        const [catRes, examRes] = await Promise.all([
          supabase.from("categories").select("*").order("sort_order"),
          supabase
            .from("exams")
            .select(`
              *,
              questions(count),
              passages(count)
            `)
            .eq("is_published", true)
            .eq("approval_status", "approved")
            .order("year", { ascending: false }),
        ]);
        if (catRes.data) setCategories(catRes.data);
        if (examRes.data) setExams(examRes.data);
      }
    } catch (err) {
      console.error("Failed to load exams lobby:", err);
    } finally {
      // Read local learning state
      setLocalState(getLocalState());
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData(false);
  }, []);

  const handleForceRefresh = () => {
    try {
      sessionStorage.removeItem("enway_cache_cats");
      sessionStorage.removeItem("enway_cache_exams");
      sessionStorage.removeItem("enway_cache_time");
    } catch {}
    loadData(true);
  };

  const filteredExams = activeCat === "all" 
    ? exams 
    : exams.filter((e) => e.category_id === activeCat);

  return (
    <div className="space-y-8 animate-in fade-in duration-200">
      {/* Hero / Learning Overview Card */}
      <div className="bg-gradient-to-r from-slate-950 via-indigo-950 to-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-xl relative overflow-hidden border border-slate-800">
        <div className="absolute right-0 top-0 -mt-8 -mr-8 w-72 h-72 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none" />
        
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-200 text-xs font-semibold mb-3.5">
            <Flame className="w-3.5 h-3.5 text-amber-400" />
            <span>全国大学英语四六级 · 全国统考硕士研招英语权威真题</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-black tracking-tight leading-tight">
            权威考点透析 · 真题精研逐题练 · 考场状态实时防丢
          </h1>
          <p className="mt-2.5 text-xs sm:text-sm text-slate-300 leading-relaxed max-w-2xl">
            严谨还原官方考试试卷结构，长篇仔细阅读与完形填空左右对照；选项作答即刻反馈精析与考点定位，全真限时模考统一百分制自动核算，做题记录实时本地加密暂存。
          </p>

          {/* Quick Learning Stats */}
          {localState && (
            <div className="mt-6 pt-5 border-t border-slate-800/80 grid grid-cols-3 gap-4 max-w-md">
              <div className="bg-slate-900/60 p-3 rounded-2xl border border-slate-700/50">
                <span className="text-[11px] text-slate-400 block font-medium">待攻克错题</span>
                <span className="text-xl font-black text-amber-400 mt-0.5 block">
                  {localState.mistakes.filter(m => !m.isMastered).length}
                </span>
              </div>
              <div className="bg-slate-900/60 p-3 rounded-2xl border border-slate-700/50">
                <span className="text-[11px] text-slate-400 block font-medium">核心收录词汇</span>
                <span className="text-xl font-black text-emerald-400 mt-0.5 block">
                  {localState.vocabulary.length}
                </span>
              </div>
              <div className="bg-slate-900/60 p-3 rounded-2xl border border-slate-700/50">
                <span className="text-[11px] text-slate-400 block font-medium">已测模考卷</span>
                <span className="text-xl font-black text-sky-400 mt-0.5 block">
                  {Object.keys(localState.examResults).length}
                </span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Category Tabs & Quick Refresh Button */}
      <div className="flex items-center justify-between gap-3 border-b border-slate-200 pb-2">
        <div className="flex items-center space-x-2 overflow-x-auto pb-1">
          <button
            onClick={() => setActiveCat("all")}
            className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-bold whitespace-nowrap transition-all ${
              activeCat === "all"
                ? "bg-indigo-600 text-white shadow-sm"
                : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
            }`}
          >
            全部科目真题
          </button>
          {categories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCat(cat.id)}
              className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-bold whitespace-nowrap transition-all ${
                activeCat === cat.id
                  ? "bg-indigo-600 text-white shadow-sm"
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              {cat.name}
            </button>
          ))}
        </div>

        {/* Refresh Button (Sync immediately from Supabase) */}
        <button
          onClick={handleForceRefresh}
          disabled={loading}
          className="px-3.5 py-2 rounded-xl border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 hover:text-indigo-600 text-xs font-semibold flex items-center space-x-1.5 transition-all shrink-0 shadow-xs"
          title="清除本地短期缓存，秒级同步 Supabase 最新发布的真题与考卷"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? "animate-spin text-indigo-600" : "text-slate-500"}`} />
          <span className="hidden sm:inline">{loading ? "同步中..." : "刷新题库"}</span>
        </button>
      </div>

      {/* Exam Cards Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {[1, 2].map((i) => (
            <div key={i} className="h-52 bg-slate-100 animate-pulse rounded-3xl" />
          ))}
        </div>
      ) : filteredExams.length === 0 ? (
        <div className="text-center py-20 bg-white rounded-3xl border border-dashed border-slate-300">
          <BookOpen className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <p className="text-slate-600 font-bold text-sm">当前分类暂无发布的真题卷</p>
          <p className="text-xs text-slate-400 mt-1">管理员在后台导入并审核上架后即可在此研习</p>
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
                className="bg-white rounded-3xl border border-slate-200/90 hover:border-indigo-300 hover:shadow-xl transition-all p-6 sm:p-7 flex flex-col justify-between group"
              >
                <div>
                  <div className="flex items-start justify-between gap-3 mb-2.5">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-black bg-indigo-50 text-indigo-700 uppercase">
                      {exam.category_id} · {exam.year} 年
                    </span>
                    {pastResult ? (
                      <div className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-bold ${
                        pastResult.isPassed ? "bg-emerald-50 text-emerald-700" : "bg-rose-50 text-rose-700"
                      }`}>
                        <Award className="w-3.5 h-3.5" />
                        <span>最近成绩: {pastResult.score}分 ({pastResult.isPassed ? "合格" : "未达标"})</span>
                      </div>
                    ) : draft ? (
                      <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-50 text-amber-700 flex items-center space-x-1">
                        <Clock className="w-3.5 h-3.5" />
                        <span>答题草稿暂存中</span>
                      </span>
                    ) : null}
                  </div>

                  <h3 className="text-lg font-black text-slate-900 leading-snug group-hover:text-indigo-600 transition-colors">
                    {exam.title}
                  </h3>

                  <div className="mt-4 flex items-center space-x-4 text-xs text-slate-500 font-medium">
                    <span className="flex items-center space-x-1">
                      <Clock className="w-3.5 h-3.5 text-slate-400" />
                      <span>限时 {exam.duration_minutes} 分钟</span>
                    </span>
                    <span className="flex items-center space-x-1">
                      <HelpCircle className="w-3.5 h-3.5 text-slate-400" />
                      <span>满分 {exam.total_score}分 (合格 {exam.pass_score}分)</span>
                    </span>
                    <span>共 {qCount} 道客观题</span>
                  </div>
                </div>

                {/* Card Action Buttons */}
                <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between gap-3">
                  <div className="flex items-center space-x-2.5">
                    {/* Practice Mode (精读逐题练) */}
                    <Link
                      href={`/practice?id=${exam.id}`}
                      className="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-50 text-indigo-700 hover:bg-indigo-100 transition-colors flex items-center space-x-1.5"
                    >
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>精读逐题练</span>
                    </Link>

                    {/* Mock Exam Mode (标准限时模考) */}
                    <Link
                      href={`/exam?id=${exam.id}`}
                      className="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-200 transition-colors flex items-center space-x-1.5"
                    >
                      <Play className="w-3.5 h-3.5 fill-current" />
                      <span>{draft ? "继续限时模考" : "标准限时模考"}</span>
                    </Link>
                  </div>

                  {/* Print / Export Link */}
                  <Link
                    href={`/exam?id=${exam.id}&mode=print`}
                    title="导出或打印标准纸质练习卷"
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
