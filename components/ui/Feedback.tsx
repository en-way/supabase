import React from "react";
import { Loader2 } from "lucide-react";

export function Skeleton({ className = "" }: { className?: string }) {
  return <div className={`rounded-md bg-surface-3/80 animate-pulse ${className}`} />;
}

export function Spinner({ className = "w-5 h-5 text-primary" }: { className?: string }) {
  return <Loader2 className={`animate-spin ${className}`} />;
}

export interface EmptyStateProps {
  icon?: React.ReactNode;
  title: string;
  description?: string;
  action?: React.ReactNode;
  className?: string;
}

export function EmptyState({
  icon,
  title,
  description,
  action,
  className = "",
}: EmptyStateProps) {
  return (
    <div
      className={`flex flex-col items-center justify-center text-center rounded-lg border border-dashed border-border-strong bg-surface p-8 sm:p-12 ${className}`}
    >
      {icon && (
        <div className="w-11 h-11 rounded-lg bg-surface-2 text-fg-muted flex items-center justify-center mb-3">
          {icon}
        </div>
      )}
      <h3 className="text-sm font-bold text-fg">{title}</h3>
      {description && <p className="text-xs text-fg-muted mt-1 max-w-sm">{description}</p>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  );
}
