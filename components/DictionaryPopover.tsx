"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import {
  lookupWord,
  lookupWordAsync,
  cleanEnglishWord,
  DictEntry,
} from "@/lib/dictionary";
import { addVocab, getLocalState, subscribeLocalState } from "@/lib/storage";
import { BottomSheet } from "@/components/ui/BottomSheet";
import {
  Volume2,
  Bookmark,
  Check,
  X,
  Sparkles,
  Loader2,
  Volume1,
} from "lucide-react";

interface PopoverPosition {
  x: number;
  y: number;
  arrowX: number;
  isAbove: boolean;
}

function isInsideHighlighterToolbar(target: EventTarget | null): boolean {
  const el =
    target instanceof Element
      ? target
      : target instanceof Node
      ? target.parentElement
      : null;
  return Boolean(el?.closest(".passage-highlighter-toolbar"));
}

function computeDesktopPosition(rect: DOMRect): PopoverPosition {
  const popoverWidth = 340;
  const popoverHeight = 220;
  const padding = 12;

  const wordCenterX = rect.left + rect.width / 2;
  let x = wordCenterX - popoverWidth / 2;
  if (x < padding) x = padding;
  if (x + popoverWidth > window.innerWidth - padding) {
    x = window.innerWidth - popoverWidth - padding;
  }

  let arrowX = wordCenterX - x;
  arrowX = Math.max(18, Math.min(popoverWidth - 18, arrowX));

  let isAbove = true;
  let y = rect.top - popoverHeight - 12;
  if (rect.top < 230) {
    isAbove = false;
    y = rect.bottom + 12;
  }

  return { x, y, arrowX, isAbove };
}

export default function DictionaryPopover() {
  const [isOpen, setIsOpen] = useState(false);
  const [position, setPosition] = useState<PopoverPosition>({
    x: 0,
    y: 0,
    arrowX: 170,
    isAbove: true,
  });
  const [selectedWord, setSelectedWord] = useState<string>("");
  const [dictEntry, setDictEntry] = useState<DictEntry | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isAdded, setIsAdded] = useState(false);
  const [contextSentence, setContextSentence] = useState<string>("");
  const [playingType, setPlayingType] = useState<"us" | "uk" | null>(null);

  const [isMobile, setIsMobile] = useState(false);
  const popoverRef = useRef<HTMLDivElement | null>(null);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const clearSelTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const activeWordRef = useRef<string>("");
  const activeRangeRef = useRef<Range | null>(null);
  const currentAudioRef = useRef<HTMLAudioElement | null>(null);

  const stopActiveAudio = useCallback(() => {
    if (currentAudioRef.current) {
      try {
        currentAudioRef.current.pause();
        currentAudioRef.current.currentTime = 0;
      } catch {}
      currentAudioRef.current = null;
    }
    setPlayingType(null);
  }, []);

  const handleClose = useCallback(() => {
    stopActiveAudio();
    activeRangeRef.current = null;
    setIsOpen(false);
    if (window.getSelection()?.toString().trim()) {
      window.getSelection()?.removeAllRanges();
    }
  }, [stopActiveAudio]);

  useEffect(() => {
    return () => {
      if (clearSelTimerRef.current) {
        clearTimeout(clearSelTimerRef.current);
        clearSelTimerRef.current = null;
      }
      if (currentAudioRef.current) {
        try {
          currentAudioRef.current.pause();
          currentAudioRef.current.currentTime = 0;
        } catch {}
        currentAudioRef.current = null;
      }
    };
  }, []);

  useEffect(() => {
    const updateIsMobile = () => {
      setIsMobile(typeof window !== "undefined" && window.innerWidth < 640);
    };
    updateIsMobile();
    window.addEventListener("resize", updateIsMobile);
    return () => window.removeEventListener("resize", updateIsMobile);
  }, []);

  // Desktop outside-click / Esc handler (mobile uses BottomSheet's built-in Backdrop + Esc)
  useEffect(() => {
    if (!isOpen || isMobile) return;

    const handleOutside = (e: MouseEvent | TouchEvent) => {
      const target = (e instanceof MouseEvent ? e.target : (e as TouchEvent).target) as Node | null;
      if (isInsideHighlighterToolbar(target)) {
        return;
      }
      if (popoverRef.current && (!target || !popoverRef.current.contains(target))) {
        handleClose();
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        handleClose();
      }
    };

    document.addEventListener("mousedown", handleOutside);
    document.addEventListener("touchstart", handleOutside, { passive: true });
    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("mousedown", handleOutside);
      document.removeEventListener("touchstart", handleOutside);
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [isOpen, isMobile, handleClose]);

  // Desktop scroll tracking: reposition anchored popover or close if word scrolls out of view
  useEffect(() => {
    if (!isOpen || isMobile) return;

    let rafId: number | null = null;
    const handleScroll = (e: Event) => {
      const target = e.target as Node | null;
      if (target && popoverRef.current?.contains(target)) {
        return;
      }
      if (rafId !== null) return;
      rafId = window.requestAnimationFrame(() => {
        rafId = null;
        const range = activeRangeRef.current;
        if (!range) return;
        const rect = range.getBoundingClientRect();
        if (
          !rect ||
          rect.width === 0 ||
          rect.bottom < 0 ||
          rect.top > window.innerHeight
        ) {
          handleClose();
          return;
        }
        setPosition(computeDesktopPosition(rect));
      });
    };

    window.addEventListener("scroll", handleScroll, true);
    return () => {
      window.removeEventListener("scroll", handleScroll, true);
      if (rafId !== null) window.cancelAnimationFrame(rafId);
    };
  }, [isOpen, isMobile, handleClose]);

  useEffect(() => {
    if (!isOpen || !selectedWord) return;
    const targetWordLower = selectedWord.toLowerCase();
    return subscribeLocalState((state) => {
      const exists = (state.vocabulary || []).some(
        (v) => v.word.toLowerCase() === targetWordLower
      );
      setIsAdded(exists);
    });
  }, [isOpen, selectedWord]);

  const triggerWordLookup = useCallback(
    async (clean: string, rect: DOMRect | null, context: string, range: Range | null) => {
      if (!clean) return;

      setSelectedWord(clean);
      setContextSentence(context);

      const state = getLocalState();
      const exists = (state.vocabulary || []).some(
        (v) => v.word.toLowerCase() === clean.toLowerCase()
      );
      setIsAdded(exists);

      const mobileCheck = typeof window !== "undefined" && window.innerWidth < 640;
      setIsMobile(mobileCheck);

      if (!mobileCheck && rect) {
        activeRangeRef.current = range ? range.cloneRange() : null;
        setPosition(computeDesktopPosition(rect));
      } else {
        activeRangeRef.current = null;
      }

      setIsOpen(true);

      try {
        window.getSelection()?.removeAllRanges();
      } catch {}
      if (clearSelTimerRef.current) clearTimeout(clearSelTimerRef.current);
      clearSelTimerRef.current = setTimeout(() => {
        clearSelTimerRef.current = null;
        try {
          window.getSelection()?.removeAllRanges();
        } catch {}
      }, 20);

      activeWordRef.current = clean;

      const instant = lookupWord(clean);
      if (instant) {
        setDictEntry(instant);
        setIsLoading(false);
      } else {
        setDictEntry(null);
        setIsLoading(true);
        const edgeEntry = await lookupWordAsync(clean);
        if (activeWordRef.current === clean) {
          setDictEntry(edgeEntry ?? null);
          setIsLoading(false);
        }
      }
    },
    []
  );

  // Selection & Double-click / Touch listener
  useEffect(() => {
    const processSelection = () => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
        return;
      }

      const rawText = selection.toString().trim();
      if (/\s/.test(rawText)) {
        return;
      }

      const clean = cleanEnglishWord(rawText);
      if (!clean || clean.length < 2 || clean.length > 35) {
        return;
      }

      const activeElement = document.activeElement;
      if (
        activeElement instanceof HTMLInputElement ||
        activeElement instanceof HTMLTextAreaElement ||
        (activeElement as HTMLElement)?.isContentEditable
      ) {
        return;
      }

      const range = selection.getRangeAt(0);
      const containerNode = range.commonAncestorContainer;
      const containerElem =
        containerNode instanceof Element ? containerNode : containerNode.parentElement;
      if (
        containerElem?.closest(".dictionary-popover-container, .passage-highlighter-toolbar")
      ) {
        return;
      }

      if (isOpen && selectedWord.toLowerCase() === clean.toLowerCase()) {
        return;
      }

      let rect = range.getBoundingClientRect();
      if (
        (!rect || (rect.width === 0 && rect.height === 0)) &&
        range.getClientRects().length > 0
      ) {
        rect = range.getClientRects()[0];
      }

      let context = "";
      try {
        const fullNodeText = range.startContainer.textContent || "";
        const start = Math.max(0, range.startOffset - 60);
        const end = Math.min(fullNodeText.length, range.endOffset + 60);
        context = fullNodeText.slice(start, end).trim();
      } catch {}

      triggerWordLookup(clean, rect, context, range);
    };

    const handleMouseUp = (e: MouseEvent) => {
      if (
        (popoverRef.current && popoverRef.current.contains(e.target as Node)) ||
        isInsideHighlighterToolbar(e.target)
      ) {
        return;
      }

      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      timeoutRef.current = setTimeout(processSelection, 150);
    };

    const handleTouchEnd = (e: TouchEvent) => {
      const target = e.target as Node | null;
      if (
        (popoverRef.current && target && popoverRef.current.contains(target)) ||
        isInsideHighlighterToolbar(target)
      ) {
        return;
      }
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      timeoutRef.current = setTimeout(processSelection, 250);
    };

    const handleSelectionChange = () => {
      if (typeof window !== "undefined" && window.innerWidth < 640) {
        if (timeoutRef.current) clearTimeout(timeoutRef.current);
        timeoutRef.current = setTimeout(processSelection, 350);
      }
    };

    document.addEventListener("mouseup", handleMouseUp);
    document.addEventListener("touchend", handleTouchEnd, { passive: true });
    document.addEventListener("selectionchange", handleSelectionChange);

    return () => {
      document.removeEventListener("mouseup", handleMouseUp);
      document.removeEventListener("touchend", handleTouchEnd);
      document.removeEventListener("selectionchange", handleSelectionChange);
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
    };
  }, [isOpen, selectedWord, triggerWordLookup]);

  const handlePlayAudio = (type: "us" | "uk") => {
    if (!selectedWord) return;
    const url = type === "uk" ? dictEntry?.ukAudioUrl : dictEntry?.usAudioUrl;
    if (!url) return;

    if (currentAudioRef.current) {
      currentAudioRef.current.pause();
      currentAudioRef.current = null;
    }

    setPlayingType(type);
    try {
      const audio = new Audio(url);
      currentAudioRef.current = audio;
      audio.onended = () => {
        setPlayingType(null);
        currentAudioRef.current = null;
      };
      audio.onerror = () => {
        setPlayingType(null);
        currentAudioRef.current = null;
      };
      audio.play().catch(() => {
        setPlayingType(null);
        currentAudioRef.current = null;
      });
    } catch {
      setPlayingType(null);
      currentAudioRef.current = null;
    }
  };

  const handleAddToVocab = () => {
    if (!selectedWord || !dictEntry) return;

    if (typeof window !== "undefined" && "vibrate" in navigator) {
      try {
        navigator.vibrate([10, 25, 10]);
      } catch {}
    }

    addVocab(selectedWord, dictEntry.definition, dictEntry.phonetic, contextSentence);
    setIsAdded(true);
  };

  if (!isOpen || !selectedWord) return null;

  const audioButtons = (
    <div className="flex items-center gap-1 shrink-0">
      <button
        type="button"
        onClick={() => handlePlayAudio("us")}
        className={`px-2 py-1 rounded-sm text-[11px] font-semibold flex items-center gap-1 transition-colors duration-150 ${
          playingType === "us"
            ? "bg-primary text-primary-fg"
            : "text-fg-muted hover:text-fg hover:bg-surface-2"
        }`}
        title="美音标准发音"
      >
        {playingType === "us" ? <Volume1 className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5" />}
        <span>美</span>
      </button>

      <button
        type="button"
        onClick={() => handlePlayAudio("uk")}
        className={`px-2 py-1 rounded-sm text-[11px] font-semibold flex items-center gap-1 transition-colors duration-150 ${
          playingType === "uk"
            ? "bg-primary text-primary-fg"
            : "text-fg-muted hover:text-fg hover:bg-surface-2"
        }`}
        title="英音标准发音"
      >
        {playingType === "uk" ? <Volume1 className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5" />}
        <span>英</span>
      </button>
    </div>
  );

  const bodyAndFooter = (
    <>
      <div className="py-3 space-y-2 text-xs">
        {isLoading ? (
          <div className="flex items-center gap-2 text-fg-muted py-2">
            <Loader2 className="w-3.5 h-3.5 animate-spin text-primary" />
            <span>从边缘词库快速载入中...</span>
          </div>
        ) : (
          <>
            <div className="flex items-start gap-2">
              {dictEntry?.pos && (
                <span className="px-1.5 py-0.5 rounded-sm text-[10px] font-bold font-mono bg-surface-2 text-fg-muted border border-border shrink-0 mt-0.5">
                  {dictEntry.pos}
                </span>
              )}
              {dictEntry?.baseWord && (
                <span className="px-1.5 py-0.5 rounded-sm text-[10px] font-bold font-mono bg-warning-soft text-warning border border-warning/20 shrink-0 mt-0.5">
                  原形: {dictEntry.baseWord}
                </span>
              )}
              <p className="text-fg font-semibold leading-relaxed flex-1 select-text">
                {dictEntry?.definition || "在真题语境中出现"}
              </p>
            </div>

            {dictEntry?.enDefinition && (
              <p className="text-[11px] text-fg-muted italic leading-snug select-text line-clamp-2 pt-1 border-t border-border">
                &ldquo;{dictEntry.enDefinition}&rdquo;
              </p>
            )}
          </>
        )}
      </div>

      <div className="pt-2.5 border-t border-border flex items-center justify-between text-[11px]">
        <div className="flex items-center gap-1 text-fg-subtle">
          <Sparkles className="w-3 h-3 text-primary" />
          <span>边缘离线词库</span>
        </div>

        <button
          type="button"
          onClick={handleAddToVocab}
          disabled={isAdded || isLoading || !dictEntry}
          className={`px-3 py-1.5 rounded-md font-semibold flex items-center gap-1 transition-colors duration-150 ${
            isAdded
              ? "bg-success-soft text-success border border-success/25"
              : "bg-primary hover:bg-primary-hover text-primary-fg shadow-1 disabled:opacity-50 disabled:cursor-not-allowed"
          }`}
        >
          {isAdded ? (
            <>
              <Check className="w-3.5 h-3.5" />
              <span>已入生词本</span>
            </>
          ) : (
            <>
              <Bookmark className="w-3.5 h-3.5" />
              <span>加入生词本</span>
            </>
          )}
        </button>
      </div>
    </>
  );

  // Mobile: unified BottomSheet with Backdrop, useDrawerSwipe, useBodyScrollLock & safe-area padding
  if (isMobile) {
    return (
      <BottomSheet
        open={isOpen}
        onClose={handleClose}
        zIndexClass="z-popover"
        className="dictionary-popover-container no-print pb-[env(safe-area-inset-bottom)]"
        title={
          <span className="flex items-center gap-2 truncate">
            <span className="text-base font-bold text-fg truncate">{selectedWord}</span>
            {dictEntry?.phonetic && (
              <span className="text-xs text-primary-soft-fg font-mono font-medium bg-primary-soft border border-primary/20 px-1.5 py-0.5 rounded-sm">
                {dictEntry.phonetic}
              </span>
            )}
          </span>
        }
        subtitle="点击读音试听，下滑关闭"
      >
        <div className="flex items-center justify-between mb-1">{audioButtons}</div>
        {bodyAndFooter}
      </BottomSheet>
    );
  }

  // Desktop: anchored floating Popover above drawers (z-popover)
  return (
    <div
      ref={popoverRef}
      style={{
        position: "fixed",
        left: `${position.x}px`,
        top: `${position.y}px`,
      }}
      className={`dictionary-popover-container z-popover w-[340px] max-h-[82vh] overflow-y-auto bg-surface/98 backdrop-blur-md rounded-lg border border-border shadow-pop p-4 text-fg select-none text-left no-print animate-in fade-in zoom-in-95 duration-150 ${
        position.isAbove ? "slide-in-from-bottom-2" : "slide-in-from-top-2"
      }`}
    >
      <div
        style={{ left: `${position.arrowX}px` }}
        className={`absolute -translate-x-1/2 w-0 h-0 border-solid pointer-events-none ${
          position.isAbove
            ? "bottom-[-7px] border-t-[7px] border-t-surface border-l-[7px] border-l-transparent border-r-[7px] border-r-transparent border-b-0"
            : "top-[-7px] border-b-[7px] border-b-surface border-l-[7px] border-l-transparent border-r-[7px] border-r-transparent border-t-0"
        }`}
      />

      <div className="flex items-center justify-between gap-2 border-b border-border pb-2.5">
        <div className="flex items-center gap-2 truncate">
          <h4 className="text-base font-bold text-fg tracking-tight truncate">{selectedWord}</h4>
          {dictEntry?.phonetic && (
            <span className="text-xs text-primary-soft-fg font-mono font-medium bg-primary-soft border border-primary/20 px-1.5 py-0.5 rounded-sm">
              {dictEntry.phonetic}
            </span>
          )}
        </div>

        <div className="flex items-center gap-1 shrink-0">
          {audioButtons}
          <button
            type="button"
            onClick={handleClose}
            className="p-1 rounded-sm text-fg-subtle hover:text-fg hover:bg-surface-2 transition-colors ml-0.5"
            title="关闭窗口 (Esc)"
            aria-label="关闭查词浮窗"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>

      {bodyAndFooter}
    </div>
  );
}
