"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { WifiOff, Wifi, X } from "lucide-react";

const PROBE_TIMEOUT_MS = 4000;

export default function NetworkStatusIndicator() {
  const [isOnline, setIsOnline] = useState<boolean>(true);
  const [showRestoredNotice, setShowRestoredNotice] = useState<boolean>(false);
  const [dismissed, setDismissed] = useState<boolean>(false);

  const isOnlineRef = useRef<boolean>(true);
  const restoreTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const probeSeqRef = useRef<number>(0);
  const activeAbortRef = useRef<AbortController | null>(null);

  const triggerRestoredNotice = useCallback(() => {
    setShowRestoredNotice(true);
    if (restoreTimerRef.current) clearTimeout(restoreTimerRef.current);
    restoreTimerRef.current = setTimeout(() => {
      restoreTimerRef.current = null;
      setShowRestoredNotice(false);
    }, 3500);
  }, []);

  /**
   * Active same-origin reachability probe (0 Supabase quota).
   * Prevents false-positive offline banners in VPN/TUN/proxy/WebView environments
   * where `navigator.onLine` inaccurately reports `false`.
   */
  const verifyReachability = useCallback(
    async (notifyIfRestored: boolean) => {
      const seq = ++probeSeqRef.current;
      if (activeAbortRef.current) {
        activeAbortRef.current.abort();
      }
      const controller = new AbortController();
      activeAbortRef.current = controller;
      const timeoutId = setTimeout(() => controller.abort(), PROBE_TIMEOUT_MS);

      try {
        const res = await fetch(`/data/version.json?probe=${Date.now()}`, {
          method: "HEAD",
          cache: "no-store",
          signal: controller.signal,
        });
        if (seq !== probeSeqRef.current) return;

        // Only treat 5xx server gateway errors or thrown network errors as unreachable
        const reachable = res.ok || res.status < 500;
        if (reachable) {
          const wasOffline = !isOnlineRef.current;
          isOnlineRef.current = true;
          setIsOnline(true);
          setDismissed(false);
          if (wasOffline && notifyIfRestored) {
            triggerRestoredNotice();
          }
        } else {
          if (isOnlineRef.current) setDismissed(false);
          isOnlineRef.current = false;
          setIsOnline(false);
          setShowRestoredNotice(false);
        }
      } catch (err) {
        if (seq !== probeSeqRef.current) return;
        // Ignore aborts triggered by a newer probe or unmount
        if (controller.signal.aborted && err instanceof DOMException && err.name === "AbortError") {
          // Only timeout aborts without a newer seq mean offline
          if (seq === probeSeqRef.current) {
            if (isOnlineRef.current) setDismissed(false);
            isOnlineRef.current = false;
            setIsOnline(false);
            setShowRestoredNotice(false);
          }
          return;
        }
        if (isOnlineRef.current) setDismissed(false);
        isOnlineRef.current = false;
        setIsOnline(false);
        setShowRestoredNotice(false);
      } finally {
        clearTimeout(timeoutId);
        if (activeAbortRef.current === controller) {
          activeAbortRef.current = null;
        }
      }
    },
    [triggerRestoredNotice]
  );

  useEffect(() => {
    if (typeof window === "undefined") return;

    // On initial mount, only probe if navigator.onLine claims offline (zero cost on normal load)
    if (!navigator.onLine) {
      void verifyReachability(false);
    }

    const handleOnline = () => {
      if (!isOnlineRef.current) {
        isOnlineRef.current = true;
        setIsOnline(true);
        setDismissed(false);
        triggerRestoredNotice();
      } else {
        void verifyReachability(false);
      }
    };

    const handleOffline = () => {
      // Verify with same-origin HTTP probe before declaring offline
      void verifyReachability(true);
    };

    const handleFocus = () => {
      if (!isOnlineRef.current) {
        void verifyReachability(true);
      }
    };

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);
    window.addEventListener("focus", handleFocus);

    return () => {
      probeSeqRef.current += 1;
      if (activeAbortRef.current) {
        activeAbortRef.current.abort();
        activeAbortRef.current = null;
      }
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
      window.removeEventListener("focus", handleFocus);
      if (restoreTimerRef.current) {
        clearTimeout(restoreTimerRef.current);
        restoreTimerRef.current = null;
      }
    };
  }, [triggerRestoredNotice, verifyReachability]);

  if (!isOnline && !dismissed) {
    return (
      <div
        role="status"
        aria-live="polite"
        className="fixed left-3 right-3 sm:left-4 sm:right-auto bottom-[calc(var(--bottom-nav-h)+var(--safe-bottom)+0.75rem)] sm:bottom-4 z-toast max-w-md no-print animate-in fade-in slide-in-from-bottom-3 duration-200"
      >
        <div className="px-3.5 py-2 bg-warning text-primary-fg shadow-pop rounded-full flex items-center gap-2 text-xs font-semibold border border-border">
          <WifiOff className="w-4 h-4 shrink-0" />
          <span className="flex-1 min-w-0 leading-snug">
            网络已断开 · 离线保护已激活，作答安全保存在本地
          </span>
          <button
            type="button"
            onClick={() => setDismissed(true)}
            aria-label="关闭离线提示"
            className="p-1 -mr-1 rounded-full hover:bg-primary-fg/15 transition-colors shrink-0"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    );
  }

  if (showRestoredNotice) {
    return (
      <div
        role="status"
        aria-live="polite"
        className="fixed left-3 right-3 sm:left-4 sm:right-auto bottom-[calc(var(--bottom-nav-h)+var(--safe-bottom)+0.75rem)] sm:bottom-4 z-toast max-w-md no-print animate-in fade-in slide-in-from-bottom-3 duration-200"
      >
        <div className="px-3.5 py-2 bg-success text-primary-fg shadow-pop rounded-full flex items-center gap-2 text-xs font-semibold border border-border">
          <Wifi className="w-4 h-4 shrink-0" />
          <span className="flex-1 min-w-0 leading-snug">
            网络已恢复连接 · 本地答题数据同步就绪
          </span>
          <button
            type="button"
            onClick={() => setShowRestoredNotice(false)}
            aria-label="关闭恢复提示"
            className="p-1 -mr-1 rounded-full hover:bg-primary-fg/15 transition-colors shrink-0"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    );
  }

  return null;
}
