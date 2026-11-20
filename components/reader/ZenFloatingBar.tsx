"use client";

import { Keyboard, ListOrdered, Minimize2 } from "lucide-react";

interface ZenFloatingBarProps {
  modeLabel: string;
  title?: string;
  metaText: string;
  mobileCompactText?: string;
  onOpenAnswerSheet?: () => void;
  answerSheetLabel?: string;
  disableAnswerSheet?: boolean;
  onOpenShortcuts: () => void;
  onExitZen: () => void;
}

export function ZenFloatingBar({
  modeLabel,
  title,
  metaText,
  mobileCompactText,
  onOpenAnswerSheet,
  answerSheetLabel,
  disableAnswerSheet = false,
  onOpenShortcuts,
  onExitZen,
}: ZenFloatingBarProps) {
  return (
    <div className="sticky top-2 z-sticky bg-surface/95 backdrop-blur-md text-fg px-3 sm:px-4 py-2 rounded-2xl shadow-pop border border-border flex items-center justify-between gap-2 sm:gap-4 animate-in slide-in-from-top duration-200 no-print">
      <div className="flex items-center gap-2 sm:gap-3 min-w-0 flex-1">
        {mobileCompactText ? (
          <>
            <span className="lg:hidden text-xs font-mono font-bold text-primary min-w-0 truncate">
              {mobileCompactText}
            </span>
            <div className="hidden lg:flex items-center gap-3 min-w-0">
              <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-primary-soft text-primary border border-primary/20 shrink-0">
                {modeLabel}
              </span>
              {title && (
                <span className="text-xs font-bold truncate max-w-sm">
                  {title}
                </span>
              )}
              <span className="text-xs font-mono tabular-nums text-fg-muted shrink-0">
                {metaText}
              </span>
            </div>
          </>
        ) : (
          <>
            <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-primary-soft text-primary border border-primary/20 shrink-0">
              {modeLabel}
            </span>
            {title && (
              <span className="text-xs font-bold truncate max-w-sm hidden lg:inline">
                {title}
              </span>
            )}
            <span className="text-xs font-mono tabular-nums text-fg-muted min-w-0 truncate">
              {metaText}
            </span>
          </>
        )}
      </div>

      <div className="flex items-center gap-1.5 sm:gap-2 shrink-0">
        {onOpenAnswerSheet && (
          <button
            type="button"
            onClick={onOpenAnswerSheet}
            disabled={disableAnswerSheet}
            className="px-2.5 py-1.5 rounded-xl bg-surface-2 hover:bg-border/60 text-fg text-xs font-semibold inline-flex items-center gap-1.5 transition-colors disabled:opacity-50 shrink-0 whitespace-nowrap"
            title="打开答题卡 (M)"
          >
            <ListOrdered className="w-3.5 h-3.5 text-primary shrink-0" />
            <span>{answerSheetLabel || "答题卡"}</span>
          </button>
        )}
        <button
          type="button"
          onClick={onOpenShortcuts}
          className="hidden lg:inline-flex p-1.5 rounded-xl bg-surface-2 hover:bg-border/60 text-fg-muted hover:text-fg text-xs transition-colors shrink-0"
          title="快捷键速查 (?)"
          aria-label="快捷键速查"
        >
          <Keyboard className="w-3.5 h-3.5" />
        </button>
        <button
          type="button"
          onClick={onExitZen}
          className="px-2.5 sm:px-3 py-1.5 rounded-xl bg-primary text-primary-fg hover:opacity-95 text-xs font-bold inline-flex items-center gap-1 transition-opacity shrink-0 whitespace-nowrap"
        >
          <Minimize2 className="w-3.5 h-3.5 shrink-0" />
          <span>
            退出专注<span className="hidden lg:inline"> (Esc)</span>
          </span>
        </button>
      </div>
    </div>
  );
}
