"use client";

import { useState, useEffect, useRef } from "react";
import { WifiOff, Wifi } from "lucide-react";

export default function NetworkStatusIndicator() {
  const [isOnline, setIsOnline] = useState<boolean>(true);
  const [showRestoredNotice, setShowRestoredNotice] = useState<boolean>(false);
  const restoreTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (typeof window === "undefined") return;

    setIsOnline(navigator.onLine);

    const handleOnline = () => {
      setIsOnline(true);
      setShowRestoredNotice(true);
      if (restoreTimerRef.current) clearTimeout(restoreTimerRef.current);
      restoreTimerRef.current = setTimeout(() => {
        setShowRestoredNotice(false);
      }, 3500);
    };

    const handleOffline = () => {
      setIsOnline(false);
      setShowRestoredNotice(false);
      if (restoreTimerRef.current) clearTimeout(restoreTimerRef.current);
    };

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
      if (restoreTimerRef.current) clearTimeout(restoreTimerRef.current);
    };
  }, []);

  if (!isOnline) {
    return (
      <div className="fixed top-3 left-1/2 -translate-x-1/2 z-toast max-w-[calc(100vw-2rem)] animate-in fade-in slide-in-from-top-4 duration-200">
        <div className="px-4 py-2 bg-warning text-primary-fg shadow-pop rounded-full flex items-center gap-2 text-xs font-semibold border border-border">
          <WifiOff className="w-4 h-4 shrink-0" />
          <span>网络已断开 · 离线保护已激活，所有作答持续安全保存在本地</span>
        </div>
      </div>
    );
  }

  if (showRestoredNotice) {
    return (
      <div className="fixed top-3 left-1/2 -translate-x-1/2 z-toast max-w-[calc(100vw-2rem)] animate-in fade-in slide-in-from-top-4 duration-200">
        <div className="px-4 py-2 bg-success text-primary-fg shadow-pop rounded-full flex items-center gap-2 text-xs font-semibold border border-border">
          <Wifi className="w-4 h-4 shrink-0" />
          <span>网络已恢复连接 · 本地答题数据同步就绪</span>
        </div>
      </div>
    );
  }

  return null;
}
