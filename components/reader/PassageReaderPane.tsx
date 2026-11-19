"use client";

import type { RefObject } from "react";
import type { PassageRecord, QuestionRecord } from "@/types/exam";
import type { ReaderLineHeight } from "@/hooks/useReaderPrefs";
import PassageHighlighter from "@/components/PassageHighlighter";
import { BookOpen, FileText, ZoomIn, ZoomOut, AlignJustify } from "lucide-react";

interface PassageReaderPaneProps {
  passages: PassageRecord[];
  activePassageId: string;
  onSelectPassage?: (passageId: string) => void;
  questions: QuestionRecord[];
  answers: Record<string, string>;
  focusedIndex: number;
  onBlankClick?: (blankNum: number) => void;
  isSubmitted?: boolean;
  isPrintMode?: boolean;
  visibleOnMobile: boolean;
  onReturnToQuestions: () => void;
  returnLabel: string;
  fontSize: number;
  lineHeight: ReaderLineHeight;
  onUpdateFontSize: (updater: (prev: number) => number) => void;
  onCycleLineHeight: () => void;
  containerRef: RefObject<HTMLDivElement | null>;
}

function getPassageShortLabel(title: string, idx: number): string {
  if (title.includes("Use of English") || title.includes("完型")) return "完型填空";
  if (title.includes("Text 1")) return "Text 1";
  if (title.includes("Text 2")) return "Text 2";
  if (title.includes("Text 3")) return "Text 3";
  if (title.includes("Text 4")) return "Text 4";
  if (
    title.includes("Part B") ||
    title.includes("新题型") ||
    title.includes("多项") ||
    title.includes("小标题") ||
    title.includes("排序")
  ) {
    return "新题型";
  }
  return `篇章 ${idx + 1}`;
}

export function PassageReaderPane({
  passages,
  activePassageId,
  onSelectPassage,
  questions,
  answers,
  focusedIndex,
  onBlankClick,
  isSubmitted = false,
  isPrintMode = false,
  visibleOnMobile,
  onReturnToQuestions,
  returnLabel,
  fontSize,
  lineHeight,
  onUpdateFontSize,
  onCycleLineHeight,
  containerRef,
}: PassageReaderPaneProps) {
  if (passages.length === 0) return null;

  const displayPassages = isPrintMode
    ? passages
    : passages.filter((p) => p.id === activePassageId).length > 0
      ? passages.filter((p) => p.id === activePassageId)
      : passages.slice(0, 1);

  const showTabs = Boolean(onSelectPassage) && passages.length > 1;

  return (
    <div
      className={`${
        visibleOnMobile ? "flex" : "hidden"
      } lg:flex w-full bg-surface rounded-2xl border border-border shadow-1 flex-col ${
        isPrintMode
          ? "h-auto overflow-visible"
          : "overflow-hidden lg:sticky lg:top-36 h-[calc(100dvh-12rem)] min-h-[360px] lg:h-[78vh]"
      } print-page transition-colors duration-200`}
    >
      {/* Passage Header: Tabs + Typography Controls */}
      <div className="px-4 sm:px-5 py-2.5 border-b border-border bg-surface-2/70 flex items-center justify-between gap-2 shrink-0 no-print">
        <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar min-w-0">
          <BookOpen className="w-3.5 h-3.5 text-fg-subtle shrink-0" />
          {showTabs ? (
            passages.map((p, idx) => (
              <button
                key={p.id}
                type="button"
                onClick={() => onSelectPassage?.(p.id)}
                className={`px-3 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition-colors ${
                  activePassageId === p.id
                    ? "bg-primary text-primary-fg shadow-1"
                    : "bg-surface text-fg-muted hover:text-fg border border-border"
                }`}
              >
                {getPassageShortLabel(p.title || "", idx)}
              </button>
            ))
          ) : (
            <span className="text-xs font-bold text-fg truncate">
              {displayPassages[0]?.title}
            </span>
          )}
        </div>

        {/* Font Size & Line Height Controls */}
        <div className="flex items-center gap-1 text-xs text-fg-muted shrink-0">
          <button
            type="button"
            onClick={() => onUpdateFontSize((prev) => Math.max(13, prev - 1))}
            className="p-1.5 border border-border bg-surface rounded-md hover:bg-surface-2 text-fg-muted hover:text-fg transition-colors"
            title="缩小字号"
            aria-label="缩小字号"
          >
            <ZoomOut className="w-3.5 h-3.5" />
          </button>
          <span className="font-mono tabular-nums text-xs w-6 text-center text-fg">
            {fontSize}
          </span>
          <button
            type="button"
            onClick={() => onUpdateFontSize((prev) => Math.min(22, prev + 1))}
            className="p-1.5 border border-border bg-surface rounded-md hover:bg-surface-2 text-fg-muted hover:text-fg transition-colors"
            title="放大字号"
            aria-label="放大字号"
          >
            <ZoomIn className="w-3.5 h-3.5" />
          </button>
          <button
            type="button"
            onClick={onCycleLineHeight}
            className="ml-0.5 px-2 py-1 border border-border bg-surface rounded-md hover:bg-surface-2 text-fg-muted hover:text-fg font-mono text-[11px] inline-flex items-center gap-1 transition-colors"
            title="切换行距（1.65 / 1.8 / 2.0）"
            aria-label="切换阅读行距"
          >
            <AlignJustify className="w-3 h-3" />
            <span className="hidden sm:inline">{lineHeight}</span>
          </button>
        </div>
      </div>

      {/* Reading Content Area */}
      <div
        ref={containerRef}
        className={`flex-1 p-5 sm:p-7 ${
          isPrintMode ? "overflow-visible space-y-8" : "overflow-y-auto overscroll-contain"
        } select-text text-fg`}
      >
        {displayPassages.map((p) => {
          const isCloze =
            p.title.includes("Use of English") ||
            p.title.includes("完型") ||
            p.content.includes("[1]");
          const paras = p.content
            .split(/\n\s*\n/)
            .filter((x: string) => x.trim().length > 0);

          return (
            <div key={p.id} className="space-y-4">
              <div className="flex items-center justify-between pb-2.5 border-b border-border/80">
                <h4 className="font-bold text-sm tracking-wide text-fg font-sans">
                  {p.title}
                </h4>
                <span className="text-[11px] text-fg-subtle no-print font-sans shrink-0">
                  双击查词 · 划选高亮
                </span>
              </div>

              <div
                style={{ fontSize: `${fontSize}px`, lineHeight: String(lineHeight) }}
                className="reading-prose text-justify select-text text-fg"
              >
                {isCloze && onBlankClick ? (
                  <div className="space-y-4">
                    {paras.map((paraText: string, pIdx: number) => {
                      const tokens = paraText.split(/(\[\s*\d+\s*\])/g);
                      return (
                        <p key={pIdx}>
                          {tokens.map((token: string, tIdx: number) => {
                            const match = token.match(/\[\s*(\d+)\s*\]/);
                            if (match) {
                              const blankNum = Number.parseInt(match[1], 10);
                              const qIdx = blankNum - 1;
                              const targetQ = questions[qIdx];
                              const qId = targetQ?.id;
                              const userAns = qId ? answers[qId] : undefined;
                              const isFocused = focusedIndex === qIdx;
                              const isCorrect =
                                isSubmitted &&
                                userAns &&
                                userAns === targetQ?.correct_answer;
                              const isWrong =
                                isSubmitted &&
                                userAns &&
                                userAns !== targetQ?.correct_answer;

                              return (
                                <button
                                  type="button"
                                  key={`b-${tIdx}`}
                                  id={`cloze-blank-${blankNum}`}
                                  onClick={() => onBlankClick(blankNum)}
                                  title={`点击定位作答第 ${blankNum} 题`}
                                  className={`inline-flex items-center justify-center font-mono font-bold mx-1 px-2 py-0.5 rounded-lg text-xs transition-all duration-150 cursor-pointer select-none active:scale-95 ${
                                    isSubmitted
                                      ? isCorrect
                                        ? "bg-success-soft text-success border border-success/50"
                                        : isWrong
                                          ? "bg-danger-soft text-danger border border-danger/50"
                                          : "bg-surface-2 text-fg-subtle border border-border"
                                      : isFocused
                                        ? "bg-primary text-primary-fg ring-2 ring-primary/40 shadow-1"
                                        : userAns
                                          ? "bg-primary-soft text-primary border border-primary/30"
                                          : "bg-surface-2 text-fg-muted border border-border hover:border-primary/50"
                                  }`}
                                >
                                  [{blankNum}
                                  {userAns ? `: ${userAns}` : ""}]
                                </button>
                              );
                            }
                            return <span key={`t-${tIdx}`}>{token}</span>;
                          })}
                        </p>
                      );
                    })}
                  </div>
                ) : (
                  <PassageHighlighter
                    passageId={p.id}
                    content={p.content}
                    className="text-justify"
                  />
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Mobile Return to Questions Bar */}
      <div className="lg:hidden p-3 border-t border-border bg-surface-2/80 flex justify-between items-center shrink-0 no-print">
        <span className="text-xs text-fg-muted">阅读完毕？随时返回作答</span>
        <button
          type="button"
          onClick={onReturnToQuestions}
          className="px-4 py-1.5 rounded-xl bg-primary text-primary-fg text-xs font-bold shadow-1 flex items-center gap-1.5 active:scale-95"
        >
          <span>{returnLabel}</span>
          <FileText className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
}
