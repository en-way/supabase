"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState, useEffect } from "react";
import { FileText, AlertCircle, Bookmark, User } from "lucide-react";
import { getLocalState, subscribeLocalState, type LocalLearningState } from "@/lib/storage";

export default function MobileTabBar() {
  const pathname = usePathname();
  const [unmasteredCount, setUnmasteredCount] = useState<number>(0);
  const [vocabCount, setVocabCount] = useState<number>(0);

  useEffect(() => {
    const applyCounts = (state: LocalLearningState) => {
      try {
        const unmastered = (state.mistakes || []).filter((m) => !m.isMastered).length;
        setUnmasteredCount(unmastered);
        setVocabCount((state.vocabulary || []).length);
      } catch {}
    };

    applyCounts(getLocalState());
    return subscribeLocalState(applyCounts);
  }, [pathname]);

  const isLoginPage =
    pathname === "/login" || pathname === "/login/" || pathname?.startsWith("/login");
  const isExamPage =
    pathname === "/exam" || pathname === "/exam/" || pathname?.startsWith("/exam");
  const isPracticePage =
    pathname === "/practice" || pathname === "/practice/" || pathname?.startsWith("/practice");

  if (isLoginPage || isExamPage || isPracticePage) {
    return null;
  }

  const navItems = [
    {
      name: "大厅",
      href: "/",
      icon: FileText,
      isActive: pathname === "/" || pathname === "",
      badge: null as string | number | null,
      badgeClass: "",
    },
    {
      name: "错题集",
      href: "/mistakes",
      icon: AlertCircle,
      isActive: pathname.startsWith("/mistakes"),
      badge: unmasteredCount > 0 ? (unmasteredCount > 99 ? "99+" : unmasteredCount) : null,
      badgeClass: "bg-danger text-primary-fg",
    },
    {
      name: "生词库",
      href: "/vocabulary",
      icon: Bookmark,
      isActive: pathname.startsWith("/vocabulary"),
      badge: vocabCount > 0 ? (vocabCount > 99 ? "99+" : vocabCount) : null,
      badgeClass: "bg-primary text-primary-fg",
    },
    {
      name: "我的",
      href: "/profile",
      icon: User,
      isActive: pathname.startsWith("/profile") || pathname.startsWith("/admin"),
      badge: null as string | number | null,
      badgeClass: "",
    },
  ];

  return (
    <nav
      aria-label="移动端底部导航"
      className="md:hidden fixed bottom-0 left-0 right-0 z-nav min-h-[var(--bottom-nav-h)] bg-surface/95 backdrop-blur-md border-t border-border px-3 pt-1.5 pb-[max(0.5rem,var(--safe-bottom))] transition-colors duration-150"
    >
      <div className="flex items-center justify-around max-w-md mx-auto">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex-1 flex flex-col items-center justify-center py-1 rounded-md transition-colors duration-150 active:scale-95 ${
                item.isActive ? "text-primary font-bold" : "text-fg-muted hover:text-fg font-medium"
              }`}
            >
              <div className="relative">
                <Icon className="w-5 h-5" />
                {item.badge !== null && (
                  <span
                    className={`absolute -top-1.5 -right-3 text-[10px] font-mono font-bold px-1.5 py-0.5 leading-none rounded-full ring-2 ring-surface ${item.badgeClass}`}
                  >
                    {item.badge}
                  </span>
                )}
              </div>
              <span className="text-[11px] mt-1 tracking-tight">{item.name}</span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
