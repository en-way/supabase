"use client";

import Link from "next/link";
import type { ExamRecord, QuestionRecord } from "@/types/exam";
import type { ExamResult } from "@/lib/storage";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { ArrowLeft, BookOpenCheck, Clock, RotateCcw } from "lucide-react";

interface ExamResultSummaryProps {
  exam: ExamRecord;
  result: ExamResult;
  questions: QuestionRecord[];
  totalQuestions: number;
  standalone?: boolean;
  onEnterReview?: () => void;
  onRetake?: () => void;
}

interface SectionBreakdown {
  key: string;
  label: string;
  totalCount: number;
  correctCount: number;
  answeredCount: number;
  earnedScore: number;
  maxScore: number;
}

function buildSectionBreakdown(
  questions: QuestionRecord[],
  answers: ExamResult["answers"]
): SectionBreakdown[] {
  const defs = [
    { key: "cloze", label: "Section I · 完形填空 (1-20)", list: questions.slice(0, 20) },
    { key: "partA", label: "Section II · Part A 阅读 (21-40)", list: questions.slice(20, 40) },
    {
      key: "partB",
      label: `Section II · Part B 新题型 (41-${questions.length})`,
      list: questions.slice(40),
    },
  ];

  return defs
    .filter((d) => d.list.length > 0)
    .map((d) => {
      let correctCount = 0;
      let answeredCount = 0;
      let earnedScore = 0;
      let maxScore = 0;

      d.list.forEach((q) => {
        const pts = q.points !== undefined && q.points !== null ? Number(q.points) : 2.0;
        maxScore += pts;
        const entry = answers?.[q.id];
        if (entry?.userAnswer) answeredCount += 1;
        if (entry?.isCorrect) {
          correctCount += 1;
          earnedScore += pts;
        }
      });

      return {
        key: d.key,
        label: d.label,
        totalCount: d.list.length,
        correctCount,
        answeredCount,
        earnedScore: Math.round(earnedScore * 10) / 10,
        maxScore: Math.round(maxScore * 10) / 10,
      };
    });
}

export default function ExamResultSummary({
  exam,
  result,
  questions,
  totalQuestions,
  standalone = false,
  onEnterReview,
  onRetake,
}: ExamResultSummaryProps) {
  const answerEntries = Object.values(result.answers || {});
  const correctCount = answerEntries.filter((a) => a?.isCorrect).length;
  const answeredCount = answerEntries.filter((a) => Boolean(a?.userAnswer)).length;
  const accuracy =
    totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
  const totalScore = result.totalScore || exam.total_score || 60;
  const passScore =
    exam.pass_score && exam.total_score === totalScore
      ? exam.pass_score
      : Math.round(totalScore * 0.6);

  const sections = buildSectionBreakdown(questions, result.answers || {});
  const mins = Math.floor(result.durationSeconds / 60);
  const secs = result.durationSeconds % 60;

  if (standalone) {
    return (
      <div className="max-w-3xl mx-auto py-4 sm:py-8 animate-in fade-in zoom-in-95 duration-200 no-print">
        <Card className="p-6 sm:p-8 space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-5 pb-6 border-b border-border">
            <div className="flex items-center gap-4 sm:gap-5">
              <div
                className={`w-20 h-20 sm:w-24 sm:h-24 rounded-2xl flex flex-col items-center justify-center border shrink-0 font-mono tabular-nums ${
                  result.isPassed
                    ? "bg-success-soft border-success/40 text-success"
                    : "bg-danger-soft border-danger/40 text-danger"
                }`}
              >
                <span className="text-3xl sm:text-4xl font-black leading-none">
                  {result.score}
                </span>
                <span className="text-[11px] font-semibold mt-1 opacity-80">
                  / {totalScore} 分
                </span>
              </div>

              <div className="space-y-1.5 min-w-0">
                <div className="flex flex-wrap items-center gap-2">
                  <Badge tone={result.isPassed ? "success" : "danger"}>
                    {result.isPassed ? "达到合格线" : "未达合格基准分（需重点攻关）"}
                  </Badge>
                  <span className="text-xs text-fg-subtle font-mono tabular-nums">
                    及格线：{passScore} 分
                  </span>
                </div>
                <h2 className="text-lg sm:text-xl font-bold text-fg leading-snug">
                  {result.examTitle} · 全真模考成绩报告
                </h2>
                <p className="text-xs text-fg-muted flex items-center gap-1.5">
                  <Clock className="w-3.5 h-3.5 text-fg-subtle shrink-0" />
                  <span>
                    答题用时：{mins} 分 {secs} 秒 · 错题与未答题目已自动归入“智能错题集”
                  </span>
                </p>
              </div>
            </div>
          </div>

          {/* Core Metrics */}
          <div className="grid grid-cols-3 gap-3">
            <div className="p-3.5 rounded-xl bg-surface-2 border border-border text-center">
              <span className="text-[11px] text-fg-subtle block">全卷正确率</span>
              <span className="text-xl sm:text-2xl font-bold font-mono tabular-nums text-primary mt-0.5 block">
                {accuracy}%
              </span>
            </div>
            <div className="p-3.5 rounded-xl bg-surface-2 border border-border text-center">
              <span className="text-[11px] text-fg-subtle block">答对 / 总题数</span>
              <span className="text-xl sm:text-2xl font-bold font-mono tabular-nums text-fg mt-0.5 block">
                {correctCount} / {totalQuestions}
              </span>
            </div>
            <div className="p-3.5 rounded-xl bg-surface-2 border border-border text-center">
              <span className="text-[11px] text-fg-subtle block">已作答 / 未答</span>
              <span className="text-xl sm:text-2xl font-bold font-mono tabular-nums text-fg mt-0.5 block">
                {answeredCount} / {Math.max(0, totalQuestions - answeredCount)}
              </span>
            </div>
          </div>

          {/* Per-Section Score Breakdown */}
          {sections.length > 0 && (
            <div className="space-y-3">
              <h3 className="text-xs font-bold uppercase tracking-wider text-fg-subtle">
                分题型得分明细
              </h3>
              <div
                className={`grid grid-cols-1 gap-3 ${
                  sections.length === 2 ? "sm:grid-cols-2" : "sm:grid-cols-3"
                }`}
              >
                {sections.map((sec) => {
                  const pct =
                    sec.maxScore > 0 ? Math.round((sec.earnedScore / sec.maxScore) * 100) : 0;
                  return (
                    <div
                      key={sec.key}
                      className="p-4 rounded-xl bg-surface-2/80 border border-border space-y-2.5"
                    >
                      <div className="text-xs font-bold text-fg leading-snug">{sec.label}</div>
                      <div className="flex items-baseline justify-between font-mono tabular-nums">
                        <span className="text-lg font-extrabold text-fg">
                          {sec.earnedScore}{" "}
                          <span className="text-xs font-normal text-fg-subtle">
                            / {sec.maxScore} 分
                          </span>
                        </span>
                        <span className="text-[11px] text-fg-muted">
                          对 {sec.correctCount}/{sec.totalCount} 题
                        </span>
                      </div>
                      <ProgressBar value={pct} max={100} tone="primary" />
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* Action Buttons */}
          <div className="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center justify-center gap-3">
            {onEnterReview && (
              <Button size="md" onClick={onEnterReview} className="sm:min-w-[180px] px-5 py-2.5">
                <BookOpenCheck className="w-4 h-4" />
                <span>进入逐题复盘</span>
              </Button>
            )}
            {onRetake && (
              <Button variant="secondary" size="md" onClick={onRetake} className="px-5 py-2.5">
                <RotateCcw className="w-4 h-4" />
                <span>重新测验</span>
              </Button>
            )}
            <Link
              href="/"
              className="inline-flex items-center justify-center gap-2 min-h-11 sm:min-h-10 rounded-md border border-border bg-surface hover:bg-surface-2 px-5 py-2.5 text-xs sm:text-sm font-semibold text-fg-muted hover:text-fg transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>返回真题大厅</span>
            </Link>
          </div>
        </Card>
      </div>
    );
  }

  return (
    <Card className="p-5 sm:p-7 space-y-4 animate-in fade-in zoom-in-95 duration-200 no-print">
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
              答题耗时：{mins} 分 {secs} 秒 · 做错小题已自动归入“智能错题集”
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

      {sections.length > 0 && (
        <div
          className={`pt-4 border-t border-border grid grid-cols-1 gap-2.5 ${
            sections.length === 2 ? "sm:grid-cols-2" : "sm:grid-cols-3"
          }`}
        >
          {sections.map((sec) => (
            <div
              key={sec.key}
              className="px-3.5 py-2.5 rounded-xl bg-surface-2/70 border border-border flex items-center justify-between gap-2 text-xs"
            >
              <span className="font-semibold text-fg-muted truncate">{sec.label}</span>
              <span className="font-mono tabular-nums font-bold text-fg shrink-0">
                {sec.earnedScore}/{sec.maxScore}分 ({sec.correctCount}/{sec.totalCount})
              </span>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}
