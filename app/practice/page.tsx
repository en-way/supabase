"use client";

import { Suspense } from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import { useSearchParams } from "next/navigation";
import { usePracticeSession } from "@/hooks/usePracticeSession";
import { useReaderPrefs } from "@/hooks/useReaderPrefs";
import SplitPane from "@/components/SplitPane";
import { PassageReaderPane } from "@/components/reader/PassageReaderPane";
import { ZenFloatingBar } from "@/components/reader/ZenFloatingBar";
import { PracticeTopBar } from "@/components/practice/PracticeTopBar";
import { PracticeQuestionCard } from "@/components/practice/PracticeQuestionCard";
import { PracticePassageDrawer } from "@/components/practice/PracticePassageDrawer";
import { PracticeAnswerSheetDrawer } from "@/components/practice/PracticeAnswerSheetDrawer";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Spinner } from "@/components/ui/Feedback";
import { Kbd } from "@/components/ui/Kbd";
import { BookOpen, ChevronLeft, ChevronRight, HelpCircle } from "lucide-react";

const KeyboardShortcutsModal = dynamic(
  () => import("@/components/KeyboardShortcutsModal"),
  { ssr: false }
);

function PracticeContent() {
  const searchParams = useSearchParams();
  const examId = searchParams.get("id");

  const { fontSize, lineHeight, updateFontSize, cycleLineHeight } =
    useReaderPrefs();
  const session = usePracticeSession(examId);

  const {
    exam,
    passages,
    questions,
    loading,
    currentIndex,
    userAnswers,
    favoriteIds,
    editingNotes,
    activePassageId,
    practiceMobileTab,
    setPracticeMobileTab,
    showAnswerSheet,
    setShowAnswerSheet,
    showPassageSheet,
    setShowPassageSheet,
    isZenMode,
    setIsZenMode,
    showShortcutsModal,
    setShowShortcutsModal,
    passageContainerRef,
    handleTouchStart,
    handleTouchEnd,
    navigateTo,
    handleJumpToQuestion,
    handleJumpToFirstUnanswered,
    handleResetPractice,
    handleSelectOption,
    handleToggleFav,
    handleSaveNote,
  } = session;

  if (!examId) {
    return (
      <Card className="py-16 text-center space-y-4">
        <p className="text-fg-muted text-sm">缺少试卷 ID 参数</p>
        <Link
          href="/"
          className="inline-flex px-4 py-2 bg-primary text-primary-fg rounded-xl text-xs font-semibold"
        >
          返回试卷大厅
        </Link>
      </Card>
    );
  }

  if (loading) {
    return (
      <div className="py-24 flex flex-col items-center justify-center gap-3 text-fg-muted">
        <Spinner className="w-8 h-8" />
        <p className="font-medium text-sm">正在加载随做随练题库...</p>
      </div>
    );
  }

  const currentQ = questions[currentIndex] || questions[0];

  if (!questions.length || !currentQ) {
    return (
      <Card className="py-16 text-center space-y-4">
        <p className="text-fg-muted text-sm">该试卷暂无题目</p>
        <Link
          href="/"
          className="inline-flex px-4 py-2 bg-primary text-primary-fg rounded-xl text-sm font-semibold"
        >
          返回试卷大厅
        </Link>
      </Card>
    );
  }

  const relatedPassage = currentQ.passage_id
    ? passages.find((p) => p.id === currentQ.passage_id) || passages[0] || null
    : passages[0] || null;

  const totalQuestions = questions.length;
  let answeredCount = 0;
  let correctCount = 0;
  let currentScore = 0;
  questions.forEach((q) => {
    const ans = userAnswers[q.id];
    if (ans) {
      answeredCount++;
      if (ans === q.correct_answer) {
        correctCount++;
        const qPts =
          q.points !== undefined && q.points !== null ? Number(q.points) : 2.0;
        currentScore += qPts;
      }
    }
  });
  currentScore = Math.round(currentScore * 10) / 10;
  const accuracy =
    answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
  const progressPercent =
    totalQuestions > 0 ? Math.round((answeredCount / totalQuestions) * 100) : 0;

  const cycleFontSize = () => {
    updateFontSize((prev) => (prev < 17 ? 17 : prev < 19 ? 19 : 15));
  };

  const leftPane = relatedPassage ? (
    <PassageReaderPane
      passages={[relatedPassage]}
      activePassageId={activePassageId}
      questions={questions}
      answers={userAnswers}
      focusedIndex={currentIndex}
      visibleOnMobile={practiceMobileTab === "passage"}
      onReturnToQuestions={() => setPracticeMobileTab("question")}
      returnLabel={`查看题目作答 (${currentIndex + 1}/${questions.length})`}
      fontSize={fontSize}
      lineHeight={lineHeight}
      onUpdateFontSize={updateFontSize}
      onCycleLineHeight={cycleLineHeight}
      containerRef={passageContainerRef}
    />
  ) : null;

  const rightPane = (
    <div
      className={`${
        practiceMobileTab === "question" ? "block" : "hidden"
      } lg:block space-y-5`}
    >
      <PracticeQuestionCard
        question={currentQ}
        index={currentIndex}
        hasPassage={Boolean(relatedPassage)}
        selectedAnswer={userAnswers[currentQ.id]}
        isFavorited={favoriteIds.has(currentQ.id)}
        noteValue={editingNotes[currentQ.id] || ""}
        onOpenPassageDrawer={() => setShowPassageSheet(true)}
        onToggleFavorite={handleToggleFav}
        onSelectOption={(key) => handleSelectOption(key)}
        onSaveNote={(noteText) => handleSaveNote(noteText, currentQ.id)}
      />

      <div className="flex items-center justify-between gap-3 pt-2">
        <Button
          variant="secondary"
          onClick={() => navigateTo(currentIndex - 1)}
          disabled={currentIndex === 0}
          className="flex-1 sm:flex-none"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>上一题</span>
          <Kbd className="hidden lg:inline-flex">←</Kbd>
        </Button>

        <span className="text-xs font-mono tabular-nums font-bold text-fg-muted sm:hidden">
          {currentIndex + 1} / {questions.length}
        </span>

        <Button
          onClick={() => navigateTo(currentIndex + 1)}
          disabled={currentIndex === questions.length - 1}
          className="flex-1 sm:flex-none"
        >
          <span>下一题</span>
          <Kbd variant="onPrimary" className="hidden lg:inline-flex">
            →
          </Kbd>
          <ChevronRight className="w-4 h-4" />
        </Button>
      </div>
    </div>
  );

  return (
    <div
      onTouchStart={handleTouchStart}
      onTouchEnd={handleTouchEnd}
      className="space-y-6 animate-in fade-in duration-200 pb-20 lg:pb-0"
    >
      {isZenMode ? (
        <ZenFloatingBar
          modeLabel="专注模式"
          title={exam?.title}
          metaText={`题号 ${currentIndex + 1} / ${questions.length} · 正确率 ${accuracy}%`}
          onOpenAnswerSheet={() => setShowAnswerSheet(true)}
          answerSheetLabel={`${answeredCount}/${totalQuestions}`}
          onOpenShortcuts={() => setShowShortcutsModal(true)}
          onExitZen={() => setIsZenMode(false)}
        />
      ) : (
        <PracticeTopBar
          exam={exam}
          currentIndex={currentIndex}
          totalQuestions={totalQuestions}
          answeredCount={answeredCount}
          progressPercent={progressPercent}
          currentScore={currentScore}
          accuracy={accuracy}
          isZenMode={isZenMode}
          fontSize={fontSize}
          onToggleZen={() => setIsZenMode((p) => !p)}
          onOpenShortcuts={() => setShowShortcutsModal(true)}
          onOpenAnswerSheet={() => setShowAnswerSheet(true)}
          onResetPractice={handleResetPractice}
          onCycleFontSize={cycleFontSize}
        />
      )}

      {relatedPassage && (
        <div className="lg:hidden sticky top-[4.5rem] z-sticky flex items-center bg-surface-2/95 backdrop-blur-md p-1 rounded-xl border border-border shadow-1 no-print">
          <button
            type="button"
            onClick={() => setPracticeMobileTab("passage")}
            className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
              practiceMobileTab === "passage"
                ? "bg-surface text-primary shadow-1"
                : "text-fg-muted"
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>阅读篇章材料</span>
          </button>
          <button
            type="button"
            onClick={() => setPracticeMobileTab("question")}
            className={`flex-1 py-2 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
              practiceMobileTab === "question"
                ? "bg-surface text-primary shadow-1"
                : "text-fg-muted"
            }`}
          >
            <HelpCircle className="w-3.5 h-3.5" />
            <span>
              本题研习 ({currentIndex + 1}/{questions.length})
            </span>
          </button>
        </div>
      )}

      {relatedPassage ? (
        <SplitPane
          storageKey="enway_split_ratio_practice"
          defaultRatio={60}
          isZenMode={isZenMode}
          leftPane={leftPane}
          rightPane={rightPane}
        />
      ) : (
        <div className="max-w-3xl mx-auto">{rightPane}</div>
      )}

      {/* Mobile Fixed Bottom Dock */}
      <div className="lg:hidden fixed bottom-0 left-0 right-0 z-nav bg-surface/95 backdrop-blur-xl border-t border-border px-3.5 py-2 pb-[max(0.75rem,env(safe-area-inset-bottom))] shadow-2 flex items-center justify-between gap-3 no-print">
        <Button
          variant="secondary"
          size="sm"
          className="flex-1"
          onClick={() => navigateTo(currentIndex - 1)}
          disabled={currentIndex === 0}
        >
          <ChevronLeft className="w-4 h-4" />
          <span>上一题</span>
        </Button>

        <span className="font-mono tabular-nums text-xs font-semibold text-fg-muted shrink-0 px-1 select-none">
          {currentIndex + 1} / {totalQuestions}
        </span>

        <Button
          size="sm"
          className="flex-1"
          onClick={() => navigateTo(currentIndex + 1)}
          disabled={currentIndex === questions.length - 1}
        >
          <span>下一题</span>
          <ChevronRight className="w-4 h-4" />
        </Button>
      </div>

      <PracticePassageDrawer
        open={showPassageSheet}
        onClose={() => setShowPassageSheet(false)}
        passage={relatedPassage}
        currentIndex={currentIndex}
        fontSize={fontSize}
        lineHeight={lineHeight}
        onUpdateFontSize={updateFontSize}
      />

      <PracticeAnswerSheetDrawer
        open={showAnswerSheet}
        onClose={() => setShowAnswerSheet(false)}
        questions={questions}
        answers={userAnswers}
        currentIndex={currentIndex}
        answeredCount={answeredCount}
        currentScore={currentScore}
        accuracy={accuracy}
        onJump={handleJumpToQuestion}
        onJumpFirstUnanswered={handleJumpToFirstUnanswered}
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

export default function PracticePage() {
  return (
    <Suspense
      fallback={
        <div className="py-24 flex flex-col items-center justify-center gap-3 text-fg-muted">
          <Spinner className="w-8 h-8" />
          <p className="text-sm font-medium">正在初始化...</p>
        </div>
      }
    >
      <PracticeContent />
    </Suspense>
  );
}
