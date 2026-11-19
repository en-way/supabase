"use client";

import { Suspense } from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import { useSearchParams } from "next/navigation";
import { normalizeOptions } from "@/lib/storage";
import { useExamSession, formatExamTimer } from "@/hooks/useExamSession";
import { useReaderPrefs } from "@/hooks/useReaderPrefs";
import SplitPane from "@/components/SplitPane";
import { PassageReaderPane } from "@/components/reader/PassageReaderPane";
import { QuestionOptionList } from "@/components/reader/QuestionOptionList";
import { AnswerSheetSections } from "@/components/reader/AnswerSheetSections";
import { ZenFloatingBar } from "@/components/reader/ZenFloatingBar";
import { ExamTopBar } from "@/components/exam/ExamTopBar";
import ExamResultSummary from "@/components/exam/ExamResultSummary";
import { TimeUpLockBanner } from "@/components/exam/TimeUpLockBanner";
import { ExamAnswerSheetDrawer } from "@/components/exam/ExamAnswerSheetDrawer";
import { ExamSubmitReviewSheet } from "@/components/exam/ExamSubmitReviewSheet";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Spinner } from "@/components/ui/Feedback";
import { Kbd } from "@/components/ui/Kbd";
import {
  BookOpen,
  CheckCircle2,
  FileText,
  HelpCircle,
  Keyboard,
  ListOrdered,
  Send,
  XCircle,
} from "lucide-react";

const KeyboardShortcutsModal = dynamic(
  () => import("@/components/KeyboardShortcutsModal"),
  { ssr: false }
);

const ExamPrintBar = dynamic(() => import("@/components/exam/ExamPrintBar"), {
  ssr: false,
});

function ExamContent() {
  const searchParams = useSearchParams();
  const examId = searchParams.get("id");
  const modeParam = searchParams.get("mode");

  const { fontSize, lineHeight, updateFontSize, cycleLineHeight } =
    useReaderPrefs();
  const session = useExamSession(examId, modeParam);

  const {
    exam,
    passages,
    questions,
    loading,
    isPrintMode,
    answers,
    remainingSeconds,
    isTimeUp,
    isSubmitted,
    reportOnlyMode,
    setReportOnlyMode,
    result,
    activePassageId,
    setActivePassageId,
    showPrintAnswers,
    setShowPrintAnswers,
    focusedIndex,
    setFocusedIndex,
    mobileTab,
    setMobileTab,
    showMobileAnswerSheet,
    setShowMobileAnswerSheet,
    showSubmitReviewSheet,
    setShowSubmitReviewSheet,
    isZenMode,
    setIsZenMode,
    showShortcutsModal,
    setShowShortcutsModal,
    questionRefs,
    passageContainerRef,
    handleSelectAnswer,
    handleSubmit,
    executeSubmit,
    handleRetake,
    handleBlankClick,
    scrollToFirstUnanswered,
    jumpToQuestionIndex,
  } = session;

  if (loading) {
    return (
      <div className="py-24 flex flex-col items-center justify-center gap-3 text-fg-muted">
        <Spinner className="w-8 h-8" />
        <p className="font-semibold text-sm">正在加载全真考卷数据与答题卡...</p>
      </div>
    );
  }

  if (!exam) {
    return (
      <Card className="py-16 text-center space-y-4">
        <p className="text-danger font-bold">考卷不存在或已被下架</p>
        <Link
          href="/"
          className="inline-flex items-center justify-center px-4 py-2 rounded-xl bg-primary text-primary-fg text-sm font-semibold"
        >
          返回真题大厅
        </Link>
      </Card>
    );
  }

  const answeredCount = Object.keys(answers).length;
  const totalExamQuestions = questions.length;
  const examCorrectCount =
    isSubmitted && result?.answers
      ? Object.values(result.answers).filter((a) => a?.isCorrect).length
      : 0;
  const examAccuracy =
    totalExamQuestions > 0 && isSubmitted
      ? Math.round((examCorrectCount / totalExamQuestions) * 100)
      : 0;

  const unansweredQuestions = questions
    .map((q, idx) => ({ id: q.id, num: idx + 1, idx }))
    .filter((item) => !answers[item.id]);

  const leftPane = (
    <PassageReaderPane
      passages={passages}
      activePassageId={activePassageId}
      onSelectPassage={setActivePassageId}
      questions={questions}
      answers={answers}
      focusedIndex={focusedIndex}
      onBlankClick={handleBlankClick}
      isSubmitted={isSubmitted}
      isPrintMode={isPrintMode}
      visibleOnMobile={mobileTab === "passage" || isSubmitted || isPrintMode}
      onReturnToQuestions={() => setMobileTab("questions")}
      returnLabel={`返回答卷 (${answeredCount}/${questions.length})`}
      fontSize={fontSize}
      lineHeight={lineHeight}
      onUpdateFontSize={updateFontSize}
      onCycleLineHeight={cycleLineHeight}
      containerRef={passageContainerRef}
    />
  );

  const rightPane = (
    <div
      className={`${
        mobileTab === "questions" || isSubmitted || isPrintMode ? "block" : "hidden"
      } lg:block w-full space-y-6 pb-28 lg:pb-0`}
    >
      {questions.map((q, idx) => {
        const userAns = answers[q.id];
        const isQAnswered = Boolean(userAns);
        const isQCorrect = userAns === q.correct_answer;
        const isFocused = idx === focusedIndex;
        const options = normalizeOptions(q.options);

        return (
          <div
            key={q.id}
            ref={(el) => {
              questionRefs.current[q.id] = el;
            }}
          >
            <Card
              onClick={() => setFocusedIndex(idx)}
              className={`p-5 sm:p-6 transition-all duration-150 print-card cursor-pointer ${
                isSubmitted
                  ? isQCorrect
                    ? "border-success/40 bg-success-soft/30"
                    : "border-danger/40 bg-danger-soft/30"
                  : isFocused
                    ? "border-primary ring-1 ring-primary"
                    : isQAnswered
                      ? "bg-surface-2/40"
                      : "hover:border-primary/40"
              }`}
            >
            <div className="flex items-center justify-between gap-2 mb-3.5">
              <div className="flex items-center gap-2">
                <span
                  className={`w-6 h-6 rounded-lg text-xs font-bold font-mono tabular-nums flex items-center justify-center ${
                    isFocused
                      ? "bg-primary text-primary-fg"
                      : "bg-surface-2 text-fg-muted"
                  }`}
                >
                  {idx + 1}
                </span>
                <span className="text-xs text-fg-subtle font-medium">
                  分值：{q.points} 分
                </span>
                {isFocused && (
                  <Badge tone="primary" className="text-[10px] font-mono">
                    当前答题
                  </Badge>
                )}
              </div>

              {q.passage_id && passages.length > 0 && !isSubmitted && (
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    if (q.passage_id) setActivePassageId(q.passage_id);
                    setMobileTab("passage");
                  }}
                  className="lg:hidden text-[11px] font-semibold text-primary bg-primary-soft border border-primary/25 px-2 py-0.5 rounded-md flex items-center gap-1 active:scale-95"
                >
                  <BookOpen className="w-3 h-3" />
                  <span>查阅篇章</span>
                </button>
              )}

              {isSubmitted && (
                <div className="flex items-center gap-1.5 text-xs font-bold no-print">
                  {isQCorrect ? (
                    <span className="text-success flex items-center gap-1">
                      <CheckCircle2 className="w-3.5 h-3.5" />
                      <span>正确 (+{q.points}分)</span>
                    </span>
                  ) : (
                    <span className="text-danger flex items-center gap-1">
                      <XCircle className="w-3.5 h-3.5" />
                      <span>选错 (正确: {q.correct_answer})</span>
                    </span>
                  )}
                </div>
              )}
            </div>

            <h4 className="text-sm sm:text-base font-bold text-fg mb-4 leading-relaxed">
              {q.stem}
            </h4>

            <QuestionOptionList
              options={options}
              selectedAnswer={userAns}
              correctAnswer={q.correct_answer}
              showResult={isSubmitted}
              disabled={isSubmitted || isTimeUp || isPrintMode}
              onSelect={(key) => {
                setFocusedIndex(idx);
                handleSelectAnswer(q.id, key);
              }}
            />

            {((isSubmitted && q.explanation) ||
              (isPrintMode &&
                showPrintAnswers &&
                (q.explanation || q.correct_answer))) && (
              <div
                className={`mt-4 p-4 rounded-xl bg-surface-2/80 border border-border text-xs text-fg space-y-1 ${
                  isPrintMode && showPrintAnswers ? "" : "no-print"
                }`}
              >
                <div className="flex items-center gap-1.5 font-bold text-fg">
                  <HelpCircle className="w-3.5 h-3.5 text-primary" />
                  <span>考点精析 · 正确答案：{q.correct_answer}</span>
                </div>
                {q.explanation && (
                  <p className="text-fg-muted leading-relaxed whitespace-pre-line pt-1">
                    {q.explanation}
                  </p>
                )}
              </div>
            )}
            </Card>
          </div>
        );
      })}

      {/* Inline Answer Sheet Overview */}
      <Card className="p-5 sm:p-6 space-y-5 no-print">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-border text-xs">
          <div>
            <span className="font-bold text-sm text-fg">
              答题卡总览 ({answeredCount} / {questions.length})
            </span>
            <span className="text-fg-subtle ml-2">点击题号快速定位到对应试题</span>
          </div>
          {!isSubmitted && answeredCount < questions.length && (
            <Button
              variant="secondary"
              size="sm"
              onClick={scrollToFirstUnanswered}
              className="self-start sm:self-auto"
            >
              定位首道未答题
            </Button>
          )}
        </div>

        <AnswerSheetSections
          questions={questions}
          answers={answers}
          activeIndex={focusedIndex}
          showCorrectness={isSubmitted}
          onJump={(idx) => jumpToQuestionIndex(idx, false)}
          buttonSize="compact"
        />
      </Card>
    </div>
  );

  return (
    <div className="space-y-6 pb-20 animate-in fade-in duration-200">
      {isZenMode && !isPrintMode ? (
        <ZenFloatingBar
          modeLabel="专注考场"
          title={exam.title}
          metaText={`${formatExamTimer(remainingSeconds)} · 已答 ${answeredCount}/${questions.length} 题`}
          onOpenAnswerSheet={() => setShowMobileAnswerSheet(true)}
          answerSheetLabel={`${answeredCount}/${questions.length}`}
          disableAnswerSheet={isTimeUp}
          onOpenShortcuts={() => setShowShortcutsModal(true)}
          onExitZen={() => setIsZenMode(false)}
        />
      ) : (
        <ExamTopBar
          exam={exam}
          isPrintMode={isPrintMode}
          isSubmitted={isSubmitted}
          isTimeUp={isTimeUp}
          result={result}
          examAccuracy={examAccuracy}
          answeredCount={answeredCount}
          totalQuestions={totalExamQuestions}
          remainingSeconds={remainingSeconds}
          isZenMode={isZenMode}
          onToggleZen={() => setIsZenMode((p) => !p)}
          onOpenShortcuts={() => setShowShortcutsModal(true)}
          onOpenAnswerSheet={() => setShowMobileAnswerSheet(true)}
          onRequestSubmit={() => handleSubmit(false)}
          onRetake={handleRetake}
        />
      )}

      <TimeUpLockBanner visible={isTimeUp && !isSubmitted && !isPrintMode} />

      {isPrintMode && (
        <ExamPrintBar
          exam={exam}
          showPrintAnswers={showPrintAnswers}
          onTogglePrintAnswers={setShowPrintAnswers}
        />
      )}

      {isSubmitted && result && reportOnlyMode && !isPrintMode ? (
        <ExamResultSummary
          standalone
          exam={exam}
          result={result}
          questions={questions}
          totalQuestions={questions.length}
          onEnterReview={() => {
            setReportOnlyMode(false);
            window.scrollTo({ top: 0, behavior: "smooth" });
          }}
          onRetake={handleRetake}
        />
      ) : (
        <>
          {isSubmitted && result && (
            <ExamResultSummary
              exam={exam}
              result={result}
              questions={questions}
              totalQuestions={questions.length}
            />
          )}

          {!isSubmitted && !isPrintMode && (
            <div className="hidden lg:flex items-center justify-between px-3.5 py-2 bg-surface-2/80 border border-border rounded-xl text-xs text-fg-muted no-print">
              <div className="flex items-center gap-2">
                <Keyboard className="w-3.5 h-3.5 text-fg-subtle" />
                <span className="font-semibold text-fg">键盘快捷键：</span>
                <span className="flex items-center gap-1">
                  键入 <Kbd>A</Kbd> <Kbd>B</Kbd> <Kbd>C</Kbd> <Kbd>D</Kbd> 瞬选答案，方向键{" "}
                  <Kbd>←</Kbd> <Kbd>→</Kbd> 切题
                </span>
              </div>
              <span className="text-[11px] text-fg-subtle font-mono tabular-nums">
                当前聚焦：第 {focusedIndex + 1} 题
              </span>
            </div>
          )}

          {passages.length > 0 && !isSubmitted && !isPrintMode && (
            <div className="lg:hidden sticky top-[4.5rem] z-sticky flex items-center bg-surface-2/95 backdrop-blur-md p-1 rounded-xl border border-border shadow-1 no-print">
              <button
                type="button"
                onClick={() => setMobileTab("passage")}
                className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
                  mobileTab === "passage"
                    ? "bg-surface text-primary shadow-1"
                    : "text-fg-muted"
                }`}
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>阅读材料 ({passages.length})</span>
              </button>
              <button
                type="button"
                onClick={() => setMobileTab("questions")}
                className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
                  mobileTab === "questions"
                    ? "bg-surface text-primary shadow-1"
                    : "text-fg-muted"
                }`}
              >
                <FileText className="w-3.5 h-3.5" />
                <span>
                  试卷作答 ({answeredCount}/{questions.length})
                </span>
              </button>
            </div>
          )}

          {isPrintMode ? (
            <div className="max-w-4xl mx-auto space-y-8">
              {leftPane}
              {rightPane}
            </div>
          ) : passages.length > 0 ? (
            <SplitPane
              storageKey="enway_split_ratio_exam"
              defaultRatio={55}
              isZenMode={isZenMode}
              leftPane={leftPane}
              rightPane={rightPane}
            />
          ) : (
            <div className="max-w-3xl mx-auto">{rightPane}</div>
          )}

          {!isSubmitted && !isPrintMode && (
            <div className="lg:hidden fixed bottom-0 left-0 right-0 z-nav bg-surface/95 backdrop-blur-xl border-t border-border px-4 py-2.5 pb-[max(0.75rem,env(safe-area-inset-bottom))] shadow-2 flex items-center justify-between gap-3 no-print">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => setShowMobileAnswerSheet(true)}
                disabled={isTimeUp}
              >
                <ListOrdered className="w-4 h-4 text-primary" />
                <span className="font-mono tabular-nums">
                  答题卡 ({answeredCount}/{questions.length})
                </span>
              </Button>

              <div className="flex items-center gap-2">
                {passages.length > 0 && (
                  <Button
                    variant="secondary"
                    size="sm"
                    onClick={() =>
                      setMobileTab(mobileTab === "questions" ? "passage" : "questions")
                    }
                  >
                    <BookOpen className="w-3.5 h-3.5" />
                    <span>{mobileTab === "questions" ? "看原文" : "看试题"}</span>
                  </Button>
                )}

                <Button
                  size="sm"
                  onClick={() => handleSubmit(false)}
                  disabled={isTimeUp}
                >
                  <Send className="w-3.5 h-3.5" />
                  <span>{isTimeUp ? "交卷中" : "交卷"}</span>
                </Button>
              </div>
            </div>
          )}
        </>
      )}

      <ExamAnswerSheetDrawer
        open={showMobileAnswerSheet}
        onClose={() => setShowMobileAnswerSheet(false)}
        questions={questions}
        answers={answers}
        focusedIndex={focusedIndex}
        isSubmitted={isSubmitted}
        isTimeUp={isTimeUp}
        answeredCount={answeredCount}
        onJump={(idx) => jumpToQuestionIndex(idx, true)}
        onScrollToFirstUnanswered={scrollToFirstUnanswered}
        onSubmitNow={() => {
          setShowMobileAnswerSheet(false);
          handleSubmit(false);
        }}
      />

      <ExamSubmitReviewSheet
        open={showSubmitReviewSheet}
        onClose={() => setShowSubmitReviewSheet(false)}
        answeredCount={answeredCount}
        totalQuestions={questions.length}
        unansweredQuestions={unansweredQuestions}
        onJumpToQuestion={(idx) => {
          setShowSubmitReviewSheet(false);
          jumpToQuestionIndex(idx, true);
        }}
        onConfirmSubmit={() => executeSubmit(false)}
      />

      {showShortcutsModal && (
        <KeyboardShortcutsModal
          isOpen={showShortcutsModal}
          onClose={() => setShowShortcutsModal(false)}
        />
      )}
    </div>
  );
}

export default function ExamPage() {
  return (
    <Suspense
      fallback={
        <div className="py-24 flex flex-col items-center justify-center gap-3 text-fg-muted">
          <Spinner className="w-8 h-8" />
          <p className="font-semibold text-sm">正在载入全真考场环境...</p>
        </div>
      }
    >
      <ExamContent />
    </Suspense>
  );
}
