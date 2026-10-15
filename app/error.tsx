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
      <div className="max-w-md w-full bg-white dark:bg-[#11131a] rounded-3xl border border-slate-200 dark:border-cyan-500/25 shadow-xl p-8 text-center space-y-5 animate-in fade-in zoom-in-95 duration-200">
        <div className={`w-16 h-16 rounded-2xl flex items-center justify-center mx-auto ${
          isChunkError 
            ? "bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-500/30 text-amber-500 dark:text-amber-400"
            : "bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-500/30 text-rose-500 dark:text-rose-400"
        }`}>
          {isChunkError ? (
            <RefreshCw className={`w-8 h-8 ${isAutoReloading ? "animate-spin" : ""}`} />
          ) : (
            <AlertTriangle className="w-8 h-8" />
          )}
        </div>

        <div className="space-y-2">
          <h2 className="text-xl font-black text-slate-900 dark:text-zinc-100 font-serif">
            {isChunkError ? "检测到系统新版本发布" : "页面运行遇到意外异常"}
          </h2>
          <p className="text-xs text-slate-500 dark:text-zinc-400 leading-relaxed">
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
            <div className="mt-3 p-2.5 bg-slate-50 dark:bg-zinc-900 rounded-xl border border-slate-200/80 dark:border-zinc-800 text-[11px] text-slate-600 dark:text-zinc-400 font-mono text-left break-all max-h-24 overflow-y-auto">
              {error.message}
            </div>
          )}
        </div>

        <div className="flex items-center justify-center gap-3 pt-2">
          <button
            onClick={handleReload}
            className="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>重新载入</span>
          </button>

          <Link
            href="/"
            className="px-4 py-2.5 rounded-xl border border-slate-200 dark:border-zinc-700 hover:bg-slate-50 dark:hover:bg-zinc-800 text-slate-700 dark:text-zinc-300 text-xs font-bold flex items-center space-x-1.5 transition-all"
          >
            <Home className="w-3.5 h-3.5" />
            <span>返回真题大厅</span>
          </Link>
        </div>
      </div>
    </div>
  );
}
