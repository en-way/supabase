"use client";

import React, { useState, useEffect, useRef } from "react";
import { Highlighter, Trash2, Check, Sparkles } from "lucide-react";

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
}

export function getPassageHighlights(passageId: string): HighlightItem[] {
  if (typeof window === "undefined" || !passageId) return [];
  try {
    const raw = localStorage.getItem(`enway_highlights_${passageId}`);
    return raw ? JSON.parse(raw) : [];
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
}: PassageHighlighterProps) {
  const [highlights, setHighlights] = useState<HighlightItem[]>([]);
  const [selectedText, setSelectedText] = useState<string>("");
  const [tooltipPos, setTooltipPos] = useState<{ x: number; y: number } | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  // Load highlights on passage change
  useEffect(() => {
    if (!passageId) {
      setHighlights([]);
      return;
    }
    const loaded = getPassageHighlights(passageId);
    setHighlights(loaded);
    setTooltipPos(null);
    setSelectedText("");
  }, [passageId]);

  // Selection detection
  useEffect(() => {
    const handleMouseUp = () => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
        setTooltipPos(null);
        setSelectedText("");
        return;
      }

      const text = selection.toString().trim();
      // Only highlight if text length between 2 and 300 characters
      if (text.length < 2 || text.length > 300) {
        setTooltipPos(null);
        setSelectedText("");
        return;
      }

      // Ensure selection is inside this container
      const range = selection.getRangeAt(0);
      if (!containerRef.current?.contains(range.commonAncestorContainer)) {
        setTooltipPos(null);
        setSelectedText("");
        return;
      }

      const rect = range.getBoundingClientRect();
      if (rect && rect.width > 0) {
        setSelectedText(text);
        setTooltipPos({
          x: rect.left + rect.width / 2,
          y: rect.top - 10,
        });
      }
    };

    const handleSelectionChange = () => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed) {
        setTooltipPos(null);
        setSelectedText("");
      }
    };

    document.addEventListener("mouseup", handleMouseUp);
    document.addEventListener("selectionchange", handleSelectionChange);
    return () => {
      document.removeEventListener("mouseup", handleMouseUp);
      document.removeEventListener("selectionchange", handleSelectionChange);
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
    if (!highlights || highlights.length === 0) {
      return content;
    }

    // Sort highlights by length descending to match longer phrases first
    const sorted = [...highlights].sort((a, b) => b.text.length - a.text.length);

    // Build regex pattern safely
    const escapeRegExp = (str: string) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const pattern = new RegExp(
      `(${sorted.map((h) => escapeRegExp(h.text)).join("|")})`,
      "gi"
    );

    const parts = content.split(pattern);

    return parts.map((part, idx) => {
      const match = sorted.find((h) => h.text.toLowerCase() === part.toLowerCase());
      if (match) {
        const isYellow = match.color === "yellow";
        return (
          <mark
            key={idx}
            onClick={() => {
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
      return <React.Fragment key={idx}>{part}</React.Fragment>;
    });
  };

  return (
    <div className="relative">
      {/* Mini Floating Highlighter Toolbar when text selected */}
      {tooltipPos && selectedText && (
        <div
          style={{
            position: "fixed",
            left: `${tooltipPos.x}px`,
            top: `${tooltipPos.y}px`,
            transform: "translate(-50%, -100%)",
            zIndex: 60,
          }}
          className="bg-stone-900/95 dark:bg-zinc-900/95 text-white backdrop-blur-md px-2 py-1 rounded-xl shadow-xl border border-white/10 flex items-center space-x-1.5 animate-in fade-in zoom-in-95 duration-100"
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
          largeFont ? "text-lg leading-[2.1]" : "text-[15px] sm:text-base leading-[1.85]"
        }`}
      >
        {renderContent()}
      </div>
    </div>
  );
}
