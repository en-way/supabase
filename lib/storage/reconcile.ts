import { supabase } from "../supabase";
import type { FavoriteItem, LocalLearningState, ReconcileResult } from "@/types/storage";
import { getLocalState, saveLocalState } from "./local";
import { uploadBackupToCloud } from "./cloud";

// ------------------- Reconciliation Engine (存档智能校对与更正自愈) -------------------

export async function reconcileLearningState(
  targetState?: LocalLearningState
): Promise<ReconcileResult> {
  const state = targetState || getLocalState();
  let hasChanges = false;
  let deletedQuestionsCount = 0;
  let fixedAnswersCount = 0;
  let deletedExamsCount = 0;

  try {
    // 🛡️ Gate 1: Session Guard. If unauthenticated, Supabase RLS forbids SELECT on questions/exams for anon.
    // Must NOT query Supabase to prevent empty arrays from clearing local data.
    const { data: { session } } = await supabase.auth.getSession();
    if (!session?.user) {
      return {
        completed: false,
        hasChanges: false,
        deletedQuestionsCount: 0,
        fixedAnswersCount: 0,
        deletedExamsCount: 0,
        summaryText: "未登录状态，已安全保留本地学习记录",
      };
    }

    // 1. Collect all Question IDs
    const mistakeQIds = (state.mistakes || []).map((m) => m.questionId);
    const favQIds = (state.favorites || []).map((f) => f.questionId);
    const allQIds = Array.from(new Set([...mistakeQIds, ...favQIds]));

    // 2. Collect all Exam IDs
    const draftExamIds = Object.keys(state.examDrafts || {});
    const practiceExamIds = Object.keys(state.practiceDrafts || {});
    const resultExamIds = Object.keys(state.examResults || {});
    const mistakeExamIds = (state.mistakes || []).map((m) => m.examId).filter(Boolean) as string[];
    const favoriteExamIds = (state.favorites || []).map((f) => f.examId).filter(Boolean) as string[];
    const allExamIds = Array.from(
      new Set([...draftExamIds, ...practiceExamIds, ...resultExamIds, ...mistakeExamIds, ...favoriteExamIds])
    );

    // 3. Batch query valid questions in chunks of 50 to prevent HTTP 414 URI Too Long
    const validQuestionsMap: Record<string, { id: string; correct_answer: string; exam_id: string; category_id: string }> = {};
    const CHUNK_SIZE = 50;
    if (allQIds.length > 0) {
      for (let i = 0; i < allQIds.length; i += CHUNK_SIZE) {
        const chunk = allQIds.slice(i, i + CHUNK_SIZE);
        const { data: qRows, error: qErr } = await supabase
          .from("questions")
          .select("id, correct_answer, exam_id, category_id")
          .in("id", chunk);

        // 🛡️ Critical Safety Fuse: If network or Supabase fails, abort reconcile to prevent wiping user data!
        if (qErr) {
          console.warn("[Reconcile] Supabase questions query failed, safely aborting to prevent false data wipe:", qErr);
          return {
            completed: false,
            hasChanges: false,
            deletedQuestionsCount: 0,
            fixedAnswersCount: 0,
            deletedExamsCount: 0,
            summaryText: "云端题目校验查询失败，已安全保留本地学习记录",
          };
        }

        if (qRows) {
          (qRows as Array<{ id: string; correct_answer: string; exam_id: string; category_id: string }>).forEach((q) => {
            validQuestionsMap[q.id] = q;
          });
        }
      }
    }

    // 🛡️ Gate 2: Zero-Wipe Safety Fuse. If questions were requested, but Supabase returned 0 rows,
    // this indicates an RLS failure, network disconnect, or maintenance — NOT that all questions were deleted.
    if (allQIds.length > 0 && Object.keys(validQuestionsMap).length === 0) {
      console.warn("[Reconcile] Supabase returned 0 matching questions for non-empty ID list. Safety fuse triggered: aborting reconciliation to prevent catastrophic data wipe.");
      return {
        completed: false,
        hasChanges: false,
        deletedQuestionsCount: 0,
        fixedAnswersCount: 0,
        deletedExamsCount: 0,
        summaryText: "云端校验响应异常，已触发安全熔断保护本地数据",
      };
    }

    // 4. Batch query valid approved exams in chunks of 50
    const validExamsMap: Record<string, boolean> = {};
    if (allExamIds.length > 0) {
      for (let i = 0; i < allExamIds.length; i += CHUNK_SIZE) {
        const chunk = allExamIds.slice(i, i + CHUNK_SIZE);
        const { data: eRows, error: eErr } = await supabase
          .from("exams")
          .select("id, is_published, approval_status")
          .in("id", chunk);

        // 🛡️ Critical Safety Fuse: If network or Supabase fails, abort reconcile immediately!
        if (eErr) {
          console.warn("[Reconcile] Supabase exams query failed, safely aborting to prevent false data wipe:", eErr);
          return {
            completed: false,
            hasChanges: false,
            deletedQuestionsCount: 0,
            fixedAnswersCount: 0,
            deletedExamsCount: 0,
            summaryText: "云端考卷状态查询失败，已安全保留本地进度",
          };
        }

        if (eRows) {
          (eRows as Array<{ id: string; is_published: boolean; approval_status: string }>).forEach((e) => {
            if (e.approval_status === "approved" && e.is_published === true) {
              validExamsMap[e.id] = true;
            }
          });
        }
      }
    }

    // 🛡️ Gate 3: Exam Zero-Wipe Safety Fuse. If exams were requested, but 0 valid approved exams returned,
    // abort to avoid wiping student drafts and exam results.
    if (allExamIds.length > 0 && Object.keys(validExamsMap).length === 0) {
      console.warn("[Reconcile] Supabase returned 0 valid exams for non-empty exam list. Safety fuse triggered: aborting reconciliation.");
      return {
        completed: false,
        hasChanges: false,
        deletedQuestionsCount: 0,
        fixedAnswersCount: 0,
        deletedExamsCount: 0,
        summaryText: "云端考卷状态校验异常，已安全保留本地进度",
      };
    }

    // 5. Reconcile mistakes
    if (state.mistakes && state.mistakes.length > 0) {
      const originalCount = state.mistakes.length;
      // Filter out physically deleted questions
      state.mistakes = state.mistakes.filter((m) => Boolean(validQuestionsMap[m.questionId]));
      const pruned = originalCount - state.mistakes.length;
      if (pruned > 0) {
        deletedQuestionsCount += pruned;
        hasChanges = true;
      }

      // Check if admin corrected answers
      state.mistakes.forEach((m) => {
        const q = validQuestionsMap[m.questionId];
        if (q) {
          if (q.category_id && m.categoryId !== q.category_id) {
            m.categoryId = q.category_id;
            hasChanges = true;
          }
          if (q.exam_id && m.examId !== q.exam_id) {
            m.examId = q.exam_id;
            hasChanges = true;
          }
          // Answer correction self-healing: if student's wrong answer now matches new correct answer
          if (m.wrongAnswer && m.wrongAnswer === q.correct_answer && !m.isMastered) {
            m.isMastered = true;
            fixedAnswersCount += 1;
            hasChanges = true;
          }
        }
      });
    }

    // 6. Reconcile favorites
    if (state.favorites && state.favorites.length > 0) {
      const originalFavCount = state.favorites.length;
      state.favorites = state.favorites.filter((f) => Boolean(validQuestionsMap[f.questionId]));
      const prunedFav = originalFavCount - state.favorites.length;
      if (prunedFav > 0) {
        deletedQuestionsCount += prunedFav;
        hasChanges = true;
      }
    }

    // 7. Reconcile exam drafts (remove drafts of deleted or unapproved exams)
    if (state.examDrafts) {
      const drafts = state.examDrafts;
      Object.keys(drafts).forEach((examId) => {
        if (!validExamsMap[examId]) {
          delete drafts[examId];
          deletedExamsCount += 1;
          hasChanges = true;
        }
      });
    }

    // 7b. Reconcile practice drafts (remove practice drafts of deleted or unapproved exams)
    if (state.practiceDrafts) {
      const pDrafts = state.practiceDrafts;
      Object.keys(pDrafts).forEach((examId) => {
        if (!validExamsMap[examId]) {
          delete pDrafts[examId];
          deletedExamsCount += 1;
          hasChanges = true;
        }
      });
    }

    // 8. Reconcile exam results
    if (state.examResults) {
      const results = state.examResults;
      Object.keys(results).forEach((examId) => {
        if (!validExamsMap[examId]) {
          delete results[examId];
          deletedExamsCount += 1;
          hasChanges = true;
        }
      });
    }

    // 8. Reconcile favorites (strip legacy bulky fields to free LocalStorage quota)
    if (Array.isArray(state.favorites)) {
      state.favorites = state.favorites.map((f: FavoriteItem) => {
        if (f && (f.stem || f.options || f.explanation || f.correctAnswer)) {
          hasChanges = true;
          return {
            questionId: f.questionId,
            examId: f.examId || "",
            note: f.note || "",
            addedAt: f.addedAt || new Date().toISOString(),
          };
        }
        return f;
      });
    }

    // 9. If modified, persist to local storage and throttle silent cloud writeback (max once per hour)
    if (hasChanges) {
      saveLocalState(state);
      try {
        const now = Date.now();
        let lastSilentTs = 0;
        if (typeof window !== "undefined") {
          lastSilentTs = Number(sessionStorage.getItem("enway_last_silent_backup") || "0");
        }
        // At most once every 60 minutes per session to strictly preserve Supabase storage and DB quotas
        if (now - lastSilentTs > 60 * 60 * 1000) {
          const uploadRes = await uploadBackupToCloud();
          if (uploadRes.success && typeof window !== "undefined") {
            sessionStorage.setItem("enway_last_silent_backup", String(now));
          }
        }
      } catch (err) {
        console.warn("Silent cloud writeback failed during reconcile:", err);
      }
    }
  } catch (err) {
    console.error("Reconciliation error:", err);
    return {
      completed: false,
      hasChanges: false,
      deletedQuestionsCount: 0,
      fixedAnswersCount: 0,
      deletedExamsCount: 0,
      summaryText: "校对过程出现异常，已安全保留本地学习记录",
    };
  }

  const parts: string[] = [];
  if (deletedQuestionsCount > 0) parts.push(`清理了 ${deletedQuestionsCount} 道已下线题目`);
  if (fixedAnswersCount > 0) parts.push(`更正了 ${fixedAnswersCount} 道已修正答案错题`);
  if (deletedExamsCount > 0) parts.push(`清除了 ${deletedExamsCount} 份已下线试卷`);
  const summaryText = parts.length > 0 ? `已为您自动校对并更新存档：${parts.join("，")}` : "";

  return {
    completed: true,
    hasChanges,
    deletedQuestionsCount,
    fixedAnswersCount,
    deletedExamsCount,
    summaryText,
  };
}
