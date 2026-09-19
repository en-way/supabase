import { supabase } from "./supabase";

export interface QuestionOption {
  key: string;
  text: string;
}

export interface MistakeItem {
  questionId: string;
  examId: string;
  categoryId: string;
  stem: string;
  options: QuestionOption[];
  correctAnswer: string;
  explanation: string;
  wrongAnswer: string;
  wrongCount: number;
  isMastered: boolean;
  lastWrongAt: string;
}

export interface VocabItem {
  word: string;
  phonetic?: string;
  translation: string;
  context?: string;
  addedAt: string;
}

export interface FavoriteItem {
  questionId: string;
  examId: string;
  stem: string;
  options: QuestionOption[];
  correctAnswer: string;
  explanation: string;
  note?: string;
  addedAt: string;
}

export interface ExamDraft {
  examId: string;
  answers: Record<string, string>;
  remainingSeconds: number;
  lastUpdated: string;
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
}

const STORAGE_KEY = "enway_local_learning_data";

export function getLocalState(): LocalLearningState {
  if (typeof window === "undefined") {
    return { mistakes: [], vocabulary: [], favorites: [], examResults: {}, examDrafts: {} };
  }
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      return { mistakes: [], vocabulary: [], favorites: [], examResults: {}, examDrafts: {} };
    }
    return JSON.parse(raw);
  } catch (e) {
    console.error("Error reading local state", e);
    return { mistakes: [], vocabulary: [], favorites: [], examResults: {}, examDrafts: {} };
  }
}

export function saveLocalState(state: LocalLearningState) {
  if (typeof window === "undefined") return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (e) {
    console.error("Error saving local state", e);
  }
}

// ------------------- Mistake Book -------------------
export function recordMistake(item: Omit<MistakeItem, "wrongCount" | "isMastered" | "lastWrongAt">) {
  const state = getLocalState();
  const existingIndex = state.mistakes.findIndex((m) => m.questionId === item.questionId);
  const now = new Date().toISOString();

  if (existingIndex >= 0) {
    state.mistakes[existingIndex].wrongCount += 1;
    state.mistakes[existingIndex].wrongAnswer = item.wrongAnswer;
    state.mistakes[existingIndex].lastWrongAt = now;
    state.mistakes[existingIndex].isMastered = false; // Reset to unmastered on new error
  } else {
    state.mistakes.unshift({
      ...item,
      wrongCount: 1,
      isMastered: false,
      lastWrongAt: now,
    });
  }
  saveLocalState(state);
}

export function toggleMistakeMastered(questionId: string, isMastered?: boolean) {
  const state = getLocalState();
  const target = state.mistakes.find((m) => m.questionId === questionId);
  if (target) {
    target.isMastered = isMastered !== undefined ? isMastered : !target.isMastered;
    saveLocalState(state);
  }
}

export function removeMistake(questionId: string) {
  const state = getLocalState();
  state.mistakes = state.mistakes.filter((m) => m.questionId !== questionId);
  saveLocalState(state);
}

// ------------------- Vocabulary -------------------
export function addVocab(word: string, translation: string, phonetic?: string, context?: string) {
  const state = getLocalState();
  const cleanWord = word.trim().toLowerCase();
  const exists = state.vocabulary.some((v) => v.word.toLowerCase() === cleanWord);
  if (!exists) {
    state.vocabulary.unshift({
      word: cleanWord,
      translation,
      phonetic,
      context,
      addedAt: new Date().toISOString(),
    });
    saveLocalState(state);
  }
}

export function removeVocab(word: string) {
  const state = getLocalState();
  const cleanWord = word.trim().toLowerCase();
  state.vocabulary = state.vocabulary.filter((v) => v.word.toLowerCase() !== cleanWord);
  saveLocalState(state);
}

// ------------------- Favorites -------------------
export function toggleFavorite(item: Omit<FavoriteItem, "addedAt">) {
  const state = getLocalState();
  const index = state.favorites.findIndex((f) => f.questionId === item.questionId);
  if (index >= 0) {
    state.favorites.splice(index, 1);
  } else {
    state.favorites.unshift({
      ...item,
      addedAt: new Date().toISOString(),
    });
  }
  saveLocalState(state);
}

export function updateFavoriteNote(questionId: string, note: string) {
  const state = getLocalState();
  const target = state.favorites.find((f) => f.questionId === questionId);
  if (target) {
    target.note = note;
    saveLocalState(state);
  }
}

// ------------------- Exam Drafts (Auto-Save Resilience) -------------------
export function saveExamDraft(examId: string, answers: Record<string, string>, remainingSeconds: number) {
  const state = getLocalState();
  state.examDrafts[examId] = {
    examId,
    answers,
    remainingSeconds,
    lastUpdated: new Date().toISOString(),
  };
  saveLocalState(state);
}

export function getExamDraft(examId: string): ExamDraft | null {
  const state = getLocalState();
  return state.examDrafts[examId] || null;
}

export function clearExamDraft(examId: string) {
  const state = getLocalState();
  delete state.examDrafts[examId];
  saveLocalState(state);
}

// ------------------- Exam Results (Latest Overwrite) -------------------
export function saveExamResult(result: ExamResult) {
  const state = getLocalState();
  state.examResults[result.examId] = result;
  // Clear draft once submitted
  delete state.examDrafts[result.examId];
  saveLocalState(state);
}

// ------------------- Cloud Backup & Restore -------------------
export async function uploadBackupToCloud(): Promise<{ success: boolean; error?: string }> {
  try {
    const { data: { user }, error: userErr } = await supabase.auth.getUser();
    if (userErr || !user) {
      return { success: false, error: "未登录，无法备份到云端" };
    }

    const state = getLocalState();
    const summary = {
      mistakesCount: state.mistakes.length,
      vocabCount: state.vocabulary.length,
      favoritesCount: state.favorites.length,
      examsCount: Object.keys(state.examResults).length,
      backedUpAt: new Date().toISOString(),
    };

    const { error } = await supabase
      .from("user_backups")
      .upsert({
        user_id: user.id,
        backup_data: state,
        summary,
        updated_at: new Date().toISOString(),
      });

    if (error) throw error;
    return { success: true };
  } catch (err: any) {
    return { success: false, error: err.message || "上传备份失败" };
  }
}

export async function downloadBackupFromCloud(): Promise<{ success: boolean; summary?: any; error?: string }> {
  try {
    const { data: { user }, error: userErr } = await supabase.auth.getUser();
    if (userErr || !user) {
      return { success: false, error: "未登录，无法拉取云端数据" };
    }

    const { data, error } = await supabase
      .from("user_backups")
      .select("backup_data, summary, updated_at")
      .eq("user_id", user.id)
      .single();

    if (error) {
      if (error.code === "PGRST116") {
        return { success: false, error: "云端暂无备份记录" };
      }
      throw error;
    }

    if (data?.backup_data) {
      // Overwrite local state
      saveLocalState(data.backup_data as LocalLearningState);
      return { success: true, summary: data.summary };
    }

    return { success: false, error: "云端数据为空" };
  } catch (err: any) {
    return { success: false, error: err.message || "下载恢复失败" };
  }
}

export async function fetchCloudBackupInfo(): Promise<{ exists: boolean; summary?: any; updatedAt?: string }> {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return { exists: false };

    const { data } = await supabase
      .from("user_backups")
      .select("summary, updated_at")
      .eq("user_id", user.id)
      .maybeSingle();

    if (data) {
      return { exists: true, summary: data.summary, updatedAt: data.updated_at };
    }
    return { exists: false };
  } catch {
    return { exists: false };
  }
}

// ------------------- Clear Local Data -------------------
export function clearLocalData(scope: "all" | "mistakes" | "vocab" | "drafts") {
  const state = getLocalState();
  if (scope === "all") {
    saveLocalState({ mistakes: [], vocabulary: [], favorites: [], examResults: {}, examDrafts: {} });
  } else if (scope === "mistakes") {
    state.mistakes = [];
    saveLocalState(state);
  } else if (scope === "vocab") {
    state.vocabulary = [];
    saveLocalState(state);
  } else if (scope === "drafts") {
    state.examDrafts = {};
    saveLocalState(state);
  }
}
