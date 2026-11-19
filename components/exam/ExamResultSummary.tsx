"use client";

import type { ExamRecord } from "@/types/exam";
import type { ExamResult } from "@/lib/storage";
import { Badge } from "@/components/ui/Badge";
import { Card } from "@/components/ui/Card";

interface ExamResultSummaryProps {
  exam: ExamRecord;
  result: ExamResult;
  totalQuestions: number;
}

export default function ExamResultSummary({
  exam,
  result,
  totalQuestions,
}: ExamResultSummaryProps) {
  const correctCount = Object.values(result.answers || {}).filter(
    (a) => a?.isCorrect
  ).length;
  const accuracy =
    totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
  const totalScore = result.totalScore || 60;
  const passScore = exam.pass_score || Math.round(totalScore * 0.6);

  return (
    <Card className="p-5 sm:p-8 animate-in fade-in zoom-in-95 duration-200 no-print">
      <div className="flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="flex items-center gap-4 sm:gap-5">
          <div
            className={`w-16 h-16 sm:w-20 sm:h-20 rounded-2xl flex items-center justify-center text-2xl sm:text-3xl font-black font-mono tabular-nums border shrink-0 ${
              result.isPassed
                ? "bg-success-soft border-success/40 text-success"
                : "bg-danger-soft border-danger/40 text-danger"
            }`}
          >
            {result.score}
          </div>
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <Badge tone={result.isPassed ? "success" : "danger"}>
                {result.isPassed ? "达到合格线" : "未达合格基准分（需重点攻关）"}
              </Badge>
              <span className="text-xs text-fg-subtle font-mono tabular-nums">
                满分 {totalScore} 分（及格线：{passScore} 分）
              </span>
            </div>
            <h3 className="text-base sm:text-lg font-bold mt-1 text-fg">
              {result.examTitle} 测评报告
            </h3>
            <p className="text-xs text-fg-muted mt-1">
              答题耗时：{Math.floor(result.durationSeconds / 60)} 分{" "}
              {result.durationSeconds % 60} 秒 · 做错小题已自动归入“智能错题集”
            </p>
          </div>
        </div>

        <div className="flex items-center gap-4 bg-surface-2 px-4 py-3.5 rounded-xl border border-border shrink-0">
          <div className="text-center px-2 sm:px-3">
            <span className="text-[11px] text-fg-subtle block">答对题数</span>
            <span className="text-lg sm:text-xl font-bold font-mono tabular-nums text-fg">
              {correctCount} / {totalQuestions}
            </span>
          </div>
          <div className="h-8 w-px bg-border" />
          <div className="text-center px-2 sm:px-3">
            <span className="text-[11px] text-fg-subtle block">得分率</span>
            <span className="text-lg sm:text-xl font-bold font-mono tabular-nums text-primary">
              {accuracy}%
            </span>
          </div>
        </div>
      </div>
    </Card>
  );
}
