"use client";

import { useState, useEffect } from "react";
import { lookupWord, DictEntry } from "@/lib/dictionary";
import { addVocab } from "@/lib/storage";
import { Volume2, Bookmark, Check, X } from "lucide-react";

export default function WordLookupModal() {
  const [selectedWord, setSelectedWord] = useState<string | null>(null);
  const [dictInfo, setDictInfo] = useState<DictEntry | null>(null);
  const [contextSentence, setContextSentence] = useState<string>("");
  const [isSaved, setIsSaved] = useState(false);
  const [position, setPosition] = useState<{ x: number; y: number } | null>(null);

  useEffect(() => {
    const handleDoubleClick = () => {
      const selection = window.getSelection();
      if (!selection || selection.rangeCount === 0) return;

      const text = selection.toString().trim();
      // Only single English word (allowing hyphens)
      if (text && /^[a-zA-Z-]+$/.test(text) && text.length > 1) {
        const info = lookupWord(text);
        if (info) {
          setSelectedWord(text);
          setDictInfo(info);
          setIsSaved(false);

          // Get context sentence around the word
          const anchorNode = selection.anchorNode;
          const fullText = anchorNode?.textContent || "";
          setContextSentence(fullText.slice(0, 150));

          // Position the popup near selection
          const range = selection.getRangeAt(0);
          const rect = range.getBoundingClientRect();
          setPosition({
            x: Math.min(window.innerWidth - 320, Math.max(16, rect.left)),
            y: rect.bottom + window.scrollY + 8,
          });
        }
      }
    };

    document.addEventListener("dblclick", handleDoubleClick);
    return () => document.removeEventListener("dblclick", handleDoubleClick);
  }, []);

  const handleSpeak = () => {
    if (!selectedWord || typeof window === "undefined" || !("speechSynthesis" in window)) return;
    const utterance = new SpeechSynthesisUtterance(selectedWord);
    utterance.lang = "en-US";
    window.speechSynthesis.speak(utterance);
  };

  const handleSaveToVocab = () => {
    if (!selectedWord || !dictInfo) return;
    addVocab(selectedWord, dictInfo.definition, dictInfo.phonetic, contextSentence);
    setIsSaved(true);
    setTimeout(() => {
      setSelectedWord(null);
      setPosition(null);
    }, 1200);
  };

  if (!selectedWord || !dictInfo || !position) return null;

  return (
    <div
      style={{ left: `${position.x}px`, top: `${position.y}px` }}
      className="fixed z-50 w-72 bg-white rounded-xl shadow-xl border border-indigo-100 p-4 animate-in fade-in zoom-in-95 duration-150"
    >
      <div className="flex items-start justify-between">
        <div>
          <div className="flex items-center space-x-2">
            <h4 className="font-bold text-slate-900 text-lg capitalize">{selectedWord}</h4>
            <button
              onClick={handleSpeak}
              title="发音朗读"
              className="p-1 hover:bg-slate-100 text-indigo-600 rounded-md transition-colors"
            >
              <Volume2 className="w-4 h-4" />
            </button>
          </div>
          {dictInfo.phonetic && (
            <span className="text-xs font-mono text-slate-500 block mb-1">
              {dictInfo.phonetic}
            </span>
          )}
        </div>
        <button
          onClick={() => { setSelectedWord(null); setPosition(null); }}
          className="text-slate-400 hover:text-slate-600 p-0.5 rounded-md"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      <div className="mt-2 text-sm text-slate-700 bg-slate-50 p-2 rounded-lg border border-slate-100">
        <span className="text-xs font-semibold text-indigo-600 mr-1.5">{dictInfo.pos}</span>
        {dictInfo.definition}
      </div>

      <div className="mt-3 flex justify-end">
        <button
          onClick={handleSaveToVocab}
          disabled={isSaved}
          className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
            isSaved
              ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
              : "bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm"
          }`}
        >
          {isSaved ? (
            <>
              <Check className="w-3.5 h-3.5" />
              <span>已加入生词本</span>
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
