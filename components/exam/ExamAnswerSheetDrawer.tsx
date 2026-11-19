"use client";

import type { QuestionRecord } from "@/types/exam";
import { useDrawerSwipe } from "@/hooks/useDrawerSwipe";
import { triggerHaptic } from "@/hooks/useReaderPrefs";
import { AnswerSheetSections } from "@/components/reader/AnswerSheetSections";
import { Button } from "@/components/ui/Button";
import { ListOrdered, X } from "lucide-react";

interface ExamAnswerSheetDrawerProps {
  open: boolean;
  onClose: () => void;
  questions: QuestionRecord[];
  answers: Record<string, string>;
  focusedIndex: number;
  isSubmitted: boolean;
  isTimeUp: boolean;
  answeredCount: number;
  onJump: (idx: number) => void;
  onScrollToFirstUnanswered: () => void;
  onSubmitNow: () => void;
}

export function ExamAnswerSheetDrawer({
  open,
  onClose,
  questions,
  answers,
  focusedIndex,
  isSubmitted,
  isTimeUp,
  answeredCount,
  onJump,
  onScrollToFirstUnanswered,
  onSubmitNow,
}: ExamAnswerSheetDrawerProps) {
  const {
    panelStyle,
    backdropStyle,
    handleDrawerTouchStart,
    handleDrawerTouchMove,
    handleDrawerTouchEnd,
  } = useDrawerSwipe({
    open,
    onDismissHaptic: () => triggerHaptic(8),
  });

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-modal flex items-end sm:items-center justify-center p-0 sm:p-4"
      role="dialog"
      aria-modal="true"
      aria-label="答题卡总览"
    >
      <div
        className="fixed inset-0 bg-overlay/50 backdrop-blur-sm animate-in fade-in duration-150"
        style={backdropStyle}
        onClick={onClose}
      />
      <div
        style={panelStyle}
        className="relative bg-surface rounded-t-3xl sm:rounded-3xl border-t sm:border border-border p-5 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-pop max-h-[85dvh] w-full max-w-xl flex flex-col animate-in slide-in-from-bottom duration-200"
      >
        <div
          onTouchStart={handleDrawerTouchStart}
          onTouchMove={handleDrawerTouchMove}
          onTouchEnd={(e) => handleDrawerTouchEnd(e, onClose)}
          className="touch-none select-none cursor-grab active:cursor-grabbing pb-3 border-b border-border shrink-0"
        >
          <div className="w-12 h-1.5 bg-border rounded-full mx-auto mb-2.5 sm:hidden" />
          <div className="flex items-center justify-between">
            <div>
              <h4 className="text-sm sm:text-base font-bold text-fg flex items-center gap-2">
                <ListOrdered className="w-4 h-4 text-primary" />
                <span>
                  答题卡总览 ({answeredCount} / {questions.length})
                </span>
              </h4>
              <span className="text-[11px] text-fg-subtle">
                点击题号快速定位到对应试题
              </span>
            </div>
            <button
              type="button"
              onClick={onClose}
              aria-label="关闭答题卡"
              className="p-1.5 rounded-full bg-surface-2 text-fg-muted hover:text-fg transition-colors"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto overscroll-contain py-4 pr-1">
          <AnswerSheetSections
            questions={questions}
            answers={answers}
            activeIndex={focusedIndex}
            showCorrectness={isSubmitted}
            onJump={onJump}
            buttonSize="drawer"
          />
        </div>

        <div className="pt-3 border-t border-border flex flex-col sm:flex-row justify-between items-center gap-3 text-xs text-fg-muted shrink-0">
          <div className="flex items-center gap-3">
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full bg-primary inline-block" />
              <span>已答</span>
            </span>
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full bg-border inline-block" />
              <span>未答</span>
            </span>
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full ring-2 ring-primary inline-block" />
              <span>当前聚焦</span>
            </span>
          </div>
          <div className="flex items-center gap-2 w-full sm:w-auto">
            {!isSubmitted && answeredCount < questions.length && (
              <Button
                variant="secondary"
                size="sm"
                className="flex-1 sm:flex-none"
                onClick={onScrollToFirstUnanswered}
              >
                定位首道未答题
              </Button>
            )}
            {!isSubmitted && (
              <Button
                size="sm"
                className="flex-1 sm:flex-none"
                disabled={isTimeUp}
                onClick={onSubmitNow}
              >
                立即交卷
              </Button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
