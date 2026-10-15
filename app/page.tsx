"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { getLocalState, LocalLearningState, getExamCardStats } from "@/lib/storage";
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
  Sparkles,
  Search,
  ChevronLeft,
  ChevronRight,
  X,
  Target,
  BarChart2,
  LayoutGrid,
  List
} from "lucide-react";

export default function HomePage() {
  const [exams, setExams] = useState<any[]>([]);
  const [categories, setCategories] = useState<any[]>([]);
  const [activeCat, setActiveCat] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [loading, setLoading] = useState(true);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);
  const [viewMode, setViewMode] = useState<"grid" | "table">("grid");

  // Load persisted view mode from localStorage
  useEffect(() => {
    try {
      const saved = localStorage.getItem("enway_home_view_mode");
      if (saved === "table" || saved === "grid") {
        setViewMode(saved);
      }
    } catch {}
  }, []);

  const handleViewModeChange = (mode: "grid" | "table") => {
    setViewMode(mode);
    try {
      localStorage.setItem("enway_home_view_mode", mode);
    } catch {}
  };

  const PAGE_SIZE = 8;

  const loadData = async () => {
    setLoading(true);
    try {
      const { categories: cats, exams: examList } = await fetchExamLobbyData();
      if (cats && cats.length > 0) setCategories(cats);
      if (examList && examList.length > 0) setExams(examList);
    } catch (err) {
      console.error("Failed to load exams lobby:", err);
    } finally {
      // Read local learning state
      setLocalState(getLocalState());
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();

    const handleLobbyRevalidated = (e: any) => {
      if (e.detail?.categories?.length > 0) setCategories(e.detail.categories);
      if (e.detail?.exams?.length > 0) setExams(e.detail.exams);
    };

    window.addEventListener("enway_lobby_revalidated", handleLobbyRevalidated);
    return () => {
      window.removeEventListener("enway_lobby_revalidated", handleLobbyRevalidated);
    };
  }, []);

  const handleForceRefresh = async () => {
    try {
      await clearStaticExamCache();
    } catch {}
    await loadData();
  };

  const handleCatChange = (catId: string) => {
    setActiveCat(catId);
    setCurrentPage(1);
  };

  const handleSearchChange = (query: string) => {
    setSearchQuery(query);
    setCurrentPage(1);
  };

  const filteredExams = exams.filter((e) => {
    const matchCat = activeCat === "all" || e.category_id === activeCat;
    if (!matchCat) return false;
    if (!searchQuery.trim()) return true;
    const q = searchQuery.trim().toLowerCase();
    const title = (e.title || "").toLowerCase();
    const year = String(e.year || "");
    const cat = (e.category_id || "").toLowerCase();
    return title.includes(q) || year.includes(q) || cat.includes(q);
  });

  const totalPages = Math.max(1, Math.ceil(filteredExams.length / PAGE_SIZE));
  const pagedExams = filteredExams.slice((currentPage - 1) * PAGE_SIZE, currentPage * PAGE_SIZE);

  const handlePageChange = (newPage: number) => {
    const safePage = Math.max(1, Math.min(totalPages, newPage));
    setCurrentPage(safePage);
    document.getElementById("exam-list-top")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-200">
      {/* Hero / Learning Overview Section */}
      <div className="bg-white dark:bg-[#11131a] rounded-2xl p-7 sm:p-9 shadow-card border border-black/[0.06] dark:border-cyan-500/20 relative overflow-hidden transition-colors duration-300">
        <div className="absolute right-0 top-0 -mt-16 -mr-16 w-80 h-80 bg-emerald-50/60 dark:bg-cyan-900/20 rounded-full blur-3xl pointer-events-none transition-colors duration-300" />
        <div className="absolute left-1/3 bottom-0 -mb-16 w-60 h-60 bg-amber-50/50 dark:bg-violet-900/20 rounded-full blur-3xl pointer-events-none transition-colors duration-300" />
        
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-stone-100/90 dark:bg-zinc-900/90 border border-black/[0.04] dark:border-cyan-500/25 text-stone-700 dark:text-cyber-300 text-xs font-medium mb-3.5">
            <Flame className="w-3.5 h-3.5 text-amber-500" />
            <span>全国统考硕士研招 · 考研英语一与英语二权威真题</span>
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
        <div className="flex items-center space-x-1.5 overflow-x-auto no-scrollbar pb-0.5">
          <button
            onClick={() => handleCatChange("all")}
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
              onClick={() => handleCatChange(cat.id)}
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

      {/* Keyword Search Bar & Filter Stats */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-stone-50/70 dark:bg-zinc-900/50 p-2.5 rounded-2xl border border-black/[0.04] dark:border-cyan-500/15">
        <div className="relative flex-1">
          <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-stone-400 dark:text-zinc-500" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => handleSearchChange(e.target.value)}
            placeholder="搜索真题关键词（如：2024、英语一、英语二、六级、阅读、完形...）"
            className="w-full pl-10 pr-9 py-2 text-xs rounded-xl bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/25 text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-600/30 dark:focus:ring-cyber-400/40 shadow-subtle"
          />
          {searchQuery && (
            <button
              onClick={() => handleSearchChange("")}
              className="absolute right-3 top-1/2 -translate-y-1/2 p-0.5 text-stone-400 hover:text-stone-700 dark:hover:text-zinc-200 rounded-full"
              title="清除搜索关键字"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>

        <div className="flex items-center justify-between sm:justify-end space-x-2 text-xs text-stone-500 dark:text-zinc-400 px-1">
          <span className="font-medium font-mono">
            共找到 <strong className="text-emerald-700 dark:text-cyber-300 font-bold">{filteredExams.length}</strong> 套真题
          </span>
          {searchQuery && (
            <button
              onClick={() => handleSearchChange("")}
              className="text-[11px] px-2 py-0.5 rounded-md bg-stone-200/80 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 hover:bg-stone-300 transition-colors"
            >
              清空搜索
            </button>
          )}

          {/* Desktop View Mode Switcher (Grid / Table) */}
          <div className="hidden sm:flex items-center space-x-0.5 bg-stone-200/60 dark:bg-zinc-800/80 p-0.5 rounded-lg border border-black/[0.04] dark:border-cyan-500/15 ml-2">
            <button
              type="button"
              onClick={() => handleViewModeChange("grid")}
              title="网格大卡片视图"
              className={`p-1.5 rounded-md text-xs transition-all ${
                viewMode === "grid"
                  ? "bg-white dark:bg-zinc-700 text-stone-900 dark:text-zinc-100 shadow-sm font-bold"
                  : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
              }`}
            >
              <LayoutGrid className="w-3.5 h-3.5" />
            </button>
            <button
              type="button"
              onClick={() => handleViewModeChange("table")}
              title="紧凑高密列表视图 (PC 大屏专属)"
              className={`p-1.5 rounded-md text-xs transition-all ${
                viewMode === "table"
                  ? "bg-white dark:bg-zinc-700 text-stone-900 dark:text-zinc-100 shadow-sm font-bold"
                  : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
              }`}
            >
              <List className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>

      <div id="exam-list-top" className="scroll-mt-24" />

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
          <p className="text-stone-700 dark:text-zinc-300 font-semibold text-sm">
            {searchQuery ? `未找到包含 "${searchQuery}" 的真题卷` : "当前分类暂无发布的真题卷"}
          </p>
          <p className="text-xs text-stone-400 dark:text-zinc-500 mt-1">
            {searchQuery ? "请尝试其他关键字（如年份 2025、2024 或科目 英语一、英语二、KY-1、KY-2）" : "管理员在后台导入并审核上架后即可在此研习"}
          </p>
        </div>
      ) : viewMode === "table" ? (
        <>
          {/* PC Desktop Compact High-Density Table View */}
          <div className="hidden sm:block bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card overflow-hidden transition-colors duration-300">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-stone-50/80 dark:bg-zinc-900/80 border-b border-black/[0.05] dark:border-cyan-500/15 text-[11px] font-bold text-stone-400 dark:text-zinc-500 uppercase tracking-wider">
                  <tr>
                    <th className="py-3 px-4">真题考卷</th>
                    <th className="py-3 px-3">题量 / 时长</th>
                    <th className="py-3 px-4">精读练习进度</th>
                    <th className="py-3 px-4">限时模考档案</th>
                    <th className="py-3 px-4 text-right">研习操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-stone-100 dark:divide-zinc-800 font-sans">
                  {pagedExams.map((exam) => {
                    const pastResult = localState?.examResults?.[exam.id];
                    const draft = localState?.examDrafts?.[exam.id];
                    const qCount = exam.questions?.[0]?.count || 0;
                    const stats = getExamCardStats(exam.id, exam.total_score, qCount, localState);

                    return (
                      <tr 
                        key={exam.id}
                        className="hover:bg-stone-50/70 dark:hover:bg-zinc-900/50 transition-colors group"
                      >
                        {/* Exam Title & Year */}
                        <td className="py-3.5 px-4">
                          <div className="flex items-center space-x-2.5">
                            <span className="px-2 py-0.5 rounded text-[10px] font-bold font-mono bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 uppercase shrink-0">
                              {exam.category_id} · {exam.year}
                            </span>
                            <span className="font-bold text-stone-900 dark:text-zinc-100 group-hover:text-emerald-700 dark:group-hover:text-cyber-400 transition-colors truncate max-w-xs">
                              {exam.title}
                            </span>
                          </div>
                        </td>

                        {/* Specs */}
                        <td className="py-3.5 px-3 text-stone-500 dark:text-zinc-400 font-mono text-[11px] whitespace-nowrap">
                          <span>{qCount} 题 · {exam.duration_minutes} 分钟</span>
                        </td>

                        {/* Practice Progress */}
                        <td className="py-3.5 px-4">
                          {stats.hasPracticeRecord ? (
                            <div className="space-y-1 min-w-[130px] max-w-[170px]">
                              <div className="flex items-center justify-between text-[11px] font-mono">
                                <span className="text-stone-700 dark:text-zinc-300 font-medium">
                                  {stats.practiceAnsweredCount}/{stats.practiceTotalQuestions} 题 ({stats.practicePercent}%)
                                </span>
                                <span className="font-bold text-emerald-700 dark:text-cyber-300">
                                  {stats.practiceAccuracy}%
                                </span>
                              </div>
                              <div className="w-full h-1.5 rounded-full bg-stone-200/70 dark:bg-zinc-800 overflow-hidden">
                                <div
                                  className="h-full rounded-full bg-emerald-600 dark:bg-cyber-400 transition-all duration-300"
                                  style={{ width: `${stats.practicePercent}%` }}
                                />
                              </div>
                            </div>
                          ) : (
                            <span className="text-[11px] text-stone-400 dark:text-zinc-500">未开始</span>
                          )}
                        </td>

                        {/* Mock Exam Result */}
                        <td className="py-3.5 px-4 font-mono whitespace-nowrap">
                          {stats.hasExamRecord ? (
                            <div className="flex items-center space-x-2">
                              <span className="font-bold text-stone-900 dark:text-zinc-100 text-xs">
                                {stats.examScore} <span className="text-[10px] text-stone-400 dark:text-zinc-500 font-normal">/ {stats.examTotalScore}分</span>
                              </span>
                              <span className={`px-1.5 py-0.5 rounded text-[10px] font-bold ${
                                stats.examIsPassed
                                  ? "bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300"
                                  : "bg-rose-100 dark:bg-rose-950/60 text-rose-800 dark:text-rose-300"
                              }`}>
                                正确率 {stats.examAccuracy}%
                              </span>
                            </div>
                          ) : draft ? (
                            <span className="px-2 py-0.5 rounded text-[11px] font-medium bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300">
                              答题暂存中
                            </span>
                          ) : (
                            <span className="text-[11px] text-stone-400 dark:text-zinc-500">尚未模考</span>
                          )}
                        </td>

                        {/* Actions */}
                        <td className="py-3.5 px-4 text-right whitespace-nowrap">
                          <div className="flex items-center justify-end space-x-1.5">
                            <Link
                              href={`/practice?id=${exam.id}`}
                              className="px-2.5 py-1.5 rounded-lg text-xs font-semibold bg-stone-100 dark:bg-zinc-800 hover:bg-stone-200 dark:hover:bg-zinc-700 text-stone-800 dark:text-zinc-200 transition-all active:scale-95 flex items-center space-x-1"
                            >
                              <BookOpen className="w-3 h-3 text-stone-500 dark:text-zinc-400" />
                              <span>{stats.hasPracticeRecord ? "继续精读" : "精读"}</span>
                            </Link>

                            <Link
                              href={`/exam?id=${exam.id}`}
                              className="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] shadow-subtle transition-all active:scale-95 flex items-center space-x-1"
                            >
                              <Play className="w-3 h-3 fill-current" />
                              <span>{draft ? "继续模考" : "模考"}</span>
                            </Link>

                            <Link
                              href={`/exam?id=${exam.id}&mode=print`}
                              title="导出或打印标准纸质练习卷"
                              className="p-1.5 text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-200 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-lg transition-colors"
                            >
                              <Printer className="w-3.5 h-3.5" />
                            </Link>
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

          {/* Mobile Fallback to Cards (Visible only on < sm) */}
          <div className="block sm:hidden space-y-4">
            {pagedExams.map((exam) => {
              const pastResult = localState?.examResults?.[exam.id];
              const draft = localState?.examDrafts?.[exam.id];
              const qCount = exam.questions?.[0]?.count || 0;
              const stats = getExamCardStats(exam.id, exam.total_score, qCount, localState);

              return (
                <div
                  key={exam.id}
                  className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-5 shadow-card space-y-4"
                >
                  <div className="flex items-start justify-between gap-3">
                    <span className="px-2 py-0.5 rounded-md text-[11px] font-bold font-mono bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-cyber-300 uppercase">
                      {exam.category_id} · {exam.year} 年
                    </span>
                    {pastResult ? (
                      <span className="text-xs font-bold font-mono text-emerald-700 dark:text-emerald-300">
                        {pastResult.score}分
                      </span>
                    ) : null}
                  </div>
                  <h3 className="text-base font-bold text-stone-900 dark:text-zinc-100">{exam.title}</h3>
                  <div className="flex items-center gap-2">
                    <Link
                      href={`/practice?id=${exam.id}`}
                      className="flex-1 justify-center py-2 rounded-xl text-xs font-semibold bg-stone-100 dark:bg-zinc-800 text-stone-800 dark:text-zinc-200 flex items-center space-x-1"
                    >
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>精读练</span>
                    </Link>
                    <Link
                      href={`/exam?id=${exam.id}`}
                      className="flex-1 justify-center py-2 rounded-xl text-xs font-bold bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] flex items-center space-x-1"
                    >
                      <Play className="w-3 h-3 fill-current" />
                      <span>模考</span>
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        </>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {pagedExams.map((exam) => {
            const pastResult = localState?.examResults?.[exam.id];
            const draft = localState?.examDrafts?.[exam.id];
            const qCount = exam.questions?.[0]?.count || 0;
            const stats = getExamCardStats(exam.id, exam.total_score, qCount, localState);

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

                  <div className="mt-3 flex items-center space-x-4 text-xs text-stone-400 dark:text-zinc-500 font-medium">
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

                  {/* Learning Stats & Progress Bar */}
                  <div className="mt-4 p-3 rounded-xl bg-stone-50/80 dark:bg-zinc-900/60 border border-black/[0.04] dark:border-cyan-500/15 space-y-2.5">
                    {/* Row 1: Mock Exam Record */}
                    <div className="flex items-center justify-between text-xs">
                      <span className="flex items-center space-x-1.5 text-stone-500 dark:text-zinc-400 font-medium">
                        <Award className="w-3.5 h-3.5 text-amber-500 dark:text-amber-400" />
                        <span>限时模考</span>
                      </span>
                      {stats.hasExamRecord ? (
                        <div className="flex items-center space-x-2 font-mono">
                          <span className="font-bold text-stone-900 dark:text-zinc-100">
                            {stats.examScore} <span className="text-[11px] font-normal text-stone-400 dark:text-zinc-500">/ {stats.examTotalScore}分</span>
                          </span>
                          <span className={`px-1.5 py-0.5 rounded text-[10px] font-bold ${
                            stats.examIsPassed
                              ? "bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300"
                              : "bg-rose-100 dark:bg-rose-950/60 text-rose-800 dark:text-rose-300"
                          }`}>
                            正确率 {stats.examAccuracy}%
                          </span>
                        </div>
                      ) : (
                        <span className="text-[11px] text-stone-400 dark:text-zinc-500">尚未模考</span>
                      )}
                    </div>

                    {/* Row 2: Practice Mode Progress */}
                    <div className="space-y-1">
                      <div className="flex items-center justify-between text-xs">
                        <span className="flex items-center space-x-1.5 text-stone-500 dark:text-zinc-400 font-medium">
                          <Target className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
                          <span>精读进度</span>
                        </span>
                        {stats.hasPracticeRecord ? (
                          <div className="flex items-center space-x-2 font-mono">
                            <span className="text-stone-700 dark:text-zinc-300 text-[11px]">
                              {stats.practiceAnsweredCount}/{stats.practiceTotalQuestions} 题 ({stats.practicePercent}%)
                            </span>
                            <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 dark:bg-cyan-950/60 text-emerald-700 dark:text-cyber-300 border border-emerald-200/50 dark:border-cyan-500/20">
                              正确率 {stats.practiceAccuracy}%
                            </span>
                          </div>
                        ) : (
                          <span className="text-[11px] text-stone-400 dark:text-zinc-500">未开始 (0/{stats.practiceTotalQuestions}题)</span>
                        )}
                      </div>

                      {/* Visual Progress Bar */}
                      <div className="w-full h-1.5 rounded-full bg-stone-200/70 dark:bg-zinc-800 overflow-hidden">
                        <div 
                          className="h-full rounded-full bg-emerald-600 dark:bg-cyber-400 transition-all duration-300 ease-out" 
                          style={{ width: `${stats.practicePercent}%` }} 
                        />
                      </div>
                    </div>
                  </div>
                </div>

                {/* Card Action Buttons */}
                <div className="mt-5 pt-4 border-t border-stone-100 dark:border-zinc-800 flex items-center justify-between gap-2.5">
                  <div className="flex items-center gap-2 flex-1 sm:flex-initial">
                    {/* Practice Mode (精读逐题练) */}
                    <Link
                      href={`/practice?id=${exam.id}`}
                      className="flex-1 sm:flex-initial justify-center px-3 sm:px-3.5 py-2 rounded-xl text-xs font-semibold bg-stone-100/90 dark:bg-zinc-800 hover:bg-stone-200/80 dark:hover:bg-zinc-700 text-stone-800 dark:text-zinc-200 transition-all duration-150 active:scale-[0.98] flex items-center space-x-1.5"
                    >
                      <BookOpen className="w-3.5 h-3.5 text-stone-500 dark:text-zinc-400 shrink-0" />
                      <span className="truncate">{stats.hasPracticeRecord ? `继续精读 (${stats.practiceAnsweredCount}/${stats.practiceTotalQuestions})` : "精读逐题练"}</span>
                    </Link>

                    {/* Mock Exam Mode (标准限时模考) */}
                    <Link
                      href={`/exam?id=${exam.id}`}
                      className="flex-1 sm:flex-initial justify-center px-3.5 sm:px-4 py-2 rounded-xl text-xs font-bold bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] shadow-subtle hover:shadow-card dark:shadow-glow-cyan transition-all duration-150 active:scale-[0.98] flex items-center space-x-1.5"
                    >
                      <Play className="w-3 h-3 fill-current shrink-0" />
                      <span className="truncate">{draft ? "继续限时模考" : "标准限时模考"}</span>
                    </Link>
                  </div>

                  {/* Print / Export Link */}
                  <Link
                    href={`/exam?id=${exam.id}&mode=print`}
                    title="导出或打印标准纸质练习卷"
                    className="p-2 text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-200 hover:bg-stone-100 dark:hover:bg-zinc-800 rounded-xl transition-colors shrink-0"
                  >
                    <Printer className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Pagination Controls */}
      {filteredExams.length > PAGE_SIZE && (
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-black/[0.06] dark:border-cyan-500/15">
          <div className="text-xs text-stone-400 dark:text-zinc-500 font-mono">
            第 {currentPage} / {totalPages} 页 · 每页 {PAGE_SIZE} 套 · 共 {filteredExams.length} 套试卷
          </div>

          <div className="flex items-center space-x-1.5">
            <button
              onClick={() => handlePageChange(currentPage - 1)}
              disabled={currentPage <= 1}
              className="px-3 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-[#11131a] hover:bg-stone-50 dark:hover:bg-zinc-800 disabled:opacity-30 disabled:pointer-events-none text-xs font-semibold text-stone-700 dark:text-zinc-300 flex items-center space-x-1 shadow-subtle active:scale-[0.98] transition-all"
            >
              <ChevronLeft className="w-3.5 h-3.5" />
              <span>上一页</span>
            </button>

            <div className="flex items-center space-x-1">
              {Array.from({ length: totalPages }, (_, i) => i + 1)
                .filter((p) => p === 1 || p === totalPages || Math.abs(p - currentPage) <= 1)
                .reduce<number[]>((acc, p) => {
                  if (acc.length > 0 && p - acc[acc.length - 1] > 1) {
                    acc.push(-1);
                  }
                  acc.push(p);
                  return acc;
                }, [])
                .map((p, idx) => {
                  if (p === -1) {
                    return (
                      <span key={`dots-${idx}`} className="px-1 text-xs text-stone-400 dark:text-zinc-600">
                        ...
                      </span>
                    );
                  }
                  const isActive = p === currentPage;
                  return (
                    <button
                      key={p}
                      onClick={() => handlePageChange(p)}
                      className={`w-8 h-8 rounded-xl text-xs font-bold font-mono transition-all active:scale-95 ${
                        isActive
                          ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle dark:shadow-glow-cyan"
                          : "bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/20 text-stone-600 dark:text-zinc-400 hover:bg-stone-50 dark:hover:bg-zinc-800 shadow-subtle"
                      }`}
                    >
                      {p}
                    </button>
                  );
                })}
            </div>

            <button
              onClick={() => handlePageChange(currentPage + 1)}
              disabled={currentPage >= totalPages}
              className="px-3 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-[#11131a] hover:bg-stone-50 dark:hover:bg-zinc-800 disabled:opacity-30 disabled:pointer-events-none text-xs font-semibold text-stone-700 dark:text-zinc-300 flex items-center space-x-1 shadow-subtle active:scale-[0.98] transition-all"
            >
              <span>下一页</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
