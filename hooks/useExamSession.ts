"use client";

import { useEffect, useRef, useState } from "react";
import {
  clearExamDraft,
  clearExamResult,
  getExamDraft,
  getExamResult,
  normalizeOptions,
  recordMistake,
  saveExamDraft,
  saveExamResult,
  type ExamResult,
} from "@/lib/storage";
import { enqueueSubmissionTask } from "@/lib/submissionQueue";
import { useExamDetail } from "@/hooks/useExamDetail";
import { useBodyScrollLock } from "@/hooks/useBodyScrollLock";
import { useKeyboardGuard } from "@/hooks/useKeyboardGuard";
import { triggerHaptic } from "@/hooks/useReaderPrefs";

export function formatExamTimer(seconds: number): string {
  const safe = Math.max(0, seconds);
  const m = Math.floor(safe / 60);
  const s = safe % 60;
  return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
}

export function useExamSession(examId: string | null, modeParam: string | null) {
  const isPrintMode = modeParam === "print";

  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [remainingSeconds, setRemainingSeconds] = useState<number>(3600);
  const [isTimeUp, setIsTimeUp] = useState<boolean>(false);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);
  const [reportOnlyMode, setReportOnlyMode] = useState<boolean>(false);
  const [result, setResult] = useState<ExamResult | null>(null);
  const [activePassageId, setActivePassageId] = useState<string>("");
  const [showPrintAnswers, setShowPrintAnswers] = useState<boolean>(false);
  const [focusedIndex, setFocusedIndex] = useState<number>(0);

  const [mobileTab, setMobileTab] = useState<"questions" | "passage">("questions");
  const [showMobileAnswerSheet, setShowMobileAnswerSheet] = useState<boolean>(false);
  const [showSubmitReviewSheet, setShowSubmitReviewSheet] = useState<boolean>(false);
  const [isZenMode, setIsZenMode] = useState<boolean>(false);
  const [showShortcutsModal, setShowShortcutsModal] = useState<boolean>(false);

  const hasAutoPrintedRef = useRef<string | null>(null);
  const questionRefs = useRef<Record<string, HTMLDivElement | null>>({});
  const passageContainerRef = useRef<HTMLDivElement | null>(null);
  const isSubmittingRef = useRef(false);
  const autoSubmitTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    document.body.classList.toggle("enway-zen-mode", isZenMode);
    return () => {
      document.body.classList.remove("enway-zen-mode");
    };
  }, [isZenMode]);

  const { exam, passages, questions, loading } = useExamDetail(examId, {
    reloadKey: modeParam,
    onBeforeLoad: () => {
      isSubmittingRef.current = false;
      if (autoSubmitTimerRef.current) {
        clearTimeout(autoSubmitTimerRef.current);
        autoSubmitTimerRef.current = null;
      }
      questionRefs.current = {};
      setFocusedIndex(0);
      setIsTimeUp(false);
      setReportOnlyMode(false);
      setShowMobileAnswerSheet(false);
      setShowSubmitReviewSheet(false);
      setMobileTab("questions");
    },
    onEmpty: () => {
      setActivePassageId("");
      setAnswers({});
      setResult(null);
      setIsSubmitted(false);
      setReportOnlyMode(false);
      setIsTimeUp(false);
    },
    onLoaded: (detail, loadedExamId) => {
      const examData = detail?.exam || null;
      const passageData = detail?.passages || [];
      const questionData = detail?.questions || [];

      setActivePassageId(passageData.length > 0 ? passageData[0].id : "");

      const isRetake = modeParam === "retake";
      const isPrint = modeParam === "print";
      const draft = getExamDraft(loadedExamId);
      const pastResult = getExamResult(loadedExamId);
      const defaultDuration = (examData?.duration_minutes || 75) * 60;

      if (isPrint) {
        setAnswers({});
        setIsSubmitted(false);
        setIsTimeUp(false);
        setResult(null);
        setFocusedIndex(0);
        setRemainingSeconds(defaultDuration);
      } else if (draft && !isRetake) {
        setAnswers(draft.answers || {});
        const restoredSec =
          typeof draft.remainingSeconds === "number"
            ? draft.remainingSeconds
            : defaultDuration;
        setRemainingSeconds(restoredSec);
        setIsTimeUp(restoredSec <= 0);
        if (
          typeof draft.focusedIndex === "number" &&
          draft.focusedIndex >= 0 &&
          draft.focusedIndex < questionData.length
        ) {
          setFocusedIndex(draft.focusedIndex);
        } else {
          setFocusedIndex(0);
        }
        setIsSubmitted(false);
        setResult(null);
      } else if (pastResult && !isRetake) {
        const restoredAnswers: Record<string, string> = {};
        if (pastResult.answers) {
          Object.entries(pastResult.answers).forEach(([qId, val]) => {
            if (val && typeof val.userAnswer === "string") {
              restoredAnswers[qId] = val.userAnswer;
            }
          });
        }
        setAnswers(restoredAnswers);
        setResult(pastResult);
        setIsSubmitted(true);
        setReportOnlyMode(false);
        setIsTimeUp(false);
        setRemainingSeconds(0);
      } else {
        setAnswers({});
        setIsSubmitted(false);
        setReportOnlyMode(false);
        setIsTimeUp(false);
        setResult(null);
        setFocusedIndex(0);
        setRemainingSeconds(defaultDuration);
      }
    },
    onError: (err) => {
      console.error("Failed to load exam data:", err);
    },
  });

  const latestRef = useRef({
    exam,
    questions,
    answers,
    remainingSeconds,
    focusedIndex,
    isSubmitted,
    isTimeUp,
  });
  latestRef.current = {
    exam,
    questions,
    answers,
    remainingSeconds,
    focusedIndex,
    isSubmitted,
    isTimeUp,
  };

  const executeSubmit = (_auto = false) => {
    if (isSubmittingRef.current) return;
    const {
      exam: curExam,
      questions: curQuestions,
      answers: curAnswers,
      remainingSeconds: curSec,
    } = latestRef.current;
    if (!curExam) return;

    isSubmittingRef.current = true;
    setShowSubmitReviewSheet(false);
    setShowMobileAnswerSheet(false);

    if (autoSubmitTimerRef.current) {
      clearTimeout(autoSubmitTimerRef.current);
      autoSubmitTimerRef.current = null;
    }

    let earnedRawPoints = 0;
    let totalRawPoints = 0;
    const detailAnswers: Record<string, { userAnswer: string; isCorrect: boolean }> = {};

    curQuestions.forEach((q) => {
      const uAns = curAnswers[q.id] || "";
      const isCorr = uAns === q.correct_answer;
      const qPts =
        q.points !== undefined && q.points !== null ? Number(q.points) : 2.0;
      totalRawPoints += qPts;
      if (isCorr) {
        earnedRawPoints += qPts;
      } else {
        recordMistake({
          questionId: q.id,
          examId: curExam.id,
          categoryId: curExam.category_id,
          wrongAnswer: uAns || "未作答",
        });
      }

      detailAnswers[q.id] = {
        userAnswer: uAns,
        isCorrect: isCorr,
      };
    });

    const examTotal = Number(
      totalRawPoints > 0 ? totalRawPoints : curExam.total_score || 60
    );
    const passLine = Number(
      curExam.pass_score && curExam.total_score === examTotal
        ? curExam.pass_score
        : Math.round(examTotal * 0.6)
    );
    const finalScore = Math.round(earnedRawPoints * 10) / 10;
    const passed = finalScore >= passLine;

    const examDuration = Number(curExam?.duration_minutes || 60);
    const examRes: ExamResult = {
      examId: curExam.id,
      examTitle: curExam.title,
      score: finalScore,
      totalScore: examTotal,
      isPassed: passed,
      durationSeconds: Math.max(0, examDuration * 60 - curSec),
      submittedAt: new Date().toISOString(),
      answers: detailAnswers,
    };

    saveExamResult(examRes);
    enqueueSubmissionTask("exam_result", { examId: curExam.id, score: finalScore });
    clearExamDraft(curExam.id);
    setResult(examRes);
    setIsSubmitted(true);
    setReportOnlyMode(true);
    setIsZenMode(false);
    setIsTimeUp(false);

    if (passed) {
      import("canvas-confetti")
        .then((mod) => {
          mod.default({
            particleCount: 80,
            spread: 70,
            origin: { y: 0.6 },
          });
        })
        .catch((err) => {
          console.warn("Confetti effect skipped:", err);
        });
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  // 1. Countdown timer with 0–12s Uniform Jitter + immediate Time-Up lock state
  useEffect(() => {
    if (loading || isSubmitted || isPrintMode) return;

    const triggerTimeUpAutoSubmit = () => {
      latestRef.current.remainingSeconds = 0;
      latestRef.current.isTimeUp = true;
      setRemainingSeconds(0);
      setIsTimeUp(true);
      setShowMobileAnswerSheet(false);
      setShowSubmitReviewSheet(false);
      if (!isSubmittingRef.current && !autoSubmitTimerRef.current) {
        const jitterMs = Math.floor(Math.random() * 12000);
        autoSubmitTimerRef.current = setTimeout(() => {
          autoSubmitTimerRef.current = null;
          executeSubmit(true);
        }, jitterMs);
      }
    };

    if (latestRef.current.remainingSeconds <= 0) {
      triggerTimeUpAutoSubmit();
      return () => {
        if (autoSubmitTimerRef.current) {
          clearTimeout(autoSubmitTimerRef.current);
          autoSubmitTimerRef.current = null;
        }
      };
    }

    const timer = setInterval(() => {
      const cur = latestRef.current.remainingSeconds;
      if (cur <= 1) {
        clearInterval(timer);
        triggerTimeUpAutoSubmit();
        return;
      }
      const nextSec = cur - 1;
      latestRef.current.remainingSeconds = nextSec;
      setRemainingSeconds(nextSec);
    }, 1000);

    return () => {
      clearInterval(timer);
      if (autoSubmitTimerRef.current) {
        clearTimeout(autoSubmitTimerRef.current);
        autoSubmitTimerRef.current = null;
      }
    };
  }, [loading, isSubmitted, isPrintMode]);

  // 2. Periodic 5s draft sync
  useEffect(() => {
    if (!examId || isSubmitted || loading || isPrintMode) return;
    const draftInterval = setInterval(() => {
      const { answers: curAns, remainingSeconds: curSec, focusedIndex: curIdx } =
        latestRef.current;
      if (examId && Object.keys(curAns).length > 0) {
        saveExamDraft(examId, curAns, curSec, curIdx);
      }
    }, 5000);
    return () => clearInterval(draftInterval);
  }, [examId, isSubmitted, loading, isPrintMode]);

  // 3. BeforeUnload Exit Protection
  useEffect(() => {
    if (!examId || isSubmitted || loading || isPrintMode) return;
    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      const { answers: curAns, remainingSeconds: curSec, focusedIndex: curIdx } =
        latestRef.current;
      if (examId) {
        saveExamDraft(examId, curAns, curSec, curIdx);
      }
      if (Object.keys(curAns).length > 0) {
        e.preventDefault();
        e.returnValue = "";
      }
    };
    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [examId, isSubmitted, loading, isPrintMode]);

  // Trigger print dialog once automatically when opening ?mode=print
  useEffect(() => {
    if (!isPrintMode || loading || !exam) return;
    if (hasAutoPrintedRef.current === exam.id) return;
    hasAutoPrintedRef.current = exam.id;
    const timer = setTimeout(() => {
      window.print();
    }, 400);
    return () => clearTimeout(timer);
  }, [isPrintMode, loading, exam]);

  const scrollToQuestion = (qId?: string) => {
    if (!qId) return;
    const el = questionRefs.current[qId];
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  const handleSelectAnswer = (qId: string, optionKey: string) => {
    if (latestRef.current.isSubmitted || isPrintMode || latestRef.current.isTimeUp) {
      return;
    }
    triggerHaptic(10);
    const {
      answers: curAnswers,
      remainingSeconds: curSec,
      focusedIndex: curIdx,
    } = latestRef.current;
    const next = {
      ...curAnswers,
      [qId]: optionKey,
    };
    latestRef.current.answers = next;
    setAnswers(next);
    if (examId) {
      saveExamDraft(examId, next, curSec, curIdx);
    }
  };

  // 4. Keyboard shortcuts (guarded against inputs, IME, and Time-Up lock)
  const keydownRef = useRef({
    questions,
    focusedIndex,
    isOverlayOpen:
      showMobileAnswerSheet ||
      showSubmitReviewSheet ||
      showShortcutsModal ||
      reportOnlyMode,
  });
  keydownRef.current = {
    questions,
    focusedIndex,
    isOverlayOpen:
      showMobileAnswerSheet ||
      showSubmitReviewSheet ||
      showShortcutsModal ||
      reportOnlyMode,
  };

  useKeyboardGuard((e: KeyboardEvent) => {
    const { questions: qs, focusedIndex: fIdx, isOverlayOpen } = keydownRef.current;
    if (!qs || qs.length === 0) return;

    const key = e.key.toUpperCase();
    const currentQ = qs[fIdx];
    const validKeys = currentQ
      ? normalizeOptions(currentQ.options).map((o) => o.key.toUpperCase())
      : ["A", "B", "C", "D"];

    if (e.key === "Escape") {
      setShowShortcutsModal(false);
      setShowMobileAnswerSheet(false);
      setShowSubmitReviewSheet(false);
      setIsZenMode(false);
      return;
    }

    if (e.key === "?" || key === "H") {
      e.preventDefault();
      setShowShortcutsModal((prev) => !prev);
      return;
    }

    if (key === "Z" && !isOverlayOpen) {
      e.preventDefault();
      setIsZenMode((prev) => !prev);
      return;
    }

    if (key === "M" || e.key === "Tab") {
      e.preventDefault();
      if (!latestRef.current.isTimeUp) {
        setShowMobileAnswerSheet((prev) => !prev);
      }
      return;
    }

    if (isOverlayOpen) return;

    const isNextKey =
      e.key === "ArrowRight" || e.code === "ArrowRight" || e.key === "Right" || key === "K";
    const isPrevKey =
      e.key === "ArrowLeft" || e.code === "ArrowLeft" || e.key === "Left" || key === "J";
    const isScrollUpKey = e.key === "ArrowUp" || e.code === "ArrowUp";
    const isScrollDownKey = e.key === "ArrowDown" || e.code === "ArrowDown";

    if (validKeys.includes(key)) {
      e.preventDefault();
      if (
        !latestRef.current.isSubmitted &&
        !isPrintMode &&
        !latestRef.current.isTimeUp &&
        currentQ
      ) {
        handleSelectAnswer(currentQ.id, key);
      }
    } else if (isNextKey) {
      e.preventDefault();
      const nextIdx = Math.min(qs.length - 1, fIdx + 1);
      keydownRef.current.focusedIndex = nextIdx;
      latestRef.current.focusedIndex = nextIdx;
      setFocusedIndex(nextIdx);
      scrollToQuestion(qs[nextIdx]?.id);
    } else if (isPrevKey) {
      e.preventDefault();
      const prevIdx = Math.max(0, fIdx - 1);
      keydownRef.current.focusedIndex = prevIdx;
      latestRef.current.focusedIndex = prevIdx;
      setFocusedIndex(prevIdx);
      scrollToQuestion(qs[prevIdx]?.id);
    } else if (isScrollUpKey) {
      e.preventDefault();
      passageContainerRef.current?.scrollBy({ top: -140, behavior: "smooth" });
    } else if (isScrollDownKey) {
      e.preventDefault();
      passageContainerRef.current?.scrollBy({ top: 140, behavior: "smooth" });
    }
  }, !loading);

  // Two-way auto-synchronization: switch left reading canvas when question changes
  useEffect(() => {
    if (questions.length === 0 || passages.length === 0) return;
    const currentQ = questions[focusedIndex];
    if (currentQ?.passage_id && currentQ.passage_id !== activePassageId) {
      setActivePassageId(currentQ.passage_id);
    }
    const curP = passages.find(
      (p) => p.id === (currentQ?.passage_id || activePassageId)
    );
    const isCloze =
      curP &&
      (curP.title.includes("Use of English") ||
        curP.title.includes("完型") ||
        curP.content.includes("[1]"));
    if (isCloze && focusedIndex < 20) {
      const timer = setTimeout(() => {
        const blankEl = document.getElementById(`cloze-blank-${focusedIndex + 1}`);
        if (blankEl) {
          blankEl.scrollIntoView({ behavior: "smooth", block: "center" });
        }
      }, 50);
      return () => clearTimeout(timer);
    }
  }, [focusedIndex, questions, passages, activePassageId]);

  useBodyScrollLock(showMobileAnswerSheet || showSubmitReviewSheet || showShortcutsModal);

  const handleBlankClick = (blankNum: number) => {
    const qIdx = blankNum - 1;
    if (qIdx >= 0 && qIdx < questions.length) {
      setFocusedIndex(qIdx);
      scrollToQuestion(questions[qIdx]?.id);
      if (mobileTab === "passage") {
        setMobileTab("questions");
      }
    }
  };

  const requestSubmit = () => {
    if (isSubmittingRef.current || isSubmitted) return;
    setShowSubmitReviewSheet(true);
  };

  const handleSubmit = (auto = false) => {
    if (auto) {
      executeSubmit(true);
    } else {
      requestSubmit();
    }
  };

  const handleRetake = () => {
    if (
      window.confirm(
        "重新测验将清空本次作答记录与成绩，重新进入考场计时。确定重做吗？"
      )
    ) {
      if (examId) {
        clearExamDraft(examId);
        clearExamResult(examId);
      }
      setAnswers({});
      setIsSubmitted(false);
      setReportOnlyMode(false);
      setIsTimeUp(false);
      setResult(null);
      setRemainingSeconds((exam?.duration_minutes || 60) * 60);
      setFocusedIndex(0);
      isSubmittingRef.current = false;
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  const scrollToFirstUnanswered = () => {
    const targetQ = questions.find((q) => !answers[q.id]);
    if (targetQ) {
      const targetIdx = questions.findIndex((q) => q.id === targetQ.id);
      if (targetIdx >= 0) setFocusedIndex(targetIdx);
      scrollToQuestion(targetQ.id);
      setShowMobileAnswerSheet(false);
    }
  };

  const jumpToQuestionIndex = (idx: number, closeDrawer = false) => {
    const targetQ = questions[idx];
    if (!targetQ) return;
    setReportOnlyMode(false);
    setFocusedIndex(idx);
    if (closeDrawer) {
      setMobileTab("questions");
      setShowMobileAnswerSheet(false);
      setTimeout(() => scrollToQuestion(targetQ.id), 50);
    } else {
      scrollToQuestion(targetQ.id);
    }
  };

  return {
    exam,
    passages,
    questions,
    loading,
    isPrintMode,
    answers,
    remainingSeconds,
    isTimeUp,
    isSubmitted,
    reportOnlyMode,
    setReportOnlyMode,
    result,
    activePassageId,
    setActivePassageId,
    showPrintAnswers,
    setShowPrintAnswers,
    focusedIndex,
    setFocusedIndex,
    mobileTab,
    setMobileTab,
    showMobileAnswerSheet,
    setShowMobileAnswerSheet,
    showSubmitReviewSheet,
    setShowSubmitReviewSheet,
    isZenMode,
    setIsZenMode,
    showShortcutsModal,
    setShowShortcutsModal,
    questionRefs,
    passageContainerRef,
    handleSelectAnswer,
    handleSubmit,
    executeSubmit,
    handleRetake,
    handleBlankClick,
    scrollToFirstUnanswered,
    jumpToQuestionIndex,
    scrollToQuestion,
  };
}
