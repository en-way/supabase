"use client";

import Link from "next/link";
import type { ExamRecord } from "@/types/exam";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Kbd } from "@/components/ui/Kbd";
import { ProgressBar } from "@/components/ui/ProgressBar";
import {
  ArrowLeft,
  Award,
  CheckCircle2,
  Keyboard,
  ListOrdered,
  Maximize2,
  Minimize2,
  RotateCcw,
  Target,
  Type,
} from "lucide-react";

interface PracticeTopBarProps {
  exam: ExamRecord | null;
  currentIndex: number;
  totalQuestions: number;
  answeredCount: number;
  progressPercent: number;
  currentScore: number;
  accuracy: number;
  isZenMode: boolean;
  fontSize: number;
  onToggleZen: () => void;
  onOpenShortcuts: () => void;
  onOpenAnswerSheet: () => void;
  onResetPractice: () => void;
  onCycleFontSize: () => void;
}

export function PracticeTopBar({
  exam,
  currentIndex,
  totalQuestions,
  answeredCount,
  progressPercent,
  currentScore,
  accuracy,
  isZenMode,
  fontSize,
  onToggleZen,
  onOpenShortcuts,
  onOpenAnswerSheet,
  onResetPractice,
  onCycleFontSize,
}: PracticeTopBarProps) {
  return (
    <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-surface/90 backdrop-blur-xl p-3.5 sm:p-4 rounded-2xl border border-border shadow-1 transition-colors duration-200">
      <div className="flex items-center gap-3 min-w-0">
        <Link
          href="/"
          className="p-2 text-fg-muted hover:text-fg hover:bg-surface-2 rounded-xl transition-colors shrink-0"
          title="返回真题大厅"
          aria-label="返回真题大厅"
        >
          <ArrowLeft className="w-4 h-4" />
        </Link>
        <div className="min-w-0">
          <div className="flex items-center gap-2">
            <Badge tone="neutral" className="font-mono tracking-wide shrink-0">
              精读逐题练
            </Badge>
            <h2 className="text-sm sm:text-base font-bold text-fg truncate">
              {exam?.title}
            </h2>
          </div>

          <div className="flex flex-wrap items-center gap-2 mt-1.5 text-xs font-mono tabular-nums">
            <div className="flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-surface-2 text-fg-muted border border-border">
              <Target className="w-3 h-3 text-primary" />
              <span>
                已练 <strong className="text-fg">{answeredCount}</strong>/{totalQuestions}（
                {progressPercent}%）
              </span>
              <div className="w-12 hidden sm:block">
                <ProgressBar value={progressPercent} max={100} tone="primary" />
              </div>
            </div>

            <Badge tone="warning">
              <Award className="w-3 h-3" />
              <span>得分 {currentScore} 分</span>
            </Badge>

            <Badge tone="success">
              <CheckCircle2 className="w-3 h-3" />
              <span>正确率 {accuracy}%</span>
            </Badge>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-1.5 sm:gap-2 self-end sm:self-center shrink-0">
        <Button
          variant={isZenMode ? "primary" : "secondary"}
          size="sm"
          onClick={onToggleZen}
          title="专注全屏模式 (快捷键 Z)"
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

        <Button
          variant="secondary"
          size="sm"
          onClick={onOpenAnswerSheet}
          title="打开全卷答题卡快速跳转 (快捷键 M)"
        >
          <ListOrdered className="w-3.5 h-3.5 text-primary" />
          <span>答题卡</span>
          <span className="font-mono text-[10px] px-1.5 py-0.5 rounded-full bg-surface-2 text-fg font-bold">
            {answeredCount}/{totalQuestions}
          </span>
          <Kbd className="hidden lg:inline-flex">M</Kbd>
        </Button>

        {answeredCount > 0 && (
          <Button
            variant="secondary"
            size="sm"
            onClick={onResetPractice}
            title="清空当前做题记录重新开始"
            className="hover:text-danger hover:border-danger/40"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">重做</span>
          </Button>
        )}

        <Button
          variant="secondary"
          size="sm"
          onClick={onCycleFontSize}
          title={`切换阅读字号（当前 ${fontSize}px）`}
        >
          <Type className="w-3.5 h-3.5" />
          <span className="font-mono tabular-nums text-[11px]">{fontSize}px</span>
        </Button>

        <div className="text-xs font-bold text-fg bg-surface-2 border border-border px-2.5 py-1.5 rounded-xl font-mono tabular-nums">
          {currentIndex + 1}/{totalQuestions}
        </div>
      </div>
    </div>
  );
}
