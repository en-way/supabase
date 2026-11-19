"use client";

import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import {
  getLastLocalUserId,
  setLastLocalUserId,
  isLoginSyncInProgress,
} from "@/lib/storage";
import { Skeleton } from "@/components/ui/Feedback";

const KNOWN_STATIC_ROUTES = /^\/(mistakes|vocabulary|profile|exam|practice|login|admin)$/;

function normalizeRouteTrailingSlash(pathname: string): string {
  return KNOWN_STATIC_ROUTES.test(pathname) ? `${pathname}/` : pathname;
}

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

    return normalizeRouteTrailingSlash(parsed.pathname) + parsed.search;
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
        const {
          data: { session },
        } = await supabase.auth.getSession();
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

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
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

  const isLoginPage =
    pathname === "/login" || pathname === "/login/" || pathname?.startsWith("/login");

  // 2. Pure route protection and redirection (0 Supabase API calls on navigation)
  useEffect(() => {
    if (isAuthenticated === null) return;

    if (!isAuthenticated && !isLoginPage) {
      const currentPath =
        typeof window !== "undefined" ? window.location.pathname : pathname;
      const currentSearch =
        typeof window !== "undefined" ? window.location.search : "";
      const normalizedPath = normalizeRouteTrailingSlash(currentPath || "/");
      const currentUrl = normalizedPath + currentSearch;
      const redirectUrl =
        currentUrl && currentUrl !== "/" && currentUrl !== "/login/"
          ? `/login/?redirect=${encodeURIComponent(currentUrl)}`
          : "/login/";
      router.replace(redirectUrl);
    } else if (isAuthenticated && isLoginPage && !loginSyncing) {
      router.replace(getSafeRedirectTarget());
    }
  }, [pathname, router, isAuthenticated, isLoginPage, loginSyncing]);

  // 1. If on login page, render only if NOT authenticated or while login sync is finishing
  if (isLoginPage) {
    return isAuthenticated === true && !loginSyncing ? null : <>{children}</>;
  }

  // 2. Structural app skeleton while checking session (prevents full-screen splash flash)
  if (isAuthenticated === null) {
    return (
      <div
        aria-busy="true"
        aria-label="正在校验登录状态"
        className="min-h-screen flex flex-col bg-bg text-fg z-blocking"
      >
        <div className="h-16 border-b border-border bg-surface/85 px-4 sm:px-6 flex items-center justify-between">
          <div className="max-w-7xl w-full mx-auto flex items-center justify-between">
            <div className="flex items-center gap-6">
              <div className="flex items-center gap-2.5">
                <Skeleton className="w-8 h-8 rounded-md" />
                <div className="space-y-1">
                  <Skeleton className="w-16 h-3.5" />
                  <Skeleton className="w-20 h-2.5" />
                </div>
              </div>
              <Skeleton className="hidden md:block w-64 h-8 rounded-md" />
            </div>
            <div className="flex items-center gap-2">
              <Skeleton className="w-9 h-9 rounded-md" />
              <Skeleton className="w-24 h-9 rounded-full" />
            </div>
          </div>
        </div>
        <div className="max-w-7xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
          <Skeleton className="w-full h-32 rounded-lg" />
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <Skeleton className="h-44 rounded-lg" />
            <Skeleton className="h-44 rounded-lg" />
            <Skeleton className="h-44 rounded-lg hidden lg:block" />
          </div>
        </div>
      </div>
    );
  }

  // 3. Unauthenticated non-login pages: wait for redirect cleanly
  if (!isAuthenticated) {
    return null;
  }

  return <>{children}</>;
}
