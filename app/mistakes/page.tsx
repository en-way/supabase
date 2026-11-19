"use client";

import { useState, useEffect, useMemo, useRef, useCallback } from "react";
import Link from "next/link";
import {
  getLocalState,
  subscribeLocalState,
  toggleMistakeMastered,
  removeMistake,
  reconcileLearningState,
  normalizeOptions,
  getLastReconcileTimestamp,
  setLastReconcileTimestamp,
  clearLastReconcileTimestamp,
  type MistakeItem,
} from "@/lib/storage";
import { supabase } from "@/lib/supabase";
import { fetchExamDetailWithFallback, clearStaticExamCache } from "@/lib/examLoader";
import { useBodyScrollLock } from "@/hooks/useBodyScrollLock";
import { useKeyboardGuard } from "@/hooks/useKeyboardGuard";
import type { PassageRecord, QuestionRecord, RawQuestionOptions } from "@/types/exam";
import { QuestionOptionList } from "@/components/reader/QuestionOptionList";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { EmptyState, Spinner } from "@/components/ui/Feedback";
import { Select } from "@/components/ui/Field";
import { Kbd } from "@/components/ui/Kbd";
import { PageHeader } from "@/components/ui/PageHeader";
import { SegmentedControl } from "@/components/ui/SegmentedControl";
import {
  AlertCircle,
  CheckCircle2,
  RotateCcw,
  Trash2,
  Printer,
  Download,
  BookOpen,
  SplitSquareVertical,
  ChevronLeft,
  ChevronRight,
  X,
  HelpCircle,
  Sparkles,
} from "lucide-react";

interface OnlineQuestionDetail {
  id: string;
  exam_id: string;
  passage_id?: string | null;
  category_id: string;
  q_type: string;
  stem: string;
  options: { key: string; text: string }[];
  correct_answer: string;
  explanation: string;
  points: number;
  sort_order: number;
  passages?: {
    id: string;
    title: string;
    content: string;
    section_type: string;
  } | null;
  exams?: {
    id: string;
    title: string;
    year: number;
  } | null;
}

type FallbackPassageRef = NonNullable<OnlineQuestionDetail["passages"]>;
type FallbackExamRef = NonNullable<OnlineQuestionDetail["exams"]>;

interface FallbackQuestionRow {
  id: string;
  exam_id: string | null;
  passage_id: string | null;
  category_id: string | null;
  q_type: string;
  stem: string;
  options: RawQuestionOptions;
  correct_answer: string;
  explanation: string | null;
  points: number | null;
  sort_order: number | null;
  passages: FallbackPassageRef | FallbackPassageRef[] | null;
  exams: FallbackExamRef | FallbackExamRef[] | null;
}

const unwrapRelation = <T,>(value: T | T[] | null | undefined): T | null =>
  Array.isArray(value) ? (value[0] ?? null) : (value ?? null);

const questionDetailsCache: Record<string, OnlineQuestionDetail> = {};

export default function MistakesPage() {
  const [mistakes, setMistakes] = useState<MistakeItem[]>([]);
  const [questionMap, setQuestionMap] = useState<Record<string, OnlineQuestionDetail>>({});
  const [isLoadingOnline, setIsLoadingOnline] = useState(false);
  const [activeTab, setActiveTab] = useState<"unmastered" | "mastered">("unmastered");
  const [categoryFilter, setCategoryFilter] = useState<string>("all");

  const [retestAnswers, setRetestAnswers] = useState<Record<string, string>>({});
  const [congratsId, setCongratsId] = useState<string | null>(null);
  const [toastMsg, setToastMsg] = useState<string | null>(null);
  const [isReconciling, setIsReconciling] = useState(false);

  const [sideBySideItem, setSideBySideItem] = useState<{
    mistake: MistakeItem;
    detail: OnlineQuestionDetail;
    index: number;
  } | null>(null);
  const [articleFontSize, setArticleFontSize] = useState<number>(16);
  const [printWithAnswers, setPrintWithAnswers] = useState(true);
  const [studioMobileTab, setStudioMobileTab] = useState<"passage" | "question">("question");

  const mountedRef = useRef(true);
  const fetchSeqRef = useRef(0);
  const toastTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const showToast = useCallback((msg: string) => {
    if (!mountedRef.current) return;
    if (toastTimerRef.current !== null) {
      clearTimeout(toastTimerRef.current);
    }
    setToastMsg(msg);
    toastTimerRef.current = setTimeout(() => {
      toastTimerRef.current = null;
      if (mountedRef.current) setToastMsg(null);
    }, 3500);
  }, []);

  const fetchOnlineQuestionDetails = useCallback(
    async (items: MistakeItem[], skipAutoReconcile = false) => {
      if (!items || items.length === 0) return;
      const seq = ++fetchSeqRef.current;

      const allIds = Array.from(new Set(items.map((m) => m.questionId)));
      let missingIds = allIds.filter((id) => !questionDetailsCache[id]);

      const initialMap: Record<string, OnlineQuestionDetail> = {};
      allIds.forEach((id) => {
        if (questionDetailsCache[id]) {
          initialMap[id] = questionDetailsCache[id];
        }
      });
      setQuestionMap(initialMap);

      if (missingIds.length === 0) return;

      setIsLoadingOnline(true);
      try {
        const missingItems = items.filter((m) => missingIds.includes(m.questionId));
        const examIdsToFetch = Array.from(
          new Set(missingItems.map((m) => m.examId).filter((id): id is string => Boolean(id)))
        );

        if (examIdsToFetch.length > 0) {
          const examDetails = await Promise.all(
            examIdsToFetch.map((id) => fetchExamDetailWithFallback(id))
          );
          if (!mountedRef.current || seq !== fetchSeqRef.current) return;

          examDetails.forEach((detail) => {
            if (!detail || !Array.isArray(detail.questions)) return;
            const passageMap = new Map<string, PassageRecord>(
              (detail.passages || []).map((p: PassageRecord) => [p.id, p])
            );

            detail.questions.forEach((q: QuestionRecord) => {
              if (missingIds.includes(q.id)) {
                const passage = q.passage_id ? passageMap.get(q.passage_id) || null : null;
                const detailItem: OnlineQuestionDetail = {
                  id: q.id,
                  exam_id: q.exam_id || detail.exam?.id || "",
                  passage_id: q.passage_id ?? null,
                  category_id: q.category_id || detail.exam?.category_id || "ky1",
                  q_type: q.q_type,
                  stem: q.stem,
                  options: normalizeOptions(q.options),
                  correct_answer: q.correct_answer,
                  explanation: q.explanation || "",
                  points:
                    q.points !== undefined && q.points !== null ? Number(q.points) : 2,
                  sort_order: q.sort_order || 0,
                  passages: passage,
                  exams: detail.exam,
                };
                questionDetailsCache[q.id] = detailItem;
                initialMap[q.id] = detailItem;
              }
            });
          });

          missingIds = missingIds.filter((id) => !questionDetailsCache[id]);
          setQuestionMap({ ...initialMap });
        }

        if (missingIds.length > 0) {
          const CHUNK_SIZE = 50;
          for (let i = 0; i < missingIds.length; i += CHUNK_SIZE) {
            const chunk = missingIds.slice(i, i + CHUNK_SIZE);
            const { data, error } = await supabase
              .from("questions")
              .select(
                `
                id, exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order,
                passages (id, title, content, section_type),
                exams (id, title, year)
              `
              )
              .in("id", chunk);

            if (!mountedRef.current || seq !== fetchSeqRef.current) return;
            if (!error && data) {
              (data as unknown as FallbackQuestionRow[]).forEach((q) => {
                const detail: OnlineQuestionDetail = {
                  id: q.id,
                  exam_id: q.exam_id || "",
                  passage_id: q.passage_id,
                  category_id: q.category_id || "ky1",
                  q_type: q.q_type,
                  stem: q.stem,
                  options: normalizeOptions(q.options),
                  correct_answer: q.correct_answer,
                  explanation: q.explanation || "",
                  points:
                    q.points !== undefined && q.points !== null ? Number(q.points) : 2,
                  sort_order: q.sort_order || 0,
                  passages: unwrapRelation(q.passages),
                  exams: unwrapRelation(q.exams),
                };
                questionDetailsCache[q.id] = detail;
                initialMap[q.id] = detail;
              });
            }
          }
          setQuestionMap({ ...initialMap });
        }

        if (!skipAutoReconcile) {
          const {
            data: { session },
          } = await supabase.auth.getSession();
          if (!mountedRef.current || seq !== fetchSeqRef.current) return;
          const uid = session?.user?.id || null;
          if (uid) {
            const lastRecon = getLastReconcileTimestamp(uid);
            if (Date.now() - lastRecon > 7 * 24 * 60 * 60 * 1000) {
              const recon = await reconcileLearningState();
              if (!mountedRef.current || seq !== fetchSeqRef.current) return;
              if (recon.completed) {
                setLastReconcileTimestamp(uid, Date.now());
              }
              if (recon.hasChanges) {
                setMistakes(getLocalState().mistakes);
                showToast(recon.summaryText);
              }
            }
          }
        }
      } catch (err) {
        if (mountedRef.current && seq === fetchSeqRef.current) {
          console.error("Failed to fetch questions details batch:", err);
        }
      } finally {
        if (mountedRef.current && seq === fetchSeqRef.current) {
          setIsLoadingOnline(false);
        }
      }
    },
    [showToast]
  );

  const loadLocalMistakes = useCallback(() => {
    const state = getLocalState();
    const loadedMistakes = state.mistakes || [];
    setMistakes(loadedMistakes);
    fetchOnlineQuestionDetails(loadedMistakes);
  }, [fetchOnlineQuestionDetails]);

  useEffect(() => {
    mountedRef.current = true;
    loadLocalMistakes();
    const unsubscribe = subscribeLocalState((state) => {
      if (!mountedRef.current) return;
      const nextMistakes = state.mistakes || [];
      setMistakes(nextMistakes);
      if (
        nextMistakes.some((m) => m && m.questionId && !questionDetailsCache[m.questionId])
      ) {
        fetchOnlineQuestionDetails(nextMistakes);
      }
    });
    return () => {
      mountedRef.current = false;
      unsubscribe();
      if (toastTimerRef.current !== null) {
        clearTimeout(toastTimerRef.current);
        toastTimerRef.current = null;
      }
    };
  }, [loadLocalMistakes, fetchOnlineQuestionDetails]);

  const handleManualReconcile = async () => {
    if (isReconciling) return;
    setIsReconciling(true);
    try {
      await clearStaticExamCache();
      Object.keys(questionDetailsCache).forEach((k) => delete questionDetailsCache[k]);
      const {
        data: { session },
      } = await supabase.auth.getSession();
      const uid = session?.user?.id || null;
      clearLastReconcileTimestamp(uid);
      const recon = await reconcileLearningState();
      if (!mountedRef.current) return;
      if (recon.completed && uid) {
        setLastReconcileTimestamp(uid, Date.now());
      }
      const latestMistakes = getLocalState().mistakes || [];
      setMistakes(latestMistakes);
      await fetchOnlineQuestionDetails(latestMistakes, true);
      if (!mountedRef.current) return;
      if (!recon.completed) {
        showToast(recon.summaryText || "云端核对未完成，已安全保留当前本地错题状态");
      } else {
        showToast(
          recon.hasChanges ? `核对完成：${recon.summaryText}` : "已核对完成，本地错题考点均为最新"
        );
      }
    } catch (e) {
      console.error("Manual reconcile failed:", e);
      showToast("核对网络异常，已保持当前本地错题状态");
    } finally {
      if (mountedRef.current) setIsReconciling(false);
    }
  };

  const handleToggle = (qId: string) => {
    toggleMistakeMastered(qId);
    loadLocalMistakes();
    if (sideBySideItem && sideBySideItem.mistake.questionId === qId) {
      setSideBySideItem({
        ...sideBySideItem,
        mistake: {
          ...sideBySideItem.mistake,
          isMastered: !sideBySideItem.mistake.isMastered,
        },
      });
    }
  };

  const handleDelete = (qId: string) => {
    if (window.confirm("确定将这道错题从错题本中移除吗？")) {
      removeMistake(qId);
      if (sideBySideItem && sideBySideItem.mistake.questionId === qId) {
        setSideBySideItem(null);
      }
      loadLocalMistakes();
    }
  };

  const handleRetestOption = (
    questionId: string,
    correctAnswer: string,
    optionKey: string
  ) => {
    setRetestAnswers((prev) => ({ ...prev, [questionId]: optionKey }));
    if (optionKey === correctAnswer) {
      setCongratsId(questionId);
    }
  };

  const handleConfirmMastered = (qId: string) => {
    toggleMistakeMastered(qId, true);
    setCongratsId(null);
    loadLocalMistakes();
    if (sideBySideItem && sideBySideItem.mistake.questionId === qId) {
      setSideBySideItem({
        ...sideBySideItem,
        mistake: { ...sideBySideItem.mistake, isMastered: true },
      });
    }
  };

  const filteredMistakes = useMemo(() => {
    return mistakes
      .filter((m) => (activeTab === "unmastered" ? !m.isMastered : m.isMastered))
      .filter((m) => (categoryFilter === "all" ? true : m.categoryId === categoryFilter));
  }, [mistakes, activeTab, categoryFilter]);

  const handleOpenSideBySide = (mistake: MistakeItem, index: number) => {
    const detail = questionMap[mistake.questionId];
    if (detail) {
      setSideBySideItem({ mistake, detail, index });
    } else {
      showToast("题目正在联网拉取中，请稍候点击...");
    }
  };

  const handleNavigateSideBySide = (direction: "prev" | "next") => {
    if (!sideBySideItem) return;
    if (filteredMistakes.length === 0) {
      setSideBySideItem(null);
      return;
    }
    const currentPos = filteredMistakes.findIndex(
      (m) => m.questionId === sideBySideItem.mistake.questionId
    );
    let targetIdx =
      currentPos >= 0
        ? direction === "prev"
          ? currentPos - 1
          : currentPos + 1
        : direction === "prev"
          ? sideBySideItem.index - 1
          : sideBySideItem.index;

    if (targetIdx < 0) targetIdx = filteredMistakes.length - 1;
    else if (targetIdx >= filteredMistakes.length) targetIdx = 0;

    const nextMistake = filteredMistakes[targetIdx];
    if (nextMistake) {
      const detail = questionMap[nextMistake.questionId];
      if (detail) {
        setSideBySideItem({ mistake: nextMistake, detail, index: targetIdx });
      }
    }
  };

  useKeyboardGuard((e: KeyboardEvent) => {
    if (!sideBySideItem) return;
    const key = e.key.toUpperCase();
    const validKeys =
      sideBySideItem.detail.options?.length > 0
        ? sideBySideItem.detail.options.map((o) => o.key.toUpperCase())
        : ["A", "B", "C", "D"];

    if (validKeys.includes(key)) {
      e.preventDefault();
      handleRetestOption(
        sideBySideItem.detail.id,
        sideBySideItem.detail.correct_answer,
        key
      );
    } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
      e.preventDefault();
      handleNavigateSideBySide("prev");
    } else if (e.key === "ArrowRight" || e.key === "ArrowDown") {
      e.preventDefault();
      handleNavigateSideBySide("next");
    } else if (e.key === "Escape") {
      e.preventDefault();
      setSideBySideItem(null);
    }
  }, Boolean(sideBySideItem));

  useBodyScrollLock(Boolean(sideBySideItem));

  const handleExportTxt = () => {
    if (filteredMistakes.length === 0) {
      showToast("当前列表暂无错题可导出");
      return;
    }

    let textContent = `===============================\n`;
    textContent += `Enway 英语智能错题练习集 (${new Date().toLocaleDateString()})\n`;
    textContent += `总计错题: ${filteredMistakes.length} 道\n`;
    textContent += `===============================\n\n`;

    filteredMistakes.forEach((item, idx) => {
      const detail = questionMap[item.questionId];
      const stemText = detail?.stem || item.stem || "（题目加载中）";
      const opts = detail?.options || item.options || [];
      const corr = detail?.correct_answer || item.correctAnswer || "详见系统";
      const expl = detail?.explanation || item.explanation || "详见系统";

      textContent += `【第 ${idx + 1} 题】(错误次数: ${item.wrongCount})\n`;
      if (detail?.exams?.title) textContent += `[所属试卷]: ${detail.exams.title}\n`;
      if (detail?.passages?.content) {
        textContent += `[篇章材料]:\n${detail.passages.content}\n\n`;
      }
      textContent += `${stemText}\n\n`;
      opts.forEach((opt) => {
        textContent += `  ${opt.key}. ${opt.text}\n`;
      });
      textContent += `\n[正确答案]: ${corr}\n`;
      textContent += `[上次选错]: ${item.wrongAnswer}\n`;
      textContent += `[考点解析]: ${expl}\n`;
      textContent += `--------------------------------------------------\n\n`;
    });

    const blob = new Blob([textContent], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `Enway_真题错题研习集_${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const unmasteredCount = mistakes.filter((m) => !m.isMastered).length;
  const masteredCount = mistakes.filter((m) => m.isMastered).length;

  return (
    <div className="space-y-6">
      {toastMsg && (
        <div className="fixed top-20 right-6 z-toast p-3.5 bg-fg text-bg rounded-2xl shadow-pop border border-border flex items-center gap-2.5 text-xs font-semibold animate-in fade-in slide-in-from-top-4 duration-200">
          <Sparkles className="w-4 h-4 text-warning shrink-0" />
          <span>{toastMsg}</span>
        </div>
      )}

      <PageHeader
        icon={<AlertCircle className="w-5 h-5 text-warning" />}
        title="历年真题错题研习库"
        description="单项错题定向回溯文章 · 支持“边看边写”双栏研习 · 自动校准云端考题"
        badge={
          isLoadingOnline ? (
            <Badge tone="neutral">
              <Spinner className="w-3 h-3" />
              <span>拉取篇章与考题...</span>
            </Badge>
          ) : undefined
        }
        actions={
          <div className="flex flex-wrap items-center gap-2">
            <Button
              variant="secondary"
              size="sm"
              onClick={handleManualReconcile}
              disabled={isReconciling}
              title="强制刷新考卷缓存并校验本地错题最新考点"
            >
              <RotateCcw
                className={`w-3.5 h-3.5 ${isReconciling ? "animate-spin" : ""}`}
              />
              <span>{isReconciling ? "核对中..." : "核对考点"}</span>
            </Button>
            <Button variant="secondary" size="sm" onClick={handleExportTxt}>
              <Download className="w-3.5 h-3.5" />
              <span>导出 TXT</span>
            </Button>
            <Button size="sm" onClick={() => window.print()}>
              <Printer className="w-3.5 h-3.5" />
              <span>打印 / 导出 PDF</span>
            </Button>
          </div>
        }
      />

      {/* Filter Tabs & Category Filter */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-border pb-3 no-print">
        <SegmentedControl
          value={activeTab}
          onChange={setActiveTab}
          size="sm"
          options={[
            { value: "unmastered", label: `待复习 (${unmasteredCount})` },
            { value: "mastered", label: `已掌握归档 (${masteredCount})` },
          ]}
        />

        <div className="flex flex-wrap items-center gap-3 text-xs text-fg-muted">
          <div className="flex items-center gap-1.5 shrink-0">
            <span className="text-fg-subtle whitespace-nowrap shrink-0">分类：</span>
            <Select
              compact
              value={categoryFilter}
              onChange={(e) => setCategoryFilter(e.target.value)}
              className="h-8 text-xs w-auto min-w-[140px]"
            >
              <option value="all">全部分类</option>
              <option value="ky1">考研英语一 (KY-1)</option>
              <option value="ky2">考研英语二 (KY-2)</option>
            </Select>
          </div>

          <div className="flex items-center gap-1.5 shrink-0">
            <span className="text-fg-subtle whitespace-nowrap shrink-0">打印视图：</span>
            <Button
              variant={printWithAnswers ? "secondary" : "ghost"}
              size="sm"
              onClick={() => setPrintWithAnswers(!printWithAnswers)}
              className="h-8 text-xs border border-border whitespace-nowrap"
            >
              {printWithAnswers ? "含答案与解析" : "仅题目（做题卷）"}
            </Button>
          </div>
        </div>
      </div>

      {/* Printable Heading */}
      <div className="hidden print-only text-center mb-6">
        <h1 className="text-2xl font-black mb-1">Enway 英语重点错题复习卷</h1>
        <p className="text-xs text-fg-muted">
          打印时间：{new Date().toLocaleDateString()} · 共 {filteredMistakes.length} 道错题
        </p>
      </div>

      {/* Mistakes List */}
      {filteredMistakes.length === 0 ? (
        <Card className="py-12 px-4 no-print">
          <EmptyState
            icon={<CheckCircle2 className="w-8 h-8 text-success" />}
            title="太棒了！当前分类下没有待复习错题"
            description="前往真题大厅刷题或切换其他分类继续巩固。"
            action={
              <Link
                href="/"
                className="inline-flex px-4 py-2 bg-primary text-primary-fg text-xs font-bold rounded-xl"
              >
                前往试卷大厅刷题
              </Link>
            }
          />
        </Card>
      ) : (
        <div className="space-y-4">
          {filteredMistakes.map((item, idx) => {
            const detail = questionMap[item.questionId];
            const retestAns = retestAnswers[item.questionId];
            const isRetested = Boolean(retestAns);
            const corrAnswer = detail?.correct_answer || item.correctAnswer || "";
            const isShowCongrats = congratsId === item.questionId;
            const hasPassage = Boolean(detail?.passages?.content);

            const options = normalizeOptions(detail?.options || item.options || []);
            const stem = detail?.stem || item.stem || "（题目正在加载中...）";
            const explanation =
              detail?.explanation || item.explanation || "（解析加载中...）";

            return (
              <Card key={item.questionId} className="p-5 sm:p-6 print-card space-y-4">
                <div className="flex items-center justify-between flex-wrap gap-2">
                  <div className="flex items-center flex-wrap gap-2">
                    <Badge tone="neutral" className="font-mono font-bold">
                      错题 #{idx + 1}
                    </Badge>
                    {detail?.exams?.title && (
                      <Badge tone="neutral">{detail.exams.title}</Badge>
                    )}
                    <Badge tone="danger">做错 {item.wrongCount} 次</Badge>
                    <span className="text-xs text-fg-subtle">
                      上次选错：
                      <strong className="text-danger font-mono">{item.wrongAnswer}</strong>
                    </span>
                  </div>

                  <div className="flex items-center gap-2 no-print">
                    {hasPassage && (
                      <Button
                        variant="secondary"
                        size="sm"
                        onClick={() => handleOpenSideBySide(item, idx)}
                        title="打开双栏对照窗口，边读文章边写题"
                      >
                        <SplitSquareVertical className="w-3.5 h-3.5 text-primary" />
                        <span>边看边写</span>
                      </Button>
                    )}

                    <Button
                      variant={item.isMastered ? "secondary" : "primary"}
                      size="sm"
                      onClick={() => handleToggle(item.questionId)}
                    >
                      {item.isMastered ? "撤销已掌握" : "标记已掌握"}
                    </Button>

                    <button
                      type="button"
                      onClick={() => handleDelete(item.questionId)}
                      title="彻底删除"
                      aria-label="彻底删除该错题"
                      className="p-1.5 text-fg-subtle hover:text-danger rounded-lg hover:bg-danger-soft transition-colors"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>

                {detail?.passages?.content && (
                  <div className="hidden print-only p-4 rounded-xl bg-surface-2 border border-border text-xs leading-relaxed space-y-2">
                    <h4 className="font-bold text-fg">{detail.passages.title}</h4>
                    <p className="whitespace-pre-line text-fg-muted">
                      {detail.passages.content}
                    </p>
                  </div>
                )}

                <h3 className="text-base font-bold text-fg leading-relaxed">{stem}</h3>

                <QuestionOptionList
                  options={options}
                  selectedAnswer={retestAns}
                  correctAnswer={corrAnswer}
                  showResult={isRetested}
                  onSelect={(key) => handleRetestOption(item.questionId, corrAnswer, key)}
                />

                {isShowCongrats && (
                  <div className="p-3 bg-success-soft border border-success/30 rounded-xl flex items-center justify-between text-xs text-fg animate-in fade-in duration-150 no-print">
                    <span className="font-bold">
                      重做答对了！该题已攻克，是否移入“已掌握”？
                    </span>
                    <Button
                      size="sm"
                      onClick={() => handleConfirmMastered(item.questionId)}
                    >
                      移入已掌握
                    </Button>
                  </div>
                )}

                {(printWithAnswers || isRetested) && (
                  <div
                    className={`p-4 rounded-xl bg-surface-2/80 border border-border text-xs space-y-1.5 ${
                      !printWithAnswers ? "no-print" : ""
                    }`}
                  >
                    <div className="flex items-center gap-2 font-bold text-primary">
                      <HelpCircle className="w-3.5 h-3.5" />
                      <span>正确答案：{corrAnswer} · 考点精析</span>
                    </div>
                    <p className="text-fg-muted leading-relaxed whitespace-pre-line">
                      {explanation}
                    </p>
                  </div>
                )}
              </Card>
            );
          })}
        </div>
      )}

      {/* Side-by-Side Dual-Pane Review Studio Modal */}
      {sideBySideItem && (
        <div
          className="fixed inset-0 z-modal bg-overlay/60 backdrop-blur-sm flex items-center justify-center p-2 sm:p-4 animate-in fade-in duration-150"
          role="dialog"
          aria-modal="true"
          aria-label="边看边写错题精研工作台"
        >
          <div className="bg-surface w-full max-w-[96vw] xl:max-w-7xl h-[95dvh] rounded-3xl shadow-pop flex flex-col overflow-hidden border border-border">
            <div className="px-4 sm:px-6 py-3.5 bg-surface-2 border-b border-border flex items-center justify-between shrink-0 gap-3">
              <div className="flex items-center gap-3 min-w-0">
                <div className="w-8 h-8 rounded-lg bg-warning-soft text-warning border border-warning/30 flex items-center justify-center shrink-0">
                  <BookOpen className="w-4 h-4" />
                </div>
                <div className="min-w-0">
                  <h2 className="text-sm font-bold text-fg flex items-center gap-2">
                    <span>边看边写 · 错题精研工作台</span>
                    <Badge tone="primary" className="font-mono">
                      第 {sideBySideItem.index + 1} / {filteredMistakes.length} 题
                    </Badge>
                  </h2>
                  <p className="text-xs text-fg-muted truncate max-w-md">
                    {sideBySideItem.detail.exams?.title || "历年真题研习"}
                  </p>
                </div>
              </div>

              <div className="hidden md:flex items-center gap-2 text-[11px] text-fg-muted bg-surface px-3 py-1.5 rounded-xl border border-border">
                <span className="text-primary font-semibold">快捷键：</span>
                <span className="flex items-center gap-1">
                  <Kbd>A</Kbd>–<Kbd>D</Kbd> 作答
                </span>
                <span className="text-border">|</span>
                <span className="flex items-center gap-1">
                  <Kbd>←</Kbd> <Kbd>→</Kbd> 切题
                </span>
                <span className="text-border">|</span>
                <span className="flex items-center gap-1">
                  <Kbd>Esc</Kbd> 退出
                </span>
              </div>

              <div className="flex items-center gap-2 shrink-0">
                <div className="flex items-center gap-1 bg-surface p-1 rounded-xl border border-border">
                  <button
                    type="button"
                    onClick={() => handleNavigateSideBySide("prev")}
                    disabled={sideBySideItem.index <= 0}
                    className="px-2 py-1 text-fg-muted hover:text-fg disabled:opacity-40 rounded-lg hover:bg-surface-2 transition-colors text-xs flex items-center gap-1"
                    title="上一题 (←)"
                  >
                    <ChevronLeft className="w-4 h-4" />
                    <span className="hidden sm:inline">上一题</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => handleNavigateSideBySide("next")}
                    disabled={sideBySideItem.index >= filteredMistakes.length - 1}
                    className="px-2 py-1 text-fg-muted hover:text-fg disabled:opacity-40 rounded-lg hover:bg-surface-2 transition-colors text-xs flex items-center gap-1"
                    title="下一题 (→)"
                  >
                    <span className="hidden sm:inline">下一题</span>
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>

                <button
                  type="button"
                  onClick={() => setSideBySideItem(null)}
                  className="p-2 text-fg-muted hover:text-fg rounded-xl hover:bg-surface transition-colors"
                  title="关闭 (Esc)"
                  aria-label="关闭工作台"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {sideBySideItem.detail.passages?.content && (
              <div className="lg:hidden flex items-center bg-surface-2 p-1 border-b border-border shrink-0">
                <button
                  type="button"
                  onClick={() => setStudioMobileTab("passage")}
                  className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
                    studioMobileTab === "passage"
                      ? "bg-surface text-primary shadow-1"
                      : "text-fg-muted"
                  }`}
                >
                  <BookOpen className="w-3.5 h-3.5" />
                  <span>阅读篇章原文</span>
                </button>
                <button
                  type="button"
                  onClick={() => setStudioMobileTab("question")}
                  className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
                    studioMobileTab === "question"
                      ? "bg-surface text-primary shadow-1"
                      : "text-fg-muted"
                  }`}
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>错题重做与精析</span>
                </button>
              </div>
            )}

            <div className="flex-1 flex flex-col lg:flex-row overflow-hidden">
              {sideBySideItem.detail.passages?.content ? (
                <div
                  className={`${
                    studioMobileTab === "passage" ? "flex" : "hidden"
                  } lg:flex lg:w-[55%] border-r border-border flex-col bg-bg h-full overflow-hidden`}
                >
                  <div className="px-5 py-3 border-b border-border bg-surface-2/80 flex items-center justify-between shrink-0">
                    <div className="flex items-center gap-2 min-w-0">
                      <BookOpen className="w-4 h-4 text-primary shrink-0" />
                      <span className="text-xs font-bold text-fg tracking-wide truncate">
                        {sideBySideItem.detail.passages.title || "阅读篇章原文"}
                      </span>
                    </div>
                    <div className="flex items-center gap-1.5 text-xs text-fg-muted shrink-0">
                      <span className="text-[11px] text-fg-subtle">字号：</span>
                      <button
                        type="button"
                        onClick={() =>
                          setArticleFontSize((prev) => Math.max(14, prev - 1))
                        }
                        className="px-2 py-0.5 border border-border rounded bg-surface hover:bg-surface-2 text-fg font-bold text-xs"
                        title="缩小文字"
                      >
                        A-
                      </button>
                      <span className="font-mono tabular-nums text-xs w-8 text-center text-fg">
                        {articleFontSize}px
                      </span>
                      <button
                        type="button"
                        onClick={() =>
                          setArticleFontSize((prev) => Math.min(22, prev + 1))
                        }
                        className="px-2 py-0.5 border border-border rounded bg-surface hover:bg-surface-2 text-fg font-bold text-xs"
                        title="放大文字"
                      >
                        A+
                      </button>
                    </div>
                  </div>

                  <div className="flex-1 p-6 sm:p-8 overflow-y-auto overscroll-contain select-text">
                    <div
                      style={{ fontSize: `${articleFontSize}px` }}
                      className="reading-prose whitespace-pre-line space-y-4 text-fg"
                    >
                      {sideBySideItem.detail.passages.content}
                    </div>
                    <div className="mt-8 pt-4 border-t border-border text-xs text-fg-subtle flex items-center gap-2">
                      <Sparkles className="w-3.5 h-3.5 text-primary" />
                      <span>
                        提示：双击文中任意生词，即可唤醒离线词典查词并收录至生词本。
                      </span>
                    </div>
                  </div>

                  <div className="lg:hidden p-3 border-t border-border bg-surface-2 flex justify-end shrink-0">
                    <Button size="sm" onClick={() => setStudioMobileTab("question")}>
                      前往作答与查看精析 &rarr;
                    </Button>
                  </div>
                </div>
              ) : (
                <div className="hidden lg:flex lg:w-[55%] border-r border-border bg-bg p-8 flex-col items-center justify-center text-center">
                  <div className="w-14 h-14 rounded-2xl bg-warning-soft border border-warning/30 flex items-center justify-center text-warning mb-3 font-reading text-2xl font-bold">
                    §
                  </div>
                  <p className="text-sm font-bold text-fg">独立单项题研习</p>
                  <p className="text-xs text-fg-muted mt-1.5 max-w-sm">
                    本题无需对照篇章材料，请在右侧研析题干、重新作答或查看考点精析。
                  </p>
                </div>
              )}

              <div
                className={`${
                  studioMobileTab === "question" ||
                  !sideBySideItem.detail.passages?.content
                    ? "flex"
                    : "hidden"
                } lg:flex flex-1 lg:w-[45%] flex-col bg-surface h-full overflow-hidden`}
              >
                <div className="px-6 py-3 border-b border-border flex items-center justify-between shrink-0 bg-surface-2/60">
                  <div className="flex items-center gap-2">
                    <Badge tone="danger">
                      做错 {sideBySideItem.mistake.wrongCount} 次
                    </Badge>
                    <span className="text-xs text-fg-muted">
                      上次选错：
                      <strong className="text-danger font-mono">
                        {sideBySideItem.mistake.wrongAnswer}
                      </strong>
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    {sideBySideItem.detail.passages?.content && (
                      <Button
                        variant="secondary"
                        size="sm"
                        onClick={() => setStudioMobileTab("passage")}
                        className="lg:hidden"
                      >
                        <BookOpen className="w-3 h-3" />
                        <span>看原文</span>
                      </Button>
                    )}

                    <Button
                      variant={sideBySideItem.mistake.isMastered ? "secondary" : "primary"}
                      size="sm"
                      onClick={() => handleToggle(sideBySideItem.mistake.questionId)}
                    >
                      {sideBySideItem.mistake.isMastered ? "撤销已掌握" : "标为已掌握"}
                    </Button>
                  </div>
                </div>

                <div className="flex-1 p-6 overflow-y-auto overscroll-contain space-y-6">
                  <h3 className="text-base sm:text-lg font-bold text-fg leading-relaxed font-reading">
                    {sideBySideItem.detail.stem}
                  </h3>

                  <QuestionOptionList
                    options={normalizeOptions(sideBySideItem.detail.options)}
                    selectedAnswer={retestAnswers[sideBySideItem.detail.id]}
                    correctAnswer={sideBySideItem.detail.correct_answer}
                    showResult={Boolean(retestAnswers[sideBySideItem.detail.id])}
                    onSelect={(key) =>
                      handleRetestOption(
                        sideBySideItem.detail.id,
                        sideBySideItem.detail.correct_answer,
                        key
                      )
                    }
                  />

                  {congratsId === sideBySideItem.detail.id && (
                    <div className="p-4 bg-success-soft border border-success/30 rounded-2xl flex items-center justify-between text-xs text-fg animate-in fade-in duration-150">
                      <div className="flex items-center gap-2">
                        <CheckCircle2 className="w-5 h-5 text-success shrink-0" />
                        <span className="font-bold">
                          恭喜！重做答对，该考点已被攻克！
                        </span>
                      </div>
                      <Button
                        size="sm"
                        onClick={() => handleConfirmMastered(sideBySideItem.detail.id)}
                      >
                        移入已掌握
                      </Button>
                    </div>
                  )}

                  {(Boolean(retestAnswers[sideBySideItem.detail.id]) ||
                    sideBySideItem.mistake.isMastered) && (
                    <div className="p-5 rounded-2xl bg-surface-2/80 border border-border text-xs space-y-2">
                      <div className="flex items-center gap-2 font-bold text-primary">
                        <HelpCircle className="w-4 h-4" />
                        <span>
                          考点精析 · 正确答案：{sideBySideItem.detail.correct_answer}
                        </span>
                      </div>
                      <p className="text-fg-muted leading-relaxed whitespace-pre-line text-sm">
                        {sideBySideItem.detail.explanation}
                      </p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
