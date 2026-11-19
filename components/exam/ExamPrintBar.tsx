"use client";

import Link from "next/link";
import type { ExamRecord } from "@/types/exam";
import { Button } from "@/components/ui/Button";
import { Printer } from "lucide-react";

interface ExamPrintBarProps {
  exam: ExamRecord;
  showPrintAnswers: boolean;
  onTogglePrintAnswers: (checked: boolean) => void;
}

export default function ExamPrintBar({
  exam,
  showPrintAnswers,
  onTogglePrintAnswers,
}: ExamPrintBarProps) {
  return (
    <>
      <div className="bg-warning-soft border border-warning/30 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 no-print">
        <div className="flex items-center gap-2.5 text-xs text-fg">
          <Printer className="w-4 h-4 text-warning shrink-0" />
          <div>
            <span className="font-bold">纸质打印模式（已暂停计时）</span>
            <span className="text-fg-muted ml-2">
              已展开全部篇章与试题，支持直接浏览器打印或另存为 PDF
            </span>
          </div>
        </div>
        <div className="flex flex-wrap items-center gap-3">
          <label className="inline-flex items-center gap-2 text-xs font-semibold text-fg cursor-pointer select-none">
            <input
              type="checkbox"
              checked={showPrintAnswers}
              onChange={(e) => onTogglePrintAnswers(e.target.checked)}
              className="rounded border-border text-primary focus:ring-primary"
            />
            <span>打印附带参考答案与精析</span>
          </label>
          <Button size="sm" onClick={() => window.print()}>
            <Printer className="w-3.5 h-3.5" />
            <span>立即打印 / 导出 PDF</span>
          </Button>
          <Link
            href={`/exam?id=${exam.id}`}
            className="px-3 py-1.5 rounded-xl border border-border bg-surface hover:bg-surface-2 text-fg text-xs font-semibold transition-colors"
          >
            切换到限时模考
          </Link>
        </div>
      </div>

      {/* Print-only Paper Header */}
      <div className="hidden print-only border-b border-border pb-3 mb-4">
        <h1 className="text-xl font-bold">{exam.title}</h1>
        <p className="text-xs text-fg-muted mt-1">
          {exam.category_id} · {exam.year} 年 · 限时 {exam.duration_minutes || 75} 分钟 · 满分{" "}
          {exam.total_score || 60} 分
        </p>
      </div>
    </>
  );
}
