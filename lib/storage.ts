// Backward-compatible barrel entry for client learning storage modules

export type {
  QuestionOption,
  MistakeItem,
  VocabItem,
  FavoriteItem,
  ExamDraft,
  PracticeDraft,
  ExamResult,
  LocalLearningState,
  ExamCardStats,
  SanitizedLearningBackup,
  CloudBackupSummary,
  CloudBackupInfo,
  CloudBackupActionResult,
  ReconcileResult,
} from "@/types/storage";

export {
  normalizeOptions,
  normalizeLearningState,
  getLastLocalUserId,
  setLastLocalUserId,
  getLastReconcileTimestamp,
  setLastReconcileTimestamp,
  clearLastReconcileTimestamp,
  setLoginSyncInProgress,
  isLoginSyncInProgress,
  getLocalState,
  saveLocalState,
  subscribeLocalState,
  recordMistake,
  toggleMistakeMastered,
  removeMistake,
  addVocab,
  removeVocab,
  toggleVocabMastery,
  resetAllVocabMastery,
  toggleFavorite,
  updateFavoriteNote,
  saveExamDraft,
  getExamDraft,
  clearExamDraft,
  savePracticeDraft,
  getPracticeDraft,
  clearPracticeDraft,
  touchUserActivityThrottled,
  saveExamResult,
  getExamResult,
  clearExamResult,
  clearLocalData,
} from "./storage/local";

export { getExamCardStats } from "./storage/stats";

export {
  getSanitizedLearningBackup,
  uploadBackupToCloud,
  downloadBackupFromCloud,
  fetchCloudBackupInfo,
} from "./storage/cloud";

export { reconcileLearningState } from "./storage/reconcile";
