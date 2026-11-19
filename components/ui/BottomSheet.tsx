"use client";

import React, { useEffect } from "react";
import { X } from "lucide-react";
import { useBodyScrollLock } from "@/hooks/useBodyScrollLock";
import { useDrawerSwipe } from "@/hooks/useDrawerSwipe";

export interface BottomSheetProps {
  open: boolean;
  onClose: () => void;
  title?: React.ReactNode;
  subtitle?: React.ReactNode;
  children: React.ReactNode;
  footer?: React.ReactNode;
  className?: string;
  zIndexClass?: string;
  lockScroll?: boolean;
  onDismissHaptic?: () => void;
}

export function BottomSheet({
  open,
  onClose,
  title,
  subtitle,
  children,
  footer,
  className = "",
  zIndexClass = "z-sheet",
  lockScroll = true,
  onDismissHaptic,
}: BottomSheetProps) {
  useBodyScrollLock(open && lockScroll);

  const { handleDrawerTouchStart, handleDrawerTouchEnd } = useDrawerSwipe({
    onDismissHaptic,
  });

  useEffect(() => {
    if (!open) return;
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div
      className={`fixed inset-0 ${zIndexClass} flex items-end sm:items-center justify-center sm:p-4`}
      role="dialog"
      aria-modal="true"
    >
      <div
        className="fixed inset-0 bg-overlay backdrop-blur-xs animate-in fade-in duration-150"
        onClick={onClose}
      />
      <div
        className={`relative w-full sm:max-w-lg max-h-[85dvh] flex flex-col rounded-t-xl sm:rounded-xl bg-surface text-fg border border-border shadow-pop overflow-hidden animate-in fade-in slide-in-from-bottom-4 duration-200 ${className}`}
      >
        <div
          onTouchStart={handleDrawerTouchStart}
          onTouchEnd={(e) => handleDrawerTouchEnd(e, onClose)}
          className="shrink-0 pt-2.5 pb-3 px-4 border-b border-border bg-surface select-none"
        >
          <div className="w-10 h-1 rounded-full bg-border-strong mx-auto mb-2.5 sm:hidden" />
          <div className="flex items-center justify-between gap-3">
            <div className="min-w-0">
              {title && <h3 className="text-sm font-bold text-fg truncate">{title}</h3>}
              {subtitle && <p className="text-xs text-fg-muted mt-0.5 truncate">{subtitle}</p>}
            </div>
            <button
              type="button"
              onClick={onClose}
              aria-label="关闭"
              className="p-1.5 rounded-md text-fg-subtle hover:text-fg hover:bg-surface-2 transition-colors shrink-0"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto overscroll-contain p-4 pb-[max(1rem,var(--safe-bottom))]">
          {children}
        </div>

        {footer && (
          <div className="shrink-0 border-t border-border bg-surface-2 px-4 py-3 pb-[max(0.75rem,var(--safe-bottom))]">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
