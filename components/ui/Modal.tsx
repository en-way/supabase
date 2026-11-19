"use client";

import React, { useEffect } from "react";
import { X } from "lucide-react";
import { useBodyScrollLock } from "@/hooks/useBodyScrollLock";

export interface ModalProps {
  open: boolean;
  onClose: () => void;
  title?: React.ReactNode;
  subtitle?: React.ReactNode;
  maxWidthClass?: string;
  disableClose?: boolean;
  children: React.ReactNode;
  footer?: React.ReactNode;
}

export function Modal({
  open,
  onClose,
  title,
  subtitle,
  maxWidthClass = "max-w-md",
  disableClose = false,
  children,
  footer,
}: ModalProps) {
  useBodyScrollLock(open);

  useEffect(() => {
    if (!open || disableClose) return;
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  }, [open, disableClose, onClose]);

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-modal flex items-center justify-center p-4"
      role="dialog"
      aria-modal="true"
    >
      <div
        className="fixed inset-0 z-backdrop bg-overlay backdrop-blur-sm animate-in fade-in duration-150"
        onClick={() => {
          if (!disableClose) onClose();
        }}
      />
      <div
        className={`relative z-modal w-full ${maxWidthClass} rounded-xl bg-surface text-fg border border-border shadow-pop overflow-hidden animate-in fade-in zoom-in-95 duration-150`}
      >
        {(title || !disableClose) && (
          <div className="flex items-start justify-between gap-3 px-5 py-4 border-b border-border">
            <div className="min-w-0">
              {title && <h3 className="text-sm sm:text-base font-bold text-fg">{title}</h3>}
              {subtitle && <p className="text-xs text-fg-muted mt-0.5">{subtitle}</p>}
            </div>
            {!disableClose && (
              <button
                type="button"
                onClick={onClose}
                aria-label="关闭"
                className="p-1.5 rounded-md text-fg-subtle hover:text-fg hover:bg-surface-2 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>
        )}
        <div className="p-5">{children}</div>
        {footer && (
          <div className="px-5 py-3.5 border-t border-border bg-surface-2 flex items-center justify-end gap-2">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
