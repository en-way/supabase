"use client";

import { Clock, Lock } from "lucide-react";
import { Spinner } from "@/components/ui/Feedback";

interface TimeUpLockBannerProps {
  visible: boolean;
}

export function TimeUpLockBanner({ visible }: TimeUpLockBannerProps) {
  if (!visible) return null;

  return (
    <div
      role="status"
      aria-live="assertive"
      className="bg-danger-soft border border-danger/40 text-fg rounded-2xl p-4 flex items-center justify-between gap-4 shadow-1 no-print animate-in fade-in duration-150"
    >
      <div className="flex items-center gap-3 min-w-0">
        <div className="w-9 h-9 rounded-xl bg-danger text-white flex items-center justify-center shrink-0">
          <Lock className="w-4 h-4" />
        </div>
        <div className="min-w-0">
          <p className="text-sm font-bold text-danger flex items-center gap-1.5">
            <Clock className="w-4 h-4 shrink-0" />
            <span>考试时间已到，答卷已锁定并正在提交核分</span>
          </p>
          <p className="text-xs text-fg-muted mt-0.5">
            系统正在错峰排队写入您的考卷成绩与错题记录，当前已禁止修改选项，请勿关闭页面。
          </p>
        </div>
      </div>
      <Spinner className="w-5 h-5 text-danger shrink-0" />
    </div>
  );
}
