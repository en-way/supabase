import type { ExamCardStats, LocalLearningState } from "@/types/storage";

// ------------------- Exam Card Summary Statistics -------------------
export function getExamCardStats(
  examId: string,
  examTotalScore: number,
  examQuestionCount: number,
  localState: LocalLearningState | null
): ExamCardStats {
  const result = localState?.examResults?.[examId];
  const practice = localState?.practiceDrafts?.[examId];

  let hasExamRecord = false;
  let examScore = 0;
  let examAccuracy = 0;
  let examIsPassed = false;
  let examSubmittedAt: string | undefined = undefined;

  if (result) {
    hasExamRecord = true;
    examScore = result.score || 0;
    examIsPassed = !!result.isPassed;
    const answeredTotal = Object.keys(result.answers || {}).length;
    let correctCount = 0;
    Object.values(result.answers || {}).forEach((a) => {
      if (a && a.isCorrect) correctCount++;
    });
    examAccuracy = answeredTotal > 0 ? Math.round((correctCount / answeredTotal) * 100) : 0;
    examSubmittedAt = result.submittedAt;
  }

  let hasPracticeRecord = false;
  let practiceAnsweredCount = 0;
  const defaultTotalQ = examQuestionCount > 0 ? examQuestionCount : 45;
  let practiceTotalQuestions = defaultTotalQ;
  let practicePercent = 0;
  let practiceScore = 0;
  let practiceCorrectCount = 0;
  let practiceAccuracy = 0;

  if (practice && practice.answers && Object.keys(practice.answers).length > 0) {
    hasPracticeRecord = true;
    practiceAnsweredCount = practice.answeredCount ?? Object.keys(practice.answers).length;
    practiceTotalQuestions = practice.totalQuestions || defaultTotalQ;
    practicePercent = Math.min(100, Math.round((practiceAnsweredCount / practiceTotalQuestions) * 100));
    practiceScore = practice.score ?? 0;
    practiceCorrectCount = practice.correctCount ?? 0;
    practiceAccuracy = practiceAnsweredCount > 0 ? Math.round((practiceCorrectCount / practiceAnsweredCount) * 100) : 0;
  }

  return {
    hasExamRecord,
    examScore,
    examTotalScore: examTotalScore || (result ? result.totalScore : 60),
    examAccuracy,
    examIsPassed,
    examSubmittedAt,
    hasPracticeRecord,
    practiceAnsweredCount,
    practiceTotalQuestions,
    practicePercent,
    practiceScore,
    practiceCorrectCount,
    practiceAccuracy,
  };
}
