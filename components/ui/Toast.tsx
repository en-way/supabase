import React from "react";
import { AlertCircle, CheckCircle2, Info, X } from "lucide-react";

export type ToastTone = "success" | "danger" | "warning" | "info";

const TONE_CLASSES: Record<ToastTone, string> = {
  success: "bg-success-soft text-success border-success/30",
  danger: "bg-danger-soft text-danger border-danger/30",
  warning: "bg-warning-soft text-warning border-warning/30",
  info: "bg-info-soft text-info border-info/30",
};

export interface ToastProps {
  tone?: ToastTone;
  message: string;
  onClose?: () => void;
  className?: string;
}

export function Toast({
  tone = "info",
  message,
  onClose,
  className = "",
}: ToastProps) {
  const Icon =
    tone === "success" ? CheckCircle2 : tone === "danger" || tone === "warning" ? AlertCircle : Info;

  return (
    <div
      role="status"
      className={`inline-flex items-center gap-2 rounded-md border px-3.5 py-2.5 text-xs font-semibold shadow-2 ${TONE_CLASSES[tone]} ${className}`}
    >
      <Icon className="w-4 h-4 shrink-0" />
      <span className="flex-1">{message}</span>
      {onClose && (
        <button
          type="button"
          onClick={onClose}
          aria-label="关闭提示"
          className="p-0.5 rounded-sm opacity-70 hover:opacity-100 transition-opacity"
        >
          <X className="w-3.5 h-3.5" />
        </button>
      )}
    </div>
  );
}
