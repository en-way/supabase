"use client";

import React, { useEffect } from "react";
import { usePathname } from "next/navigation";
import Navbar from "@/components/Navbar";
import MobileTabBar from "@/components/MobileTabBar";
import DictionaryPopover from "@/components/DictionaryPopover";

export default function AppShell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const isLogin =
    pathname === "/login" || pathname === "/login/" || pathname?.startsWith("/login");
  const isExam =
    pathname === "/exam" || pathname === "/exam/" || pathname?.startsWith("/exam");
  const isPractice =
    pathname === "/practice" || pathname === "/practice/" || pathname?.startsWith("/practice");
  const isImmersive = Boolean(isLogin || isExam || isPractice);

  useEffect(() => {
    document.body.dataset.chrome = isImmersive ? "immersive" : "default";
    return () => {
      delete document.body.dataset.chrome;
    };
  }, [isImmersive]);

  return (
    <>
      <Navbar />
      <main
        className={`flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 pt-4 sm:pt-6 ${
          isImmersive
            ? "pb-6"
            : "pb-[calc(var(--bottom-nav-h)+var(--safe-bottom)+1rem)] md:pb-6"
        }`}
      >
        {children}
      </main>
      <MobileTabBar />
      <DictionaryPopover />
    </>
  );
}
