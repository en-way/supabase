import React from "react";

export function Kbd({
  className = "",
  children,
}: {
  className?: string;
  children: React.ReactNode;
}) {
  return (
    <kbd
      className={`inline-flex items-center justify-center rounded-sm border border-border-strong bg-surface-2 px-1.5 py-0.5 font-mono text-[11px] font-semibold text-fg-muted shadow-1 ${className}`}
    >
      {children}
    </kbd>
  );
}
