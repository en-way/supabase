"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Card } from "@/components/ui/Card";
import { Spinner } from "@/components/ui/Feedback";
import { ArrowLeft, Compass } from "lucide-react";

const KNOWN_STATIC_ROUTES = /^\/(mistakes|vocabulary|profile|exam|practice|login|admin)$/;

export default function NotFoundPage() {
  const [isRedirecting, setIsRedirecting] = useState(false);

  useEffect(() => {
    if (typeof window === "undefined") return;
    const { pathname, search, hash } = window.location;
    if (KNOWN_STATIC_ROUTES.test(pathname)) {
      setIsRedirecting(true);
      window.location.replace(`${pathname}/${search}${hash}`);
    }
  }, []);

  if (isRedirecting) {
    return (
      <div className="py-24 flex flex-col items-center justify-center gap-3 text-fg-muted">
        <Spinner className="w-7 h-7" />
        <p className="text-sm font-medium">正在跳转到规范页面...</p>
      </div>
    );
  }

  return (
    <div className="max-w-lg mx-auto py-12 sm:py-20">
      <Card className="p-6 sm:p-8 text-center space-y-5">
        <div className="w-12 h-12 rounded-2xl bg-surface-2 border border-border text-primary mx-auto flex items-center justify-center">
          <Compass className="w-6 h-6" />
        </div>
        <div className="space-y-2">
          <p className="text-xs font-mono uppercase tracking-widest text-fg-subtle">
            404 · Page Not Found
          </p>
          <h1 className="text-lg sm:text-xl font-bold text-fg">
            未找到对应研习页面
          </h1>
          <p className="text-xs sm:text-sm text-fg-muted leading-relaxed">
            请检查访问地址是否正确，或点击下方按钮返回真题大厅继续学习。
          </p>
        </div>
        <div className="pt-1">
          <Link
            href="/"
            className="inline-flex items-center justify-center gap-2 rounded-xl bg-primary text-primary-fg px-5 py-2.5 text-sm font-semibold shadow-1 hover:opacity-95 transition-opacity"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>返回真题大厅</span>
          </Link>
        </div>
      </Card>
    </div>
  );
}
