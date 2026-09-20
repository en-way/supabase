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
  Loader2
} from "lucide-react";

interface PopoverPosition {
  x: number;
  y: number;
  isAbove: boolean;
}

export default function DictionaryPopover() {
  const [isOpen, setIsOpen] = useState(false);
  const [position, setPosition] = useState<PopoverPosition>({ x: 0, y: 0, isAbove: false });
  const [selectedWord, setSelectedWord] = useState<string>("");
  const [dictEntry, setDictEntry] = useState<DictEntry | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isAdded, setIsAdded] = useState(false);
  const [contextSentence, setContextSentence] = useState<string>("");
  const [playingType, setPlayingType] = useState<"us" | "uk" | null>(null);

  const popoverRef = useRef<HTMLDivElement | null>(null);

  // Close on outside click or Esc
  useEffect(() => {
    const handleOutsideClick = (e: MouseEvent) => {
      if (popoverRef.current && !popoverRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleOutsideClick);
    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  // Selection / Double-click listener
  useEffect(() => {
    const handleSelectionChange = () => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
        return;
      }

      const rawText = selection.toString().trim();
      const clean = cleanEnglishWord(rawText);
      // Valid word between 2 and 35 chars
      if (!clean || clean.length < 2 || clean.length > 35) {
        return;
      }

      const range = selection.getRangeAt(0);
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

    const handleDoubleClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (!target) return;
      // Skip clicking inside inputs or within popover itself
      if (
        target instanceof HTMLInputElement || 
        target instanceof HTMLTextAreaElement || 
        target.closest(".dictionary-popover-container")
      ) {
        return;
      }

      setTimeout(handleSelectionChange, 20);
    };

    document.addEventListener("mouseup", handleSelectionChange);
    document.addEventListener("dblclick", handleDoubleClick);

    return () => {
      document.removeEventListener("mouseup", handleSelectionChange);
      document.removeEventListener("dblclick", handleDoubleClick);
    };
  }, []);

  const triggerWordLookup = async (clean: string, rect: DOMRect, context: string) => {
    if (!clean) return;

    setSelectedWord(clean);
    setContextSentence(context);

    // Check if word is already in local vocabulary book
    const state = getLocalState();
    const exists = (state.vocabulary || []).some((v) => v.word.toLowerCase() === clean.toLowerCase());
    setIsAdded(exists);

    // Compute smart placement coordinates
    const popoverWidth = 330;
    const popoverHeight = 210;
    const padding = 12;

    let x = rect.left + rect.width / 2 - popoverWidth / 2;
    if (x < padding) x = padding;
    if (x + popoverWidth > window.innerWidth - padding) {
      x = window.innerWidth - popoverWidth - padding;
    }

    let y = rect.bottom + 8;
    let isAbove = false;
    if (y + popoverHeight > window.innerHeight - padding) {
      y = Math.max(padding, rect.top - popoverHeight - 8);
      isAbove = true;
    }

    setPosition({ x, y, isAbove });
    setIsOpen(true);

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
      className="dictionary-popover-container w-[330px] bg-white/95 backdrop-blur-md rounded-2xl shadow-2xl border border-slate-200/95 p-4 text-slate-900 animate-in fade-in zoom-in-95 duration-150 select-none text-left no-print"
    >
      {/* Header Bar */}
      <div className="flex items-center justify-between gap-2 border-b border-slate-100 pb-2.5">
        <div className="flex items-center space-x-2 truncate">
          <h4 className="text-base font-black text-slate-900 font-serif tracking-tight truncate">
            {selectedWord}
          </h4>

          {dictEntry?.phonetic && (
            <span className="text-xs text-indigo-600 font-mono font-medium">
              {dictEntry.phonetic}
            </span>
          )}
        </div>

        <div className="flex items-center space-x-1 shrink-0">
          {/* US Audio Button */}
          <button
            onClick={() => handlePlayAudio("us")}
            className={`px-1.5 py-1 rounded-md text-[11px] font-bold flex items-center space-x-0.5 transition-colors ${
              playingType === "us"
                ? "bg-indigo-600 text-white"
                : "text-slate-600 hover:text-indigo-600 hover:bg-indigo-50"
            }`}
            title="美音发音"
          >
            <Volume2 className="w-3.5 h-3.5 mr-0.5" />
            <span>美</span>
          </button>

          {/* UK Audio Button */}
          <button
            onClick={() => handlePlayAudio("uk")}
            className={`px-1.5 py-1 rounded-md text-[11px] font-bold flex items-center space-x-0.5 transition-colors ${
              playingType === "uk"
                ? "bg-indigo-600 text-white"
                : "text-slate-600 hover:text-indigo-600 hover:bg-indigo-50"
            }`}
            title="英音发音"
          >
            <Volume2 className="w-3.5 h-3.5 mr-0.5" />
            <span>英</span>
          </button>

          {/* Close Button */}
          <button
            onClick={() => setIsOpen(false)}
            className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors ml-1"
            title="关闭窗口 (Esc)"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Body: Translation & Definition */}
      <div className="py-3 space-y-2 text-xs">
        {isLoading ? (
          <div className="flex items-center space-x-2 text-slate-400 py-2">
            <Loader2 className="w-3.5 h-3.5 animate-spin text-indigo-600" />
            <span>从 Cloudflare 边缘极速载入中...</span>
          </div>
        ) : (
          <>
            <div className="flex items-start space-x-2">
              {dictEntry?.pos && (
                <span className="px-1.5 py-0.5 rounded text-[10px] font-bold font-mono bg-indigo-50 text-indigo-700 shrink-0 mt-0.5">
                  {dictEntry.pos}
                </span>
              )}
              {dictEntry?.baseWord && (
                <span className="px-1.5 py-0.5 rounded text-[10px] font-bold font-mono bg-amber-50 text-amber-700 border border-amber-200 shrink-0 mt-0.5">
                  原形: {dictEntry.baseWord}
                </span>
              )}
              <p className="text-slate-800 font-bold leading-relaxed flex-1 select-text">
                {dictEntry?.definition || "在真题语境中出现"}
              </p>
            </div>

            {dictEntry?.enDefinition && (
              <p className="text-[11px] text-slate-500 italic leading-snug select-text line-clamp-2 pt-0.5 border-t border-slate-100">
                &ldquo;{dictEntry.enDefinition}&rdquo;
              </p>
            )}
          </>
        )}
      </div>

      {/* Footer Action Bar */}
      <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-[11px]">
        <div className="flex items-center space-x-1 text-slate-400">
          <Sparkles className="w-3 h-3 text-emerald-500" />
          <span>Cloudflare 边缘极速词库 (0ms 离线)</span>
        </div>

        <button
          onClick={handleAddToVocab}
          disabled={isAdded}
          className={`px-3 py-1.5 rounded-xl font-bold flex items-center space-x-1 transition-all ${
            isAdded
              ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
              : "bg-indigo-600 hover:bg-indigo-700 text-white shadow-xs"
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
