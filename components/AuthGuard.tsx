"use client";

import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { ShieldCheck, BookOpen } from "lucide-react";

export default function AuthGuard({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [isAuthenticated, setIsAuthenticated] = useState<boolean | null>(null);

  useEffect(() => {
    let isMounted = true;

    async function checkAuth() {
      try {
        const { data: { session } } = await supabase.auth.getSession();
        if (!isMounted) return;

        if (!session && pathname !== "/login") {
          setIsAuthenticated(false);
          const currentUrl = typeof window !== "undefined"
            ? window.location.pathname + window.location.search
            : pathname;
          const redirectUrl = currentUrl && currentUrl !== "/" 
            ? `/login?redirect=${encodeURIComponent(currentUrl)}` 
            : "/login";
          router.replace(redirectUrl);
        } else {
          setIsAuthenticated(true);
        }
      } catch (err) {
        if (pathname !== "/login") {
          setIsAuthenticated(false);
          router.replace("/login");
        }
      }
    }

    checkAuth();

    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (!isMounted) return;
      if (!session && pathname !== "/login") {
        setIsAuthenticated(false);
        const currentUrl = typeof window !== "undefined"
          ? window.location.pathname + window.location.search
          : pathname;
        const redirectUrl = currentUrl && currentUrl !== "/" 
          ? `/login?redirect=${encodeURIComponent(currentUrl)}` 
          : "/login";
        router.replace(redirectUrl);
      } else if (session) {
        setIsAuthenticated(true);
      }
    });

    return () => {
      isMounted = false;
      subscription.unsubscribe();
    };
  }, [pathname, router]);

  // If on login page, render directly without blocking
  if (pathname === "/login") {
    return <>{children}</>;
  }

  // Loading transition screen while checking session
  if (isAuthenticated === null) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 dark:bg-[#0b0d13] text-zinc-800 dark:text-zinc-200 transition-colors">
        <div className="relative flex items-center justify-center mb-5">
          <div className="w-14 h-14 rounded-2xl bg-indigo-600/10 dark:bg-cyan-500/10 border border-indigo-200 dark:border-cyan-500/20 flex items-center justify-center shadow-inner">
            <BookOpen className="w-7 h-7 text-indigo-600 dark:text-cyan-400" />
          </div>
          <div className="absolute -inset-2 border-2 border-indigo-500/30 dark:border-cyan-400/30 rounded-3xl animate-ping opacity-30" />
        </div>
        <div className="flex items-center space-x-2 text-sm font-semibold tracking-wide text-zinc-700 dark:text-zinc-300">
          <ShieldCheck className="w-4 h-4 text-emerald-500" />
          <span>正在校验安全登录状态...</span>
        </div>
        <p className="text-xs text-zinc-400 dark:text-zinc-500 mt-1">
          Enway 在线英语真题平台 · 全站安全访问保护
        </p>
      </div>
    );
  }

  // If authenticated, render protected children
  return <>{children}</>;
}
