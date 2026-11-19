import { supabase } from "../supabase";
import type {
  QuestionOption,
  MistakeItem,
  VocabItem,
  FavoriteItem,
  ExamDraft,
  PracticeDraft,
  ExamResult,
  LocalLearningState,
} from "@/types/storage";

function isQuotaExceededError(err: unknown): boolean {
  if (typeof err !== "object" || err === null) return false;
  const errObj = err as { name?: unknown; code?: unknown };
  return errObj.name === "QuotaExceededError" || errObj.code === 22;
}

/**
 * Resilient Options Parser:
 * Normalizes options whether entered in Supabase Table Editor as:
 * 1. Standard Array: [{"key":"A","text":"..."}, {"key":"B","text":"..."}]
 * 2. Simple Object: {"A":"...", "B":"..."}
 * 3. Array of strings: ["Option A text", "Option B text"]
 */
export function normalizeOptions(raw: unknown): QuestionOption[] {
  if (!raw) return [];
  if (Array.isArray(raw)) {
    return raw.map((item, idx) => {
      if (typeof item === "string") {
        const key = String.fromCharCode(65 + idx);
        return { key, text: item };
      }
      const obj = typeof item === "object" && item !== null ? (item as Record<string, unknown>) : null;
      return {
        key: String(obj?.key || String.fromCharCode(65 + idx)).trim().toUpperCase(),
        text: String(obj?.text || ""),
      };
    });
  }
  if (typeof raw === "object") {
    const obj = raw as Record<string, unknown>;
    const keys = Object.keys(obj).sort();
    return keys.map((k) => ({
      key: k.trim().toUpperCase(),
      text: String(obj[k] || ""),
    }));
  }
  if (typeof raw === "string") {
    try {
      const parsed: unknown = JSON.parse(raw);
      return normalizeOptions(parsed);
    } catch {
      return [];
    }
  }
  return [];
}

const STORAGE_KEY = "enway_local_learning_data";
const LAST_USER_ID_KEY = "enway_last_user_id";
const LEGACY_LAST_RECONCILE_KEY = "enway_last_reconcile_ts";
const LOGIN_SYNCING_TS_KEY = "enway_login_syncing_ts";
const LOGIN_SYNC_TIMEOUT_MS = 30_000;

export function normalizeLearningState(parsed: unknown): LocalLearningState {
  const isPlainObj = (val: unknown): val is Record<string, unknown> =>
    Boolean(val) && typeof val === "object" && !Array.isArray(val);

  if (!isPlainObj(parsed)) {
    return {
      mistakes: [],
      vocabulary: [],
      favorites: [],
      examResults: {},
      examDrafts: {},
      practiceDrafts: {},
    };
  }

  return {
    mistakes: Array.isArray(parsed.mistakes) ? (parsed.mistakes.filter(Boolean) as MistakeItem[]) : [],
    vocabulary: Array.isArray(parsed.vocabulary) ? (parsed.vocabulary.filter(Boolean) as VocabItem[]) : [],
    favorites: Array.isArray(parsed.favorites) ? (parsed.favorites.filter(Boolean) as FavoriteItem[]) : [],
    examResults: isPlainObj(parsed.examResults) ? (parsed.examResults as Record<string, ExamResult>) : {},
    examDrafts: isPlainObj(parsed.examDrafts) ? (parsed.examDrafts as Record<string, ExamDraft>) : {},
    practiceDrafts: isPlainObj(parsed.practiceDrafts) ? (parsed.practiceDrafts as Record<string, PracticeDraft>) : {},
  };
}

export function getLastLocalUserId(): string | null {
  if (typeof window === "undefined") return null;
  try {
    return localStorage.getItem(LAST_USER_ID_KEY) || null;
  } catch {
    return null;
  }
}

export function setLastLocalUserId(userId: string | null): void {
  if (typeof window === "undefined") return;
  try {
    if (userId) {
      localStorage.setItem(LAST_USER_ID_KEY, userId);
    } else {
      localStorage.removeItem(LAST_USER_ID_KEY);
    }
  } catch {}
}

export function getLastReconcileTimestamp(userId?: string | null): number {
  if (typeof window === "undefined") return 0;
  try {
    const key = userId ? `${LEGACY_LAST_RECONCILE_KEY}_${userId}` : LEGACY_LAST_RECONCILE_KEY;
    const raw = localStorage.getItem(key);
    const num = Number(raw || "0");
    return Number.isFinite(num) && num > 0 ? num : 0;
  } catch {
    return 0;
  }
}

export function setLastReconcileTimestamp(userId?: string | null, ts = Date.now()): void {
  if (typeof window === "undefined") return;
  try {
    const key = userId ? `${LEGACY_LAST_RECONCILE_KEY}_${userId}` : LEGACY_LAST_RECONCILE_KEY;
    localStorage.setItem(key, String(ts));
  } catch {}
}

export function clearLastReconcileTimestamp(userId?: string | null): void {
  if (typeof window === "undefined") return;
  try {
    if (userId) {
      localStorage.removeItem(`${LEGACY_LAST_RECONCILE_KEY}_${userId}`);
    }
    localStorage.removeItem(LEGACY_LAST_RECONCILE_KEY);
  } catch {}
}

export function setLoginSyncInProgress(active: boolean): void {
  if (typeof window === "undefined") return;
  try {
    if (active) {
      sessionStorage.setItem(LOGIN_SYNCING_TS_KEY, String(Date.now()));
    } else {
      sessionStorage.removeItem(LOGIN_SYNCING_TS_KEY);
    }
  } catch {}
  window.dispatchEvent(new CustomEvent("enway_login_sync_changed", { detail: { active } }));
}

export function isLoginSyncInProgress(): boolean {
  if (typeof window === "undefined") return false;
  try {
    const raw = sessionStorage.getItem(LOGIN_SYNCING_TS_KEY);
    if (!raw) return false;
    const ts = Number(raw);
    if (!Number.isFinite(ts) || Date.now() - ts >= LOGIN_SYNC_TIMEOUT_MS) {
      sessionStorage.removeItem(LOGIN_SYNCING_TS_KEY);
      return false;
    }
    return true;
  } catch {
    return false;
  }
}

export function getLocalState(): LocalLearningState {
  const defaultState: LocalLearningState = {
    mistakes: [],
    vocabulary: [],
    favorites: [],
    examResults: {},
    examDrafts: {},
    practiceDrafts: {},
  };
  if (typeof window === "undefined") {
    return defaultState;
  }
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      return defaultState;
    }
    const parsed = JSON.parse(raw);
    return normalizeLearningState(parsed);
  } catch (e) {
    console.error("Error reading local state", e);
    return defaultState;
  }
}

export function saveLocalState(state: LocalLearningState) {
  if (typeof window === "undefined") return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    window.dispatchEvent(new CustomEvent("enway_local_state_updated"));
  } catch (e: unknown) {
    console.error("Error saving local state", e);
    // If QuotaExceededError, attempt graceful degradation by pruning ephemeral drafts
    if (isQuotaExceededError(e)) {
      try {
        console.warn("[Storage] QuotaExceededError caught. Attempting graceful pruning of ephemeral drafts to protect core mistake/vocab data.");
        const fallbackState = {
          ...state,
          examDrafts: {},
          practiceDrafts: {},
        };
        localStorage.setItem(STORAGE_KEY, JSON.stringify(fallbackState));
        window.dispatchEvent(new CustomEvent("enway_local_state_updated"));
      } catch (innerErr) {
        console.error("[Storage] Fatal storage quota exhausted:", innerErr);
      }
    }
  }
}

export function subscribeLocalState(listener: (state: LocalLearningState) => void): () => void {
  if (typeof window === "undefined") return () => {};

  const handleLocalUpdate = () => {
    listener(getLocalState());
  };

  const handleStorageUpdate = (e: StorageEvent) => {
    if (e.key === null || e.key === STORAGE_KEY) {
      listener(getLocalState());
    }
  };

  window.addEventListener("enway_local_state_updated", handleLocalUpdate);
  window.addEventListener("storage", handleStorageUpdate);

  return () => {
    window.removeEventListener("enway_local_state_updated", handleLocalUpdate);
    window.removeEventListener("storage", handleStorageUpdate);
  };
}

// ------------------- Mistake Book (Index-only Lean Footprint) -------------------
export function recordMistake(item: {
  questionId: string;
  examId?: string;
  categoryId?: string;
  wrongAnswer: string;
}) {
  if (!item?.questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.mistakes)) state.mistakes = [];
  const existingIndex = state.mistakes.findIndex((m) => m && m.questionId === item.questionId);
  const now = new Date().toISOString();

  if (existingIndex >= 0) {
    state.mistakes[existingIndex].wrongCount = (state.mistakes[existingIndex].wrongCount || 1) + 1;
    state.mistakes[existingIndex].wrongAnswer = item.wrongAnswer || "未作答";
    state.mistakes[existingIndex].lastWrongAt = now;
    state.mistakes[existingIndex].isMastered = false; // Reset to unmastered on new error
    if (item.examId) state.mistakes[existingIndex].examId = item.examId;
    if (item.categoryId) state.mistakes[existingIndex].categoryId = item.categoryId;
  } else {
    state.mistakes.unshift({
      questionId: item.questionId,
      examId: item.examId,
      categoryId: item.categoryId,
      wrongAnswer: item.wrongAnswer || "未作答",
      wrongCount: 1,
      isMastered: false,
      lastWrongAt: now,
    });
  }

  // Sanitize all mistakes to strictly retain lightweight index fields (save Supabase cloud quota)
  state.mistakes = state.mistakes
    .filter((m) => m && m.questionId)
    .map((m) => ({
      questionId: m.questionId,
      examId: m.examId,
      categoryId: m.categoryId,
      wrongAnswer: m.wrongAnswer || "未作答",
      wrongCount: m.wrongCount || 1,
      isMastered: !!m.isMastered,
      lastWrongAt: m.lastWrongAt || now,
    }));

  saveLocalState(state);
}

export function toggleMistakeMastered(questionId: string, isMastered?: boolean) {
  if (!questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.mistakes)) return;
  const target = state.mistakes.find((m) => m && m.questionId === questionId);
  if (target) {
    target.isMastered = isMastered !== undefined ? isMastered : !target.isMastered;
    saveLocalState(state);
  }
}

export function removeMistake(questionId: string) {
  if (!questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.mistakes)) return;
  state.mistakes = state.mistakes.filter((m) => m && m.questionId !== questionId);
  saveLocalState(state);
}

// ------------------- Vocabulary -------------------
export function addVocab(word: string, translation: string, phonetic?: string, context?: string) {
  if (!word) return;
  const state = getLocalState();
  if (!Array.isArray(state.vocabulary)) state.vocabulary = [];
  const cleanWord = word.trim().toLowerCase();
  const exists = state.vocabulary.some((v) => v && v.word && v.word.toLowerCase() === cleanWord);
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
  if (!word) return;
  const state = getLocalState();
  if (!Array.isArray(state.vocabulary)) return;
  const cleanWord = word.trim().toLowerCase();
  state.vocabulary = state.vocabulary.filter((v) => v && v.word && v.word.toLowerCase() !== cleanWord);
  saveLocalState(state);
}

export function toggleVocabMastery(word: string, forceMastered?: boolean) {
  if (!word) return;
  const state = getLocalState();
  if (!Array.isArray(state.vocabulary)) return;
  const cleanWord = word.trim().toLowerCase();
  const item = state.vocabulary.find((v) => v && v.word && v.word.toLowerCase() === cleanWord);
  if (item) {
    item.mastered = typeof forceMastered === "boolean" ? forceMastered : !item.mastered;
    item.reviewCount = (item.reviewCount || 0) + 1;
    item.lastReviewedAt = new Date().toISOString();
    saveLocalState(state);
  }
}

export function resetAllVocabMastery() {
  const state = getLocalState();
  if (!Array.isArray(state.vocabulary)) return;
  state.vocabulary.forEach((v) => {
    if (v) v.mastered = false;
  });
  saveLocalState(state);
}

// ------------------- Favorites -------------------
export function toggleFavorite(item: Partial<FavoriteItem> & { questionId: string }) {
  if (!item?.questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.favorites)) state.favorites = [];
  const index = state.favorites.findIndex((f) => f && f.questionId === item.questionId);
  if (index >= 0) {
    state.favorites.splice(index, 1);
  } else {
    // Keep favorite item lightweight to avoid exceeding 5MB LocalStorage quota
    state.favorites.unshift({
      questionId: item.questionId,
      examId: item.examId || "",
      note: item.note || "",
      addedAt: new Date().toISOString(),
    });
  }
  saveLocalState(state);
}

export function updateFavoriteNote(questionId: string, note: string) {
  if (!questionId) return;
  const state = getLocalState();
  if (!Array.isArray(state.favorites)) return;
  const target = state.favorites.find((f) => f && f.questionId === questionId);
  if (target) {
    target.note = note;
    saveLocalState(state);
  }
}

// ------------------- Exam Drafts (Auto-Save Resilience) -------------------
export function saveExamDraft(examId: string, answers: Record<string, string>, remainingSeconds: number, focusedIndex?: number) {
  if (!examId) return;
  const state = getLocalState();
  if (!state.examDrafts || typeof state.examDrafts !== "object") {
    state.examDrafts = {};
  }
  state.examDrafts[examId] = {
    examId,
    answers: answers || {},
    remainingSeconds: typeof remainingSeconds === "number" ? remainingSeconds : 3600,
    focusedIndex: typeof focusedIndex === "number" ? focusedIndex : 0,
    lastUpdated: new Date().toISOString(),
  };
  saveLocalState(state);
}

export function getExamDraft(examId: string): ExamDraft | null {
  if (!examId) return null;
  const state = getLocalState();
  return state.examDrafts?.[examId] || null;
}

export function clearExamDraft(examId: string) {
  if (!examId) return;
  const state = getLocalState();
  if (state.examDrafts && typeof state.examDrafts === "object") {
    delete state.examDrafts[examId];
    saveLocalState(state);
  }
}

// ------------------- Practice Drafts (Smart Practice Resume) -------------------
export function savePracticeDraft(
  examId: string,
  answers: Record<string, string>,
  currentIndex: number,
  stats?: { score?: number; correctCount?: number; totalQuestions?: number; answeredCount?: number }
) {
  if (!examId) return;
  const state = getLocalState();
  if (!state.practiceDrafts || typeof state.practiceDrafts !== "object") {
    state.practiceDrafts = {};
  }
  state.practiceDrafts[examId] = {
    examId,
    answers: answers || {},
    currentIndex: typeof currentIndex === "number" ? currentIndex : 0,
    lastUpdated: new Date().toISOString(),
    ...(stats || {}),
  };
  saveLocalState(state);
}

export function getPracticeDraft(examId: string): PracticeDraft | null {
  if (!examId) return null;
  const state = getLocalState();
  return state.practiceDrafts?.[examId] || null;
}

export function clearPracticeDraft(examId: string) {
  if (!examId) return;
  const state = getLocalState();
  if (state.practiceDrafts && typeof state.practiceDrafts === "object") {
    delete state.practiceDrafts[examId];
    saveLocalState(state);
  }
}

// ------------------- Activity Presence Throttled Touch -------------------
const PRESENCE_TOUCH_KEY = "enway_last_presence_touch";
const PRESENCE_TOUCH_THROTTLE_MS = 18 * 60 * 1000;
let inFlightPresenceTouch: Promise<void> | null = null;

export function touchUserActivityThrottled(): Promise<void> {
  if (typeof window === "undefined") return Promise.resolve();
  if (inFlightPresenceTouch) return inFlightPresenceTouch;

  inFlightPresenceTouch = (async () => {
    const now = Date.now();
    try {
      const last = Number(localStorage.getItem(PRESENCE_TOUCH_KEY) || "0");
      if (now - last < PRESENCE_TOUCH_THROTTLE_MS) return;
      const { data: { session } } = await supabase.auth.getSession();
      if (!session?.user) return;
      localStorage.setItem(PRESENCE_TOUCH_KEY, String(now));
      await supabase.rpc("touch_user_activity");
    } catch {
    } finally {
      inFlightPresenceTouch = null;
    }
  })();

  return inFlightPresenceTouch;
}

// ------------------- Exam Results (Latest Overwrite) -------------------
export function saveExamResult(result: ExamResult) {
  if (!result?.examId) return;
  const state = getLocalState();
  if (!state.examResults || typeof state.examResults !== "object") {
    state.examResults = {};
  }
  if (!state.examDrafts || typeof state.examDrafts !== "object") {
    state.examDrafts = {};
  }
  state.examResults[result.examId] = result;
  // Clear draft once submitted
  delete state.examDrafts[result.examId];
  saveLocalState(state);

  // Touch active timestamp on exam submission with 18-min cross-tab throttle
  touchUserActivityThrottled().catch(() => {});
}

export function getExamResult(examId: string): ExamResult | null {
  if (!examId) return null;
  const state = getLocalState();
  return state.examResults?.[examId] || null;
}

export function clearExamResult(examId: string) {
  if (!examId) return;
  const state = getLocalState();
  if (state.examResults && state.examResults[examId]) {
    delete state.examResults[examId];
    saveLocalState(state);
  }
}

// ------------------- Clear Local Data -------------------
export function clearLocalData(scope: "all" | "mistakes" | "vocab" | "drafts") {
  const state = getLocalState();
  if (scope === "all") {
    saveLocalState({ mistakes: [], vocabulary: [], favorites: [], examResults: {}, examDrafts: {}, practiceDrafts: {} });
  } else if (scope === "mistakes") {
    state.mistakes = [];
    saveLocalState(state);
  } else if (scope === "vocab") {
    state.vocabulary = [];
    saveLocalState(state);
  } else if (scope === "drafts") {
    state.examDrafts = {};
    state.practiceDrafts = {};
    saveLocalState(state);
  }
}
