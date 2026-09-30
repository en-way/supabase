"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState, useEffect } from "react";
import { 
  FileText, 
  AlertCircle, 
  Bookmark, 
  User 
} from "lucide-react";
import { getLocalState } from "@/lib/storage";

export default function MobileTabBar() {
  const pathname = usePathname();
  const [unmasteredCount, setUnmasteredCount] = useState<number>(0);
  const [vocabCount, setVocabCount] = useState<number>(0);

  // Read local state for badge counts
  useEffect(() => {
    const updateCounts = () => {
      try {
        const state = getLocalState();
        if (state) {
          const unmastered = (state.mistakes || []).filter((m) => !m.isMastered).length;
          setUnmasteredCount(unmastered);
          setVocabCount((state.vocabulary || []).length);
        }
      } catch {}
    };

    updateCounts();
    window.addEventListener("storage", updateCounts);
    window.addEventListener("enway_local_state_updated", updateCounts);

    return () => {
      window.removeEventListener("storage", updateCounts);
      window.removeEventListener("enway_local_state_updated", updateCounts);
    };
  }, [pathname]);

  // Hide on Login page and Full Mock Exam page
  const isLoginPage = pathname === "/login" || pathname === "/login/" || pathname?.startsWith("/login");
  const isExamPage = pathname === "/exam" || pathname === "/exam/" || pathname?.startsWith("/exam");

  if (isLoginPage || isExamPage) {
    return null;
  }

  const navItems = [
    {
      name: "大厅",
      href: "/",
      icon: FileText,
      isActive: pathname === "/" || pathname === "",
      badge: null,
    },
    {
      name: "错题集",
      href: "/mistakes",
      icon: AlertCircle,
      isActive: pathname.startsWith("/mistakes"),
      badge: unmasteredCount > 0 ? (unmasteredCount > 99 ? "99+" : unmasteredCount) : null,
      badgeColor: "bg-rose-500 text-white",
    },
    {
      name: "生词库",
      href: "/vocabulary",
      icon: Bookmark,
      isActive: pathname.startsWith("/vocabulary"),
      badge: vocabCount > 0 ? (vocabCount > 99 ? "99+" : vocabCount) : null,
      badgeColor: "bg-emerald-600 text-white",
    },
    {
      name: "我的",
      href: "/profile",
      icon: User,
      isActive: pathname.startsWith("/profile") || pathname.startsWith("/admin"),
      badge: null,
    },
  ];

  return (
    <nav 
      aria-label="移动端底部导航"
      className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/90 dark:bg-[#090a0f]/90 backdrop-blur-xl border-t border-black/[0.06] dark:border-cyan-500/20 px-3 pt-2 pb-[max(0.6rem,env(safe-area-inset-bottom))] transition-all duration-300"
    >
      <div className="flex items-center justify-around max-w-md mx-auto">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex-1 flex flex-col items-center justify-center py-1 rounded-xl transition-all duration-150 active:scale-95 ${
                item.isActive
                  ? "text-emerald-700 dark:text-cyber-300 font-bold"
                  : "text-stone-500 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-zinc-200 font-medium"
              }`}
            >
              <div className="relative">
                <Icon className={`w-5 h-5 transition-transform ${item.isActive ? "scale-110" : ""}`} />
                {item.badge !== null && (
                  <span className={`absolute -top-1.5 -right-3 text-[10px] font-mono font-bold px-1.5 py-0.2 rounded-full ring-2 ring-white dark:ring-[#090a0f] ${item.badgeColor}`}>
                    {item.badge}
                  </span>
                )}
              </div>
              <span className={`text-[11px] mt-1 tracking-tight ${item.isActive ? "scale-105" : ""}`}>
                {item.name}
              </span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
