import React from "react";

export interface PopoverProps extends React.HTMLAttributes<HTMLDivElement> {
  open: boolean;
}

export const Popover = React.forwardRef<HTMLDivElement, PopoverProps>(
  ({ open, className = "", children, ...props }, ref) => {
    if (!open) return null;
    return (
      <div
        ref={ref}
        className={`rounded-lg bg-surface text-fg border border-border shadow-pop animate-in fade-in zoom-in-95 duration-150 ${className}`}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Popover.displayName = "Popover";
