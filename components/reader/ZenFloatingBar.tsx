"use client";

import { Keyboard, Minimize2 } from "lucide-react";

interface ZenFloatingBarProps {
  modeLabel: string;
  title?: string;
  metaText: string;
  onOpenShortcuts: () => void;
  onExitZen: () => void;
}

export function ZenFloatingBar({
  modeLabel,
  title,
  metaText,
  onOpenShortcuts,
  onExitZen,
}: ZenFloatingBarProps) {
  return (
    <div className="sticky top-2 z-sticky bg-surface/95 backdrop-blur-md text-fg px-4 py-2 rounded-2xl shadow-pop border border-border flex items-center justify-between gap-4 animate-in slide-in-from-top duration-200 no-print">
      <div className="flex items-center gap-3 min-w-0">
        <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-primary-soft text-primary border border-primary/20 shrink-0">
          {modeLabel}
        </span>
        {title && (
          <span className="text-xs font-bold truncate max-w-sm hidden sm:inline">
            {title}
          </span>
        )}
        <span className="text-xs font-mono tabular-nums text-fg-muted shrink-0">
          {metaText}
        </span>
      </div>

      <div className="flex items-center gap-2 shrink-0">
        <button
          type="button"
          onClick={onOpenShortcuts}
          className="p-1.5 rounded-xl bg-surface-2 hover:bg-border/60 text-fg-muted hover:text-fg text-xs transition-colors"
          title="快捷键速查 (?)"
          aria-label="快捷键速查"
        >
          <Keyboard className="w-3.5 h-3.5" />
        </button>
        <button
          type="button"
          onClick={onExitZen}
          className="px-3 py-1 rounded-xl bg-primary text-primary-fg hover:opacity-95 text-xs font-bold flex items-center gap-1 transition-opacity"
        >
          <Minimize2 className="w-3.5 h-3.5" />
          <span>退出专注 (Esc)</span>
        </button>
      </div>
    </div>
  );
}
