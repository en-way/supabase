import React from "react";

const BASE_FIELD_CLASS =
  "rounded-md border border-border bg-surface text-fg placeholder:text-fg-subtle px-3 py-2 text-sm transition-colors duration-150 focus:outline-none focus:border-primary";

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  compact?: boolean;
}

export function Input({ compact = false, className = "", ...props }: InputProps) {
  const widthClass = /\bw-/.test(className) ? "" : "w-full";
  return (
    <input
      className={`${widthClass} ${BASE_FIELD_CLASS} ${compact ? "input-compact" : ""} ${className}`}
      {...props}
    />
  );
}

export interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  compact?: boolean;
}

export function Select({ compact = false, className = "", children, ...props }: SelectProps) {
  const widthClass = /\bw-/.test(className) ? "" : "w-full";
  return (
    <select
      className={`${widthClass} ${BASE_FIELD_CLASS} ${compact ? "input-compact" : ""} ${className}`}
      {...props}
    >
      {children}
    </select>
  );
}

export function Textarea({
  className = "",
  ...props
}: React.TextareaHTMLAttributes<HTMLTextAreaElement>) {
  const widthClass = /\bw-/.test(className) ? "" : "w-full";
  return <textarea className={`${widthClass} ${BASE_FIELD_CLASS} ${className}`} {...props} />;
}

export interface SwitchProps {
  checked: boolean;
  onChange: (checked: boolean) => void;
  disabled?: boolean;
  ariaLabel?: string;
}

export function Switch({ checked, onChange, disabled = false, ariaLabel }: SwitchProps) {
  return (
    <button
      type="button"
      role="switch"
      aria-checked={checked}
      aria-label={ariaLabel}
      disabled={disabled}
      onClick={() => onChange(!checked)}
      className={`relative inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border transition-colors duration-150 ease-out disabled:opacity-50 disabled:cursor-not-allowed ${
        checked ? "bg-primary border-primary" : "bg-surface-3 border-border-strong"
      }`}
    >
      <span
        className={`inline-block h-4 w-4 rounded-full bg-surface shadow-1 transition-transform duration-150 ease-out ${
          checked ? "translate-x-5" : "translate-x-1"
        }`}
      />
    </button>
  );
}
