import { supabase } from "@/lib/supabase";

export interface ExamDetailData {
  exam: any;
  passages: any[];
  questions: any[];
  fromStaticMirror?: boolean;
}

const CACHE_NAME = "enway-static-v3";
const LEGACY_CACHE_NAMES = ["enway-static-v1", "enway-static-v2"];
const hasCacheStorage = typeof window !== "undefined" && "caches" in window;

// Purge legacy caches on client load
if (hasCacheStorage) {
  LEGACY_CACHE_NAMES.forEach((oldName) => {
    caches.delete(oldName).catch(() => {});
  });
}

// In-memory session cache for loaded exam packages (Tier 1: 0ms)
const examDetailMemoryCache: Record<string, ExamDetailData> = {};
let lobbyMemoryCache: { categories: any[]; exams: any[] } | null = null;
let hasRevalidatedLobby = false;

/**
 * Reads a cached Response object from browser CacheStorage
 */
async function getCachedResponse(url: string): Promise<Response | null> {
  if (!hasCacheStorage) return null;
  try {
    const cache = await caches.open(CACHE_NAME);
    const match = await cache.match(url);
    return match || null;
  } catch {
    return null;
  }
}

/**
 * Stores a Response object into browser CacheStorage
 */
async function putCachedResponse(url: string, res: Response): Promise<void> {
  if (!hasCacheStorage) return;
  try {
    const cache = await caches.open(CACHE_NAME);
    await cache.put(url, res);
  } catch {
    // QuotaExceededError or private browsing restrictions, non-fatal
  }
}

/**
 * Validates that a response is legitimate JSON rather than an HTML SPA fallback
 */
function isJsonResponse(res: Response): boolean {
  if (!res.ok) return false;
  const ct = (res.headers.get("content-type") || "").toLowerCase();
  // Reject HTML fallback (e.g. Cloudflare SPA 404 rewrite returning index.html)
  if (ct.includes("text/html") || ct.includes("text/plain")) return false;
  return ct.includes("application/json") || ct === "";
}

let hasCheckedVersion = false;
let lastVersionCheckTime = 0;
const VERSION_CHECK_THROTTLE_MS = 10 * 60 * 1000; // 10 minutes throttle

/**
 * Checks /data/version.json to determine if the static exam mirror has updated.
 * If a new version hash is detected, automatically purges stale CacheStorage.
 */
export async function checkAndUpdateExamVersion(force = false): Promise<boolean> {
  if (typeof window === "undefined") return false;
  const now = Date.now();
  if (!force && hasCheckedVersion && (now - lastVersionCheckTime < VERSION_CHECK_THROTTLE_MS)) {
    return false;
  }
  hasCheckedVersion = true;
  lastVersionCheckTime = now;

  try {
    const res = await fetch("/data/version.json", { cache: "no-cache" });
    if (!isJsonResponse(res)) return false;
    const { version } = await res.json();
    const storedVersion = localStorage.getItem("enway_exam_version");
    if (storedVersion && storedVersion !== version) {
      console.log(`[ExamLoader] Upgrading exam mirror cache: ${storedVersion} -> ${version}`);
      if (hasCacheStorage) {
        await caches.delete(CACHE_NAME).catch(() => {});
      }
      lobbyMemoryCache = null;
      for (const k of Object.keys(examDetailMemoryCache)) {
        delete examDetailMemoryCache[k];
      }
      localStorage.setItem("enway_exam_version", version);
      window.dispatchEvent(new CustomEvent("enway_exam_version_updated", { detail: { version } }));
      return true;
    }
    if (version) {
      localStorage.setItem("enway_exam_version", version);
    }
    return false;
  } catch {
    return false;
  }
}

// Background foreground wake-up listener for PWA and mobile tabs
if (typeof window !== "undefined") {
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") {
      checkAndUpdateExamVersion(false);
    }
  });
}

/**
 * Background silent revalidation for lobby metadata
 */
function revalidateLobbyInBackground() {
  if (typeof window === "undefined") return;
  setTimeout(async () => {
    try {
      const [catRes, examRes] = await Promise.all([
        fetch("/data/categories.json", { cache: "reload" }),
        fetch("/data/exams.json", { cache: "reload" }),
      ]);
      if (isJsonResponse(catRes) && isJsonResponse(examRes)) {
        const catClone = catRes.clone();
        const examClone = examRes.clone();
        await Promise.all([
          putCachedResponse("/data/categories.json", catClone),
          putCachedResponse("/data/exams.json", examClone),
        ]);
        const categories = await catRes.json();
        const exams = await examRes.json();
        lobbyMemoryCache = { categories, exams };
        window.dispatchEvent(
          new CustomEvent("enway_lobby_revalidated", {
            detail: { categories, exams },
          })
        );
      }
    } catch {
      // Offline / network failure during silent background revalidate is safe to ignore
    }
  }, 1000);
}

/**
 * Loads exam lobby data (categories + approved exams).
 * Priority: 
 *   Tier 1: In-memory cache & Browser CacheStorage (0ms, 0 network, offline ready)
 *   Tier 2: Cloudflare Pages static CDN -> update CacheStorage
 *   Tier 3: Supabase fallback
 */
export async function fetchExamLobbyData(): Promise<{ categories: any[]; exams: any[] }> {
  // Silent version update check
  if (!hasCheckedVersion && typeof window !== "undefined") {
    checkAndUpdateExamVersion().catch(() => {});
  }

  // Tier 1a: Instant memory cache
  if (lobbyMemoryCache) {
    return lobbyMemoryCache;
  }

  // Tier 1b: Check browser persistent CacheStorage
  try {
    const [cachedCat, cachedExam] = await Promise.all([
      getCachedResponse("/data/categories.json"),
      getCachedResponse("/data/exams.json"),
    ]);

    if (cachedCat && cachedExam) {
      const categories = await cachedCat.json();
      const exams = await cachedExam.json();
      lobbyMemoryCache = { categories, exams };
      // Silent background revalidation (at most once per session)
      if (!hasRevalidatedLobby) {
        hasRevalidatedLobby = true;
        revalidateLobbyInBackground();
      }
      return lobbyMemoryCache;
    }
  } catch (err) {
    console.warn("[ExamLoader] CacheStorage lookup failed:", err);
  }

  // 2. Tier 2: Fetch from Cloudflare Pages static CDN
  try {
    const [catRes, examRes] = await Promise.all([
      fetch("/data/categories.json", { cache: "default" }),
      fetch("/data/exams.json", { cache: "default" }),
    ]);

    if (isJsonResponse(catRes) && isJsonResponse(examRes)) {
      const catClone = catRes.clone();
      const examClone = examRes.clone();
      putCachedResponse("/data/categories.json", catClone);
      putCachedResponse("/data/exams.json", examClone);

      const categories = await catRes.json();
      const exams = await examRes.json();
      lobbyMemoryCache = { categories, exams };
      return lobbyMemoryCache;
    }
  } catch (e) {
    console.warn("[ExamLoader] Static lobby cache miss or network failure, falling back to Supabase:", e);
  }

  // 3. Tier 3: Fallback to Supabase PostgREST with explicit fields
  try {
    const [catRes, examRes] = await Promise.all([
      supabase.from("categories").select("id, name, description, sort_order").order("sort_order"),
      supabase
        .from("exams")
        .select(`
          id, category_id, title, year, exam_type, duration_minutes, total_score, pass_score,
          questions(count),
          passages(count)
        `)
        .eq("is_published", true)
        .eq("approval_status", "approved")
        .order("year", { ascending: false }),
    ]);

    const result = {
      categories: catRes.data || [],
      exams: examRes.data || [],
    };
    lobbyMemoryCache = result;
    return result;
  } catch (err) {
    console.warn("[ExamLoader] Supabase fallback query failed:", err);
    return { categories: [], exams: [] };
  }
}

/**
 * Loads full exam details (exam info + passages + questions).
 * Tier 1: In-memory cache (0ms).
 * Tier 2: Browser persistent CacheStorage (0 network, 100% offline capable).
 * Tier 3: Cloudflare Pages static CDN mirror (/data/exams/{id}.json) (15ms, 0 Supabase DB quota).
 * Tier 4: Falls back to Supabase PostgREST if not present in static mirror.
 */
export async function fetchExamDetailWithFallback(examId: string): Promise<ExamDetailData | null> {
  if (!examId) return null;

  // Tier 1: In-memory cache hit
  if (examDetailMemoryCache[examId]) {
    return examDetailMemoryCache[examId];
  }

  const staticUrl = `/data/exams/${encodeURIComponent(examId)}.json`;

  // Tier 2: Browser persistent CacheStorage
  try {
    const cachedRes = await getCachedResponse(staticUrl);
    if (cachedRes) {
      const data: ExamDetailData = await cachedRes.json();
      data.fromStaticMirror = true;
      examDetailMemoryCache[examId] = data;
      return data;
    }
  } catch (err) {
    console.warn(`[ExamLoader] Error reading CacheStorage for ${staticUrl}:`, err);
  }

  // Tier 3: Try Cloudflare Pages static CDN mirror
  try {
    const res = await fetch(staticUrl, {
      cache: "default",
    });
    if (isJsonResponse(res)) {
      const clone = res.clone();
      putCachedResponse(staticUrl, clone);
      const data: ExamDetailData = await res.json();
      data.fromStaticMirror = true;
      examDetailMemoryCache[examId] = data;
      return data;
    }
  } catch (err) {
    console.warn(`[ExamLoader] Static exam ${staticUrl} not found or network offline, trying Supabase...`);
  }

  // Tier 4: Fallback to Supabase PostgREST with explicit column projection
  try {
    const { data: examData, error: examErr } = await supabase
      .from("exams")
      .select("id, category_id, title, year, exam_type, duration_minutes, total_score, pass_score")
      .eq("id", examId)
      .single();
    if (examErr) throw examErr;

    const [pRes, qRes] = await Promise.all([
      supabase
        .from("passages")
        .select("id, exam_id, category_id, section_type, title, content, sort_order")
        .eq("exam_id", examId)
        .order("sort_order"),
      supabase
        .from("questions")
        .select("id, exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order")
        .eq("exam_id", examId)
        .order("sort_order"),
    ]);

    const result: ExamDetailData = {
      exam: examData || null,
      passages: pRes.data || [],
      questions: qRes.data || [],
      fromStaticMirror: false,
    };

    examDetailMemoryCache[examId] = result;
    return result;
  } catch (err) {
    console.error(`[ExamLoader] Failed to load exam ${examId} from Supabase:`, err);
    return null;
  }
}

/**
 * Manually invalidates or clears the static cache
 */
export async function clearStaticExamCache(): Promise<boolean> {
  lobbyMemoryCache = null;
  hasRevalidatedLobby = false;
  for (const k of Object.keys(examDetailMemoryCache)) {
    delete examDetailMemoryCache[k];
  }
  if (!hasCacheStorage) return false;
  try {
    return await caches.delete(CACHE_NAME);
  } catch {
    return false;
  }
}
