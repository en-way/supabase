import type { QuestionOption } from "./exam";

export type { QuestionOption };

export interface MistakeItem {
  questionId: string;
  examId?: string;
  categoryId?: string;
  wrongAnswer: string;
  wrongCount: number;
  isMastered: boolean;
  lastWrongAt: string;
  // Optional legacy fields that may exist in older backups
  stem?: string;
  options?: QuestionOption[];
  correctAnswer?: string;
  explanation?: string;
}

export interface VocabItem {
  word: string;
  phonetic?: string;
  translation: string;
  context?: string;
  addedAt: string;
  mastered?: boolean;
  reviewCount?: number;
  lastReviewedAt?: string;
}

export interface FavoriteItem {
  questionId: string;
  examId?: string;
  stem?: string;
  options?: QuestionOption[];
  correctAnswer?: string;
  explanation?: string;
  note?: string;
  addedAt: string;
}

export interface ExamDraft {
  examId: string;
  answers: Record<string, string>;
  remainingSeconds: number;
  focusedIndex?: number;
  lastUpdated: string;
}

export interface PracticeDraft {
  examId: string;
  answers: Record<string, string>;
  currentIndex: number;
  lastUpdated: string;
  score?: number;
  correctCount?: number;
  totalQuestions?: number;
  answeredCount?: number;
}

export interface ExamResult {
  examId: string;
  examTitle: string;
  score: number;
  totalScore: number;
  isPassed: boolean;
  durationSeconds: number;
  submittedAt: string;
  answers: Record<string, { userAnswer: string; isCorrect: boolean }>;
}

export interface LocalLearningState {
  mistakes: MistakeItem[];
  vocabulary: VocabItem[];
  favorites: FavoriteItem[];
  examResults: Record<string, ExamResult>;
  examDrafts: Record<string, ExamDraft>;
  practiceDrafts?: Record<string, PracticeDraft>;
}

export interface ExamCardStats {
  hasExamRecord: boolean;
  examScore: number;
  examTotalScore: number;
  examAccuracy: number;
  examIsPassed: boolean;
  examSubmittedAt?: string;

  hasPracticeRecord: boolean;
  practiceAnsweredCount: number;
  practiceTotalQuestions: number;
  practicePercent: number;
  practiceScore: number;
  practiceCorrectCount: number;
  practiceAccuracy: number;
}

export interface SanitizedLearningBackup {
  mistakes: Array<{
    questionId: string;
    examId?: string;
    categoryId?: string;
    wrongAnswer: string;
    wrongCount: number;
    isMastered: boolean;
    lastWrongAt: string;
  }>;
  vocabulary: VocabItem[];
  favorites: Array<{
    questionId: string;
    examId: string;
    note: string;
    addedAt: string;
  }>;
  examResults: Record<string, ExamResult>;
}

export interface CloudBackupSummary {
  mistakesCount?: number;
  vocabCount?: number;
  favoritesCount?: number;
  examsCount?: number;
  storageType?: string;
  backedUpAt?: string;
  dataHash?: string;
}

export interface CloudBackupInfo {
  exists: boolean;
  summary?: CloudBackupSummary;
  updatedAt?: string;
  dataHash?: string;
  error?: string;
}

export interface CloudBackupActionResult {
  success: boolean;
  isIdentical?: boolean;
  message?: string;
  summary?: CloudBackupSummary;
  error?: string;
}

export interface ReconcileResult {
  completed: boolean;
  hasChanges: boolean;
  deletedQuestionsCount: number;
  fixedAnswersCount: number;
  deletedExamsCount: number;
  summaryText: string;
}

export type SubmissionTaskPayload =
  | { examId: string; score: number }
  | Record<string, unknown>;
