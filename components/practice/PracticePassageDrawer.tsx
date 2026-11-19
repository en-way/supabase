"use client";

import type React from "react";
import { useEffect, useRef, useState } from "react";
import type { PassageRecord } from "@/types/exam";
import type { ReaderLineHeight } from "@/hooks/useReaderPrefs";
import { useDrawerSwipe } from "@/hooks/useDrawerSwipe";
import { triggerHaptic } from "@/hooks/useReaderPrefs";
import { Button } from "@/components/ui/Button";
import { BookOpen, X, ZoomIn, ZoomOut } from "lucide-react";

interface PracticePassageDrawerProps {
  open: boolean;
  onClose: () => void;
  passage: PassageRecord | null;
  currentIndex: number;
  fontSize: number;
  lineHeight: ReaderLineHeight;
  onUpdateFontSize: (updater: (prev: number) => number) => void;
}

export function PracticePassageDrawer({
  open,
  onClose,
  passage,
  currentIndex,
  fontSize,
  lineHeight,
  onUpdateFontSize,
}: PracticePassageDrawerProps) {
  const [showBackToTop, setShowBackToTop] = useState(false);
  const scrollContainerRef = useRef<HTMLDivElement | null>(null);
  const scrollPosRef = useRef<Record<string, number>>({});

  const { handleDrawerTouchStart, handleDrawerTouchEnd } = useDrawerSwipe({
    onDismissHaptic: () => triggerHaptic(8),
  });

  useEffect(() => {
    if (open && passage?.id) {
      const timer = setTimeout(() => {
        if (scrollContainerRef.current) {
          const savedTop = scrollPosRef.current[passage.id] || 0;
          scrollContainerRef.current.scrollTop = savedTop;
          setShowBackToTop(savedTop > 160);
        }
      }, 40);
      return () => clearTimeout(timer);
    }
  }, [open, passage?.id]);

  if (!open || !passage) return null;

  const handleScroll = (e: React.UIEvent<HTMLDivElement>) => {
    const top = e.currentTarget.scrollTop;
    scrollPosRef.current[passage.id] = top;
    setShowBackToTop(top > 160);
  };

  const paras = passage.content
    .split(/\n\s*\n/)
    .filter((x: string) => x.trim().length > 0);
  const isCloze =
    passage.title?.includes("Use of English") ||
    passage.title?.includes("完型") ||
    passage.content.includes("[1]");

  return (
    <div
      className="lg:hidden fixed inset-0 z-modal bg-overlay/50 backdrop-blur-sm flex flex-col justify-end animate-in fade-in duration-150"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
      role="dialog"
      aria-modal="true"
      aria-label="速查阅读材料"
    >
      <div className="bg-surface rounded-t-3xl border-t border-border p-5 pb-[max(1.5rem,env(safe-area-inset-bottom))] shadow-pop max-h-[85dvh] flex flex-col relative animate-in slide-in-from-bottom duration-200">
        <div
          onTouchStart={handleDrawerTouchStart}
          onTouchEnd={(e) => handleDrawerTouchEnd(e, onClose)}
          className="touch-none select-none cursor-grab active:cursor-grabbing pb-1 shrink-0"
        >
          <div className="w-12 h-1.5 bg-border rounded-full mx-auto mb-2.5" />
          <div className="flex items-center justify-between pb-2 border-b border-border gap-2">
            <div className="flex items-center gap-2 truncate pr-2">
              <BookOpen className="w-4 h-4 text-primary shrink-0" />
              <span className="text-xs font-bold text-fg truncate">
                {passage.title}
              </span>
            </div>
            <div className="flex items-center gap-1 shrink-0">
              <button
                type="button"
                onClick={() => onUpdateFontSize((p) => Math.max(13, p - 1))}
                className="p-1.5 rounded-lg text-fg-muted hover:text-fg hover:bg-surface-2"
                aria-label="缩小字号"
              >
                <ZoomOut className="w-3.5 h-3.5" />
              </button>
              <span className="text-[11px] font-mono tabular-nums text-fg-muted w-6 text-center">
                {fontSize}
              </span>
              <button
                type="button"
                onClick={() => onUpdateFontSize((p) => Math.min(22, p + 1))}
                className="p-1.5 rounded-lg text-fg-muted hover:text-fg hover:bg-surface-2"
                aria-label="放大字号"
              >
                <ZoomIn className="w-3.5 h-3.5" />
              </button>
              <button
                type="button"
                onClick={onClose}
                aria-label="关闭材料抽屉"
                className="p-1.5 rounded-full bg-surface-2 text-fg-muted hover:text-fg ml-1"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>

        <div
          ref={scrollContainerRef}
          onScroll={handleScroll}
          style={{ fontSize: `${fontSize}px`, lineHeight: String(lineHeight) }}
          className="flex-1 overflow-y-auto overscroll-contain py-3 reading-prose text-fg"
        >
          {paras.length <= 1 ? (
            <div className="whitespace-pre-line">{passage.content}</div>
          ) : (
            paras.map((paraText: string, pIdx: number) => (
              <div key={pIdx} className="mb-4 text-justify">
                {!isCloze && (
                  <span className="inline-flex items-center justify-center select-none text-[10px] font-mono font-bold text-fg-subtle bg-surface-2 border border-border rounded px-1.5 py-0.5 mr-2 align-middle">
                    P{pIdx + 1}
                  </span>
                )}
                <span className="align-middle">{paraText.trim()}</span>
              </div>
            ))
          )}
        </div>

        {showBackToTop && (
          <button
            type="button"
            onClick={() =>
              scrollContainerRef.current?.scrollTo({ top: 0, behavior: "smooth" })
            }
            className="absolute bottom-16 right-5 z-20 px-3 py-1.5 rounded-full bg-fg text-bg text-[11px] font-bold shadow-pop active:scale-95"
          >
            ↑ 回到段首
          </button>
        )}

        <div className="pt-2.5 border-t border-border flex justify-between items-center text-xs text-fg-subtle shrink-0">
          <span>顶栏下拉收起 · 双击查词</span>
          <Button size="sm" onClick={onClose}>
            返回作答（第 {currentIndex + 1} 题）
          </Button>
        </div>
      </div>
    </div>
  );
}
