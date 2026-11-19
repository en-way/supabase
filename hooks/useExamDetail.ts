import { useEffect, useRef, useState } from "react";
import { fetchExamDetailWithFallback } from "@/lib/examLoader";
import type {
  ExamDetailData,
  ExamRecord,
  PassageRecord,
  QuestionRecord,
} from "@/types/exam";

export interface UseExamDetailOptions {
  reloadKey?: string | null;
  onBeforeLoad?: () => void;
  onEmpty?: () => void;
  onLoaded?: (detail: ExamDetailData | null, examId: string) => void;
  onError?: (err: unknown) => void;
}

export interface UseExamDetailResult {
  exam: ExamRecord | null;
  passages: PassageRecord[];
  questions: QuestionRecord[];
  loading: boolean;
}

/**
 * Cancellation-safe loader for static/CDN-first exam details with Supabase fallback.
 */
export function useExamDetail(
  examId: string | null,
  options: UseExamDetailOptions = {}
): UseExamDetailResult {
  const { reloadKey } = options;
  const [exam, setExam] = useState<ExamRecord | null>(null);
  const [passages, setPassages] = useState<PassageRecord[]>([]);
  const [questions, setQuestions] = useState<QuestionRecord[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const callbacksRef = useRef(options);
  callbacksRef.current = options;

  useEffect(() => {
    let cancelled = false;
    callbacksRef.current.onBeforeLoad?.();

    async function load() {
      if (!examId) {
        setExam(null);
        setPassages([]);
        setQuestions([]);
        callbacksRef.current.onEmpty?.();
        setLoading(false);
        return;
      }

      setLoading(true);
      try {
        const detail = await fetchExamDetailWithFallback(examId);
        if (cancelled) return;

        setExam(detail?.exam || null);
        setPassages(detail?.passages || []);
        setQuestions(detail?.questions || []);
        callbacksRef.current.onLoaded?.(detail, examId);
      } catch (err: unknown) {
        if (!cancelled) {
          callbacksRef.current.onError?.(err);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    load();
    return () => {
      cancelled = true;
    };
  }, [examId, reloadKey]);

  return { exam, passages, questions, loading };
}
