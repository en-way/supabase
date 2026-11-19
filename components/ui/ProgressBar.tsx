import React from "react";

export interface ProgressBarProps {
  value: number;
  max?: number;
  tone?: "primary" | "success" | "warning" | "danger";
  className?: string;
}

const TONE_FILL: Record<NonNullable<ProgressBarProps["tone"]>, string> = {
  primary: "bg-primary",
  success: "bg-success",
  warning: "bg-warning",
  danger: "bg-danger",
};

export function ProgressBar({
  value,
  max = 100,
  tone = "primary",
  className = "",
}: ProgressBarProps) {
  const safeMax = max > 0 ? max : 100;
  const pct = Math.max(0, Math.min(100, (value / safeMax) * 100));

  return (
    <div
      role="progressbar"
      aria-valuenow={Math.round(pct)}
      aria-valuemin={0}
      aria-valuemax={100}
      className={`w-full h-2 rounded-full bg-surface-3 overflow-hidden ${className}`}
    >
      <div
        className={`h-full rounded-full transition-all duration-200 ease-out ${TONE_FILL[tone]}`}
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}
