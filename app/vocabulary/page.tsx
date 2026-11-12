"use client";

import { useState, useEffect, useMemo, useRef, useCallback } from "react";
import { 
  getLocalState, 
  removeVocab, 
  addVocab, 
  toggleVocabMastery, 
  resetAllVocabMastery, 
  VocabItem 
} from "@/lib/storage";
import { lookupWord, getAudioUrls } from "@/lib/dictionary";
import { 
  Bookmark, 
  Search, 
  Volume2, 
  Trash2, 
  Plus, 
  Download, 
  Printer, 
  Sparkles,
  Layers,
  LayoutList,
  Shuffle,
  RotateCcw,
  ChevronLeft,
  ChevronRight,
  Eye,
  EyeOff,
  Check,
  X,
  Keyboard,
  CheckCircle2,
  AlertCircle
} from "lucide-react";

export default function VocabularyPage() {
  const [vocabList, setVocabList] = useState<VocabItem[]>([]);
  const [viewMode, setViewMode] = useState<"list" | "flashcard">("list");
  const [searchTerm, setSearchTerm] = useState("");
  const [masteryFilter, setMasteryFilter] = useState<"all" | "unmastered" | "mastered">("all");
  const [showAddModal, setShowAddModal] = useState(false);
  const [newWord, setNewWord] = useState("");
  const [newTranslation, setNewTranslation] = useState("");

  // Flashcard studio states
  const [cardIndex, setCardIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [isShuffled, setIsShuffled] = useState(false);
  const [maskContextWord, setMaskContextWord] = useState(true);
  const [autoPronounce, setAutoPronounce] = useState(false);
  const [showKeyHelp, setShowKeyHelp] = useState(false);

  // Swipe gesture refs
  const touchStartXRef = useRef<number | null>(null);
  const touchStartYRef = useRef<number | null>(null);

  useEffect(() => {
    loadVocab();
    if (typeof window !== "undefined") {
      const savedMode = localStorage.getItem("enway_vocab_view_mode");
      if (savedMode === "list" || savedMode === "flashcard") {
        setViewMode(savedMode);
      }
    }
  }, []);

  const loadVocab = () => {
    const state = getLocalState();
    setVocabList(state.vocabulary || []);
  };

  const handleSwitchMode = (mode: "list" | "flashcard") => {
    setViewMode(mode);
    setIsFlipped(false);
    if (typeof window !== "undefined") {
      try {
        localStorage.setItem("enway_vocab_view_mode", mode);
      } catch {}
    }
  };

  const triggerHaptic = (ms: number = 10) => {
    if (typeof window !== "undefined" && "vibrate" in navigator) {
      try {
        navigator.vibrate(ms);
      } catch {}
    }
  };

  const playAudio = useCallback((word: string) => {
    if (!word) return;
    triggerHaptic(10);
    try {
      const urls = getAudioUrls(word);
      const audio = new Audio(urls.us);
      audio.play().catch(() => {
        if (typeof window !== "undefined" && "speechSynthesis" in window) {
          window.speechSynthesis.cancel();
          const u = new SpeechSynthesisUtterance(word);
          u.lang = "en-US";
          window.speechSynthesis.speak(u);
        }
      });
    } catch {
      if (typeof window !== "undefined" && "speechSynthesis" in window) {
        const u = new SpeechSynthesisUtterance(word);
        u.lang = "en-US";
        window.speechSynthesis.speak(u);
      }
    }
  }, []);

  const handleDelete = (word: string) => {
    if (window.confirm(`确定从生词本中移除单词 "${word}" 吗？`)) {
      removeVocab(word);
      loadVocab();
    }
  };

  const handleToggleMastery = (word: string, force?: boolean) => {
    triggerHaptic(15);
    toggleVocabMastery(word, force);
    loadVocab();
  };

  const handleResetAllMastery = () => {
    if (window.confirm("确定要将所有生词重置为「待复习」状态吗？")) {
      resetAllVocabMastery();
      loadVocab();
    }
  };

  const handleManualAdd = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newWord.trim()) return;
    const lookup = lookupWord(newWord.trim());
    addVocab(
      newWord.trim(), 
      newTranslation.trim() || lookup?.definition || "自定义词汇", 
      lookup?.phonetic || ""
    );
    setNewWord("");
    setNewTranslation("");
    setShowAddModal(false);
    loadVocab();
  };

  const handleExportTxt = () => {
    if (vocabList.length === 0) {
      alert("生词本暂无词汇可导出");
      return;
    }

    let content = `Enway 英语专属生词复习表 (${new Date().toLocaleDateString()})\n\n`;
    vocabList.forEach((v, idx) => {
      content += `${idx + 1}. ${v.word} ${v.phonetic ? `[${v.phonetic}]` : ""}\n`;
      content += `   掌握状态: ${v.mastered ? "已掌握" : "待复习"}\n`;
      content += `   释义: ${v.translation}\n`;
      if (v.context) {
        content += `   例句/上下文: ${v.context}\n`;
      }
      content += `\n`;
    });

    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `Enway_生词本_${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Filtered list for list view search
  const filteredVocab = useMemo(() => {
    return vocabList.filter((v) => {
      const matchSearch =
        v.word.toLowerCase().includes(searchTerm.toLowerCase()) ||
        v.translation.includes(searchTerm);
      if (!matchSearch) return false;
      if (masteryFilter === "mastered") return !!v.mastered;
      if (masteryFilter === "unmastered") return !v.mastered;
      return true;
    });
  }, [vocabList, searchTerm, masteryFilter]);

  // Deck for Flashcard Studio
  const flashcardDeck = useMemo(() => {
    let list = vocabList.filter((v) => {
      if (masteryFilter === "mastered") return !!v.mastered;
      if (masteryFilter === "unmastered") return !v.mastered;
      return true;
    });

    if (isShuffled) {
      // Deterministic-like shuffle for the session
      list = [...list].sort((a, b) => a.word.localeCompare(b.word) * -1 + (a.addedAt > b.addedAt ? 1 : -1));
    }
    return list;
  }, [vocabList, masteryFilter, isShuffled]);

  const totalWords = vocabList.length;
  const masteredCount = vocabList.filter((v) => v.mastered).length;
  const unmasteredCount = totalWords - masteredCount;
  const masteryPercentage = totalWords > 0 ? Math.round((masteredCount / totalWords) * 100) : 0;

  // Active card safe index
  const safeCardIndex = flashcardDeck.length === 0 ? 0 : Math.min(cardIndex, flashcardDeck.length - 1);
  const currentCard = flashcardDeck[safeCardIndex] || null;

  const handleNextCard = useCallback(() => {
    if (flashcardDeck.length <= 1) return;
    setIsFlipped(false);
    setCardIndex((prev) => (prev + 1 < flashcardDeck.length ? prev + 1 : 0));
  }, [flashcardDeck.length]);

  const handlePrevCard = useCallback(() => {
    if (flashcardDeck.length <= 1) return;
    setIsFlipped(false);
    setCardIndex((prev) => (prev > 0 ? prev - 1 : flashcardDeck.length - 1));
  }, [flashcardDeck.length]);

  const handleCardMasteryVote = useCallback((mastered: boolean) => {
    if (!currentCard) return;
    handleToggleMastery(currentCard.word, mastered);
    // Proceed to next card automatically
    handleNextCard();
  }, [currentCard, handleNextCard]);

  // Auto pronounce on card switch
  useEffect(() => {
    if (viewMode === "flashcard" && autoPronounce && currentCard) {
      playAudio(currentCard.word);
    }
  }, [viewMode, autoPronounce, currentCard?.word, playAudio]);

  // Keyboard navigation shortcuts
  useEffect(() => {
    if (viewMode !== "flashcard") return;

    const handleKeyDown = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement)?.tagName?.toLowerCase();
      if (tag === "input" || tag === "textarea") return;

      if (e.code === "Space" || e.key === "Enter") {
        e.preventDefault();
        setIsFlipped((f) => !f);
      } else if (e.key === "ArrowRight" || e.key === "k" || e.key === "K") {
        e.preventDefault();
        handleNextCard();
      } else if (e.key === "ArrowLeft" || e.key === "j" || e.key === "J") {
        e.preventDefault();
        handlePrevCard();
      } else if (e.key === "1" || e.key === "a" || e.key === "A") {
        e.preventDefault();
        handleCardMasteryVote(false);
      } else if (e.key === "2" || e.key === "d" || e.key === "D") {
        e.preventDefault();
        handleCardMasteryVote(true);
      } else if (e.key === "p" || e.key === "P") {
        e.preventDefault();
        if (currentCard) playAudio(currentCard.word);
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [viewMode, currentCard, handleNextCard, handlePrevCard, handleCardMasteryVote, playAudio]);

  // Touch gesture listeners for mobile swipe
  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartXRef.current = e.touches[0].clientX;
    touchStartYRef.current = e.touches[0].clientY;
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (touchStartXRef.current === null || touchStartYRef.current === null) return;
    const deltaX = e.changedTouches[0].clientX - touchStartXRef.current;
    const deltaY = e.changedTouches[0].clientY - touchStartYRef.current;
    touchStartXRef.current = null;
    touchStartYRef.current = null;

    if (Math.abs(deltaX) > 45 && Math.abs(deltaX) > Math.abs(deltaY) * 1.5) {
      if (deltaX < 0) {
        handleNextCard();
      } else {
        handlePrevCard();
      }
    }
  };

  // Mask target word in context sentence
  const renderMaskedContext = (context: string, word: string, masked: boolean) => {
    if (!context) return null;
    if (!masked) return <span>&ldquo;{context}&rdquo;</span>;

    const clean = word.trim().toLowerCase();
    const regex = new RegExp(`(\\b${clean}\\w*\\b)`, "gi");
    const parts = context.split(regex);

    return (
      <span>
        &ldquo;
        {parts.map((p, i) =>
          regex.test(p) ? (
            <span
              key={i}
              className="inline-block px-1.5 py-0.5 mx-0.5 rounded font-mono font-bold bg-amber-500/15 text-amber-700 dark:text-amber-300 border border-amber-300/40 dark:border-amber-500/30"
            >
              ______
            </span>
          ) : (
            p
          )
        )}
        &rdquo;
      </span>
    );
  };

  return (
    <div className="space-y-6">
      {/* Top Banner & Control Deck */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white dark:bg-[#11131a] p-5 sm:p-6 rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 shadow-card no-print">
        <div className="flex items-center space-x-3.5">
          <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-emerald-500/20 to-teal-500/10 text-emerald-600 dark:text-cyan-400 flex items-center justify-center font-bold shadow-inner">
            <Bookmark className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h1 className="text-lg sm:text-xl font-bold text-zinc-900 dark:text-zinc-100">
                真题研读核心词汇库
              </h1>
              <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 dark:bg-cyan-500/10 dark:text-cyan-400 border border-emerald-200/50 dark:border-cyan-500/30">
                掌握率 {masteryPercentage}%
              </span>
            </div>
            <p className="text-xs text-zinc-400 dark:text-zinc-500 mt-0.5">
              真题篇章双击查词收录 · 双模沉浸背诵与考场高频语境强化
            </p>
          </div>
        </div>

        {/* Action Toolbar */}
        <div className="flex flex-wrap items-center gap-2">
          {/* View Mode Switcher Pill */}
          <div className="flex items-center p-1 rounded-xl bg-zinc-100 dark:bg-zinc-800/80 border border-zinc-200/70 dark:border-zinc-700/50">
            <button
              onClick={() => handleSwitchMode("list")}
              className={`flex items-center space-x-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                viewMode === "list"
                  ? "bg-white dark:bg-[#11131a] text-zinc-900 dark:text-cyan-400 shadow-sm"
                  : "text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-200"
              }`}
            >
              <LayoutList className="w-3.5 h-3.5" />
              <span>清单模式</span>
            </button>
            <button
              onClick={() => handleSwitchMode("flashcard")}
              className={`flex items-center space-x-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                viewMode === "flashcard"
                  ? "bg-white dark:bg-[#11131a] text-emerald-600 dark:text-cyan-400 shadow-sm"
                  : "text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-200"
              }`}
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span>3D 抽认卡背词</span>
            </button>
          </div>

          <button
            onClick={() => setShowAddModal(true)}
            className="px-3 py-1.5 rounded-xl bg-zinc-100 hover:bg-zinc-200/80 dark:bg-zinc-800/80 dark:hover:bg-zinc-700/80 text-zinc-800 dark:text-zinc-200 border border-transparent dark:border-zinc-700/50 text-xs font-semibold flex items-center space-x-1.5 transition-all shadow-subtle active:scale-[0.98]"
          >
            <Plus className="w-3.5 h-3.5" />
            <span>手动添加</span>
          </button>
          <button
            onClick={handleExportTxt}
            className="px-3 py-1.5 rounded-xl border border-black/[0.06] dark:border-cyan-500/20 bg-white dark:bg-[#151923] text-zinc-700 dark:text-zinc-300 hover:bg-zinc-50 dark:hover:bg-zinc-800 text-xs font-semibold flex items-center space-x-1.5 transition-all shadow-subtle active:scale-[0.98]"
          >
            <Download className="w-3.5 h-3.5 text-zinc-400 dark:text-zinc-500" />
            <span>导出 TXT</span>
          </button>
          <button
            onClick={() => window.print()}
            className="hidden sm:inline-flex px-3.5 py-1.5 rounded-xl bg-zinc-900 text-white hover:bg-zinc-800 dark:bg-gradient-to-r dark:from-cyan-500 dark:to-blue-600 dark:text-zinc-950 dark:font-black text-xs font-bold items-center space-x-1.5 shadow-subtle transition-all active:scale-[0.98]"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>打印</span>
          </button>
        </div>
      </div>

      {/* ======================================================== */}
      {/* MODE A: 3D FLASHCARD STUDIO                              */}
      {/* ======================================================== */}
      {viewMode === "flashcard" && (
        <div className="space-y-4 animate-in fade-in-50 duration-200 no-print">
          {/* Flashcard Studio Dashboard Header */}
          <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 p-4 shadow-card flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            {/* Filter Pills */}
            <div className="flex items-center space-x-1 overflow-x-auto no-scrollbar">
              <button
                onClick={() => { setMasteryFilter("all"); setCardIndex(0); setIsFlipped(false); }}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                  masteryFilter === "all"
                    ? "bg-zinc-900 text-white dark:bg-cyan-500 dark:text-zinc-950 shadow-sm"
                    : "bg-zinc-100 text-zinc-600 dark:bg-zinc-800/60 dark:text-zinc-400 hover:bg-zinc-200/70"
                }`}
              >
                全部 ({totalWords})
              </button>
              <button
                onClick={() => { setMasteryFilter("unmastered"); setCardIndex(0); setIsFlipped(false); }}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                  masteryFilter === "unmastered"
                    ? "bg-amber-600 text-white dark:bg-amber-500 dark:text-zinc-950 shadow-sm"
                    : "bg-zinc-100 text-zinc-600 dark:bg-zinc-800/60 dark:text-zinc-400 hover:bg-zinc-200/70"
                }`}
              >
                待复习 ({unmasteredCount})
              </button>
              <button
                onClick={() => { setMasteryFilter("mastered"); setCardIndex(0); setIsFlipped(false); }}
                className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                  masteryFilter === "mastered"
                    ? "bg-emerald-600 text-white dark:bg-emerald-500 dark:text-zinc-950 shadow-sm"
                    : "bg-zinc-100 text-zinc-600 dark:bg-zinc-800/60 dark:text-zinc-400 hover:bg-zinc-200/70"
                }`}
              >
                已掌握 ({masteredCount})
              </button>
            </div>

            {/* Studio Tools */}
            <div className="flex items-center space-x-2 justify-end">
              <button
                onClick={() => setMaskContextWord(!maskContextWord)}
                title={maskContextWord ? "当前：例句词汇已挖空（挑战记忆）" : "当前：例句显示原词"}
                className={`px-2.5 py-1.5 rounded-xl text-xs font-semibold flex items-center space-x-1 border transition-all ${
                  maskContextWord
                    ? "bg-amber-50 dark:bg-amber-500/10 border-amber-200 dark:border-amber-500/30 text-amber-700 dark:text-amber-400"
                    : "bg-zinc-50 dark:bg-zinc-800/40 border-zinc-200 dark:border-zinc-700 text-zinc-600 dark:text-zinc-400"
                }`}
              >
                {maskContextWord ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
                <span className="hidden sm:inline">{maskContextWord ? "例句挖空开" : "例句挖空关"}</span>
              </button>

              <button
                onClick={() => setIsShuffled(!isShuffled)}
                title={isShuffled ? "乱序抽查中" : "按收录时间顺序"}
                className={`px-2.5 py-1.5 rounded-xl text-xs font-semibold flex items-center space-x-1 border transition-all ${
                  isShuffled
                    ? "bg-cyan-50 dark:bg-cyan-500/10 border-cyan-200 dark:border-cyan-500/30 text-cyan-700 dark:text-cyan-400"
                    : "bg-zinc-50 dark:bg-zinc-800/40 border-zinc-200 dark:border-zinc-700 text-zinc-600 dark:text-zinc-400"
                }`}
              >
                <Shuffle className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">乱序抽查</span>
              </button>

              <button
                onClick={() => setAutoPronounce(!autoPronounce)}
                title="切换卡片时自动朗读"
                className={`px-2.5 py-1.5 rounded-xl text-xs font-semibold flex items-center space-x-1 border transition-all ${
                  autoPronounce
                    ? "bg-emerald-50 dark:bg-emerald-500/10 border-emerald-200 dark:border-emerald-500/30 text-emerald-700 dark:text-emerald-400"
                    : "bg-zinc-50 dark:bg-zinc-800/40 border-zinc-200 dark:border-zinc-700 text-zinc-600 dark:text-zinc-400"
                }`}
              >
                <Volume2 className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">自动发音</span>
              </button>

              <button
                onClick={() => setShowKeyHelp(!showKeyHelp)}
                className="p-1.5 rounded-xl text-zinc-500 hover:text-zinc-800 dark:text-zinc-400 dark:hover:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
                title="键盘快捷键说明"
              >
                <Keyboard className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Keyboard Shortcuts Hint Bar (Toggled or PC helper) */}
          {showKeyHelp && (
            <div className="bg-zinc-50 dark:bg-zinc-900/80 border border-zinc-200 dark:border-zinc-800 rounded-xl p-3 text-xs text-zinc-600 dark:text-zinc-400 flex flex-wrap items-center gap-x-4 gap-y-1.5 animate-in fade-in-50 duration-150">
              <span className="font-bold text-zinc-800 dark:text-zinc-200">极速快捷键：</span>
              <span><kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">Space</kbd> 翻转卡片</span>
              <span><kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">←</kbd> 或 <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">J</kbd> 上一词</span>
              <span><kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">→</kbd> 或 <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">K</kbd> 下一词</span>
              <span><kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">1</kbd> 标记需复习</span>
              <span><kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">2</kbd> 标记已掌握</span>
              <span><kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-zinc-700 font-mono text-[11px]">P</kbd> 重听发音</span>
            </div>
          )}

          {/* Flashcard Body */}
          {flashcardDeck.length === 0 ? (
            <div className="text-center py-20 bg-white dark:bg-[#11131a] rounded-2xl border border-dashed border-zinc-200 dark:border-zinc-800">
              <Bookmark className="w-10 h-10 text-zinc-300 dark:text-zinc-600 mx-auto mb-2.5" />
              <p className="text-zinc-700 dark:text-zinc-300 font-semibold text-sm">
                当前筛选下无匹配单词
              </p>
              <p className="text-xs text-zinc-400 dark:text-zinc-500 mt-1">
                {masteryFilter !== "all" 
                  ? "您可以切换为「全部」或去真题阅读中双击查词一键收录！"
                  : "生词本目前为空，阅读真题长难句时双击生词即可收录！"}
              </p>
              {masteryFilter !== "all" && (
                <button
                  onClick={() => setMasteryFilter("all")}
                  className="mt-3 px-3.5 py-1.5 rounded-xl bg-zinc-900 text-white dark:bg-cyan-500 dark:text-zinc-950 font-bold text-xs shadow-sm hover:opacity-90 transition-opacity"
                >
                  查看全部单词
                </button>
              )}
            </div>
          ) : (
            <div className="max-w-2xl mx-auto space-y-4">
              {/* Progress & Deck Status Bar */}
              <div className="space-y-1.5">
                <div className="flex items-center justify-between text-xs text-zinc-500 dark:text-zinc-400 font-medium px-1">
                  <span className="font-mono">
                    卡片 <span className="font-bold text-zinc-900 dark:text-zinc-100">{safeCardIndex + 1}</span> / {flashcardDeck.length}
                  </span>
                  <div className="flex items-center space-x-2">
                    <span className="text-[11px]">
                      掌握率: <span className="font-bold text-emerald-600 dark:text-cyan-400">{masteryPercentage}%</span>
                    </span>
                    {currentCard?.mastered ? (
                      <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 dark:bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-200/50 dark:border-emerald-500/20">
                        <Check className="w-2.5 h-2.5" />
                        <span>已掌握</span>
                      </span>
                    ) : (
                      <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-50 dark:bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-200/50 dark:border-amber-500/20">
                        <AlertCircle className="w-2.5 h-2.5" />
                        <span>待复习</span>
                      </span>
                    )}
                  </div>
                </div>
                {/* Visual Progress Bar */}
                <div className="w-full h-1.5 bg-zinc-200 dark:bg-zinc-800 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-emerald-500 to-teal-500 dark:from-cyan-500 dark:to-blue-500 rounded-full transition-all duration-300 ease-out"
                    style={{
                      width: `${((safeCardIndex + 1) / flashcardDeck.length) * 100}%`,
                    }}
                  />
                </div>
              </div>

              {/* 3D Flip Card Container */}
              <div 
                className="relative w-full h-[360px] sm:h-[400px] perspective-1000 select-none"
                onTouchStart={handleTouchStart}
                onTouchEnd={handleTouchEnd}
              >
                <div
                  onClick={() => setIsFlipped(!isFlipped)}
                  className={`relative w-full h-full duration-500 transform-style-3d transition-transform cursor-pointer ${
                    isFlipped ? "rotate-y-180" : ""
                  }`}
                >
                  {/* ================= FRONT SIDE ================= */}
                  <div className="absolute inset-0 w-full h-full backface-hidden bg-white dark:bg-[#11131a] rounded-3xl border border-black/[0.08] dark:border-cyan-500/25 shadow-xl p-6 sm:p-8 flex flex-col justify-between hover:border-black/[0.16] dark:hover:border-cyan-400/50 transition-colors">
                    {/* Front Header */}
                    <div className="flex items-center justify-between text-xs text-zinc-400 dark:text-zinc-500 font-mono">
                      <div className="flex items-center space-x-1.5">
                        <span className="w-2 h-2 rounded-full bg-cyan-500 animate-pulse" />
                        <span>考点词汇 · 正面</span>
                      </div>
                      <span className="text-[11px] bg-zinc-100 dark:bg-zinc-800 px-2 py-0.5 rounded-full">
                        点击卡片或按空格翻转
                      </span>
                    </div>

                    {/* Word Core Display */}
                    <div className="my-auto text-center space-y-3">
                      <div className="flex items-center justify-center space-x-3">
                        <h2 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-zinc-900 dark:text-zinc-50 tracking-tight capitalize">
                          {currentCard.word}
                        </h2>
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            playAudio(currentCard.word);
                          }}
                          title="发音 (按 P)"
                          className="p-2 sm:p-2.5 rounded-2xl bg-zinc-100 hover:bg-zinc-200 dark:bg-zinc-800/80 dark:hover:bg-zinc-700 text-zinc-700 dark:text-cyan-400 transition-all active:scale-95 shadow-sm"
                        >
                          <Volume2 className="w-5 h-5" />
                        </button>
                      </div>

                      {currentCard.phonetic && (
                        <div className="text-sm sm:text-base font-mono text-zinc-500 dark:text-cyan-400/90 font-medium">
                          /{currentCard.phonetic.replace(/[/\[\]]/g, "")}/
                        </div>
                      )}

                      {/* Context Masked Sentence */}
                      {currentCard.context && (
                        <div className="mt-4 pt-4 border-t border-zinc-100 dark:border-zinc-800/80 max-w-lg mx-auto">
                          <p className="text-xs sm:text-sm text-zinc-600 dark:text-zinc-300 italic leading-relaxed text-left bg-zinc-50/70 dark:bg-zinc-900/40 p-3.5 rounded-2xl border border-zinc-100 dark:border-zinc-800/50">
                            {renderMaskedContext(currentCard.context, currentCard.word, maskContextWord)}
                          </p>
                        </div>
                      )}
                    </div>

                    {/* Front Footer Hint */}
                    <div className="text-center pt-2 text-[11px] text-zinc-400 dark:text-zinc-500 flex items-center justify-center space-x-1">
                      <span>👆 点击卡片翻开背面看释义</span>
                    </div>
                  </div>

                  {/* ================= BACK SIDE ================= */}
                  <div className="absolute inset-0 w-full h-full backface-hidden rotate-y-180 bg-white dark:bg-[#11131a] rounded-3xl border border-emerald-500/30 dark:border-cyan-500/30 shadow-xl p-6 sm:p-8 flex flex-col justify-between">
                    {/* Back Header */}
                    <div className="flex items-center justify-between text-xs font-mono text-zinc-400 dark:text-zinc-500">
                      <div className="flex items-center space-x-1.5">
                        <span className="w-2 h-2 rounded-full bg-emerald-500" />
                        <span className="text-emerald-600 dark:text-emerald-400 font-bold">考点详析 · 背面</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleDelete(currentCard.word);
                          }}
                          title="从生词本删除"
                          className="p-1 hover:text-rose-500 rounded-lg transition-colors"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>

                    {/* Back Content */}
                    <div className="my-auto space-y-4">
                      <div className="flex items-baseline space-x-3">
                        <h3 className="text-2xl sm:text-3xl font-extrabold text-zinc-900 dark:text-zinc-100 capitalize">
                          {currentCard.word}
                        </h3>
                        {currentCard.phonetic && (
                          <span className="text-xs font-mono text-zinc-400 dark:text-cyan-400/80">
                            /{currentCard.phonetic.replace(/[/\[\]]/g, "")}/
                          </span>
                        )}
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            playAudio(currentCard.word);
                          }}
                          className="p-1 text-zinc-500 hover:text-zinc-800 dark:hover:text-cyan-400"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                      </div>

                      {/* Translation Box */}
                      <div className="bg-emerald-50/50 dark:bg-emerald-950/20 border border-emerald-200/60 dark:border-emerald-500/20 p-4 rounded-2xl">
                        <span className="text-[11px] font-bold text-emerald-700 dark:text-emerald-400 uppercase tracking-wider block mb-1">
                          核心考点释义
                        </span>
                        <p className="text-sm sm:text-base font-semibold text-zinc-900 dark:text-zinc-100 leading-relaxed">
                          {currentCard.translation}
                        </p>
                      </div>

                      {/* Full Context Sentence */}
                      {currentCard.context && (
                        <div className="bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200/50 dark:border-zinc-800 p-3.5 rounded-2xl">
                          <span className="text-[10px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-wider block mb-1">
                            真题原句上下文
                          </span>
                          <p className="text-xs sm:text-sm text-zinc-700 dark:text-zinc-300 italic leading-relaxed">
                            &ldquo;{currentCard.context}&rdquo;
                          </p>
                        </div>
                      )}
                    </div>

                    {/* Back Mastery Decision Buttons */}
                    <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800/80 flex items-center justify-between gap-3">
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleCardMasteryVote(false);
                        }}
                        className="flex-1 py-2.5 px-4 rounded-2xl border border-amber-300 dark:border-amber-500/30 bg-amber-50/60 hover:bg-amber-100/70 dark:bg-amber-950/30 dark:hover:bg-amber-950/50 text-amber-800 dark:text-amber-300 font-bold text-xs flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
                      >
                        <X className="w-4 h-4 text-amber-600 dark:text-amber-400" />
                        <span>需重背 <span className="hidden sm:inline font-mono opacity-60 text-[10px]">(按 1)</span></span>
                      </button>

                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleCardMasteryVote(true);
                        }}
                        className="flex-1 py-2.5 px-4 rounded-2xl border border-emerald-300 dark:border-emerald-500/30 bg-emerald-50/60 hover:bg-emerald-100/70 dark:bg-emerald-950/30 dark:hover:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 font-bold text-xs flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
                      >
                        <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                        <span>已掌握 <span className="hidden sm:inline font-mono opacity-60 text-[10px]">(按 2)</span></span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              {/* Navigation Action Deck */}
              <div className="flex items-center justify-between gap-3 pt-2">
                <button
                  type="button"
                  onClick={handlePrevCard}
                  className="flex-1 py-2.5 px-4 rounded-2xl bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/20 hover:border-black/[0.14] dark:hover:border-cyan-400/50 text-zinc-700 dark:text-zinc-300 font-bold text-xs flex items-center justify-center space-x-1.5 shadow-sm transition-all active:scale-[0.98]"
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>上一词 <span className="hidden sm:inline font-mono opacity-50">(←/J)</span></span>
                </button>

                <button
                  type="button"
                  onClick={() => setIsFlipped(!isFlipped)}
                  className="py-2.5 px-5 rounded-2xl bg-zinc-900 text-white hover:bg-zinc-800 dark:bg-cyan-500 dark:text-zinc-950 font-extrabold text-xs flex items-center justify-center space-x-1.5 shadow-sm transition-all active:scale-[0.98]"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>翻转 <span className="hidden sm:inline font-mono opacity-60">(Space)</span></span>
                </button>

                <button
                  type="button"
                  onClick={handleNextCard}
                  className="flex-1 py-2.5 px-4 rounded-2xl bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/20 hover:border-black/[0.14] dark:hover:border-cyan-400/50 text-zinc-700 dark:text-zinc-300 font-bold text-xs flex items-center justify-center space-x-1.5 shadow-sm transition-all active:scale-[0.98]"
                >
                  <span>下一词 <span className="hidden sm:inline font-mono opacity-50">(→/K)</span></span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* ======================================================== */}
      {/* MODE B: LIST VIEW                                        */}
      {/* ======================================================== */}
      {viewMode === "list" && (
        <div className="space-y-4 animate-in fade-in-50 duration-200">
          {/* Search & List Filter Bar */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 no-print">
            <div className="relative max-w-md w-full">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-zinc-400 dark:text-zinc-500">
                <Search className="w-4 h-4" />
              </div>
              <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="搜索生词、音标或中文释义..."
                className="w-full pl-10 pr-4 py-2 bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/20 rounded-xl text-xs text-zinc-800 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 focus:outline-none focus:ring-1 focus:ring-zinc-900 dark:focus:ring-cyan-500 shadow-subtle"
              />
            </div>

            <div className="flex items-center space-x-2">
              {/* Mastery Quick Filter */}
              <div className="flex items-center p-1 rounded-xl bg-zinc-100 dark:bg-zinc-800/80 border border-zinc-200/70 dark:border-zinc-700/50 text-xs">
                <button
                  onClick={() => setMasteryFilter("all")}
                  className={`px-2.5 py-1 rounded-lg font-semibold transition-all ${
                    masteryFilter === "all"
                      ? "bg-white dark:bg-[#11131a] text-zinc-900 dark:text-cyan-400 shadow-sm"
                      : "text-zinc-600 dark:text-zinc-400"
                  }`}
                >
                  全部 ({totalWords})
                </button>
                <button
                  onClick={() => setMasteryFilter("unmastered")}
                  className={`px-2.5 py-1 rounded-lg font-semibold transition-all ${
                    masteryFilter === "unmastered"
                      ? "bg-white dark:bg-[#11131a] text-amber-600 dark:text-amber-400 shadow-sm"
                      : "text-zinc-600 dark:text-zinc-400"
                  }`}
                >
                  待复习 ({unmasteredCount})
                </button>
                <button
                  onClick={() => setMasteryFilter("mastered")}
                  className={`px-2.5 py-1 rounded-lg font-semibold transition-all ${
                    masteryFilter === "mastered"
                      ? "bg-white dark:bg-[#11131a] text-emerald-600 dark:text-emerald-400 shadow-sm"
                      : "text-zinc-600 dark:text-zinc-400"
                  }`}
                >
                  已掌握 ({masteredCount})
                </button>
              </div>

              {masteredCount > 0 && (
                <button
                  onClick={handleResetAllMastery}
                  title="一键重置所有生词为待复习"
                  className="px-2.5 py-1.5 rounded-xl text-xs text-zinc-500 hover:text-zinc-800 dark:text-zinc-400 dark:hover:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
                >
                  重置掌握
                </button>
              )}
            </div>
          </div>

          {/* Printable Heading */}
          <div className="hidden print-only text-center mb-6">
            <h1 className="text-2xl font-black mb-1">Enway 英语生词重点复习表</h1>
            <p className="text-xs text-slate-500">
              总计收录 {filteredVocab.length} 个重点考点词汇 · 打印时间: {new Date().toLocaleDateString()}
            </p>
          </div>

          {/* Vocabulary Cards Grid */}
          {filteredVocab.length === 0 ? (
            <div className="text-center py-20 bg-white dark:bg-[#11131a] rounded-2xl border border-dashed border-zinc-200 dark:border-zinc-800 no-print">
              <Bookmark className="w-10 h-10 text-zinc-300 dark:text-zinc-600 mx-auto mb-2.5" />
              <p className="text-zinc-600 dark:text-zinc-300 font-semibold text-sm">
                {searchTerm ? "未搜索到匹配生词" : "当前分类下暂无生词"}
              </p>
              <p className="text-xs text-zinc-400 dark:text-zinc-500 mt-1">
                在试卷阅读材料中直接双击任意单词，即可一键加入生词本！
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredVocab.map((item) => (
                <div
                  key={item.word}
                  className="bg-white dark:bg-[#11131a] rounded-2xl border border-black/[0.06] dark:border-cyan-500/20 hover:border-black/[0.14] dark:hover:border-cyan-400/50 p-5 shadow-card hover:shadow-card-hover hover:-translate-y-[1px] transition-all duration-150 flex flex-col justify-between print-card group"
                >
                  <div>
                    <div className="flex items-start justify-between">
                      <div className="flex items-center space-x-2">
                        <h3 className="text-base font-bold text-zinc-900 dark:text-zinc-100 capitalize">
                          {item.word}
                        </h3>
                        <button
                          onClick={() => playAudio(item.word)}
                          title="朗读单词"
                          className="p-1 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-cyan-400 rounded-lg transition-colors no-print"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>

                      <div className="flex items-center space-x-1.5 no-print">
                        {/* Toggle Mastery Button */}
                        <button
                          onClick={() => handleToggleMastery(item.word)}
                          title={item.mastered ? "点击标记为需复习" : "点击标记为已掌握"}
                          className={`px-2 py-0.5 rounded-lg text-[10px] font-bold border transition-all ${
                            item.mastered
                              ? "bg-emerald-50 dark:bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border-emerald-200/60 dark:border-emerald-500/30"
                              : "bg-amber-50 dark:bg-amber-500/10 text-amber-700 dark:text-amber-400 border-amber-200/60 dark:border-amber-500/30"
                          }`}
                        >
                          {item.mastered ? "已掌握" : "待复习"}
                        </button>

                        <button
                          onClick={() => handleDelete(item.word)}
                          title="从生词本移除"
                          className="text-zinc-400 dark:text-zinc-600 hover:text-rose-600 dark:hover:text-rose-400 p-1 rounded-lg transition-colors"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>

                    {item.phonetic && (
                      <span className="text-xs font-mono text-zinc-400 dark:text-cyan-400/80 block mt-0.5">
                        /{item.phonetic.replace(/[/\[\]]/g, "")}/
                      </span>
                    )}

                    <p className="mt-3 text-xs text-zinc-800 dark:text-zinc-200 font-medium bg-zinc-50/80 dark:bg-zinc-900/60 p-2.5 rounded-xl border border-black/[0.03] dark:border-white/5 leading-relaxed">
                      {item.translation}
                    </p>

                    {item.context && (
                      <div className="mt-2 text-[11px] text-zinc-600 dark:text-zinc-300 italic bg-amber-50/40 dark:bg-amber-950/20 p-2 rounded-lg border border-amber-100/50 dark:border-amber-500/20">
                        &ldquo;{item.context.trim()}...&rdquo;
                      </div>
                    )}
                  </div>

                  <div className="mt-4 pt-2.5 border-t border-zinc-100 dark:border-zinc-800/80 flex items-center justify-between text-[10px] text-zinc-400 dark:text-zinc-500 no-print font-mono">
                    <span>收录于: {new Date(item.addedAt).toLocaleDateString()}</span>
                    {item.reviewCount ? <span>已复习 {item.reviewCount} 次</span> : null}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Manual Add Modal */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-[#11131a] rounded-2xl max-w-sm w-full p-6 shadow-2xl border border-transparent dark:border-cyan-500/20 space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <h3 className="font-bold text-slate-900 dark:text-zinc-100 text-base">手动添加生词</h3>
            <form onSubmit={handleManualAdd} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-zinc-300 mb-1">
                  英文单词
                </label>
                <input
                  type="text"
                  required
                  value={newWord}
                  onChange={(e) => setNewWord(e.target.value)}
                  placeholder="例如: resilient"
                  className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 rounded-xl text-xs text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-zinc-300 mb-1">
                  中文释义 (可留空自动识别)
                </label>
                <input
                  type="text"
                  value={newTranslation}
                  onChange={(e) => setNewTranslation(e.target.value)}
                  placeholder="例如: adj. 有弹性的；能复原的"
                  className="w-full px-3 py-2 bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 rounded-xl text-xs text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-500"
                />
              </div>
              <div className="flex justify-end space-x-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  className="px-3 py-2 text-xs font-semibold text-slate-600 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-xl"
                >
                  取消
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 rounded-xl shadow-sm font-bold"
                >
                  确认添加
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}