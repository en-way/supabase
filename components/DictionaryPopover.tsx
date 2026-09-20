"use client";

import { useState, useEffect, useRef } from "react";
import { 
  lookupWord, 
  lookupWordAsync, 
  cleanEnglishWord, 
  DictEntry 
} from "@/lib/dictionary";
import { addVocab, getLocalState } from "@/lib/storage";
import { 
  Volume2, 
  Bookmark, 
  Check, 
  X, 
  Sparkles, 
  Loader2,
  Volume1
} from "lucide-react";

interface PopoverPosition {
  x: number;
  y: number;
  arrowX: number;
  isAbove: boolean;
}

export default function DictionaryPopover() {
  const [isOpen, setIsOpen] = useState(false);
  const [position, setPosition] = useState<PopoverPosition>({ x: 0, y: 0, arrowX: 170, isAbove: true });
  const [selectedWord, setSelectedWord] = useState<string>("");
  const [dictEntry, setDictEntry] = useState<DictEntry | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isAdded, setIsAdded] = useState(false);
  const [contextSentence, setContextSentence] = useState<string>("");
  const [playingType, setPlayingType] = useState<"us" | "uk" | null>(null);

  const popoverRef = useRef<HTMLDivElement | null>(null);
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  // Close on outside click or Esc
  useEffect(() => {
    const handleOutsideClick = (e: MouseEvent) => {
      if (popoverRef.current && !popoverRef.current.contains(e.target as Node)) {
        setIsOpen(false);
        // Clear text selection to prevent lingering highlight from re-triggering popups
        if (window.getSelection()?.toString().trim()) {
          window.getSelection()?.removeAllRanges();
        }
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setIsOpen(false);
        if (window.getSelection()?.toString().trim()) {
          window.getSelection()?.removeAllRanges();
        }
      }
    };

    document.addEventListener("mousedown", handleOutsideClick);
    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  // Selection & Double-click listener with robust multi-word suppression and debouncing
  useEffect(() => {
    const processSelection = () => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
        return;
      }

      const rawText = selection.toString().trim();
      // If selection contains spaces or line breaks, user dragged across a sentence/phrase - DO NOT popup
      if (/\s/.test(rawText)) {
        return;
      }

      const clean = cleanEnglishWord(rawText);
      // Valid word between 2 and 35 chars
      if (!clean || clean.length < 2 || clean.length > 35) {
        return;
      }

      // Ensure target is not inside an input, textarea, or contentEditable element
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
      const containerElem = containerNode instanceof Element ? containerNode : containerNode.parentElement;
      if (containerElem?.closest(".dictionary-popover-container")) {
        return;
      }

      // If already open with the same word, avoid duplicate triggering
      if (isOpen && selectedWord.toLowerCase() === clean.toLowerCase()) {
        return;
      }

      const rect = range.getBoundingClientRect();
      if (!rect || (rect.width === 0 && rect.height === 0)) {
        return;
      }

      // Extract context sentence surrounding the word
      let context = "";
      try {
        const fullNodeText = range.startContainer.textContent || "";
        const start = Math.max(0, range.startOffset - 60);
        const end = Math.min(fullNodeText.length, range.endOffset + 60);
        context = fullNodeText.slice(start, end).trim();
      } catch {}

      triggerWordLookup(clean, rect, context);
    };

    const handleMouseUp = (e: MouseEvent) => {
      // Ignore clicks originating inside the popover itself (audio buttons, add vocab, close button, etc.)
      if (popoverRef.current && popoverRef.current.contains(e.target as Node)) {
        return;
      }

      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      // 150ms debounce allows double-click or drag selection to fully complete
      timeoutRef.current = setTimeout(processSelection, 150);
    };

    document.addEventListener("mouseup", handleMouseUp);
    return () => {
      document.removeEventListener("mouseup", handleMouseUp);
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
    };
  }, [isOpen, selectedWord]);

  const triggerWordLookup = async (clean: string, rect: DOMRect, context: string) => {
    if (!clean) return;

    setSelectedWord(clean);
    setContextSentence(context);

    // Check if word is already in local vocabulary book
    const state = getLocalState();
    const exists = (state.vocabulary || []).some((v) => v.word.toLowerCase() === clean.toLowerCase());
    setIsAdded(exists);

    // Dimension & Boundary calculations
    const popoverWidth = 340;
    const popoverHeight = 220;
    const padding = 12;

    const wordCenterX = rect.left + rect.width / 2;

    // Horizontal placement
    let x = wordCenterX - popoverWidth / 2;
    if (x < padding) x = padding;
    if (x + popoverWidth > window.innerWidth - padding) {
      x = window.innerWidth - popoverWidth - padding;
    }

    // Caret arrow horizontal position relative to the popover card
    let arrowX = wordCenterX - x;
    arrowX = Math.max(18, Math.min(popoverWidth - 18, arrowX));

    // Vertical placement: Above-first preference to avoid covering reading text
    let isAbove = true;
    let y = rect.top - popoverHeight - 12;

    // If word is near top edge of window (< 230px), flip to below
    if (rect.top < 230) {
      isAbove = false;
      y = rect.bottom + 12;
    }

    setPosition({ x, y, arrowX, isAbove });
    setIsOpen(true);

    // Immediately clear browser native selection range to dismiss browser floating copy/search toolbar
    try {
      window.getSelection()?.removeAllRanges();
    } catch {}
    setTimeout(() => {
      try {
        window.getSelection()?.removeAllRanges();
      } catch {}
    }, 20);

    // Instant local memory lookup first
    const instant = lookupWord(clean);
    if (instant) {
      setDictEntry(instant);
      setIsLoading(false);
    } else {
      // Sharded edge lookup
      setIsLoading(true);
      const edgeEntry = await lookupWordAsync(clean);
      if (edgeEntry) {
        setDictEntry(edgeEntry);
      }
      setIsLoading(false);
    }
  };

  const handlePlayAudio = (type: "us" | "uk") => {
    if (!selectedWord) return;
    const url = type === "uk" ? dictEntry?.ukAudioUrl : dictEntry?.usAudioUrl;
    if (!url) return;

    setPlayingType(type);
    try {
      const audio = new Audio(url);
      audio.onended = () => setPlayingType(null);
      audio.onerror = () => setPlayingType(null);
      audio.play().catch(() => setPlayingType(null));
    } catch {
      setPlayingType(null);
    }
  };

  const handleAddToVocab = () => {
    if (!selectedWord || !dictEntry) return;

    addVocab(
      selectedWord,
      dictEntry.definition,
      dictEntry.phonetic,
      contextSentence
    );
    setIsAdded(true);
  };

  const handleClose = () => {
    setIsOpen(false);
    if (window.getSelection()?.toString().trim()) {
      window.getSelection()?.removeAllRanges();
    }
  };

  if (!isOpen || !selectedWord) return null;

  return (
    <div
      ref={popoverRef}
      style={{
        position: "fixed",
        left: `${position.x}px`,
        top: `${position.y}px`,
        zIndex: 9999,
      }}
      className={`dictionary-popover-container w-[340px] bg-white/95 dark:bg-[#11131a]/95 backdrop-blur-2xl rounded-2xl shadow-float border border-black/[0.08] dark:border-cyan-500/25 p-4 text-stone-900 dark:text-zinc-100 select-none text-left no-print duration-200 ease-spring animate-in fade-in zoom-in-95 ${
        position.isAbove ? "slide-in-from-bottom-2" : "slide-in-from-top-2"
      }`}
    >
      {/* Visual Directional Pointer Arrow (Caret pointing to the selected word) */}
      <div
        style={{ left: `${position.arrowX}px` }}
        className={`absolute -translate-x-1/2 w-0 h-0 border-solid pointer-events-none ${
          position.isAbove
            ? "bottom-[-7px] border-t-[7px] border-t-white dark:border-t-[#11131a] border-l-[7px] border-l-transparent border-r-[7px] border-r-transparent border-b-0 filter drop-shadow-[0_2px_1px_rgba(0,0,0,0.06)]"
            : "top-[-7px] border-b-[7px] border-b-white dark:border-b-[#11131a] border-l-[7px] border-l-transparent border-r-[7px] border-r-transparent border-t-0 filter drop-shadow-[0_-1px_1px_rgba(0,0,0,0.06)]"
        }`}
      />

      {/* Header Bar */}
      <div className="flex items-center justify-between gap-2 border-b border-stone-100 dark:border-zinc-800 pb-2.5">
        <div className="flex items-center space-x-2 truncate">
          <h4 className="text-base font-bold text-stone-900 dark:text-zinc-100 font-sans tracking-tight truncate">
            {selectedWord}
          </h4>

          {dictEntry?.phonetic && (
            <span className="text-xs text-emerald-800 dark:text-cyber-300 font-mono font-medium bg-emerald-50/80 dark:bg-cyan-950/60 border border-emerald-200/60 dark:border-cyan-500/30 px-1.5 py-0.5 rounded-md">
              {dictEntry.phonetic}
            </span>
          )}
        </div>

        <div className="flex items-center space-x-1 shrink-0">
          {/* US Audio Button */}
          <button
            onClick={() => handlePlayAudio("us")}
            className={`px-2 py-1 rounded-lg text-[11px] font-bold flex items-center space-x-1 transition-all duration-150 active:scale-[0.96] ${
              playingType === "us"
                ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle"
                : "text-stone-600 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-cyber-300 hover:bg-stone-100 dark:hover:bg-zinc-800"
            }`}
            title="美音标准发音"
          >
            {playingType === "us" ? (
              <Volume1 className="w-3.5 h-3.5 animate-pulse" />
            ) : (
              <Volume2 className="w-3.5 h-3.5" />
            )}
            <span>美</span>
          </button>

          {/* UK Audio Button */}
          <button
            onClick={() => handlePlayAudio("uk")}
            className={`px-2 py-1 rounded-lg text-[11px] font-bold flex items-center space-x-1 transition-all duration-150 active:scale-[0.96] ${
              playingType === "uk"
                ? "bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-subtle"
                : "text-stone-600 dark:text-zinc-400 hover:text-stone-900 dark:hover:text-cyber-300 hover:bg-stone-100 dark:hover:bg-zinc-800"
            }`}
            title="英音标准发音"
          >
            {playingType === "uk" ? (
              <Volume1 className="w-3.5 h-3.5 animate-pulse" />
            ) : (
              <Volume2 className="w-3.5 h-3.5" />
            )}
            <span>英</span>
          </button>

          {/* Close Button */}
          <button
            onClick={handleClose}
            className="p-1 rounded-lg text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-300 hover:bg-stone-100 dark:hover:bg-zinc-800 transition-colors ml-1"
            title="关闭窗口 (Esc)"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Body: Translation & Definition */}
      <div className="py-3 space-y-2 text-xs">
        {isLoading ? (
          <div className="flex items-center space-x-2 text-stone-400 dark:text-zinc-500 py-2">
            <Loader2 className="w-3.5 h-3.5 animate-spin text-emerald-600 dark:text-cyber-400" />
            <span>从 Cloudflare 边缘极速载入中...</span>
          </div>
        ) : (
          <>
            <div className="flex items-start space-x-2">
              {dictEntry?.pos && (
                <span className="px-1.5 py-0.5 rounded text-[10px] font-bold font-mono bg-stone-100 dark:bg-zinc-800 text-stone-700 dark:text-zinc-300 shrink-0 mt-0.5">
                  {dictEntry.pos}
                </span>
              )}
              {dictEntry?.baseWord && (
                <span className="px-1.5 py-0.5 rounded text-[10px] font-bold font-mono bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 border border-amber-200/80 dark:border-amber-500/30 shrink-0 mt-0.5">
                  原形: {dictEntry.baseWord}
                </span>
              )}
              <p className="text-stone-800 dark:text-zinc-200 font-semibold leading-relaxed flex-1 select-text">
                {dictEntry?.definition || "在真题语境中出现"}
              </p>
            </div>

            {dictEntry?.enDefinition && (
              <p className="text-[11px] text-stone-500 dark:text-zinc-400 italic leading-snug select-text line-clamp-2 pt-0.5 border-t border-stone-100 dark:border-zinc-800">
                &ldquo;{dictEntry.enDefinition}&rdquo;
              </p>
            )}
          </>
        )}
      </div>

      {/* Footer Action Bar */}
      <div className="pt-2 border-t border-stone-100 dark:border-zinc-800 flex items-center justify-between text-[11px]">
        <div className="flex items-center space-x-1 text-stone-400 dark:text-zinc-500">
          <Sparkles className="w-3 h-3 text-emerald-600 dark:text-cyber-400" />
          <span>Cloudflare 边缘极速词库</span>
        </div>

        <button
          onClick={handleAddToVocab}
          disabled={isAdded}
          className={`px-3 py-1.5 rounded-xl font-bold flex items-center space-x-1 transition-all duration-150 active:scale-[0.98] ${
            isAdded
              ? "bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200/80 dark:border-emerald-500/30"
              : "bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] shadow-subtle"
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
    </div>
  );
}
