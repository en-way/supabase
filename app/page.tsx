"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { supabase } from "@/lib/supabase";
import { getLocalState, LocalLearningState } from "@/lib/storage";
import { fetchExamLobbyData, clearStaticExamCache } from "@/lib/examLoader";
import { 
  BookOpen, 
  Clock, 
  Award, 
  Play, 
  Flame, 
  HelpCircle, 
  Printer,
  RefreshCw,
  Sparkles
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

  const handleForceRefresh = async () => {
    try {
      sessionStorage.removeItem("enway_cache_cats");
      sessionStorage.removeItem("enway_cache_exams");
      sessionStorage.removeItem("enway_cache_time");
      await clearStaticExamCache();
    } catch {}
    loadData(true);
  };

  const filteredExams = activeCat === "all" 
    ? exams 
    : exams.filter((e) => e.category_id === activeCat);

  return (
    <div className="space-y-8 animate-in fade-in duration-200">
      {/* Hero / Learning Overview Section */}
      <div className="bg-white dark:bg-[#11131a] rounded-2xl p-7 sm:p-9 shadow-card border border-black/[0.06] dark:border-cyan-500/20 relative overflow-hidden transition-colors duration-300">
        <div className="absolute right-0 top-0 -mt-16 -mr-16 w-80 h-80 bg-emerald-50/60 dark:bg-cyan-900/20 rounded-full blur-3xl pointer-events-none transition-colors duration-300" />
        <div className="absolute left-1/3 bottom-0 -mb-16 w-60 h-60 bg-amber-50/50 dark:bg-violet-900/20 rounded-full blur-3xl pointer-events-none transition-colors duration-300" />
        
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-stone-100/90 dark:bg-zinc-900/90 border border-black/[0.04] dark:border-cyan-500/25 text-stone-700 dark:text-cyber-300 text-xs font-medium mb-3.5">
            <Flame className="w-3.5 h-3.5 text-amber-500" />
            <span>全国大学英语四六级 · 统考硕士研招英语权威真题</span>
          </div>

          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-stone-900 dark:text-zinc-100 leading-tight">
            权威真题研习 · 全真限时模考
          </h1>
          <p className="mt-2 text-xs sm:text-sm text-stone-500 dark:text-zinc-400 leading-relaxed max-w-2xl">
            严谨还原官方试卷结构，长篇仔细阅读与客观题左右分栏对照；实时单词即查与形态还原，客观题即刻反馈精析与考点定位，做题状态本地加密暂存。
          </p>

          {/* Quick Learning Stats (Minimalist Pill Cards) */}
          {localState && (
            <div className="mt-6 pt-5 border-t border-stone-100 dark:border-zinc-800 grid grid-cols-3 gap-3.5 max-w-md">
              <div className="bg-stone-50/90 dark:bg-zinc-900/90 p-3 rounded-xl border border-black/[0.03] dark:border-cyan-500/20 shadow-subtle">
                <span className="text-[11px] text-stone-400 dark:text-zinc-500 block font-medium">待攻克错题</span>
                <span className="text-xl font-bold text-stone-900 dark:text-cyber-300 mt-0.5 block">
                  {localState.mistakes.filter(m => !m.isMastered).length}
                </span>
              </div>
              <div className="bg-stone-50/90 dark:bg-zinc-900/90 p-3 rounded-xl border border-black/[0.03] dark:border-cyan-500/20 shadow-subtle">
                <span className="text-[11px] text-stone-400 dark:text-zinc-500 block font-medium">核心收录词汇</span>
                <span className="text-xl font-bold text-stone-900 dark:text-cyber-300 mt-0.5 block">
                  {localState.vocabulary.length}
                </span>
              </div>
              <div className="bg-stone-50/90 dark:bg-zinc-900/90 p-3 rounded-xl border border-black/[0.03] dark:border-cyan-500/20 shadow-subtle">
                <span className="text-[11px] text-stone-400 dark:text-zinc-500 block font-medium">已测模考卷</span>
                <span className="text-xl font-bold text-stone-900 dark:text-cyber-300 mt-0.5 block">
                  {Object.keys(localState.examResults).length}
                </span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Category Tabs & Quick Refresh Button */}
      <div className="flex items-center justify-between gap-3 border-b border-black/[0.06] dark:border-cyan-500/15 pb-2.5">
        <div className="flex items-center space-x-1.5 overflow-x-auto pb-0.5">
          <button
            onClick={() => setActiveCat("all")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all duration-150 ${
              activeCat === "all"
                ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle dark:shadow-glow-cyan"
                : "text-stone-600 dark:text-zinc-400 hover:text-stone-950 dark:hover:text-zinc-100 hover:bg-stone-100 dark:hover:bg-zinc-800"
            }`}
          >
            全部科目真题
          </button>
          {categories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCat(cat.id)}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all duration-150 ${
                activeCat === cat.id
                  ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle dark:shadow-glow-cyan"
                  : "text-stone-600 dark:text-zinc-400 hover:text-stone-950 dark:hover:text-zinc-100 hover:bg-stone-100 dark:hover:bg-zinc-800"
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
          className="px-3 py-1.5 rounded-lg border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-[#11131a] hover:bg-stone-50 dark:hover:bg-zinc-800 text-stone-600 dark:text-zinc-300 hover:text-stone-950 dark:hover:text-cyber-300 text-xs font-medium flex items-center space-x-1.5 transition-all shrink-0 shadow-subtle active:scale-[0.98]"
          title="清除本地短期缓存，秒级同步 Supabase 最新发布的真题与考卷"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? "animate-spin text-emerald-700 dark:text-cyber-400" : "text-stone-400 dark:text-zinc-500"}`} />
          <span className="hidden sm:inline">{loading ? "同步中..." : "刷新题库"}</span>
        </button>
      </div>

      {/* Exam Cards Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {[1, 2].map((i) => (
            <div key={i} className="h-48 bg-stone-100/70 dark:bg-zinc-900/70 animate-pulse rounded-2xl border border-black/[0.03] dark:border-cyan-500/10" />
          ))}
        </div>
      ) : filteredExams.length === 0 ? (
        <div className="text-center py-20 bg-white dark:bg-[#11131a] rounded-2xl border border-dashed border-stone-200 dark:border-zinc-800">
          <BookOpen className="w-10 h-10 text-stone-300 dark:text-zinc-700 mx-auto mb-2.5" />
          <p className="text-stone-700 dark:text-zinc-300 font-semibold text-sm">当前分类暂无发布的真题卷</p>
          <p className="text-xs text-stone-400 dark:text-zinc-500 mt-1">管理员在后台导入并审核上架后即可在此研习</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {filteredExams.map((exam) => {
            const pastResult = localState?.examResults?.[exam.id];
            const draft = localState?.examDrafts?.[exam.id];
            const qCount = exam.questions?.[0]?.count || 0;

            return (
              <div
                key={exam.id}
                className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 hover:border-emerald-600/30 dark:hover:border-cyan-400/50 shadow-card hover:shadow-card-hover dark:hover:shadow-glow-cyan hover:-translate-y-[1.5px] transition-all duration-200 ease-spring p-6 flex flex-col justify-between group"
              >
                <div>
                  <div className="flex items-start justify-between gap-3 mb-2.5">
                    <span className="px-2 py-0.5 rounded-md text-[11px] font-bold font-mono bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 uppercase tracking-wide">
                      {exam.category_id} · {exam.year} 年
                    </span>
                    {pastResult ? (
                      <div className={`flex items-center space-x-1 px-2.5 py-0.5 rounded-md text-xs font-semibold ${
                        pastResult.isPassed 
                          ? "bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300" 
                          : "bg-rose-50 dark:bg-rose-950/50 text-rose-700 dark:text-rose-300"
                      }`}>
                        <Award className="w-3.5 h-3.5" />
                        <span>最近: {pastResult.score}分 ({pastResult.isPassed ? "合格" : "未达标"})</span>
                      </div>
                    ) : draft ? (
                      <span className="px-2.5 py-0.5 rounded-md text-xs font-medium bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 flex items-center space-x-1">
                        <Clock className="w-3 h-3" />
                        <span>答题暂存中</span>
                      </span>
                    ) : null}
                  </div>

                  <h3 className="text-base sm:text-lg font-bold text-stone-900 dark:text-zinc-100 leading-snug group-hover:text-emerald-700 dark:group-hover:text-cyber-400 transition-colors">
                    {exam.title}
                  </h3>

                  <div className="mt-3.5 flex items-center space-x-4 text-xs text-stone-400 dark:text-zinc-500 font-medium">
                    <span className="flex items-center space-x-1">
                      <Clock className="w-3.5 h-3.5 text-stone-300 dark:text-zinc-600" />
                      <span>限时 {exam.duration_minutes} 分钟</span>
                    </span>
                    <span className="flex items-center space-x-1">
                      <HelpCircle className="w-3.5 h-3.5 text-stone-300 dark:text-zinc-600" />
                      <span>满分 {exam.total_score}分</span>
                    </span>
                    <span>共 {qCount} 道客观题</span>
                  </div>
                </div>

                {/* Card Action Buttons */}
                <div className="mt-6 pt-4 border-t border-stone-100 dark:border-zinc-800 flex items-center justify-between gap-3">
                  <div className="flex items-center space-x-2">
                    {/* Practice Mode (精读逐题练) */}
                    <Link
                      href={`/practice?id=${exam.id}`}
                      className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-stone-100/90 dark:bg-zinc-800 hover:bg-stone-200/80 dark:hover:bg-zinc-700 text-stone-800 dark:text-zinc-200 transition-all duration-150 active:scale-[0.98] flex items-center space-x-1.5"
                    >
                      <BookOpen className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400" />
                      <span>精读逐题练</span>
                    </Link>

                    {/* Mock Exam Mode (标准限时模考) */}
                    <Link
                      href={`/exam?id=${exam.id}`}
                      className="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] shadow-subtle hover:shadow-card dark:shadow-glow-cyan transition-all duration-150 active:scale-[0.98] flex items-center space-x-1.5"
                    >
                      <Play className="w-3 h-3 fill-current" />
                      <span>{draft ? "继续限时模考" : "标准限时模考"}</span>
                    </Link>
                  </div>

                  {/* Print / Export Link */}
                  <Link
                    href={`/exam?id=${exam.id}&mode=print`}
                    title="导出或打印标准纸质练习卷"
                    className="p-2 text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-200 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
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
