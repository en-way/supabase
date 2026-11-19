"use client";

import { useDrawerSwipe } from "@/hooks/useDrawerSwipe";
import { triggerHaptic } from "@/hooks/useReaderPrefs";
import { Button } from "@/components/ui/Button";
import { CheckCircle2, FileCheck, X } from "lucide-react";

interface UnansweredItem {
  id: string;
  num: number;
  idx: number;
}

interface ExamSubmitReviewSheetProps {
  open: boolean;
  onClose: () => void;
  answeredCount: number;
  totalQuestions: number;
  unansweredQuestions: UnansweredItem[];
  onJumpToQuestion: (idx: number) => void;
  onConfirmSubmit: () => void;
}

export function ExamSubmitReviewSheet({
  open,
  onClose,
  answeredCount,
  totalQuestions,
  unansweredQuestions,
  onJumpToQuestion,
  onConfirmSubmit,
}: ExamSubmitReviewSheetProps) {
  const { handleDrawerTouchStart, handleDrawerTouchEnd } = useDrawerSwipe({
    onDismissHaptic: () => triggerHaptic(8),
  });

  if (!open) return null;

  const unansweredCount = unansweredQuestions.length;

  return (
    <div
      className="fixed inset-0 z-modal bg-overlay/50 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4 animate-in fade-in duration-150"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
      role="dialog"
      aria-modal="true"
      aria-label="考卷作答核验与交卷"
    >
      <div className="bg-surface rounded-t-3xl sm:rounded-3xl border-t sm:border border-border p-5 sm:p-6 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-pop max-h-[85dvh] w-full max-w-lg flex flex-col animate-in slide-in-from-bottom duration-200">
        <div
          onTouchStart={handleDrawerTouchStart}
          onTouchEnd={(e) => handleDrawerTouchEnd(e, onClose)}
          className="touch-none select-none cursor-grab active:cursor-grabbing pb-3.5 border-b border-border shrink-0"
        >
          <div className="w-12 h-1.5 bg-border rounded-full mx-auto mb-2.5 sm:hidden" />
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <FileCheck className="w-5 h-5 text-primary" />
              <h3 className="font-bold text-base text-fg">考卷作答核验与交卷</h3>
            </div>
            <button
              type="button"
              onClick={onClose}
              aria-label="关闭弹窗"
              className="p-1.5 rounded-full bg-surface-2 text-fg-muted hover:text-fg transition-colors"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        <div className="py-4 space-y-4 overflow-y-auto overscroll-contain">
          <div className="grid grid-cols-2 gap-3">
            <div className="p-3.5 rounded-2xl bg-success-soft border border-success/30">
              <span className="text-[11px] font-medium text-success">已作答试题</span>
              <div className="text-2xl font-bold font-mono tabular-nums text-fg mt-0.5">
                {answeredCount}{" "}
                <span className="text-xs font-normal text-fg-muted">
                  / {totalQuestions} 题
                </span>
              </div>
            </div>
            <div
              className={`p-3.5 rounded-2xl border ${
                unansweredCount > 0
                  ? "bg-warning-soft border-warning/30 text-fg"
                  : "bg-surface-2 border-border text-fg-muted"
              }`}
            >
              <span className="text-[11px] font-medium">尚未作答</span>
              <div className="text-2xl font-bold font-mono tabular-nums mt-0.5">
                {unansweredCount} <span className="text-xs font-normal">题</span>
              </div>
            </div>
          </div>

          {unansweredCount > 0 ? (
            <div className="p-3.5 rounded-2xl bg-warning-soft border border-warning/30 space-y-2">
              <div className="flex items-center justify-between text-xs font-semibold text-fg">
                <span>待补答试题（点击快速直达补答）：</span>
                <span className="font-mono text-[11px] text-warning">
                  {unansweredCount} 题待答
                </span>
              </div>
              <div className="flex flex-wrap gap-1.5 max-h-36 overflow-y-auto pt-1 pr-1">
                {unansweredQuestions.map(({ id, num, idx }) => (
                  <button
                    key={id}
                    type="button"
                    onClick={() => onJumpToQuestion(idx)}
                    className="px-2.5 py-1.5 rounded-xl text-xs font-mono font-bold bg-surface text-fg border border-warning/40 hover:border-primary transition-colors shadow-1"
                    title={`点击快速跳转至第 ${num} 题进行作答`}
                  >
                    第 {num} 题
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="p-4 rounded-2xl bg-success-soft border border-success/30 flex items-center gap-3">
              <CheckCircle2 className="w-5 h-5 text-success shrink-0" />
              <div className="text-xs text-fg">
                <p className="font-bold">所有题目均已完成作答！</p>
                <p className="text-[11px] text-fg-muted mt-0.5">
                  确认交卷后系统将即时生成全真考卷成绩报告与逐题解析。
                </p>
              </div>
            </div>
          )}
        </div>

        <div className="pt-3.5 border-t border-border flex items-center gap-3 shrink-0">
          <Button variant="secondary" className="flex-1" onClick={onClose}>
            返回继续作答
          </Button>
          <Button className="flex-1" onClick={onConfirmSubmit}>
            确认交卷核分
          </Button>
        </div>
      </div>
    </div>
  );
}
