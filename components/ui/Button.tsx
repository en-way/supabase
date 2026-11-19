import React from "react";
import { Loader2 } from "lucide-react";

export type ButtonVariant = "primary" | "secondary" | "ghost" | "danger";
export type ButtonSize = "sm" | "md";

const VARIANT_CLASSES: Record<ButtonVariant, string> = {
  primary:
    "bg-primary text-primary-fg hover:bg-primary-hover shadow-1 border border-transparent",
  secondary:
    "bg-surface text-fg border border-border hover:bg-surface-2 hover:border-border-strong shadow-1",
  ghost:
    "bg-transparent text-fg-muted border border-transparent hover:bg-surface-2 hover:text-fg",
  danger:
    "bg-danger text-primary-fg hover:opacity-90 border border-transparent shadow-1",
};

const SIZE_CLASSES: Record<ButtonSize, string> = {
  sm: "min-h-10 sm:min-h-9 px-3 py-1.5 text-xs gap-1.5",
  md: "min-h-11 sm:min-h-10 px-4 py-2 text-xs sm:text-sm gap-2",
};

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  loading?: boolean;
}

export function Button({
  variant = "primary",
  size = "md",
  loading = false,
  disabled,
  className = "",
  children,
  type = "button",
  ...props
}: ButtonProps) {
  return (
    <button
      type={type}
      disabled={disabled || loading}
      className={`inline-flex items-center justify-center rounded-md font-semibold transition-colors duration-150 ease-out active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed ${VARIANT_CLASSES[variant]} ${SIZE_CLASSES[size]} ${className}`}
      {...props}
    >
      {loading && <Loader2 className="w-3.5 h-3.5 animate-spin shrink-0" />}
      {children}
    </button>
  );
}

export interface IconButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
}

export function IconButton({
  variant = "secondary",
  size = "sm",
  className = "",
  children,
  type = "button",
  ...props
}: IconButtonProps) {
  const iconSize = size === "sm" ? "w-10 h-10 sm:w-9 sm:h-9" : "w-11 h-11 sm:w-10 sm:h-10";
  return (
    <button
      type={type}
      className={`inline-flex items-center justify-center rounded-md transition-colors duration-150 ease-out active:scale-[0.96] disabled:opacity-50 disabled:cursor-not-allowed ${VARIANT_CLASSES[variant]} ${iconSize} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}
