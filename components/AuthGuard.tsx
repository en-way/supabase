"use client";

import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import {
  getLastLocalUserId,
  setLastLocalUserId,
  isLoginSyncInProgress,
} from "@/lib/storage";
import { ShieldCheck, BookOpen } from "lucide-react";

function getSafeRedirectTarget(): string {
  if (typeof window === "undefined") return "/";
  try {
    const params = new URLSearchParams(window.location.search);
    const r = params.get("redirect");
    if (!r) return "/";

    if (r.startsWith("//") || r.startsWith("/\\") || r.includes("\\")) {
      return "/";
    }

    const parsed = new URL(r, window.location.origin);
    if (parsed.origin !== window.location.origin) {
      return "/";
    }

    if (parsed.pathname === "/login" || parsed.pathname === "/login/" || parsed.pathname.startsWith("/login")) {
      return "/";
    }

    return parsed.pathname + parsed.search;
  } catch {
    return "/";
  }
}

export default function AuthGuard({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [isAuthenticated, setIsAuthenticated] = useState<boolean | null>(null);
  const [loginSyncing, setLoginSyncing] = useState<boolean>(() => isLoginSyncInProgress());

  useEffect(() => {
    const syncState = () => {
      setLoginSyncing(isLoginSyncInProgress());
    };
    syncState();
    window.addEventListener("enway_login_sync_changed", syncState);
    return () => {
      window.removeEventListener("enway_login_sync_changed", syncState);
    };
  }, []);

  useEffect(() => {
    if (!loginSyncing) return;
    const timer = setTimeout(() => {
      setLoginSyncing(isLoginSyncInProgress());
    }, 30_500);
    return () => clearTimeout(timer);
  }, [loginSyncing]);

  // 1. Single-mount auth state initialization & listener (0 network churn on route changes)
  useEffect(() => {
    let isMounted = true;

    async function initAuth() {
      try {
        const { data: { session } } = await supabase.auth.getSession();
        if (!isMounted) return;
        if (session?.user?.id && !getLastLocalUserId()) {
          setLastLocalUserId(session.user.id);
        }
        setIsAuthenticated(Boolean(session?.user));
      } catch {
        if (!isMounted) return;
        setIsAuthenticated(false);
      }
    }
    initAuth();

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      if (!isMounted) return;
      if (session?.user?.id && !getLastLocalUserId()) {
        setLastLocalUserId(session.user.id);
      }
      setIsAuthenticated(Boolean(session?.user));
    });

    return () => {
      isMounted = false;
      subscription.unsubscribe();
    };
  }, []);

  const isLoginPage = pathname === "/login" || pathname === "/login/" || pathname?.startsWith("/login");

  // 2. Pure route protection and redirection (0 Supabase API calls on navigation)
  useEffect(() => {
    if (isAuthenticated === null) return;

    if (!isAuthenticated && !isLoginPage) {
      const currentUrl = typeof window !== "undefined"
        ? window.location.pathname + window.location.search
        : pathname;
      const redirectUrl = currentUrl && currentUrl !== "/" && currentUrl !== "/login" && currentUrl !== "/login/"
        ? `/login?redirect=${encodeURIComponent(currentUrl)}`
        : "/login";
      router.replace(redirectUrl);
    } else if (isAuthenticated && isLoginPage && !loginSyncing) {
      router.replace(getSafeRedirectTarget());
    }
  }, [pathname, router, isAuthenticated, isLoginPage, loginSyncing]);

  // 1. If on login page, render only if NOT authenticated or while login sync is finishing
  if (isLoginPage) {
    return isAuthenticated === true && !loginSyncing ? null : <>{children}</>;
  }

  // 2. Loading transition screen while checking session
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

  // 3. Prevent protected content flash when unauthenticated
  if (isAuthenticated === false) {
    return null;
  }

  // 4. If authenticated, render protected children
  return <>{children}</>;
}
