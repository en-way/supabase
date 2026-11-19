"use client";

import Link from "next/link";
import type { ExamRecord } from "@/types/exam";
import type { ExamResult } from "@/lib/storage";
import { formatExamTimer } from "@/hooks/useExamSession";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Kbd } from "@/components/ui/Kbd";
import {
  ArrowLeft,
  Award,
  Clock,
  Keyboard,
  Maximize2,
  Minimize2,
  Printer,
  RotateCcw,
  Send,
} from "lucide-react";

interface ExamTopBarProps {
  exam: ExamRecord;
  isPrintMode: boolean;
  isSubmitted: boolean;
  isTimeUp: boolean;
  result: ExamResult | null;
  examAccuracy: number;
  answeredCount: number;
  totalQuestions: number;
  remainingSeconds: number;
  isZenMode: boolean;
  onToggleZen: () => void;
  onOpenShortcuts: () => void;
  onRequestSubmit: () => void;
  onRetake: () => void;
}

export function ExamTopBar({
  exam,
  isPrintMode,
  isSubmitted,
  isTimeUp,
  result,
  examAccuracy,
  answeredCount,
  totalQuestions,
  remainingSeconds,
  isZenMode,
  onToggleZen,
  onOpenShortcuts,
  onRequestSubmit,
  onRetake,
}: ExamTopBarProps) {
  return (
    <div className="sticky top-16 z-sticky bg-surface/90 backdrop-blur-xl border border-border p-3.5 sm:px-6 rounded-2xl shadow-1 flex items-center justify-between gap-3 sm:gap-4 no-print transition-colors duration-200">
      <div className="flex items-center gap-3 min-w-0">
        <Link
          href="/"
          className="p-2 hover:bg-surface-2 rounded-xl text-fg-muted hover:text-fg transition-colors shrink-0"
          title="返回真题大厅"
          aria-label="返回真题大厅"
        >
          <ArrowLeft className="w-4 h-4" />
        </Link>

        <div className="min-w-0">
          <div className="flex flex-wrap items-center gap-1.5 sm:gap-2">
            <Badge tone="neutral" className="font-mono uppercase tracking-wider">
              {exam.category_id} · {exam.year}
            </Badge>

            {isSubmitted && result ? (
              <div className="flex flex-wrap items-center gap-1.5 font-mono tabular-nums">
                <Badge tone="info">模考复盘</Badge>
                <Badge tone="warning">
                  <Award className="w-3 h-3" />
                  <span>
                    得分: {result.score} / {result.totalScore}分
                  </span>
                </Badge>
                <Badge tone={result.isPassed ? "success" : "danger"}>
                  正确率: {examAccuracy}%
                </Badge>
              </div>
            ) : (
              <div className="flex items-center gap-1.5 text-xs text-fg-muted font-mono tabular-nums">
                <span className="font-bold text-fg">
                  已答 {answeredCount} / {totalQuestions} 题
                </span>
                <span className="text-[11px] text-fg-subtle hidden sm:inline">
                  （
                  {totalQuestions - answeredCount > 0
                    ? `待答 ${totalQuestions - answeredCount} 题`
                    : "已全答"}
                  ）
                </span>
              </div>
            )}

            {!isSubmitted && !isPrintMode && !isTimeUp && (
              <Badge tone="primary" className="hidden lg:inline-flex">
                <span className="w-1.5 h-1.5 rounded-full bg-primary animate-pulse" />
                <span>实时草稿保全</span>
              </Badge>
            )}
          </div>

          <h2 className="text-sm sm:text-base font-bold text-fg truncate mt-0.5">
            {exam.title}
          </h2>
        </div>
      </div>

      <div className="flex items-center gap-2 shrink-0">
        {!isPrintMode && (
          <Button
            variant={isZenMode ? "primary" : "secondary"}
            size="sm"
            onClick={onToggleZen}
            title="专注考场模式 (快捷键 Z)"
          >
            {isZenMode ? (
              <Minimize2 className="w-3.5 h-3.5" />
            ) : (
              <Maximize2 className="w-3.5 h-3.5" />
            )}
            <span className="hidden sm:inline">
              {isZenMode ? "退出专注" : "专注模式"}
            </span>
            <Kbd className="hidden lg:inline-flex">Z</Kbd>
          </Button>
        )}

        {!isPrintMode && (
          <Button
            variant="secondary"
            size="sm"
            onClick={onOpenShortcuts}
            title="PC 快捷键速查表 (快捷键 ? 或 H)"
            aria-label="PC 快捷键速查表"
            className="hidden sm:inline-flex px-2.5"
          >
            <Keyboard className="w-3.5 h-3.5" />
          </Button>
        )}

        {isPrintMode ? (
          <div className="flex items-center gap-2">
            <Link
              href={`/exam?id=${exam.id}`}
              className="px-3.5 py-1.5 rounded-xl border border-border bg-surface hover:bg-surface-2 text-fg text-xs font-semibold transition-colors"
            >
              切换到限时模考
            </Link>
            <Button size="sm" onClick={() => window.print()}>
              <Printer className="w-3.5 h-3.5" />
              <span>立即打印 / 导出 PDF</span>
            </Button>
          </div>
        ) : !isSubmitted ? (
          <>
            <div
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl font-mono tabular-nums text-xs sm:text-sm font-bold border ${
                isTimeUp
                  ? "bg-danger-soft border-danger/40 text-danger"
                  : remainingSeconds < 300
                    ? "bg-danger-soft border-danger/30 text-danger animate-pulse"
                    : "bg-surface-2 border-border text-fg"
              }`}
            >
              <Clock className="w-3.5 h-3.5" />
              <span>
                {isTimeUp ? "已到时" : formatExamTimer(remainingSeconds)}
              </span>
            </div>

            <Button
              size="sm"
              onClick={onRequestSubmit}
              disabled={isTimeUp}
            >
              <Send className="w-3.5 h-3.5" />
              <span>{isTimeUp ? "交卷中..." : "交卷核分"}</span>
            </Button>
          </>
        ) : (
          <div className="flex items-center gap-2">
            <Button variant="secondary" size="sm" onClick={onRetake}>
              <RotateCcw className="w-3.5 h-3.5" />
              <span>重新测验</span>
            </Button>
            <Button size="sm" onClick={() => window.print()}>
              <Printer className="w-3.5 h-3.5" />
              <span>纸质打印试卷</span>
            </Button>
          </div>
        )}
      </div>
    </div>
  );
}
