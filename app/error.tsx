"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { AlertTriangle, RotateCcw, Home, RefreshCw } from "lucide-react";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  const [isAutoReloading, setIsAutoReloading] = useState(false);

  const isChunkError =
    error?.name === "ChunkLoadError" ||
    error?.message?.includes("Loading chunk") ||
    error?.message?.includes("Failed to fetch dynamically imported module") ||
    error?.message?.includes("Importing a module script failed");

  useEffect(() => {
    console.error("Application client-side exception caught by boundary:", error);

    // Auto-heal when a new version was deployed and old chunks return 404
    if (isChunkError && typeof window !== "undefined") {
      const lastReload = Number(sessionStorage.getItem("enway_chunk_reload_ts") || "0");
      if (Date.now() - lastReload > 8000) {
        setIsAutoReloading(true);
        sessionStorage.setItem("enway_chunk_reload_ts", String(Date.now()));
        const timer = setTimeout(() => {
          window.location.reload();
        }, 1200);
        return () => clearTimeout(timer);
      }
    }
  }, [error, isChunkError]);

  const handleReload = () => {
    if (typeof window !== "undefined") {
      window.location.reload();
    } else {
      reset();
    }
  };

  return (
    <div className="min-h-[60vh] flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-surface rounded-3xl border border-border shadow-2 p-8 text-center space-y-5 animate-in fade-in zoom-in-95 duration-200">
        <div
          className={`w-16 h-16 rounded-2xl flex items-center justify-center mx-auto border ${
            isChunkError
              ? "bg-warning-soft border-warning/30 text-warning"
              : "bg-danger-soft border-danger/30 text-danger"
          }`}
        >
          {isChunkError ? (
            <RefreshCw className={`w-8 h-8 ${isAutoReloading ? "animate-spin" : ""}`} />
          ) : (
            <AlertTriangle className="w-8 h-8" />
          )}
        </div>

        <div className="space-y-2">
          <h2 className="text-xl font-black text-fg font-reading">
            {isChunkError ? "检测到系统新版本发布" : "页面运行遇到意外异常"}
          </h2>
          <p className="text-xs text-fg-muted leading-relaxed">
            {isChunkError ? (
              isAutoReloading ? (
                <span>正在自动为您重新加载页面以获取最新的前端资源与考务模块...</span>
              ) : (
                <span>系统刚刚部署了新版本更新，请点击下方按钮重新载入页面以应用最新模块。</span>
              )
            ) : (
              <span>系统已拦截该客户端异常并保护了您的作答数据。您可以尝试重新加载当前测验，或返回真题大厅。</span>
            )}
          </p>
          {error?.message && (
            <div className="mt-3 p-2.5 bg-surface-2 rounded-xl border border-border text-[11px] text-fg-muted font-mono text-left break-all max-h-24 overflow-y-auto">
              {error.message}
            </div>
          )}
        </div>

        <div className="flex items-center justify-center gap-3 pt-2">
          <button
            onClick={handleReload}
            className="px-4 py-2.5 rounded-xl bg-primary text-primary-fg hover:opacity-95 text-xs font-bold flex items-center gap-1.5 shadow-1 transition-opacity"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>重新载入</span>
          </button>

          <Link
            href="/"
            className="px-4 py-2.5 rounded-xl border border-border hover:bg-surface-2 text-fg text-xs font-bold flex items-center gap-1.5 transition-colors"
          >
            <Home className="w-3.5 h-3.5" />
            <span>返回真题大厅</span>
          </Link>
        </div>
      </div>
    </div>
  );
}
