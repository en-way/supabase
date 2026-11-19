import React from "react";

export type BadgeTone = "neutral" | "primary" | "success" | "danger" | "warning" | "info";

const TONE_CLASSES: Record<BadgeTone, string> = {
  neutral: "bg-surface-2 text-fg-muted border-border",
  primary: "bg-primary-soft text-primary-soft-fg border-primary/20",
  success: "bg-success-soft text-success border-success/20",
  danger: "bg-danger-soft text-danger border-danger/20",
  warning: "bg-warning-soft text-warning border-warning/20",
  info: "bg-info-soft text-info border-info/20",
};

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  tone?: BadgeTone;
}

export function Badge({
  tone = "neutral",
  className = "",
  children,
  ...props
}: BadgeProps) {
  return (
    <span
      className={`inline-flex items-center gap-1 rounded-sm border px-2 py-0.5 text-[11px] font-semibold leading-normal ${TONE_CLASSES[tone]} ${className}`}
      {...props}
    >
      {children}
    </span>
  );
}
