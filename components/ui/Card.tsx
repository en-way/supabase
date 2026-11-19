import React from "react";

export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  interactive?: boolean;
}

export function Card({
  interactive = false,
  className = "",
  children,
  ...props
}: CardProps) {
  return (
    <div
      className={`bg-surface text-fg border border-border rounded-lg shadow-1 ${
        interactive
          ? "transition-all duration-150 ease-out hover:shadow-2 hover:border-border-strong"
          : ""
      } ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}

export function Panel({
  className = "",
  children,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={`bg-surface-2 text-fg border border-border rounded-lg ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}
