import { supabase } from "@/lib/supabase";

export interface ExamDetailData {
  exam: any;
  passages: any[];
  questions: any[];
  fromStaticMirror?: boolean;
}

const CACHE_NAME = "enway-static-v2";
const LEGACY_CACHE_NAMES = ["enway-static-v1"];
const hasCacheStorage = typeof window !== "undefined" && "caches" in window;

// Purge legacy caches on client load
if (hasCacheStorage) {
  LEGACY_CACHE_NAMES.forEach((oldName) => {
    caches.delete(oldName).catch(() => {});
  });
}

// In-memory session cache for loaded exam packages (Tier 1: 0ms)
const examDetailMemoryCache: Record<string, ExamDetailData> = {};

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
 * Stores a cloned Response object into browser CacheStorage
 */
async function putCachedResponse(url: string, res: Response): Promise<void> {
  if (!hasCacheStorage) return;
  try {
    const cache = await caches.open(CACHE_NAME);
    await cache.put(url, res.clone());
  } catch {
    // QuotaExceededError or private browsing restrictions, non-fatal
  }
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
      if (catRes.ok && examRes.ok) {
        await Promise.all([
          putCachedResponse("/data/categories.json", catRes),
          putCachedResponse("/data/exams.json", examRes),
        ]);
      }
    } catch {
      // Offline / network failure during silent background revalidate is safe to ignore
    }
  }, 1000);
}

/**
 * Loads exam lobby data (categories + approved exams).
 * Priority: 
 *   Tier 1: Browser CacheStorage (0ms, 0 network, offline ready)
 *   Tier 2: Cloudflare Pages static CDN -> update CacheStorage
 *   Tier 3: Supabase fallback
 */
export async function fetchExamLobbyData(): Promise<{ categories: any[]; exams: any[] }> {
  // 1. Tier 1: Check browser persistent CacheStorage first
  try {
    const [cachedCat, cachedExam] = await Promise.all([
      getCachedResponse("/data/categories.json"),
      getCachedResponse("/data/exams.json"),
    ]);

    if (cachedCat && cachedExam) {
      const categories = await cachedCat.json();
      const exams = await cachedExam.json();
      // Silent background revalidation keeps data fresh without slowing down rendering
      revalidateLobbyInBackground();
      return { categories, exams };
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

    if (catRes.ok && examRes.ok) {
      putCachedResponse("/data/categories.json", catRes);
      putCachedResponse("/data/exams.json", examRes);

      const categories = await catRes.json();
      const exams = await examRes.json();
      return { categories, exams };
    }
  } catch (e) {
    console.warn("[ExamLoader] Static lobby cache miss or network failure, falling back to Supabase:", e);
  }

  // 3. Tier 3: Fallback to Supabase PostgREST
  const [catRes, examRes] = await Promise.all([
    supabase.from("categories").select("*").order("sort_order"),
    supabase
      .from("exams")
      .select(`
        *,
        questions(count),
        passages(count)
      `)
      .eq("is_published", true)
      .eq("approval_status", "approved")
      .order("year", { ascending: false }),
  ]);

  return {
    categories: catRes.data || [],
    exams: examRes.data || [],
  };
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
    if (res.ok) {
      putCachedResponse(staticUrl, res);
      const data: ExamDetailData = await res.json();
      data.fromStaticMirror = true;
      examDetailMemoryCache[examId] = data;
      return data;
    }
  } catch (err) {
    console.warn(`[ExamLoader] Static exam ${staticUrl} not found or network offline, trying Supabase...`);
  }

  // Tier 4: Fallback to Supabase PostgREST
  try {
    const { data: examData, error: examErr } = await supabase
      .from("exams")
      .select("*")
      .eq("id", examId)
      .single();
    if (examErr) throw examErr;

    const [pRes, qRes] = await Promise.all([
      supabase
        .from("passages")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order"),
      supabase
        .from("questions")
        .select("*")
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
  if (!hasCacheStorage) return false;
  try {
    return await caches.delete(CACHE_NAME);
  } catch {
    return false;
  }
}
