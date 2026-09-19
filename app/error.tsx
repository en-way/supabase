"use client";

import { useEffect } from "react";
import Link from "next/link";
import { AlertTriangle, RotateCcw, Home } from "lucide-react";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("Application client-side exception caught by boundary:", error);
  }, [error]);

  return (
    <div className="min-h-[60vh] flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white rounded-3xl border border-slate-200 shadow-xl p-8 text-center space-y-5 animate-in fade-in zoom-in-95 duration-200">
        <div className="w-16 h-16 bg-rose-50 border border-rose-200 rounded-2xl flex items-center justify-center mx-auto text-rose-500">
          <AlertTriangle className="w-8 h-8" />
        </div>

        <div className="space-y-2">
          <h2 className="text-xl font-black text-slate-900 font-serif">
            页面运行遇到意外异常
          </h2>
          <p className="text-xs text-slate-500 leading-relaxed">
            系统已拦截该客户端异常并保护了您的作答数据。您可以尝试重新加载当前测验，或返回真题大厅。
          </p>
          {error?.message && (
            <div className="mt-3 p-2.5 bg-slate-50 rounded-xl border border-slate-200/80 text-[11px] text-slate-600 font-mono text-left break-all max-h-24 overflow-y-auto">
              {error.message}
            </div>
          )}
        </div>

        <div className="flex items-center justify-center gap-3 pt-2">
          <button
            onClick={() => reset()}
            className="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>重新载入</span>
          </button>

          <Link
            href="/"
            className="px-4 py-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-700 text-xs font-bold flex items-center space-x-1.5 transition-all"
          >
            <Home className="w-3.5 h-3.5" />
            <span>返回真题大厅</span>
          </Link>
        </div>
      </div>
    </div>
  );
}
