"use client";

import type React from "react";
import { useEffect, useRef, useState } from "react";
import {
  clearPracticeDraft,
  getLocalState,
  getPracticeDraft,
  normalizeOptions,
  recordMistake,
  savePracticeDraft,
  toggleFavorite,
  updateFavoriteNote,
} from "@/lib/storage";
import { useExamDetail } from "@/hooks/useExamDetail";
import { useBodyScrollLock } from "@/hooks/useBodyScrollLock";
import { useKeyboardGuard } from "@/hooks/useKeyboardGuard";
import { triggerHaptic } from "@/hooks/useReaderPrefs";

export function usePracticeSession(examId: string | null) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [showExplanation, setShowExplanation] = useState<Record<string, boolean>>({});
  const [favoriteIds, setFavoriteIds] = useState<Set<string>>(new Set());
  const [editingNotes, setEditingNotes] = useState<Record<string, string>>({});

  const [practiceMobileTab, setPracticeMobileTab] = useState<"question" | "passage">(
    "question"
  );
  const [showAnswerSheet, setShowAnswerSheet] = useState(false);
  const [showPassageSheet, setShowPassageSheet] = useState(false);
  const [isZenMode, setIsZenMode] = useState(false);
  const [showShortcutsModal, setShowShortcutsModal] = useState(false);

  const passageContainerRef = useRef<HTMLDivElement | null>(null);
  const touchStartRef = useRef<{ x: number; y: number } | null>(null);

  const { exam, passages, questions, loading } = useExamDetail(examId, {
    onBeforeLoad: () => {
      setShowAnswerSheet(false);
      setShowPassageSheet(false);
    },
    onEmpty: () => {
      setUserAnswers({});
      setShowExplanation({});
      setCurrentIndex(0);
    },
    onLoaded: (detail, loadedExamId) => {
      const loadedQuestions = detail?.questions || [];
      const state = getLocalState();
      const favs = Array.isArray(state?.favorites) ? state.favorites : [];
      setFavoriteIds(new Set(favs.map((f) => f?.questionId).filter(Boolean)));
      const notesMap: Record<string, string> = {};
      favs.forEach((f) => {
        if (f && f.questionId && f.note) notesMap[f.questionId] = f.note;
      });
      setEditingNotes(notesMap);

      const draft = getPracticeDraft(loadedExamId);
      if (draft) {
        setUserAnswers(draft.answers || {});
        if (
          typeof draft.currentIndex === "number" &&
          draft.currentIndex >= 0 &&
          draft.currentIndex < loadedQuestions.length
        ) {
          setCurrentIndex(draft.currentIndex);
        } else {
          setCurrentIndex(0);
        }
        const expMap: Record<string, boolean> = {};
        Object.keys(draft.answers || {}).forEach((qId) => {
          expMap[qId] = true;
        });
        setShowExplanation(expMap);
      } else {
        setUserAnswers({});
        setShowExplanation({});
        setCurrentIndex(0);
      }
    },
    onError: (err) => {
      console.error("Failed to load practice data:", err);
    },
  });

  const activePassageId =
    questions[currentIndex]?.passage_id || passages[0]?.id || "";

  const practiceStateRef = useRef({
    currentIndex,
    questions,
    userAnswers,
    examId,
    exam,
    editingNotes,
  });
  practiceStateRef.current = {
    currentIndex,
    questions,
    userAnswers,
    examId,
    exam,
    editingNotes,
  };

  useEffect(() => {
    document.body.classList.toggle("enway-zen-mode", isZenMode);
    return () => {
      document.body.classList.remove("enway-zen-mode");
    };
  }, [isZenMode]);

  const persistDraft = (answers: Record<string, string>, targetIdx: number) => {
    const { examId: curExamId, questions: qs } = practiceStateRef.current;
    if (!curExamId) return;
    let aCount = 0;
    let cCount = 0;
    let score = 0;
    qs.forEach((q) => {
      const ans = answers[q.id];
      if (ans) {
        aCount++;
        if (ans === q.correct_answer) {
          cCount++;
          const qPts =
            q.points !== undefined && q.points !== null ? Number(q.points) : 2.0;
          score += qPts;
        }
      }
    });
    score = Math.round(score * 10) / 10;
    savePracticeDraft(curExamId, answers, targetIdx, {
      score,
      correctCount: cCount,
      totalQuestions: qs.length,
      answeredCount: aCount,
    });
  };

  const navigateTo = (newIdx: number) => {
    const {
      questions: qs,
      currentIndex: cIdx,
      userAnswers: uAns,
    } = practiceStateRef.current;
    if (qs.length === 0) return;
    const safeIdx = Math.max(0, Math.min(qs.length - 1, newIdx));
    if (safeIdx !== cIdx) {
      triggerHaptic(8);
    }
    practiceStateRef.current.currentIndex = safeIdx;
    setCurrentIndex(safeIdx);
    persistDraft(uAns, safeIdx);

    if (passageContainerRef.current) {
      passageContainerRef.current.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  const handleTouchStart = (e: React.TouchEvent) => {
    if (e.touches.length === 1) {
      const clientX = e.touches[0].clientX;
      if (
        typeof window !== "undefined" &&
        (clientX < 25 || clientX > window.innerWidth - 25)
      ) {
        touchStartRef.current = null;
        return;
      }
      touchStartRef.current = { x: clientX, y: e.touches[0].clientY };
    }
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (!touchStartRef.current) return;
    const deltaX = e.changedTouches[0].clientX - touchStartRef.current.x;
    const deltaY = e.changedTouches[0].clientY - touchStartRef.current.y;
    touchStartRef.current = null;

    if (showAnswerSheet || showPassageSheet || showShortcutsModal) return;
    if (typeof window !== "undefined" && window.getSelection()?.toString().trim())
      return;

    if (Math.abs(deltaX) > 48 && Math.abs(deltaX) > Math.abs(deltaY) * 1.8) {
      if (deltaX < 0) {
        if (currentIndex < questions.length - 1) navigateTo(currentIndex + 1);
      } else {
        if (currentIndex > 0) navigateTo(currentIndex - 1);
      }
    }
  };

  useBodyScrollLock(showAnswerSheet || showPassageSheet || showShortcutsModal);

  const handleSelectOption = (key: string, targetIndex?: number) => {
    const {
      currentIndex: curIdx,
      questions: qs,
      userAnswers: uAns,
      examId: eId,
      exam: curExam,
    } = practiceStateRef.current;
    const idx = typeof targetIndex === "number" ? targetIndex : curIdx;
    const q = qs[idx] || qs[0];
    if (!q || uAns[q.id]) return;

    const nextAnswers = { ...uAns, [q.id]: key };
    practiceStateRef.current.userAnswers = nextAnswers;
    setUserAnswers(nextAnswers);
    setShowExplanation((prev) => ({ ...prev, [q.id]: true }));

    const isCorrect = key === q.correct_answer;
    triggerHaptic(isCorrect ? [10, 25, 10] : 18);

    if (eId) {
      persistDraft(nextAnswers, idx);
    }

    if (key !== q.correct_answer) {
      recordMistake({
        questionId: q.id,
        examId: curExam?.id,
        categoryId: curExam?.category_id,
        wrongAnswer: key,
      });
    }
  };

  const handleToggleFav = () => {
    const {
      questions: qs,
      currentIndex: cIdx,
      exam: curExam,
      editingNotes: notes,
    } = practiceStateRef.current;
    const q = qs[cIdx] || qs[0];
    if (!q) return;
    toggleFavorite({
      questionId: q.id,
      examId: curExam?.id || "",
      stem: q.stem,
      options: normalizeOptions(q.options),
      correctAnswer: q.correct_answer,
      explanation: q.explanation ?? undefined,
      note: notes[q.id] || "",
    });

    setFavoriteIds((prev) => {
      const next = new Set(prev);
      if (next.has(q.id)) next.delete(q.id);
      else next.add(q.id);
      return next;
    });
  };

  const handleSaveNote = (noteText: string) => {
    const q = questions[currentIndex] || questions[0];
    if (!q) return;
    setEditingNotes((prev) => ({ ...prev, [q.id]: noteText }));
    updateFavoriteNote(q.id, noteText);
  };

  const handleJumpToQuestion = (targetIdx: number) => {
    navigateTo(targetIdx);
    setShowAnswerSheet(false);
    setPracticeMobileTab("question");
  };

  const handleJumpToFirstUnanswered = () => {
    const firstUnansweredIdx = questions.findIndex((q) => !userAnswers[q.id]);
    if (firstUnansweredIdx >= 0) {
      handleJumpToQuestion(firstUnansweredIdx);
    } else {
      setShowAnswerSheet(false);
    }
  };

  const handleResetPractice = () => {
    if (
      !window.confirm(
        "确定要重新开始本卷练习吗？当前已作答的选项与解析进度将被重置。"
      )
    ) {
      return;
    }
    if (examId) {
      clearPracticeDraft(examId);
    }
    practiceStateRef.current.userAnswers = {};
    practiceStateRef.current.currentIndex = 0;
    setUserAnswers({});
    setShowExplanation({});
    setCurrentIndex(0);
  };

  useEffect(() => {
    if (!examId || loading) return;
    const handleBeforeUnload = () => {
      const { userAnswers: uAns, currentIndex: cIdx } = practiceStateRef.current;
      if (Object.keys(uAns).length > 0) {
        persistDraft(uAns, cIdx);
      }
    };
    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [examId, loading, questions]);

  useKeyboardGuard((e: KeyboardEvent) => {
    const { currentIndex: cIdx, questions: qs } = practiceStateRef.current;
    const targetQ = qs[cIdx];
    const validKeys = targetQ
      ? normalizeOptions(targetQ.options).map((o) => o.key.toUpperCase())
      : ["A", "B", "C", "D"];
    const key = e.key.toUpperCase();

    if (e.key === "Escape") {
      setShowShortcutsModal(false);
      setShowAnswerSheet(false);
      setShowPassageSheet(false);
      setIsZenMode(false);
      return;
    }

    if (e.key === "?" || key === "H") {
      e.preventDefault();
      setShowShortcutsModal((prev) => !prev);
      return;
    }

    if (key === "Z") {
      e.preventDefault();
      setIsZenMode((prev) => !prev);
      return;
    }

    if (key === "M" || e.key === "Tab") {
      e.preventDefault();
      setShowAnswerSheet((prev) => !prev);
      return;
    }

    if (validKeys.includes(key)) {
      e.preventDefault();
      handleSelectOption(key, cIdx);
    } else if (key === "F") {
      e.preventDefault();
      handleToggleFav();
    } else if (e.key === "ArrowLeft" || key === "J") {
      e.preventDefault();
      navigateTo(cIdx - 1);
    } else if (e.key === "ArrowRight" || key === "K") {
      e.preventDefault();
      navigateTo(cIdx + 1);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      passageContainerRef.current?.scrollBy({ top: -140, behavior: "smooth" });
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      passageContainerRef.current?.scrollBy({ top: 140, behavior: "smooth" });
    }
  }, !loading && questions.length > 0);

  return {
    exam,
    passages,
    questions,
    loading,
    currentIndex,
    userAnswers,
    showExplanation,
    favoriteIds,
    editingNotes,
    activePassageId,
    practiceMobileTab,
    setPracticeMobileTab,
    showAnswerSheet,
    setShowAnswerSheet,
    showPassageSheet,
    setShowPassageSheet,
    isZenMode,
    setIsZenMode,
    showShortcutsModal,
    setShowShortcutsModal,
    passageContainerRef,
    handleTouchStart,
    handleTouchEnd,
    navigateTo,
    handleJumpToQuestion,
    handleJumpToFirstUnanswered,
    handleResetPractice,
    handleSelectOption,
    handleToggleFav,
    handleSaveNote,
  };
}
