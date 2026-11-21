"use client";

import { Suspense, useState, useEffect, useRef, useCallback, useMemo } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import {
  getLocalState,
  LocalLearningState,
  getExamCardStats,
  subscribeLocalState,
} from "@/lib/storage";
import { fetchExamLobbyData, clearStaticExamCache } from "@/lib/examLoader";
import type { CategoryRecord, ExamLobbyData, ExamRecord } from "@/types/exam";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { EmptyState, Skeleton } from "@/components/ui/Feedback";
import { ProgressBar } from "@/components/ui/ProgressBar";
import {
  BookOpen,
  Clock,
  Award,
  Play,
  Flame,
  HelpCircle,
  Printer,
  RefreshCw,
  Search,
  ChevronLeft,
  ChevronRight,
  X,
  Target,
  LayoutGrid,
  List,
  ArrowRight,
  Sparkles,
} from "lucide-react";

const PAGE_SIZE = 8;

type ResumeTarget =
  | {
      kind: "exam-draft";
      exam: ExamRecord;
      answeredCount: number;
      remainingSeconds: number;
      lastUpdated: string;
    }
  | {
      kind: "practice-draft";
      exam: ExamRecord;
      answeredCount: number;
      lastUpdated: string;
    }
  | {
      kind: "latest-exam";
      exam: ExamRecord;
    };

function formatRemainingMinutes(seconds: number): string {
  const mins = Math.max(0, Math.ceil(seconds / 60));
  return `剩余约 ${mins} 分钟`;
}

function ExamCard({
  exam,
  localState,
}: {
  exam: ExamRecord;
  localState: LocalLearningState | null;
}) {
  const pastResult = localState?.examResults?.[exam.id];
  const draft = localState?.examDrafts?.[exam.id];
  const qCount = exam.questions?.[0]?.count || 0;
  const stats = getExamCardStats(exam.id, exam.total_score, qCount, localState);

  return (
    <Card
      interactive
      className="p-5 sm:p-6 flex flex-col justify-between group hover:border-primary/40 hover:-translate-y-0.5 transition-all duration-200"
    >
      <div>
        <div className="flex items-start justify-between gap-2.5 mb-2.5">
          <Badge tone="neutral" className="font-mono uppercase tracking-wide">
            {exam.category_id} · {exam.year} 年
          </Badge>

          {pastResult ? (
            <Badge tone={pastResult.isPassed ? "success" : "danger"} className="shrink-0">
              <Award className="w-3 h-3" />
              <span>
                最近 {pastResult.score}分（{pastResult.isPassed ? "合格" : "未达标"}）
              </span>
            </Badge>
          ) : draft ? (
            <Badge tone="warning" className="shrink-0">
              <Clock className="w-3 h-3" />
              <span>模考暂存中</span>
            </Badge>
          ) : null}
        </div>

        <h3 className="text-base sm:text-lg font-bold text-fg leading-snug group-hover:text-primary transition-colors">
          {exam.title}
        </h3>

        <div className="mt-2.5 flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-fg-subtle font-medium">
          <span className="inline-flex items-center gap-1">
            <Clock className="w-3.5 h-3.5 text-fg-subtle/80" />
            <span>限时 {exam.duration_minutes} 分钟</span>
          </span>
          <span className="inline-flex items-center gap-1">
            <HelpCircle className="w-3.5 h-3.5 text-fg-subtle/80" />
            <span>满分 {exam.total_score} 分</span>
          </span>
          <span className="font-mono tabular-nums">共 {qCount} 题</span>
        </div>

        {/* Learning Stats & Progress */}
        <div className="mt-4 p-3 rounded-xl bg-surface-2/80 border border-border/80 space-y-2.5">
          <div className="flex items-center justify-between gap-2 text-xs">
            <span className="inline-flex items-center gap-1.5 text-fg-muted font-medium">
              <Award className="w-3.5 h-3.5 text-warning shrink-0" />
              <span>限时模考</span>
            </span>
            {stats.hasExamRecord ? (
              <div className="flex items-center gap-2 font-mono tabular-nums">
                <span className="font-bold text-fg">
                  {stats.examScore}{" "}
                  <span className="text-[11px] font-normal text-fg-subtle">
                    / {stats.examTotalScore}分
                  </span>
                </span>
                <Badge tone={stats.examIsPassed ? "success" : "danger"} className="text-[10px]">
                  正确率 {stats.examAccuracy}%
                </Badge>
              </div>
            ) : (
              <span className="text-[11px] text-fg-subtle">尚未模考</span>
            )}
          </div>

          <div className="space-y-1.5">
            <div className="flex items-center justify-between gap-2 text-xs">
              <span className="inline-flex items-center gap-1.5 text-fg-muted font-medium">
                <Target className="w-3.5 h-3.5 text-primary shrink-0" />
                <span>精读进度</span>
              </span>
              {stats.hasPracticeRecord ? (
                <div className="flex items-center gap-1.5 font-mono tabular-nums">
                  <span className="text-[11px] text-fg-muted">
                    {stats.practiceAnsweredCount}/{stats.practiceTotalQuestions} 题（
                    {stats.practicePercent}%）
                  </span>
                  <Badge tone="primary" className="text-[10px]">
                    正确率 {stats.practiceAccuracy}%
                  </Badge>
                </div>
              ) : (
                <span className="text-[11px] text-fg-subtle font-mono tabular-nums">
                  未开始（0/{stats.practiceTotalQuestions}题）
                </span>
              )}
            </div>
            <ProgressBar value={stats.practicePercent} max={100} tone="primary" />
          </div>
        </div>
      </div>

      {/* Action Footer */}
      <div className="mt-5 pt-4 border-t border-border/80 flex items-center justify-between gap-2">
        <div className="flex items-center gap-2 flex-1 min-w-0">
          <Link
            href={`/practice?id=${exam.id}`}
            className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold bg-surface-2 hover:bg-border/60 text-fg border border-border transition-colors active:scale-[0.98] min-w-0"
          >
            <BookOpen className="w-3.5 h-3.5 text-fg-muted shrink-0" />
            <span className="truncate">
              {stats.hasPracticeRecord
                ? `继续精读 (${stats.practiceAnsweredCount}/${stats.practiceTotalQuestions})`
                : "精读逐题练"}
            </span>
          </Link>

          <Link
            href={`/exam?id=${exam.id}`}
            className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold bg-primary hover:opacity-95 text-primary-fg shadow-1 transition-all active:scale-[0.98] min-w-0"
          >
            <Play className="w-3 h-3 fill-current shrink-0" />
            <span className="truncate">
              {draft ? "继续限时模考" : stats.hasExamRecord ? "模考复盘" : "标准限时模考"}
            </span>
          </Link>
        </div>

        <Link
          href={`/exam?id=${exam.id}&mode=print`}
          title="导出或打印标准纸质练习卷"
          aria-label={`打印或导出 ${exam.title}`}
          className="inline-flex items-center justify-center gap-1 px-2.5 py-2 text-xs font-medium text-fg-muted hover:text-fg hover:bg-surface-2 border border-transparent hover:border-border rounded-xl transition-colors shrink-0"
        >
          <Printer className="w-4 h-4" />
          <span className="sm:hidden">打印</span>
        </Link>
      </div>
    </Card>
  );
}

function parseLobbySearch(params: URLSearchParams) {
  const cat = params.get("cat") || "all";
  const q = params.get("q") || "";
  const pageRaw = Number.parseInt(params.get("page") || "1", 10);
  const page = Number.isFinite(pageRaw) && pageRaw > 0 ? pageRaw : 1;
  return { cat, q, page };
}

function ExamLobbyContent() {
  const searchParams = useSearchParams();
  const initialQuery = parseLobbySearch(searchParams);

  const [exams, setExams] = useState<ExamRecord[]>([]);
  const [categories, setCategories] = useState<CategoryRecord[]>([]);
  const [selectedCat, setSelectedCat] = useState<string>(initialQuery.cat);
  const [searchInput, setSearchInput] = useState<string>(initialQuery.q);
  const [currentPage, setCurrentPage] = useState<number>(initialQuery.page);
  const [loading, setLoading] = useState(true);
  const [localState, setLocalState] = useState<LocalLearningState | null>(null);
  const [viewMode, setViewMode] = useState<"grid" | "table">("grid");

  const searchDebounceRef = useRef<number | null>(null);
  const lastWrittenQsRef = useRef<string | null>(null);
  const filterStateRef = useRef({
    cat: selectedCat,
    q: searchInput,
    page: currentPage,
  });
  filterStateRef.current = {
    cat: selectedCat,
    q: searchInput,
    page: currentPage,
  };

  const syncUrlParams = useCallback(
    (next: { cat?: string; q?: string; page?: number }) => {
      if (typeof window === "undefined") return;
      const cur = filterStateRef.current;
      const nextCat = next.cat !== undefined ? next.cat : cur.cat;
      const nextQ = next.q !== undefined ? next.q : cur.q;
      const nextPage = next.page !== undefined ? next.page : cur.page;

      const params = new URLSearchParams(window.location.search);
      if (nextCat && nextCat !== "all") params.set("cat", nextCat);
      else params.delete("cat");

      if (nextQ.trim()) params.set("q", nextQ.trim());
      else params.delete("q");

      if (nextPage > 1) params.set("page", String(nextPage));
      else params.delete("page");

      const qs = params.toString();
      lastWrittenQsRef.current = qs;
      const targetUrl = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
      const currentFull = `${window.location.pathname}${window.location.search}`;
      if (currentFull !== targetUrl) {
        window.history.replaceState(window.history.state, "", targetUrl);
      }
    },
    []
  );

  // Sync local state if Next.js route navigation or browser back/forward changes URL
  const searchParamsStr = searchParams.toString();
  useEffect(() => {
    if (lastWrittenQsRef.current !== null && searchParamsStr === lastWrittenQsRef.current) {
      return;
    }
    const parsed = parseLobbySearch(searchParams);
    setSelectedCat(parsed.cat);
    setSearchInput(parsed.q);
    setCurrentPage(parsed.page);
    lastWrittenQsRef.current = searchParamsStr;
  }, [searchParams, searchParamsStr]);

  useEffect(() => {
    const handlePopState = () => {
      const params = new URLSearchParams(window.location.search);
      const parsed = parseLobbySearch(params);
      if (searchDebounceRef.current !== null) {
        window.clearTimeout(searchDebounceRef.current);
        searchDebounceRef.current = null;
      }
      lastWrittenQsRef.current = params.toString();
      setSelectedCat(parsed.cat);
      setSearchInput(parsed.q);
      setCurrentPage(parsed.page);
    };
    window.addEventListener("popstate", handlePopState);
    return () => {
      window.removeEventListener("popstate", handlePopState);
      if (searchDebounceRef.current !== null) {
        window.clearTimeout(searchDebounceRef.current);
        searchDebounceRef.current = null;
      }
    };
  }, []);

  // Load persisted desktop view mode
  useEffect(() => {
    try {
      const saved = localStorage.getItem("enway_home_view_mode");
      if (saved === "table" || saved === "grid") {
        setViewMode(saved);
      }
    } catch {}
  }, []);

  const handleSearchInputChange = (val: string) => {
    setSearchInput(val);
    setCurrentPage(1);
    if (searchDebounceRef.current !== null) {
      window.clearTimeout(searchDebounceRef.current);
      searchDebounceRef.current = null;
    }
    searchDebounceRef.current = window.setTimeout(() => {
      searchDebounceRef.current = null;
      syncUrlParams({ cat: filterStateRef.current.cat, q: val, page: 1 });
    }, 180);
  };

  const handleViewModeChange = (mode: "grid" | "table") => {
    setViewMode(mode);
    try {
      localStorage.setItem("enway_home_view_mode", mode);
    } catch {}
  };

  const mountedRef = useRef(true);
  const loadSeqRef = useRef(0);

  const loadData = useCallback(async () => {
    const seq = ++loadSeqRef.current;
    setLoading(true);
    try {
      const { categories: cats, exams: examList } = await fetchExamLobbyData();
      if (!mountedRef.current || seq !== loadSeqRef.current) return;
      if (cats && cats.length > 0) setCategories(cats);
      if (examList && examList.length > 0) setExams(examList);
    } catch (err) {
      if (mountedRef.current && seq === loadSeqRef.current) {
        console.error("Failed to load exams lobby:", err);
      }
    } finally {
      if (mountedRef.current && seq === loadSeqRef.current) {
        setLocalState(getLocalState());
        setLoading(false);
      }
    }
  }, []);

  useEffect(() => {
    mountedRef.current = true;
    loadData();

    const handleLobbyRevalidated = (e: Event) => {
      if (!mountedRef.current) return;
      const detail = (e as CustomEvent<Partial<ExamLobbyData>>).detail;
      if (detail?.categories && detail.categories.length > 0) setCategories(detail.categories);
      if (detail?.exams && detail.exams.length > 0) setExams(detail.exams);
    };

    const handleExamVersionUpdated = () => {
      if (!mountedRef.current) return;
      loadData();
    };

    const unsubscribeLocal = subscribeLocalState((nextState) => {
      if (mountedRef.current) {
        setLocalState(nextState);
      }
    });

    window.addEventListener("enway_lobby_revalidated", handleLobbyRevalidated);
    window.addEventListener("enway_exam_version_updated", handleExamVersionUpdated);
    return () => {
      mountedRef.current = false;
      unsubscribeLocal();
      window.removeEventListener("enway_lobby_revalidated", handleLobbyRevalidated);
      window.removeEventListener("enway_exam_version_updated", handleExamVersionUpdated);
    };
  }, [loadData]);

  const handleForceRefresh = async () => {
    try {
      await clearStaticExamCache();
    } catch {}
    await loadData();
  };

  const handleCatChange = (catId: string) => {
    setSelectedCat(catId);
    setCurrentPage(1);
    syncUrlParams({ cat: catId, q: filterStateRef.current.q, page: 1 });
  };

  const handleClearSearch = () => {
    if (searchDebounceRef.current !== null) {
      window.clearTimeout(searchDebounceRef.current);
      searchDebounceRef.current = null;
    }
    setSearchInput("");
    setCurrentPage(1);
    syncUrlParams({ cat: filterStateRef.current.cat, q: "", page: 1 });
  };

  // Validate active category against loaded categories
  const activeCat = useMemo(() => {
    if (selectedCat === "all" || categories.length === 0) return selectedCat;
    return categories.some((c) => c.id === selectedCat) ? selectedCat : "all";
  }, [selectedCat, categories]);

  const filteredExams = useMemo(() => {
    const q = searchInput.trim().toLowerCase();
    return exams.filter((e) => {
      const matchCat = activeCat === "all" || e.category_id === activeCat;
      if (!matchCat) return false;
      if (!q) return true;
      const title = (e.title || "").toLowerCase();
      const year = String(e.year || "");
      const cat = (e.category_id || "").toLowerCase();
      return title.includes(q) || year.includes(q) || cat.includes(q);
    });
  }, [exams, activeCat, searchInput]);

  const totalPages = Math.max(1, Math.ceil(filteredExams.length / PAGE_SIZE));
  const safePage = Math.max(1, Math.min(totalPages, currentPage));
  const pagedExams = filteredExams.slice((safePage - 1) * PAGE_SIZE, safePage * PAGE_SIZE);

  const handlePageChange = (newPage: number) => {
    const nextSafe = Math.max(1, Math.min(totalPages, newPage));
    setCurrentPage(nextSafe);
    syncUrlParams({ cat: activeCat, q: filterStateRef.current.q, page: nextSafe });
    document.getElementById("exam-list-top")?.scrollIntoView({ behavior: "smooth" });
  };

  // Determine the highest-value quick resume target (most recently updated draft, or newest exam)
  const resumeTarget = useMemo<ResumeTarget | null>(() => {
    if (exams.length === 0) return null;
    const examById = new Map(exams.map((e) => [e.id, e]));

    type Candidate = { ts: number; target: ResumeTarget };
    const candidates: Candidate[] = [];

    if (localState?.examDrafts) {
      for (const draft of Object.values(localState.examDrafts)) {
        const exam = examById.get(draft.examId);
        if (!exam) continue;
        const ts = Date.parse(draft.lastUpdated || "") || 0;
        candidates.push({
          ts,
          target: {
            kind: "exam-draft",
            exam,
            answeredCount: Object.keys(draft.answers || {}).length,
            remainingSeconds: draft.remainingSeconds,
            lastUpdated: draft.lastUpdated,
          },
        });
      }
    }

    if (localState?.practiceDrafts) {
      for (const draft of Object.values(localState.practiceDrafts)) {
        const exam = examById.get(draft.examId);
        if (!exam) continue;
        const answeredCount = draft.answeredCount ?? Object.keys(draft.answers || {}).length;
        if (answeredCount === 0 && draft.currentIndex === 0) continue;
        const ts = Date.parse(draft.lastUpdated || "") || 0;
        candidates.push({
          ts,
          target: {
            kind: "practice-draft",
            exam,
            answeredCount,
            lastUpdated: draft.lastUpdated,
          },
        });
      }
    }

    if (candidates.length > 0) {
      candidates.sort((a, b) => b.ts - a.ts);
      return candidates[0].target;
    }

    const sortedLatest = [...exams].sort((a, b) => (b.year || 0) - (a.year || 0));
    return { kind: "latest-exam", exam: sortedLatest[0] };
  }, [exams, localState]);

  const unmasteredMistakes = localState
    ? localState.mistakes.filter((m) => !m.isMastered).length
    : 0;
  const vocabCount = localState ? localState.vocabulary.length : 0;
  const completedExamCount = localState ? Object.keys(localState.examResults).length : 0;

  return (
    <div className="space-y-6 sm:space-y-8 animate-in fade-in duration-200">
      {/* Editorial Hero & Quick Resume */}
      <Card className="p-5 sm:p-8">
        <div className="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-6 items-start">
          <div className="min-w-0">
            <Badge tone="neutral" className="mb-3">
              <Flame className="w-3.5 h-3.5 text-warning" />
              <span>全国统考硕士研招 · 考研英语一与英语二权威真题</span>
            </Badge>

            <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-fg leading-tight">
              权威真题研习 · 全真限时模考
            </h1>
            <p className="mt-2 text-xs sm:text-sm text-fg-muted leading-relaxed max-w-2xl">
              严谨还原官方试卷结构，长篇仔细阅读与客观题左右分栏对照；实时单词即查与形态还原，客观题即刻反馈精析与考点定位，做题状态本地可靠暂存。
            </p>

            {/* Quick Learning Stats (Compact & Safe on <=375px screens) */}
            {localState && (
              <div className="mt-5 pt-4 border-t border-border/80 grid grid-cols-3 gap-2 sm:gap-3.5 max-w-md">
                <Link
                  href="/mistakes"
                  className="bg-surface-2/80 hover:bg-surface-2 p-2.5 sm:p-3 rounded-xl border border-border/80 transition-colors min-w-0"
                >
                  <span className="text-[11px] text-fg-subtle block font-medium truncate">
                    待攻克错题
                  </span>
                  <span className="text-lg sm:text-xl font-bold font-mono tabular-nums text-fg mt-0.5 block">
                    {unmasteredMistakes}
                  </span>
                </Link>
                <Link
                  href="/vocabulary"
                  className="bg-surface-2/80 hover:bg-surface-2 p-2.5 sm:p-3 rounded-xl border border-border/80 transition-colors min-w-0"
                >
                  <span className="text-[11px] text-fg-subtle block font-medium truncate">
                    核心词汇
                  </span>
                  <span className="text-lg sm:text-xl font-bold font-mono tabular-nums text-fg mt-0.5 block">
                    {vocabCount}
                  </span>
                </Link>
                <Link
                  href="/profile"
                  className="bg-surface-2/80 hover:bg-surface-2 p-2.5 sm:p-3 rounded-xl border border-border/80 transition-colors min-w-0"
                >
                  <span className="text-[11px] text-fg-subtle block font-medium truncate">
                    已测模考
                  </span>
                  <span className="text-lg sm:text-xl font-bold font-mono tabular-nums text-primary mt-0.5 block">
                    {completedExamCount}
                  </span>
                </Link>
              </div>
            )}
          </div>

          {/* Right Column: Continue Last Draft / Start Latest Exam */}
          <div className="bg-surface-2/70 border border-border rounded-2xl p-4 sm:p-5 overflow-visible flex flex-col justify-between gap-4">
            {loading && !resumeTarget ? (
              <div className="space-y-3">
                <Skeleton className="h-4 w-24" />
                <Skeleton className="h-5 w-full" />
                <Skeleton className="h-3 w-36" />
                <Skeleton className="h-9 w-full rounded-xl" />
              </div>
            ) : resumeTarget ? (
              <>
                <div className="space-y-2.5 pt-0.5 overflow-visible">
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    <Badge
                      tone={
                        resumeTarget.kind === "latest-exam" ? "primary" : "warning"
                      }
                    >
                      {resumeTarget.kind === "exam-draft" ? (
                        <>
                          <Clock className="w-3 h-3" />
                          <span>继续上次模考</span>
                        </>
                      ) : resumeTarget.kind === "practice-draft" ? (
                        <>
                          <BookOpen className="w-3 h-3" />
                          <span>继续上次精读</span>
                        </>
                      ) : (
                        <>
                          <Sparkles className="w-3 h-3" />
                          <span>推荐最新真题</span>
                        </>
                      )}
                    </Badge>
                    <span className="text-[11px] font-mono text-fg-subtle">
                      {resumeTarget.exam.category_id} · {resumeTarget.exam.year}
                    </span>
                  </div>

                  <h2 className="text-sm font-bold text-fg leading-snug line-clamp-2">
                    {resumeTarget.exam.title}
                  </h2>

                  <p className="text-xs text-fg-muted font-mono tabular-nums">
                    {resumeTarget.kind === "exam-draft"
                      ? `已作答 ${resumeTarget.answeredCount} 题 · ${formatRemainingMinutes(
                          resumeTarget.remainingSeconds
                        )}`
                      : resumeTarget.kind === "practice-draft"
                        ? `已精读作答 ${resumeTarget.answeredCount} 题`
                        : `限时 ${resumeTarget.exam.duration_minutes} 分钟 · 满分 ${resumeTarget.exam.total_score} 分`}
                  </p>
                </div>

                {resumeTarget.kind === "exam-draft" ? (
                  <Link
                    href={`/exam?id=${resumeTarget.exam.id}`}
                    className="w-full inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl text-xs font-bold bg-primary text-primary-fg hover:opacity-95 shadow-1 transition-all active:scale-[0.98]"
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span>恢复模考现场</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                ) : resumeTarget.kind === "practice-draft" ? (
                  <Link
                    href={`/practice?id=${resumeTarget.exam.id}`}
                    className="w-full inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl text-xs font-bold bg-primary text-primary-fg hover:opacity-95 shadow-1 transition-all active:scale-[0.98]"
                  >
                    <BookOpen className="w-3.5 h-3.5" />
                    <span>继续逐题精读</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                ) : (
                  <div className="flex items-center gap-2">
                    <Link
                      href={`/practice?id=${resumeTarget.exam.id}`}
                      className="flex-1 inline-flex items-center justify-center gap-1 px-3 py-2 rounded-xl text-xs font-semibold bg-surface hover:bg-surface-2 text-fg border border-border transition-colors"
                    >
                      <BookOpen className="w-3.5 h-3.5 text-fg-muted" />
                      <span>精读练习</span>
                    </Link>
                    <Link
                      href={`/exam?id=${resumeTarget.exam.id}`}
                      className="flex-1 inline-flex items-center justify-center gap-1 px-3 py-2 rounded-xl text-xs font-bold bg-primary text-primary-fg hover:opacity-95 shadow-1 transition-all"
                    >
                      <Play className="w-3 h-3 fill-current" />
                      <span>开始模考</span>
                    </Link>
                  </div>
                )}
              </>
            ) : (
              <p className="text-xs text-fg-muted">暂无可用真题，请稍后刷新题库。</p>
            )}
          </div>
        </div>
      </Card>

      {/* Category Tabs & Quick Refresh */}
      <div className="flex items-center justify-between gap-3 border-b border-border pb-2.5">
        <div
          className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-0.5"
          role="tablist"
          aria-label="真题科目分类"
        >
          <button
            type="button"
            role="tab"
            aria-selected={activeCat === "all"}
            onClick={() => handleCatChange("all")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-colors ${
              activeCat === "all"
                ? "bg-primary text-primary-fg shadow-1"
                : "text-fg-muted hover:text-fg hover:bg-surface-2"
            }`}
          >
            全部科目真题
          </button>
          {categories.map((cat) => (
            <button
              key={cat.id}
              type="button"
              role="tab"
              aria-selected={activeCat === cat.id}
              onClick={() => handleCatChange(cat.id)}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-colors ${
                activeCat === cat.id
                  ? "bg-primary text-primary-fg shadow-1"
                  : "text-fg-muted hover:text-fg hover:bg-surface-2"
              }`}
            >
              {cat.name}
            </button>
          ))}
        </div>

        <Button
          variant="secondary"
          size="sm"
          onClick={handleForceRefresh}
          disabled={loading}
          title="清除本地短期缓存，秒级同步最新发布的真题与考卷"
          className="shrink-0"
        >
          <RefreshCw
            className={`w-3.5 h-3.5 ${loading ? "animate-spin text-primary" : "text-fg-subtle"}`}
          />
          <span className="hidden sm:inline">{loading ? "同步中..." : "刷新题库"}</span>
        </Button>
      </div>

      {/* Keyword Search Bar & Desktop View Mode Switcher */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-surface-2/70 p-2.5 rounded-2xl border border-border">
        <div className="relative flex-1">
          <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-fg-subtle pointer-events-none" />
          <input
            type="text"
            value={searchInput}
            onChange={(e) => handleSearchInputChange(e.target.value)}
            placeholder="搜索真题关键词（如：2024、英语一、英语二、阅读、完形...）"
            aria-label="搜索真题关键词"
            className="input-compact w-full h-9 pl-10 pr-9 text-xs rounded-xl bg-surface border border-border text-fg placeholder:text-fg-subtle focus:outline-none focus:ring-2 focus:ring-primary/30 transition-colors"
          />
          {searchInput && (
            <button
              type="button"
              onClick={handleClearSearch}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 p-1 text-fg-subtle hover:text-fg rounded-md transition-colors"
              title="清除搜索关键字"
              aria-label="清除搜索关键字"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>

        <div className="flex items-center justify-between sm:justify-end gap-2 text-xs text-fg-muted px-1">
          <span className="font-medium font-mono tabular-nums">
            共找到 <strong className="text-primary font-bold">{filteredExams.length}</strong> 套真题
          </span>
          {searchInput && (
            <button
              type="button"
              onClick={handleClearSearch}
              className="text-[11px] px-2 py-0.5 rounded-md bg-surface border border-border text-fg-muted hover:text-fg transition-colors"
            >
              清空搜索
            </button>
          )}

          {/* Desktop-only (md+) View Mode Switcher */}
          <div className="hidden md:flex items-center gap-0.5 bg-surface p-0.5 rounded-lg border border-border ml-1">
            <button
              type="button"
              onClick={() => handleViewModeChange("grid")}
              title="网格卡片视图"
              aria-label="网格卡片视图"
              aria-pressed={viewMode === "grid"}
              className={`p-1.5 rounded-md transition-colors ${
                viewMode === "grid"
                  ? "bg-surface-2 text-fg shadow-1 font-semibold"
                  : "text-fg-subtle hover:text-fg"
              }`}
            >
              <LayoutGrid className="w-3.5 h-3.5" />
            </button>
            <button
              type="button"
              onClick={() => handleViewModeChange("table")}
              title="紧凑高密列表视图"
              aria-label="紧凑高密列表视图"
              aria-pressed={viewMode === "table"}
              className={`p-1.5 rounded-md transition-colors ${
                viewMode === "table"
                  ? "bg-surface-2 text-fg shadow-1 font-semibold"
                  : "text-fg-subtle hover:text-fg"
              }`}
            >
              <List className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>

      <div id="exam-list-top" className="scroll-mt-24" />

      {/* Exam List */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {[1, 2, 3, 4].map((i) => (
            <Card key={i} className="p-6 space-y-4">
              <div className="flex items-center justify-between">
                <Skeleton className="h-5 w-24" />
                <Skeleton className="h-5 w-20" />
              </div>
              <Skeleton className="h-6 w-3/4" />
              <Skeleton className="h-16 w-full rounded-xl" />
              <div className="flex gap-2 pt-2">
                <Skeleton className="h-9 flex-1 rounded-xl" />
                <Skeleton className="h-9 flex-1 rounded-xl" />
              </div>
            </Card>
          ))}
        </div>
      ) : filteredExams.length === 0 ? (
        <Card className="py-12 px-4">
          <EmptyState
            icon={<BookOpen className="w-8 h-8" />}
            title={
              searchInput.trim()
                ? `未找到包含 "${searchInput.trim()}" 的真题卷`
                : "当前分类暂无发布的真题卷"
            }
            description={
              searchInput.trim()
                ? "请尝试其他关键字（如年份 2025、2024 或科目 英语一、英语二）"
                : "管理员在后台导入并审核上架后即可在此研习"
            }
            action={
              searchInput.trim() ? (
                <Button variant="secondary" size="sm" onClick={handleClearSearch}>
                  清空搜索条件
                </Button>
              ) : undefined
            }
          />
        </Card>
      ) : viewMode === "table" ? (
        <>
          {/* Desktop (md+) Compact High-Density Table View */}
          <Card className="hidden md:block overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-surface-2/80 border-b border-border text-[11px] font-bold text-fg-subtle uppercase tracking-wider">
                  <tr>
                    <th className="py-3 px-4">真题考卷</th>
                    <th className="py-3 px-3">题量 / 时长</th>
                    <th className="py-3 px-4">精读练习进度</th>
                    <th className="py-3 px-4">限时模考档案</th>
                    <th className="py-3 px-4 text-right">研习操作</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-border/70">
                  {pagedExams.map((exam) => {
                    const draft = localState?.examDrafts?.[exam.id];
                    const qCount = exam.questions?.[0]?.count || 0;
                    const stats = getExamCardStats(exam.id, exam.total_score, qCount, localState);

                    return (
                      <tr key={exam.id} className="hover:bg-surface-2/60 transition-colors group">
                        <td className="py-3.5 px-4">
                          <div className="flex items-center gap-2.5">
                            <Badge tone="neutral" className="font-mono uppercase shrink-0">
                              {exam.category_id} · {exam.year}
                            </Badge>
                            <span className="font-bold text-fg group-hover:text-primary transition-colors truncate max-w-xs">
                              {exam.title}
                            </span>
                          </div>
                        </td>

                        <td className="py-3.5 px-3 text-fg-muted font-mono tabular-nums text-[11px] whitespace-nowrap">
                          {qCount} 题 · {exam.duration_minutes} 分钟
                        </td>

                        <td className="py-3.5 px-4">
                          {stats.hasPracticeRecord ? (
                            <div className="space-y-1.5 min-w-[168px] max-w-[220px]">
                              <div className="flex items-center justify-between gap-2 text-[11px] font-mono tabular-nums whitespace-nowrap">
                                <span className="text-fg-muted font-medium">
                                  {stats.practiceAnsweredCount}/{stats.practiceTotalQuestions} 题 (
                                  {stats.practicePercent}%)
                                </span>
                                <span className="font-bold text-primary shrink-0">
                                  正确率 {stats.practiceAccuracy}%
                                </span>
                              </div>
                              <ProgressBar value={stats.practicePercent} max={100} tone="primary" />
                            </div>
                          ) : (
                            <span className="text-[11px] text-fg-subtle">未开始</span>
                          )}
                        </td>

                        <td className="py-3.5 px-4 font-mono tabular-nums whitespace-nowrap">
                          {stats.hasExamRecord ? (
                            <div className="flex items-center gap-2">
                              <span className="font-bold text-fg text-xs">
                                {stats.examScore}{" "}
                                <span className="text-[10px] text-fg-subtle font-normal">
                                  / {stats.examTotalScore}分
                                </span>
                              </span>
                              <Badge tone={stats.examIsPassed ? "success" : "danger"} className="text-[10px]">
                                正确率 {stats.examAccuracy}%
                              </Badge>
                            </div>
                          ) : draft ? (
                            <Badge tone="warning" className="text-[11px]">
                              答题暂存中
                            </Badge>
                          ) : (
                            <span className="text-[11px] text-fg-subtle">尚未模考</span>
                          )}
                        </td>

                        <td className="py-3.5 px-4 text-right whitespace-nowrap">
                          <div className="flex items-center justify-end gap-1.5">
                            <Link
                              href={`/practice?id=${exam.id}`}
                              className="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-semibold bg-surface-2 hover:bg-border/60 text-fg border border-border transition-colors active:scale-95"
                            >
                              <BookOpen className="w-3 h-3 text-fg-muted" />
                              <span>{stats.hasPracticeRecord ? "继续精读" : "精读"}</span>
                            </Link>

                            <Link
                              href={`/exam?id=${exam.id}`}
                              className="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold bg-primary hover:opacity-95 text-primary-fg shadow-1 transition-all active:scale-95"
                            >
                              <Play className="w-3 h-3 fill-current" />
                              <span>
                                {draft ? "继续模考" : stats.hasExamRecord ? "模考复盘" : "模考"}
                              </span>
                            </Link>

                            <Link
                              href={`/exam?id=${exam.id}&mode=print`}
                              title="导出或打印标准纸质练习卷"
                              aria-label={`打印或导出 ${exam.title}`}
                              className="p-1.5 text-fg-subtle hover:text-fg hover:bg-surface-2 rounded-lg transition-colors"
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
          </Card>

          {/* Mobile (< md) Card Fallback with Full Information Hierarchy */}
          <div className="grid grid-cols-1 gap-4 md:hidden">
            {pagedExams.map((exam) => (
              <ExamCard key={exam.id} exam={exam} localState={localState} />
            ))}
          </div>
        </>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {pagedExams.map((exam) => (
            <ExamCard key={exam.id} exam={exam} localState={localState} />
          ))}
        </div>
      )}

      {/* Pagination Controls */}
      {filteredExams.length > PAGE_SIZE && (
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-border">
          <div className="text-xs text-fg-subtle font-mono tabular-nums">
            第 {safePage} / {totalPages} 页 · 每页 {PAGE_SIZE} 套 · 共 {filteredExams.length} 套试卷
          </div>

          <div className="flex items-center gap-1.5">
            <Button
              variant="secondary"
              size="sm"
              onClick={() => handlePageChange(safePage - 1)}
              disabled={safePage <= 1}
            >
              <ChevronLeft className="w-3.5 h-3.5" />
              <span>上一页</span>
            </Button>

            <div className="flex items-center gap-1">
              {Array.from({ length: totalPages }, (_, i) => i + 1)
                .filter((p) => p === 1 || p === totalPages || Math.abs(p - safePage) <= 1)
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
                      <span key={`dots-${idx}`} className="px-1 text-xs text-fg-subtle">
                        ...
                      </span>
                    );
                  }
                  const isActive = p === safePage;
                  return (
                    <button
                      key={p}
                      type="button"
                      onClick={() => handlePageChange(p)}
                      aria-current={isActive ? "page" : undefined}
                      className={`w-8 h-8 rounded-xl text-xs font-bold font-mono tabular-nums transition-colors active:scale-95 ${
                        isActive
                          ? "bg-primary text-primary-fg shadow-1"
                          : "bg-surface border border-border text-fg-muted hover:text-fg hover:bg-surface-2"
                      }`}
                    >
                      {p}
                    </button>
                  );
                })}
            </div>

            <Button
              variant="secondary"
              size="sm"
              onClick={() => handlePageChange(safePage + 1)}
              disabled={safePage >= totalPages}
            >
              <span>下一页</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

export default function HomePage() {
  return (
    <Suspense
      fallback={
        <div className="space-y-6">
          <Card className="p-6 sm:p-8 space-y-4">
            <Skeleton className="h-5 w-56" />
            <Skeleton className="h-8 w-80 max-w-full" />
            <Skeleton className="h-4 w-full max-w-xl" />
          </Card>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {[1, 2].map((i) => (
              <Card key={i} className="p-6 space-y-4">
                <Skeleton className="h-5 w-28" />
                <Skeleton className="h-6 w-3/4" />
                <Skeleton className="h-16 w-full rounded-xl" />
              </Card>
            ))}
          </div>
        </div>
      }
    >
      <ExamLobbyContent />
    </Suspense>
  );
}
