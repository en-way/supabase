"use client";

import { useState, useEffect } from "react";
import { ShieldAlert, AlertTriangle, CheckCircle2, RotateCcw } from "lucide-react";
import { SentinelAlertDetail, resetSentinelState } from "@/lib/quotaSentinel";

export default function SentinelAlertCapsule() {
  const [alert, setAlert] = useState<SentinelAlertDetail | null>(null);
  const [countdown, setCountdown] = useState<number>(0);

  useEffect(() => {
    const handleAlert = (e: any) => {
      const detail: SentinelAlertDetail = e.detail;
      setAlert(detail);
      setCountdown(detail.remainingCooldownSeconds);
    };

    window.addEventListener("enway_sentinel_alert", handleAlert);
    return () => {
      window.removeEventListener("enway_sentinel_alert", handleAlert);
    };
  }, []);

  // Cooldown countdown timer
  useEffect(() => {
    if (countdown <= 0) {
      if (alert?.state === "OPEN") {
        setAlert((prev) => (prev ? { ...prev, state: "CLOSED" } : null));
      }
      return;
    }

    const timer = setInterval(() => {
      setCountdown((c) => {
        if (c <= 1) {
          clearInterval(timer);
          return 0;
        }
        return c - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [countdown, alert?.state]);

  // Only render when circuit breaker is active (OPEN) or has countdown
  if (!alert || alert.state === "CLOSED" || countdown <= 0) {
    return null;
  }

  return (
    <aside
      aria-live="polite"
      className="fixed bottom-5 right-5 z-50 max-w-sm w-full animate-in fade-in slide-in-from-bottom-5 duration-300 pointer-events-auto"
    >
      <div className="bg-amber-950/90 dark:bg-stone-900/95 text-white p-4 rounded-2xl shadow-2xl border border-amber-500/40 dark:border-amber-400/30 backdrop-blur-xl space-y-2.5">
        <div className="flex items-start justify-between gap-3">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0">
              <ShieldAlert className="w-4 h-4 animate-pulse" />
            </div>
            <div>
              <h4 className="text-xs font-bold tracking-wide text-amber-200">
                流量防刷保护生效中
              </h4>
              <p className="text-[11px] text-amber-300/80">
                检测到短时间高频请求，已暂停云端同步
              </p>
            </div>
          </div>

          <span className="px-2 py-0.5 rounded-full bg-amber-500/30 text-amber-300 font-mono text-[11px] font-bold shrink-0">
            {countdown}s
          </span>
        </div>

        <p className="text-[11px] text-stone-300 dark:text-stone-400 leading-relaxed">
          为杜绝异常死循环或脚本消耗免费配额，系统已临时阻断非关键 API。您的本地作答进度完好无损，{countdown} 秒后自动恢复。
        </p>

        <div className="pt-1 flex items-center justify-between border-t border-white/10 text-[10px] text-stone-400">
          <span>峰值速率: {alert.currentWindowRps} req/s</span>
          <button
            onClick={() => {
              resetSentinelState();
              setAlert(null);
            }}
            className="text-amber-300 hover:text-amber-100 font-semibold flex items-center space-x-1 transition-colors"
          >
            <RotateCcw className="w-3 h-3 mr-0.5" />
            <span>立即解除限制</span>
          </button>
        </div>
      </div>
    </aside>
  );
}
