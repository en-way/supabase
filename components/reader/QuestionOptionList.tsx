"use client";

import type { QuestionOption } from "@/types/exam";
import { CheckCircle2, XCircle } from "lucide-react";

interface QuestionOptionListProps {
  options: QuestionOption[];
  selectedAnswer?: string;
  correctAnswer: string;
  showResult: boolean;
  disabled?: boolean;
  onSelect: (key: string) => void;
  showCheckIcons?: boolean;
}

export function QuestionOptionList({
  options,
  selectedAnswer,
  correctAnswer,
  showResult,
  disabled = false,
  onSelect,
  showCheckIcons = false,
}: QuestionOptionListProps) {
  const isGrid = options.length > 5;

  return (
    <div
      className={
        isGrid
          ? "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2"
          : "space-y-2.5"
      }
    >
      {options.map((opt) => {
        const isSelected = selectedAnswer === opt.key;
        const isCorrectKey = opt.key === correctAnswer;

        let optionCls =
          "bg-surface-2/70 border-border text-fg hover:bg-surface-2 hover:border-primary/40";
        let badgeCls = "bg-surface border-border text-fg-muted";

        if (showResult) {
          if (isCorrectKey) {
            optionCls =
              "bg-success-soft border-success/50 text-fg font-semibold ring-1 ring-success/40";
            badgeCls = "bg-success text-white border-success font-bold";
          } else if (isSelected && !isCorrectKey) {
            optionCls =
              "bg-danger-soft border-danger/50 text-fg font-semibold";
            badgeCls = "bg-danger text-white border-danger font-bold";
          } else {
            optionCls =
              "bg-surface-2/40 border-border/60 text-fg-subtle opacity-65";
            badgeCls = "bg-surface-2 border-border/60 text-fg-subtle";
          }
        } else if (isSelected) {
          optionCls =
            "bg-primary border-primary text-primary-fg font-bold shadow-1";
          badgeCls = "bg-surface text-primary border-surface font-bold";
        }

        return (
          <button
            key={opt.key}
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              onSelect(opt.key);
            }}
            disabled={disabled}
            title={opt.text}
            className={
              isGrid
                ? `min-h-[44px] p-2 sm:p-2.5 rounded-xl border text-left flex items-center gap-2 transition-all duration-150 active:scale-[0.98] disabled:cursor-default ${optionCls}`
                : `w-full min-h-[44px] p-3 sm:p-3.5 rounded-xl border text-left flex items-start gap-3 transition-all duration-150 active:scale-[0.99] disabled:cursor-default ${optionCls}`
            }
          >
            <span
              className={`w-6 h-6 rounded-lg text-xs font-bold font-mono flex items-center justify-center shrink-0 border ${badgeCls}`}
            >
              {opt.key}
            </span>
            <span
              className={`text-xs ${
                isGrid ? "truncate font-medium" : "sm:text-sm pt-0.5 leading-relaxed"
              } flex-1`}
            >
              {opt.text}
            </span>
            {!showResult && !disabled && !isGrid && (
              <span
                className={`text-[10px] font-mono hidden sm:inline ml-auto pt-0.5 ${
                  isSelected ? "text-primary-fg/80" : "text-fg-subtle"
                }`}
              >
                [{opt.key}]
              </span>
            )}
            {showCheckIcons && showResult && isCorrectKey && (
              <CheckCircle2 className="w-3.5 h-3.5 text-success ml-auto shrink-0" />
            )}
            {showCheckIcons && showResult && isSelected && !isCorrectKey && (
              <XCircle className="w-3.5 h-3.5 text-danger ml-auto shrink-0" />
            )}
          </button>
        );
      })}
    </div>
  );
}
