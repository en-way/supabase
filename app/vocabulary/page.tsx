"use client";

import { useState, useEffect, useMemo, useRef, useCallback } from "react";
import {
  getLocalState,
  subscribeLocalState,
  removeVocab,
  addVocab,
  toggleVocabMastery,
  resetAllVocabMastery,
  type VocabItem,
} from "@/lib/storage";
import { lookupWordAsync, getAudioUrls } from "@/lib/dictionary";
import { useKeyboardGuard } from "@/hooks/useKeyboardGuard";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { EmptyState } from "@/components/ui/Feedback";
import { Input } from "@/components/ui/Field";
import { Kbd } from "@/components/ui/Kbd";
import { Modal } from "@/components/ui/Modal";
import { PageHeader } from "@/components/ui/PageHeader";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { SegmentedControl } from "@/components/ui/SegmentedControl";
import {
  Bookmark,
  Search,
  Volume2,
  Trash2,
  Plus,
  Download,
  Printer,
  Sparkles,
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
  AlertCircle,
} from "lucide-react";

export default function VocabularyPage() {
  const [vocabList, setVocabList] = useState<VocabItem[]>([]);
  const [viewMode, setViewMode] = useState<"list" | "flashcard">("list");
  const [searchTerm, setSearchTerm] = useState("");
  const [masteryFilter, setMasteryFilter] = useState<"all" | "unmastered" | "mastered">(
    "all"
  );
  const [showAddModal, setShowAddModal] = useState(false);
  const [newWord, setNewWord] = useState("");
  const [newTranslation, setNewTranslation] = useState("");

  // Flashcard studio states
  const [cardIndex, setCardIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [isShuffled, setIsShuffled] = useState(false);
  const [shuffledOrder, setShuffledOrder] = useState<Record<string, number>>({});
  const [hideListTranslation, setHideListTranslation] = useState(false);
  const [autoPronounce, setAutoPronounce] = useState(false);
  const [showKeyHelp, setShowKeyHelp] = useState(false);

  const touchStartXRef = useRef<number | null>(null);
  const touchStartYRef = useRef<number | null>(null);
  const activeAudioRef = useRef<HTMLAudioElement | null>(null);

  const loadVocab = useCallback(() => {
    const state = getLocalState();
    setVocabList(state.vocabulary || []);
  }, []);

  useEffect(() => {
    loadVocab();
    if (typeof window !== "undefined") {
      const savedMode = localStorage.getItem("enway_vocab_view_mode");
      if (savedMode === "list" || savedMode === "flashcard") {
        setViewMode(savedMode);
      }
    }
    const unsubscribe = subscribeLocalState((state) => {
      setVocabList(state.vocabulary || []);
    });
    return () => unsubscribe();
  }, [loadVocab]);

  useEffect(() => {
    return () => {
      if (activeAudioRef.current) {
        try {
          activeAudioRef.current.pause();
        } catch {}
      }
    };
  }, []);

  const triggerHaptic = (ms: number = 10) => {
    if (typeof window !== "undefined" && "vibrate" in navigator) {
      try {
        navigator.vibrate(ms);
      } catch {}
    }
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

  const playAudio = useCallback((word: string) => {
    if (!word) return;
    triggerHaptic(10);

    if (activeAudioRef.current) {
      try {
        activeAudioRef.current.pause();
        activeAudioRef.current.currentTime = 0;
      } catch {}
      activeAudioRef.current = null;
    }
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      try {
        window.speechSynthesis.cancel();
      } catch {}
    }

    try {
      const urls = getAudioUrls(word);
      const audio = new Audio(urls.us);
      activeAudioRef.current = audio;
      audio.onended = () => {
        if (activeAudioRef.current === audio) activeAudioRef.current = null;
      };
      audio.play().catch(() => {
        if (typeof window !== "undefined" && "speechSynthesis" in window) {
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

  const handleToggleMastery = useCallback(
    (word: string, force?: boolean) => {
      triggerHaptic(15);
      toggleVocabMastery(word, force);
      loadVocab();
    },
    [loadVocab]
  );

  const handleResetAllMastery = () => {
    if (window.confirm("确定要将所有生词重置为「待复习」状态吗？")) {
      resetAllVocabMastery();
      loadVocab();
    }
  };

  const handleManualAdd = async (e: React.FormEvent) => {
    e.preventDefault();
    const trimmedWord = newWord.trim();
    if (!trimmedWord) return;

    let definition = newTranslation.trim();
    let phonetic = "";

    if (!definition) {
      try {
        const lookup = await lookupWordAsync(trimmedWord);
        if (lookup?.definition) {
          definition = lookup.definition;
          phonetic = lookup.phonetic || "";
        }
      } catch {}
    }

    if (!definition) definition = "自定义词汇";

    addVocab(trimmedWord, definition, phonetic);
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
      if (v.context) content += `   例句/上下文: ${v.context}\n`;
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

  const handleToggleShuffle = () => {
    if (!isShuffled) {
      const words = vocabList.map((v) => v.word);
      for (let i = words.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [words[i], words[j]] = [words[j], words[i]];
      }
      const rankMap: Record<string, number> = {};
      words.forEach((w, idx) => {
        rankMap[w] = idx;
      });
      setShuffledOrder(rankMap);
      setIsShuffled(true);
    } else {
      setIsShuffled(false);
    }
    setCardIndex(0);
    setIsFlipped(false);
  };

  const flashcardDeck = useMemo(() => {
    let list = vocabList.filter((v) => {
      if (masteryFilter === "mastered") return !!v.mastered;
      if (masteryFilter === "unmastered") return !v.mastered;
      return true;
    });

    if (isShuffled) {
      list = [...list].sort(
        (a, b) =>
          (shuffledOrder[a.word] ?? Number.MAX_SAFE_INTEGER) -
          (shuffledOrder[b.word] ?? Number.MAX_SAFE_INTEGER)
      );
    }
    return list;
  }, [vocabList, masteryFilter, isShuffled, shuffledOrder]);

  const totalWords = vocabList.length;
  const masteredCount = vocabList.filter((v) => v.mastered).length;
  const unmasteredCount = totalWords - masteredCount;
  const masteryPercentage =
    totalWords > 0 ? Math.round((masteredCount / totalWords) * 100) : 0;

  const safeCardIndex =
    flashcardDeck.length === 0 ? 0 : Math.min(cardIndex, flashcardDeck.length - 1);
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

  const handleCardMasteryVote = useCallback(
    (mastered: boolean) => {
      if (!currentCard) return;
      setIsFlipped(false);
      handleToggleMastery(currentCard.word, mastered);

      const willBeRemoved =
        (masteryFilter === "unmastered" && mastered === true) ||
        (masteryFilter === "mastered" && mastered === false);

      if (willBeRemoved) {
        setCardIndex((prev) =>
          prev >= flashcardDeck.length - 1 ? Math.max(0, flashcardDeck.length - 2) : prev
        );
      } else {
        handleNextCard();
      }
    },
    [
      currentCard,
      masteryFilter,
      flashcardDeck.length,
      handleNextCard,
      handleToggleMastery,
    ]
  );

  useEffect(() => {
    if (viewMode === "flashcard" && autoPronounce && currentCard) {
      playAudio(currentCard.word);
    }
  }, [viewMode, autoPronounce, currentCard, playAudio]);

  useKeyboardGuard(
    (e: KeyboardEvent) => {
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
    },
    viewMode === "flashcard" && !showAddModal
  );

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
      if (deltaX < 0) handleNextCard();
      else handlePrevCard();
    }
  };

  const escapeRegExp = (str: string) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

  const renderMaskedContext = (context: string, word: string, masked: boolean) => {
    if (!context) return null;
    if (!masked) return <span>&ldquo;{context}&rdquo;</span>;

    const clean = word.trim().toLowerCase();
    if (!clean) return <span>&ldquo;{context}&rdquo;</span>;

    try {
      const safePattern = escapeRegExp(clean);
      const regex = new RegExp(`(\\b${safePattern}\\w*\\b)`, "gi");
      const parts = context.split(regex);

      return (
        <span>
          &ldquo;
          {parts.map((p, i) =>
            i % 2 === 1 ? (
              <span
                key={i}
                className="inline-block px-1.5 py-0.5 mx-0.5 rounded font-mono font-bold bg-warning-soft text-warning border border-warning/30"
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
    } catch {
      return <span>&ldquo;{context}&rdquo;</span>;
    }
  };

  return (
    <div className="space-y-6">
      <PageHeader
        icon={<Bookmark className="w-5 h-5 text-primary" />}
        title="真题研读核心词汇库"
        description="真题篇章双击查词收录 · 双模沉浸背诵与考场高频语境强化"
        badge={<Badge tone="primary">掌握率 {masteryPercentage}%</Badge>}
        actions={
          <div className="flex flex-wrap items-center gap-2">
            <SegmentedControl
              value={viewMode}
              onChange={handleSwitchMode}
              size="sm"
              options={[
                {
                  value: "list",
                  label: (
                    <span className="inline-flex items-center gap-1">
                      <LayoutList className="w-3.5 h-3.5" />
                      <span>清单模式</span>
                    </span>
                  ),
                },
                {
                  value: "flashcard",
                  label: (
                    <span className="inline-flex items-center gap-1">
                      <Sparkles className="w-3.5 h-3.5" />
                      <span>3D 抽认卡</span>
                    </span>
                  ),
                },
              ]}
            />

            <Button
              variant="secondary"
              size="sm"
              onClick={() => setShowAddModal(true)}
            >
              <Plus className="w-3.5 h-3.5" />
              <span>手动添加</span>
            </Button>

            <Button variant="secondary" size="sm" onClick={handleExportTxt}>
              <Download className="w-3.5 h-3.5" />
              <span>导出 TXT</span>
            </Button>

            <Button
              size="sm"
              onClick={() => window.print()}
              className="hidden sm:inline-flex"
            >
              <Printer className="w-3.5 h-3.5" />
              <span>打印</span>
            </Button>
          </div>
        }
      />

      {/* MODE A: 3D FLASHCARD STUDIO */}
      {viewMode === "flashcard" && (
        <div className="space-y-4 animate-in fade-in duration-200 no-print">
          <Card className="p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <SegmentedControl
              value={masteryFilter}
              onChange={(val) => {
                setMasteryFilter(val);
                setCardIndex(0);
                setIsFlipped(false);
              }}
              size="sm"
              options={[
                { value: "all", label: `全部 (${totalWords})` },
                { value: "unmastered", label: `待复习 (${unmasteredCount})` },
                { value: "mastered", label: `已掌握 (${masteredCount})` },
              ]}
            />

            <div className="flex items-center gap-2 justify-start sm:justify-end flex-wrap">
              <Button
                variant={isShuffled ? "primary" : "secondary"}
                size="sm"
                onClick={handleToggleShuffle}
                title={isShuffled ? "乱序抽查中" : "按收录时间顺序"}
              >
                <Shuffle className="w-3.5 h-3.5" />
                <span className="sm:hidden">乱序</span>
                <span className="hidden sm:inline">乱序抽查</span>
              </Button>

              <Button
                variant={autoPronounce ? "primary" : "secondary"}
                size="sm"
                onClick={() => setAutoPronounce(!autoPronounce)}
                title="切换卡片时自动朗读"
              >
                <Volume2 className="w-3.5 h-3.5" />
                <span className="sm:hidden">自动读</span>
                <span className="hidden sm:inline">自动发音</span>
              </Button>

              <Button
                variant="secondary"
                size="sm"
                onClick={() => setShowKeyHelp(!showKeyHelp)}
                title="键盘快捷键说明"
                aria-label="键盘快捷键说明"
                className="px-2.5 hidden lg:inline-flex"
              >
                <Keyboard className="w-4 h-4" />
              </Button>
            </div>
          </Card>

          {showKeyHelp && (
            <div className="bg-surface-2 border border-border rounded-xl p-3 text-xs text-fg-muted flex flex-wrap items-center gap-x-4 gap-y-1.5 animate-in fade-in duration-150">
              <span className="font-bold text-fg">极速快捷键：</span>
              <span className="inline-flex items-center gap-1">
                <Kbd>Space</Kbd> 翻转卡片
              </span>
              <span className="inline-flex items-center gap-1">
                <Kbd>←</Kbd> / <Kbd>J</Kbd> 上一词
              </span>
              <span className="inline-flex items-center gap-1">
                <Kbd>→</Kbd> / <Kbd>K</Kbd> 下一词
              </span>
              <span className="inline-flex items-center gap-1">
                <Kbd>1</Kbd> 标记需复习
              </span>
              <span className="inline-flex items-center gap-1">
                <Kbd>2</Kbd> 标记已掌握
              </span>
              <span className="inline-flex items-center gap-1">
                <Kbd>P</Kbd> 重听发音
              </span>
            </div>
          )}

          {flashcardDeck.length === 0 ? (
            <Card className="py-12 px-4">
              <EmptyState
                icon={<Bookmark className="w-8 h-8" />}
                title="当前筛选下无匹配单词"
                description={
                  masteryFilter !== "all"
                    ? "您可以切换为「全部」或去真题阅读中双击查词一键收录！"
                    : "生词本目前为空，阅读真题长难句时双击生词即可收录！"
                }
                action={
                  masteryFilter !== "all" ? (
                    <Button size="sm" onClick={() => setMasteryFilter("all")}>
                      查看全部单词
                    </Button>
                  ) : undefined
                }
              />
            </Card>
          ) : (
            <div className="max-w-2xl mx-auto space-y-4">
              <div className="space-y-1.5">
                <div className="flex items-center justify-between text-xs text-fg-muted font-medium px-1">
                  <span className="font-mono tabular-nums">
                    卡片 <span className="font-bold text-fg">{safeCardIndex + 1}</span> /{" "}
                    {flashcardDeck.length}
                  </span>
                  <div className="flex items-center gap-2">
                    <span className="text-[11px] font-mono tabular-nums">
                      掌握率：<span className="font-bold text-primary">{masteryPercentage}%</span>
                    </span>
                    {currentCard?.mastered ? (
                      <Badge tone="success">
                        <Check className="w-3 h-3" />
                        <span>已掌握</span>
                      </Badge>
                    ) : (
                      <Badge tone="warning">
                        <AlertCircle className="w-3 h-3" />
                        <span>待复习</span>
                      </Badge>
                    )}
                  </div>
                </div>
                <ProgressBar
                  value={safeCardIndex + 1}
                  max={flashcardDeck.length}
                  tone="primary"
                />
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
                  {/* FRONT SIDE */}
                  <div className="absolute inset-0 w-full h-full backface-hidden bg-surface rounded-3xl border border-border shadow-2 p-6 sm:p-8 flex flex-col justify-between hover:border-primary/40 transition-colors">
                    <div className="flex items-center justify-between text-xs text-fg-subtle font-mono">
                      <div className="flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-primary animate-pulse" />
                        <span>考点词汇 · 正面</span>
                      </div>
                      <Badge tone="neutral">
                        点击卡片<span className="hidden lg:inline">或按空格</span>翻转
                      </Badge>
                    </div>

                    <div className="my-auto text-center space-y-3">
                      <div className="flex items-center justify-center gap-3">
                        <h2 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-fg tracking-tight capitalize font-reading">
                          {currentCard.word}
                        </h2>
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            playAudio(currentCard.word);
                          }}
                          title="发音 (按 P)"
                          aria-label="播放单词发音"
                          className="p-2.5 rounded-2xl bg-surface-2 hover:bg-border/60 text-fg transition-colors active:scale-95 border border-border"
                        >
                          <Volume2 className="w-5 h-5" />
                        </button>
                      </div>

                      {currentCard.phonetic && (
                        <div className="text-sm sm:text-base font-mono text-primary font-medium">
                          /{currentCard.phonetic.replace(/[/\[\]]/g, "")}/
                        </div>
                      )}

                      {currentCard.context && (
                        <div className="mt-4 pt-4 border-t border-border max-w-lg mx-auto">
                          <p className="text-xs sm:text-sm text-fg-muted italic leading-relaxed text-left bg-surface-2/80 p-3.5 rounded-2xl border border-border font-reading">
                            {renderMaskedContext(
                              currentCard.context,
                              currentCard.word,
                              true
                            )}
                          </p>
                        </div>
                      )}
                    </div>

                    <div className="text-center pt-2 text-[11px] text-fg-subtle">
                      点击卡片翻开背面看释义
                    </div>
                  </div>

                  {/* BACK SIDE */}
                  <div className="absolute inset-0 w-full h-full backface-hidden rotate-y-180 bg-surface rounded-3xl border border-primary/40 shadow-2 p-6 sm:p-8 flex flex-col justify-between">
                    <div className="flex items-center justify-between text-xs font-mono text-fg-subtle">
                      <div className="flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-success" />
                        <span className="text-success font-bold">考点详析 · 背面</span>
                      </div>
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleDelete(currentCard.word);
                        }}
                        title="从生词本删除"
                        aria-label="从生词本删除"
                        className="p-1 text-fg-subtle hover:text-danger rounded-lg transition-colors"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>

                    <div className="my-auto space-y-4">
                      <div className="flex items-baseline gap-3">
                        <h3 className="text-2xl sm:text-3xl font-extrabold text-fg capitalize font-reading">
                          {currentCard.word}
                        </h3>
                        {currentCard.phonetic && (
                          <span className="text-xs font-mono text-primary">
                            /{currentCard.phonetic.replace(/[/\[\]]/g, "")}/
                          </span>
                        )}
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            playAudio(currentCard.word);
                          }}
                          aria-label="播放单词发音"
                          className="p-1 text-fg-muted hover:text-primary"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                      </div>

                      <div className="bg-primary-soft border border-primary/25 p-4 rounded-2xl">
                        <span className="text-[11px] font-bold text-primary uppercase tracking-wider block mb-1">
                          核心考点释义
                        </span>
                        <p className="text-sm sm:text-base font-semibold text-fg leading-relaxed">
                          {currentCard.translation}
                        </p>
                      </div>

                      {currentCard.context && (
                        <div className="bg-surface-2 border border-border p-3.5 rounded-2xl">
                          <span className="text-[10px] font-bold text-fg-subtle uppercase tracking-wider block mb-1">
                            真题原句上下文
                          </span>
                          <p className="text-xs sm:text-sm text-fg-muted italic leading-relaxed font-reading">
                            &ldquo;{currentCard.context}&rdquo;
                          </p>
                        </div>
                      )}
                    </div>

                    <div className="pt-2 border-t border-border flex items-center justify-between gap-3">
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleCardMasteryVote(false);
                        }}
                        className="flex-1 py-2.5 px-4 rounded-2xl border border-warning/40 bg-warning-soft hover:opacity-90 text-warning font-bold text-xs flex items-center justify-center gap-1.5 transition-opacity active:scale-[0.98]"
                      >
                        <X className="w-4 h-4" />
                        <span>
                          需重背{" "}
                          <span className="hidden sm:inline font-mono opacity-70 text-[10px]">
                            (1)
                          </span>
                        </span>
                      </button>

                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleCardMasteryVote(true);
                        }}
                        className="flex-1 py-2.5 px-4 rounded-2xl border border-success/40 bg-success-soft hover:opacity-90 text-success font-bold text-xs flex items-center justify-center gap-1.5 transition-opacity active:scale-[0.98]"
                      >
                        <Check className="w-4 h-4" />
                        <span>
                          已掌握{" "}
                          <span className="hidden sm:inline font-mono opacity-70 text-[10px]">
                            (2)
                          </span>
                        </span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <div className="flex items-center justify-between gap-3 pt-2">
                <Button
                  variant="secondary"
                  className="flex-1"
                  onClick={handlePrevCard}
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>
                    上一词{" "}
                    <span className="hidden sm:inline font-mono opacity-60">(←/J)</span>
                  </span>
                </Button>

                <Button onClick={() => setIsFlipped(!isFlipped)}>
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>
                    翻转{" "}
                    <span className="hidden sm:inline font-mono opacity-75">(Space)</span>
                  </span>
                </Button>

                <Button
                  variant="secondary"
                  className="flex-1"
                  onClick={handleNextCard}
                >
                  <span>
                    下一词{" "}
                    <span className="hidden sm:inline font-mono opacity-60">(→/K)</span>
                  </span>
                  <ChevronRight className="w-4 h-4" />
                </Button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* MODE B: LIST VIEW */}
      {viewMode === "list" && (
        <div className="space-y-4 animate-in fade-in duration-200">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 no-print">
            <div className="relative max-w-md w-full">
              <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-fg-subtle pointer-events-none" />
              <Input
                compact
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="搜索生词、音标或中文释义..."
                className="pl-10"
              />
            </div>

            <div className="flex items-center gap-2 flex-wrap">
              <SegmentedControl
                value={masteryFilter}
                onChange={setMasteryFilter}
                size="sm"
                options={[
                  { value: "all", label: `全部 (${totalWords})` },
                  { value: "unmastered", label: `待复习 (${unmasteredCount})` },
                  { value: "mastered", label: `已掌握 (${masteredCount})` },
                ]}
              />

              <Button
                variant={hideListTranslation ? "primary" : "secondary"}
                size="sm"
                onClick={() => setHideListTranslation((prev) => !prev)}
                title={hideListTranslation ? "显示中文释义" : "隐藏中文释义（自测记忆）"}
              >
                {hideListTranslation ? (
                  <EyeOff className="w-3.5 h-3.5" />
                ) : (
                  <Eye className="w-3.5 h-3.5" />
                )}
                <span>{hideListTranslation ? "显示释义" : "隐藏释义"}</span>
              </Button>

              {masteredCount > 0 && (
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={handleResetAllMastery}
                  title="一键重置所有生词为待复习"
                >
                  重置掌握
                </Button>
              )}
            </div>
          </div>

          <div className="hidden print-only text-center mb-6">
            <h1 className="text-2xl font-black mb-1">Enway 英语生词重点复习表</h1>
            <p className="text-xs text-fg-muted">
              总计收录 {filteredVocab.length} 个重点考点词汇 · 打印时间：
              {new Date().toLocaleDateString()}
            </p>
          </div>

          {filteredVocab.length === 0 ? (
            <Card className="py-12 px-4 no-print">
              <EmptyState
                icon={<Bookmark className="w-8 h-8" />}
                title={searchTerm ? "未搜索到匹配生词" : "当前分类下暂无生词"}
                description="在试卷阅读材料中直接双击任意单词，即可一键加入生词本！"
              />
            </Card>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredVocab.map((item) => (
                <Card
                  key={item.word}
                  interactive
                  className="p-5 flex flex-col justify-between print-card hover:border-primary/40"
                >
                  <div>
                    <div className="flex items-start justify-between gap-2">
                      <div className="flex items-center gap-2">
                        <h3 className="text-base font-bold text-fg capitalize font-reading">
                          {item.word}
                        </h3>
                        <button
                          type="button"
                          onClick={() => playAudio(item.word)}
                          title="朗读单词"
                          aria-label={`朗读 ${item.word}`}
                          className="p-1 hover:bg-surface-2 text-fg-muted hover:text-primary rounded-lg transition-colors no-print"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>

                      <div className="flex items-center gap-1.5 no-print">
                        <button
                          type="button"
                          onClick={() => handleToggleMastery(item.word)}
                          title={
                            item.mastered ? "点击标记为需复习" : "点击标记为已掌握"
                          }
                          className={`px-2 py-0.5 rounded-lg text-[10px] font-bold border transition-colors ${
                            item.mastered
                              ? "bg-success-soft text-success border-success/30"
                              : "bg-warning-soft text-warning border-warning/30"
                          }`}
                        >
                          {item.mastered ? "已掌握" : "待复习"}
                        </button>

                        <button
                          type="button"
                          onClick={() => handleDelete(item.word)}
                          title="从生词本移除"
                          aria-label={`移除 ${item.word}`}
                          className="text-fg-subtle hover:text-danger p-1 rounded-lg transition-colors"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>

                    {item.phonetic && (
                      <span className="text-xs font-mono text-primary block mt-0.5">
                        /{item.phonetic.replace(/[/\[\]]/g, "")}/
                      </span>
                    )}

                    <p
                      className={`mt-3 text-xs text-fg font-medium bg-surface-2/80 p-2.5 rounded-xl border border-border leading-relaxed transition-all ${
                        hideListTranslation ? "blur-sm select-none print:filter-none" : ""
                      }`}
                    >
                      {item.translation}
                    </p>

                    {item.context && (
                      <div className="mt-2 text-[11px] text-fg-muted italic bg-warning-soft/50 p-2 rounded-lg border border-warning/20 font-reading">
                        &ldquo;{item.context.trim()}...&rdquo;
                      </div>
                    )}
                  </div>

                  <div className="mt-4 pt-2.5 border-t border-border flex items-center justify-between text-[10px] text-fg-subtle no-print font-mono tabular-nums">
                    <span>收录于：{new Date(item.addedAt).toLocaleDateString()}</span>
                    {item.reviewCount ? <span>已复习 {item.reviewCount} 次</span> : null}
                  </div>
                </Card>
              ))}
            </div>
          )}
        </div>
      )}

      <Modal
        open={showAddModal}
        onClose={() => setShowAddModal(false)}
        title="手动添加生词"
      >
        <form onSubmit={handleManualAdd} className="space-y-3.5">
          <div>
            <label className="block text-xs font-semibold text-fg mb-1">
              英文单词
            </label>
            <Input
              compact
              type="text"
              required
              value={newWord}
              onChange={(e) => setNewWord(e.target.value)}
              placeholder="例如: resilient"
            />
          </div>
          <div>
            <label className="block text-xs font-semibold text-fg mb-1">
              中文释义（可留空自动识别）
            </label>
            <Input
              compact
              type="text"
              value={newTranslation}
              onChange={(e) => setNewTranslation(e.target.value)}
              placeholder="例如: adj. 有弹性的；能复原的"
            />
          </div>
          <div className="flex justify-end gap-2 pt-2">
            <Button
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => setShowAddModal(false)}
            >
              取消
            </Button>
            <Button type="submit" size="sm">
              确认添加
            </Button>
          </div>
        </form>
      </Modal>
    </div>
  );
}
