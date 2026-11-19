"use client";

import type { QuestionRecord } from "@/types/exam";

interface AnswerSheetSectionsProps {
  questions: QuestionRecord[];
  answers: Record<string, string>;
  activeIndex: number;
  showCorrectness: boolean;
  onJump: (index: number) => void;
  buttonSize?: "compact" | "drawer";
}

export function AnswerSheetSections({
  questions,
  answers,
  activeIndex,
  showCorrectness,
  onJump,
  buttonSize = "compact",
}: AnswerSheetSectionsProps) {
  const section1 = questions.slice(0, 20);
  const section2 = questions.slice(20, 40);
  const section3 = questions.slice(40);

  const groups = [
    { title: "Section I 英语知识运用 (完形填空 1 - 20)", list: section1, offset: 0 },
    { title: "Section II 阅读理解 Part A (传统阅读 21 - 40)", list: section2, offset: 20 },
    {
      title: `Section II 阅读理解 Part B (新题型 41 - ${questions.length})`,
      list: section3,
      offset: 40,
    },
  ].filter((g) => g.list.length > 0);

  return (
    <div className="space-y-4">
      {groups.map((group) => (
        <div key={group.title}>
          <div className="text-[11px] font-bold text-fg-subtle mb-2 uppercase tracking-wider flex items-center justify-between">
            <span>{group.title}</span>
            <span className="font-mono text-[10px] tabular-nums">
              {group.list.filter((q) => Boolean(answers[q.id])).length}/{group.list.length}
            </span>
          </div>
          <div className="grid grid-cols-5 sm:grid-cols-10 gap-1.5">
            {group.list.map((q, sIdx) => {
              const overallIdx = group.offset + sIdx;
              const uAns = answers[q.id];
              const isAns = Boolean(uAns);
              const isCorr = isAns && uAns === q.correct_answer;
              const isFocus = overallIdx === activeIndex;

              let btnStyle =
                "bg-surface-2 text-fg-muted hover:bg-border/60 hover:text-fg border border-transparent";
              if (showCorrectness) {
                if (isAns) {
                  btnStyle = isCorr
                    ? "bg-success text-white font-bold"
                    : "bg-danger text-white font-bold";
                }
              } else if (isFocus) {
                btnStyle =
                  "bg-primary text-primary-fg font-bold shadow-1 ring-2 ring-offset-2 ring-primary ring-offset-surface";
              } else if (isAns) {
                btnStyle =
                  "bg-primary-soft text-primary font-semibold border border-primary/30";
              }

              const focusRing =
                showCorrectness && isFocus
                  ? "ring-2 ring-offset-2 ring-primary ring-offset-surface scale-105 z-10"
                  : "";

              return (
                <button
                  key={q.id}
                  type="button"
                  onClick={() => onJump(overallIdx)}
                  className={`${
                    buttonSize === "drawer" ? "h-9 rounded-xl" : "py-1.5 rounded-lg"
                  } text-xs font-mono font-bold tabular-nums transition-all duration-150 flex items-center justify-center ${btnStyle} ${focusRing}`}
                  title={`第 ${overallIdx + 1} 题 ${
                    isAns
                      ? showCorrectness
                        ? isCorr
                          ? "(正确)"
                          : `(错误，选 ${uAns})`
                        : `(已作答: ${uAns})`
                      : "(未答)"
                  }`}
                >
                  {overallIdx + 1}
                </button>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}
