"use client";

import React, { useState, useEffect, useRef } from "react";
import { Highlighter, Trash2 } from "lucide-react";
import { cleanEnglishWord } from "@/lib/dictionary";

export interface HighlightItem {
  id: string;
  text: string;
  color: "yellow" | "green";
  createdAt: number;
}

interface PassageHighlighterProps {
  passageId: string;
  content: string;
  className?: string;
  largeFont?: boolean;
  fontScale?: "normal" | "medium" | "large";
}

function isSingleEnglishWordLookup(text: string): boolean {
  if (/\s/.test(text)) return false;
  const clean = cleanEnglishWord(text);
  return Boolean(clean && clean.length >= 2 && clean.length <= 35);
}

export function getPassageHighlights(passageId: string): HighlightItem[] {
  if (typeof window === "undefined" || !passageId) return [];
  try {
    const raw = localStorage.getItem(`enway_highlights_${passageId}`);
    if (!raw) return [];
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    return parsed.filter(
      (item): item is HighlightItem =>
        Boolean(item) &&
        typeof item === "object" &&
        typeof (item as HighlightItem).text === "string" &&
        (item as HighlightItem).text.trim().length > 0 &&
        ((item as HighlightItem).color === "yellow" || (item as HighlightItem).color === "green")
    );
  } catch {
    return [];
  }
}

export function savePassageHighlights(passageId: string, items: HighlightItem[]) {
  if (typeof window === "undefined" || !passageId) return;
  try {
    localStorage.setItem(`enway_highlights_${passageId}`, JSON.stringify(items));
  } catch {}
}

export default function PassageHighlighter({
  passageId,
  content,
  className = "",
  largeFont = false,
  fontScale,
}: PassageHighlighterProps) {
  const [highlights, setHighlights] = useState<HighlightItem[]>([]);
  const [selectedText, setSelectedText] = useState<string>("");
  const [tooltipPos, setTooltipPos] = useState<{ x: number; y: number; below: boolean } | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const touchTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Load highlights on passage change and sync across tabs
  useEffect(() => {
    if (!passageId) {
      setHighlights([]);
      return;
    }
    const storageKey = `enway_highlights_${passageId}`;
    setHighlights(getPassageHighlights(passageId));
    setTooltipPos(null);
    setSelectedText("");

    const handleStorage = (e: StorageEvent) => {
      if (e.key === null || e.key === storageKey) {
        setHighlights(getPassageHighlights(passageId));
      }
    };
    window.addEventListener("storage", handleStorage);
    return () => window.removeEventListener("storage", handleStorage);
  }, [passageId]);

  // Selection detection isolated from DictionaryPopover single-word lookups and editable elements
  useEffect(() => {
    const isInsideProtectedUI = (target: EventTarget | null): boolean => {
      const el =
        target instanceof Element
          ? target
          : target instanceof Node
          ? target.parentElement
          : null;
      return Boolean(el?.closest(".passage-highlighter-toolbar, .dictionary-popover-container"));
    };

    const clearTooltip = () => {
      setTooltipPos(null);
      setSelectedText("");
    };

    const updateSelectionTooltip = () => {
      const activeElement = document.activeElement;
      if (
        activeElement instanceof HTMLInputElement ||
        activeElement instanceof HTMLTextAreaElement ||
        (activeElement as HTMLElement | null)?.isContentEditable
      ) {
        clearTooltip();
        return;
      }

      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
        clearTooltip();
        return;
      }

      const text = selection.toString().trim();
      // Only highlight multi-word phrases/clauses (2..300 chars); yield single words to DictionaryPopover
      if (text.length < 2 || text.length > 300 || isSingleEnglishWordLookup(text)) {
        clearTooltip();
        return;
      }

      const range = selection.getRangeAt(0);
      if (!containerRef.current?.contains(range.commonAncestorContainer)) {
        clearTooltip();
        return;
      }

      if (isInsideProtectedUI(range.commonAncestorContainer)) {
        clearTooltip();
        return;
      }

      let rect = range.getBoundingClientRect();
      if ((!rect || (rect.width === 0 && rect.height === 0)) && range.getClientRects().length > 0) {
        rect = range.getClientRects()[0];
      }

      if (rect && rect.width > 0) {
        const minX = 92;
        const viewportWidth = typeof window !== "undefined" ? window.innerWidth : 400;
        const maxX = Math.max(minX, viewportWidth - 92);
        const clampedX = Math.max(minX, Math.min(maxX, rect.left + rect.width / 2));
        const below = rect.top < 56;
        const y = below ? rect.bottom + 10 : rect.top - 10;

        setSelectedText(text);
        setTooltipPos({ x: clampedX, y, below });
      }
    };

    const handleMouseUp = (e: MouseEvent) => {
      if (isInsideProtectedUI(e.target)) return;
      updateSelectionTooltip();
    };

    const handleTouchEnd = (e: TouchEvent) => {
      if (isInsideProtectedUI(e.target)) return;
      if (touchTimerRef.current) clearTimeout(touchTimerRef.current);
      touchTimerRef.current = setTimeout(updateSelectionTooltip, 180);
    };

    const handleSelectionChange = () => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed) {
        clearTooltip();
        return;
      }
      if (typeof window !== "undefined" && window.innerWidth < 640) {
        if (touchTimerRef.current) clearTimeout(touchTimerRef.current);
        touchTimerRef.current = setTimeout(updateSelectionTooltip, 280);
      }
    };

    document.addEventListener("mouseup", handleMouseUp);
    document.addEventListener("touchend", handleTouchEnd, { passive: true });
    document.addEventListener("selectionchange", handleSelectionChange);
    return () => {
      document.removeEventListener("mouseup", handleMouseUp);
      document.removeEventListener("touchend", handleTouchEnd);
      document.removeEventListener("selectionchange", handleSelectionChange);
      if (touchTimerRef.current) clearTimeout(touchTimerRef.current);
    };
  }, []);

  const addHighlight = (color: "yellow" | "green") => {
    if (!selectedText || !passageId) return;

    // Filter duplicates of the exact same text
    const next = [
      ...highlights.filter((h) => h.text.toLowerCase() !== selectedText.toLowerCase()),
      {
        id: Date.now().toString(),
        text: selectedText,
        color,
        createdAt: Date.now(),
      },
    ];

    setHighlights(next);
    savePassageHighlights(passageId, next);

    // Clear selection
    window.getSelection()?.removeAllRanges();
    setTooltipPos(null);
    setSelectedText("");
  };

  const removeHighlight = (textToRemove: string) => {
    const next = highlights.filter((h) => h.text !== textToRemove);
    setHighlights(next);
    savePassageHighlights(passageId, next);
  };

  const clearAllHighlights = () => {
    setHighlights([]);
    savePassageHighlights(passageId, []);
  };

  // Helper to render text with highlights
  const renderContent = () => {
    const validHighlights = highlights.filter((h) => h && typeof h.text === "string" && h.text.trim().length > 0);
    if (validHighlights.length === 0) {
      return content;
    }

    // Sort highlights by length descending to match longer phrases first
    const sorted = [...validHighlights].sort((a, b) => b.text.length - a.text.length);

    // Build regex pattern safely
    const escapeRegExp = (str: string) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const pattern = new RegExp(
      `(${sorted.map((h) => escapeRegExp(h.text)).join("|")})`,
      "gi"
    );

    const parts = content.split(pattern);

    return parts.map((part, idx) => {
      if (idx % 2 === 1) {
        const match = sorted.find((h) => h.text.toLowerCase() === part.toLowerCase());
        if (match) {
          const isYellow = match.color === "yellow";
          return (
            <mark
              key={idx}
              onClick={() => {
                if (window.getSelection()?.toString().trim()) return;
                if (window.confirm(`取消该处高亮标注？\n"${match.text}"`)) {
                  removeHighlight(match.text);
                }
              }}
              title="点击取消该处高亮"
              className={`cursor-pointer rounded px-1 transition-all hover:opacity-80 ${
                isYellow
                  ? "bg-amber-200/90 dark:bg-amber-400/35 text-amber-950 dark:text-amber-100 decoration-amber-400 font-medium"
                  : "bg-emerald-200/90 dark:bg-emerald-400/35 text-emerald-950 dark:text-emerald-100 decoration-emerald-400 font-medium"
              }`}
            >
              {part}
            </mark>
          );
        }
      }
      return <React.Fragment key={idx}>{part}</React.Fragment>;
    });
  };

  return (
    <div className="relative">
      {/* Mini Floating Highlighter Toolbar when text selected */}
      {tooltipPos && selectedText && (
        <div
          data-enway-highlighter-toolbar="true"
          style={{
            position: "fixed",
            left: `${tooltipPos.x}px`,
            top: `${tooltipPos.y}px`,
            transform: tooltipPos.below ? "translate(-50%, 0)" : "translate(-50%, -100%)",
            zIndex: 60,
          }}
          className="passage-highlighter-toolbar bg-stone-900/95 dark:bg-zinc-900/95 text-white backdrop-blur-md px-2 py-1 rounded-xl shadow-xl border border-white/10 flex items-center space-x-1.5 animate-in fade-in zoom-in-95 duration-100"
          onMouseDown={(e) => e.preventDefault()} // Prevent losing selection
        >
          <span className="text-[10px] text-stone-400 font-medium pl-1">高亮:</span>
          <button
            type="button"
            onClick={() => addHighlight("yellow")}
            className="px-2 py-1 rounded-lg bg-amber-400/30 hover:bg-amber-400/50 text-amber-300 text-xs font-bold flex items-center space-x-1 transition-colors"
            title="黄色标出线索句"
          >
            <span className="w-2.5 h-2.5 rounded-full bg-amber-400 inline-block" />
            <span>线索</span>
          </button>
          <button
            type="button"
            onClick={() => addHighlight("green")}
            className="px-2 py-1 rounded-lg bg-emerald-400/30 hover:bg-emerald-400/50 text-emerald-300 text-xs font-bold flex items-center space-x-1 transition-colors"
            title="绿色标出核心论点/词汇"
          >
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block" />
            <span>重点</span>
          </button>
        </div>
      )}

      {/* Highlights Count & Clear Bar (when there are highlights) */}
      {highlights.length > 0 && (
        <div className="mb-3 px-3 py-1.5 rounded-xl bg-stone-100/90 dark:bg-zinc-800/80 border border-black/[0.04] dark:border-cyan-500/15 flex items-center justify-between text-xs text-stone-500 dark:text-zinc-400">
          <div className="flex items-center space-x-2">
            <Highlighter className="w-3.5 h-3.5 text-amber-500" />
            <span>
              已标注 <strong className="font-bold text-stone-800 dark:text-zinc-200">{highlights.length}</strong> 处高亮线索
            </span>
            <span className="text-[11px] text-stone-400 dark:text-zinc-500 hidden sm:inline">
              (点击高亮字句可撤销)
            </span>
          </div>
          <button
            type="button"
            onClick={clearAllHighlights}
            className="text-[11px] text-stone-400 hover:text-rose-600 dark:hover:text-rose-400 flex items-center space-x-1 transition-colors"
          >
            <Trash2 className="w-3 h-3" />
            <span>清空本篇标注</span>
          </button>
        </div>
      )}

      {/* Rendered Text with Highlighting */}
      <div
        ref={containerRef}
        className={`text-stone-800 dark:text-zinc-200 font-serif selection:bg-emerald-100/70 dark:selection:bg-cyan-500/30 whitespace-pre-line tracking-wide ${className} ${
          fontScale === "large" || (largeFont && !fontScale)
            ? "text-lg sm:text-[19px] leading-[2.1]"
            : fontScale === "medium"
            ? "text-[16.5px] sm:text-[17px] leading-[1.95]"
            : "text-[15px] sm:text-base leading-[1.85]"
        }`}
      >
        {renderContent()}
      </div>
    </div>
  );
}
