"use client";

import type { QuestionRecord } from "@/types/exam";
import { normalizeOptions } from "@/lib/storage";
import { QuestionOptionList } from "@/components/reader/QuestionOptionList";
import { Badge } from "@/components/ui/Badge";
import { Card } from "@/components/ui/Card";
import { Kbd } from "@/components/ui/Kbd";
import {
  Bookmark,
  BookOpen,
  CheckCircle2,
  Edit3,
  Sparkles,
  XCircle,
} from "lucide-react";

interface PracticeQuestionCardProps {
  question: QuestionRecord;
  index: number;
  hasPassage: boolean;
  selectedAnswer?: string;
  isFavorited: boolean;
  noteValue: string;
  onOpenPassageDrawer: () => void;
  onToggleFavorite: () => void;
  onSelectOption: (key: string) => void;
  onSaveNote: (noteText: string) => void;
}

export function PracticeQuestionCard({
  question,
  index,
  hasPassage,
  selectedAnswer,
  isFavorited,
  noteValue,
  onOpenPassageDrawer,
  onToggleFavorite,
  onSelectOption,
  onSaveNote,
}: PracticeQuestionCardProps) {
  const isAnswered = Boolean(selectedAnswer);
  const isCorrect = selectedAnswer === question.correct_answer;
  const opts = normalizeOptions(question.options);

  const qTypeLabel =
    question.q_type === "reading_item"
      ? "阅读小题"
      : question.q_type === "cloze_item"
        ? "完形小题"
        : "客观题";

  return (
    <Card className="p-5 sm:p-7 space-y-5">
      <div className="flex items-start justify-between gap-3">
        <div className="flex items-center gap-2">
          <Badge tone="primary" className="font-mono font-bold">
            题号 {index + 1}
          </Badge>
          <span className="text-xs text-fg-subtle font-medium">
            {qTypeLabel}（{question.points} 分）
          </span>
        </div>

        <div className="flex items-center gap-1.5">
          {hasPassage && (
            <button
              type="button"
              onClick={onOpenPassageDrawer}
              className="lg:hidden px-2.5 py-1 rounded-lg bg-primary-soft text-primary border border-primary/25 text-xs font-bold flex items-center gap-1 active:scale-95"
              title="在当前页面升起材料抽屉速查线索句"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>速查材料</span>
            </button>
          )}

          <button
            type="button"
            onClick={onToggleFavorite}
            title="收藏本题 (快捷键 F)"
            className={`px-2.5 py-1 rounded-lg border text-xs font-medium flex items-center gap-1.5 transition-colors ${
              isFavorited
                ? "bg-warning-soft border-warning/40 text-warning font-semibold"
                : "bg-surface border-border text-fg-muted hover:text-fg"
            }`}
          >
            <Bookmark
              className={`w-3.5 h-3.5 ${isFavorited ? "fill-warning text-warning" : ""}`}
            />
            <span>{isFavorited ? "已收藏" : "收藏"}</span>
            <Kbd className="hidden lg:inline-flex">F</Kbd>
          </button>
        </div>
      </div>

      <h3 className="text-base font-bold text-fg leading-relaxed">{question.stem}</h3>

      <QuestionOptionList
        options={opts}
        selectedAnswer={selectedAnswer}
        correctAnswer={question.correct_answer}
        showResult={isAnswered}
        disabled={isAnswered}
        onSelect={onSelectOption}
        showCheckIcons
      />

      {isAnswered && (
        <div className="pt-4 border-t border-border animate-in fade-in duration-200 space-y-3.5">
          <div
            className={`p-3.5 rounded-xl border flex items-center gap-2 ${
              isCorrect
                ? "bg-success-soft border-success/40 text-fg"
                : "bg-danger-soft border-danger/40 text-fg"
            }`}
          >
            {isCorrect ? (
              <>
                <CheckCircle2 className="w-4 h-4 text-success shrink-0" />
                <span className="font-bold text-xs">
                  回答正确！加 {question.points} 分
                </span>
              </>
            ) : (
              <>
                <XCircle className="w-4 h-4 text-danger shrink-0" />
                <span className="font-bold text-xs">
                  回答错误（正确答案：{question.correct_answer}）· 已入错题本
                </span>
              </>
            )}
          </div>

          <div className="p-4 rounded-xl bg-surface-2/80 border border-border">
            <div className="flex items-center gap-1.5 text-fg font-bold text-xs mb-1.5">
              <Sparkles className="w-3.5 h-3.5 text-primary" />
              <span>考点精析与释义</span>
            </div>
            <p className="text-xs text-fg-muted leading-relaxed whitespace-pre-line">
              {question.explanation}
            </p>
          </div>

          <div className="p-3 bg-warning-soft/60 rounded-xl border border-warning/30">
            <div className="flex items-center gap-1.5 text-xs font-semibold text-fg mb-1.5">
              <Edit3 className="w-3.5 h-3.5 text-warning" />
              <span>个人做题笔记心得：</span>
            </div>
            <input
              key={question.id}
              type="text"
              defaultValue={noteValue}
              onBlur={(e) => onSaveNote(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Escape" || e.key === "Enter") {
                  e.preventDefault();
                  e.stopPropagation();
                  e.currentTarget.blur();
                }
              }}
              placeholder="在此输入个人做题笔记，按 Enter/Esc 完成并自动保存..."
              className="input-compact w-full text-xs bg-surface border border-border rounded-lg px-3 py-1.5 text-fg placeholder:text-fg-subtle focus:outline-none focus:ring-2 focus:ring-primary/30"
            />
          </div>
        </div>
      )}
    </Card>
  );
}
