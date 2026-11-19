"use client";

import type { QuestionRecord } from "@/types/exam";
import { useDrawerSwipe } from "@/hooks/useDrawerSwipe";
import { triggerHaptic } from "@/hooks/useReaderPrefs";
import { AnswerSheetSections } from "@/components/reader/AnswerSheetSections";
import { Button } from "@/components/ui/Button";
import { ListOrdered, X } from "lucide-react";

interface PracticeAnswerSheetDrawerProps {
  open: boolean;
  onClose: () => void;
  questions: QuestionRecord[];
  answers: Record<string, string>;
  currentIndex: number;
  answeredCount: number;
  currentScore: number;
  accuracy: number;
  onJump: (idx: number) => void;
  onJumpFirstUnanswered: () => void;
}

export function PracticeAnswerSheetDrawer({
  open,
  onClose,
  questions,
  answers,
  currentIndex,
  answeredCount,
  currentScore,
  accuracy,
  onJump,
  onJumpFirstUnanswered,
}: PracticeAnswerSheetDrawerProps) {
  const { handleDrawerTouchStart, handleDrawerTouchEnd } = useDrawerSwipe({
    onDismissHaptic: () => triggerHaptic(8),
  });

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-modal bg-overlay/50 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4 animate-in fade-in duration-150"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
      role="dialog"
      aria-modal="true"
      aria-label="全卷答题卡速览"
    >
      <div className="bg-surface rounded-t-3xl sm:rounded-3xl border-t sm:border border-border p-5 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-pop max-w-xl w-full max-h-[85dvh] flex flex-col animate-in slide-in-from-bottom duration-200">
        <div
          onTouchStart={handleDrawerTouchStart}
          onTouchEnd={(e) => handleDrawerTouchEnd(e, onClose)}
          className="touch-none select-none cursor-grab active:cursor-grabbing pb-3.5 border-b border-border shrink-0"
        >
          <div className="w-12 h-1.5 bg-border rounded-full mx-auto mb-2.5 sm:hidden" />
          <div className="flex items-center justify-between">
            <div>
              <div className="flex items-center gap-2">
                <ListOrdered className="w-4 h-4 text-primary" />
                <h3 className="text-sm sm:text-base font-bold text-fg">
                  全卷答题卡速览
                </h3>
              </div>
              <div className="flex items-center gap-2.5 mt-1 text-xs text-fg-muted font-mono tabular-nums">
                <span>
                  已练 <strong className="text-fg">{answeredCount}</strong>/
                  {questions.length}
                </span>
                <span>·</span>
                <span>
                  得分 <strong className="text-warning">{currentScore}</strong>分
                </span>
                <span>·</span>
                <span>
                  正确率 <strong className="text-success">{accuracy}%</strong>
                </span>
              </div>
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
            activeIndex={currentIndex}
            showCorrectness
            onJump={onJump}
            buttonSize="drawer"
          />
        </div>

        <div className="pt-3.5 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-3 text-xs shrink-0">
          <div className="flex items-center gap-3 text-[11px] text-fg-muted">
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full bg-success inline-block" />
              <span>正确</span>
            </span>
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full bg-danger inline-block" />
              <span>错误</span>
            </span>
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full bg-border inline-block" />
              <span>未答</span>
            </span>
            <span className="inline-flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded-full ring-2 ring-primary inline-block" />
              <span>当前题</span>
            </span>
          </div>

          <div className="flex items-center gap-2 w-full sm:w-auto">
            {answeredCount < questions.length && (
              <Button
                variant="secondary"
                size="sm"
                className="flex-1 sm:flex-none"
                onClick={onJumpFirstUnanswered}
              >
                定位首道未答题
              </Button>
            )}
            <Button
              size="sm"
              className="flex-1 sm:flex-none"
              onClick={onClose}
            >
              返回做题
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
