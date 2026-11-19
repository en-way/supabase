import React from "react";

export function Kbd({
  variant = "default",
  className = "",
  children,
}: {
  variant?: "default" | "onPrimary";
  className?: string;
  children: React.ReactNode;
}) {
  const variantClasses =
    variant === "onPrimary"
      ? "border-primary-fg/35 bg-primary-fg/15 text-primary-fg"
      : "border-border-strong bg-surface-2 text-fg-muted shadow-1";

  return (
    <kbd
      className={`inline-flex items-center justify-center rounded-sm border px-1.5 py-0.5 font-mono text-[11px] font-semibold ${variantClasses} ${className}`}
    >
      {children}
    </kbd>
  );
}
