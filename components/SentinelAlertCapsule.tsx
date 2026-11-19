"use client";

import { useState, useEffect, useRef } from "react";
import { ShieldAlert, RotateCcw } from "lucide-react";
import { SentinelAlertDetail, resetSentinelState } from "@/lib/quotaSentinel";

export default function SentinelAlertCapsule() {
  const [alert, setAlert] = useState<SentinelAlertDetail | null>(null);
  const [countdown, setCountdown] = useState<number>(0);
  const expiresAtRef = useRef<number>(0);

  useEffect(() => {
    const handleAlert = (e: Event) => {
      const detail = (e as CustomEvent<SentinelAlertDetail>).detail;
      if (!detail) return;
      expiresAtRef.current = Date.now() + Math.max(0, detail.remainingCooldownSeconds) * 1000;
      setAlert(detail);
      setCountdown(detail.remainingCooldownSeconds);
    };

    window.addEventListener("enway_sentinel_alert", handleAlert);
    return () => {
      window.removeEventListener("enway_sentinel_alert", handleAlert);
    };
  }, []);

  useEffect(() => {
    if (alert?.state !== "OPEN") {
      return;
    }

    const timer = setInterval(() => {
      const rem = Math.max(0, Math.ceil((expiresAtRef.current - Date.now()) / 1000));
      setCountdown(rem);
      if (rem <= 0) {
        clearInterval(timer);
      }
    }, 1000);

    return () => clearInterval(timer);
  }, [alert?.state]);

  if (!alert || alert.state === "CLOSED" || countdown <= 0) {
    return null;
  }

  return (
    <aside
      aria-live="polite"
      className="fixed bottom-[calc(var(--bottom-nav-h)+var(--safe-bottom)+0.75rem)] md:bottom-5 right-4 sm:right-5 left-4 sm:left-auto z-toast sm:max-w-sm animate-in fade-in slide-in-from-bottom-5 duration-200 pointer-events-auto"
    >
      <div className="bg-surface text-fg p-4 rounded-xl shadow-pop border border-warning/40 space-y-2.5">
        <div className="flex items-start justify-between gap-3">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-md bg-warning-soft text-warning flex items-center justify-center shrink-0">
              <ShieldAlert className="w-4 h-4" />
            </div>
            <div>
              <h4 className="text-xs font-bold tracking-wide text-fg">流量防刷保护生效中</h4>
              <p className="text-[11px] text-fg-muted">检测到短时间高频请求，已暂停云端同步</p>
            </div>
          </div>

          <span className="px-2 py-0.5 rounded-full bg-warning-soft text-warning font-mono text-[11px] font-bold shrink-0">
            {countdown}s
          </span>
        </div>

        <p className="text-[11px] text-fg-muted leading-relaxed">
          为杜绝异常死循环或脚本消耗免费配额，系统已临时阻断非关键 API。您的本地作答进度完好无损，{countdown} 秒后自动恢复。
        </p>

        <div className="pt-2 flex items-center justify-between border-t border-border text-[10px] text-fg-subtle">
          <span className="font-mono">峰值速率: {alert.currentWindowRps} req/s</span>
          <button
            type="button"
            onClick={() => {
              resetSentinelState();
              setAlert(null);
            }}
            className="text-warning hover:underline font-semibold inline-flex items-center gap-1 transition-colors"
          >
            <RotateCcw className="w-3 h-3" />
            <span>立即解除限制</span>
          </button>
        </div>
      </div>
    </aside>
  );
}
