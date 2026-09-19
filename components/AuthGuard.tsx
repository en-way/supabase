"use client";

import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";

export default function AuthGuard({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [isAuthenticated, setIsAuthenticated] = useState<boolean | null>(null);

  useEffect(() => {
    async function checkAuth() {
      const { data: { session } } = await supabase.auth.getSession();
      if (!session && pathname !== "/login") {
        setIsAuthenticated(false);
        router.replace("/login");
      } else {
        setIsAuthenticated(true);
      }
    }
    checkAuth();

    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (!session && pathname !== "/login") {
        setIsAuthenticated(false);
        router.replace("/login");
      } else if (session) {
        setIsAuthenticated(true);
      }
    });

    return () => subscription.unsubscribe();
  }, [pathname, router]);

  // If on login page, render directly
  if (pathname === "/login") {
    return <>{children}</>;
  }

  // Loading state
  if (isAuthenticated === null) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mb-4" />
        <p className="text-sm font-medium text-slate-500">验证学员身份中...</p>
      </div>
    );
  }

  // If authenticated, render app
  return <>{children}</>;
}
