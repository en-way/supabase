import { supabase } from "@/lib/supabase";

export interface ExamDetailData {
  exam: any;
  passages: any[];
  questions: any[];
  fromStaticMirror?: boolean;
}

// In-memory session cache for loaded exam packages
const examDetailMemoryCache: Record<string, ExamDetailData> = {};

/**
 * Loads exam lobby data (categories + approved exams).
 * Priority: Cloudflare Pages static CDN -> Supabase fallback.
 */
export async function fetchExamLobbyData(): Promise<{ categories: any[]; exams: any[] }> {
  try {
    const [catRes, examRes] = await Promise.all([
      fetch("/data/categories.json", { cache: "default" }),
      fetch("/data/exams.json", { cache: "default" }),
    ]);

    if (catRes.ok && examRes.ok) {
      const categories = await catRes.json();
      const exams = await examRes.json();
      return { categories, exams };
    }
  } catch (e) {
    console.warn("[ExamLoader] Static lobby cache miss or network failure, falling back to Supabase:", e);
  }

  // Fallback to Supabase PostgREST
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
 * 1. Checks memory cache (0ms).
 * 2. Fetches from Cloudflare Pages static CDN mirror (/data/exams/{id}.json) (15ms, 0 Supabase DB quota).
 * 3. Falls back to Supabase PostgREST if not present in static mirror (e.g., newly added custom mock exam).
 */
export async function fetchExamDetailWithFallback(examId: string): Promise<ExamDetailData | null> {
  if (!examId) return null;

  // 1. In-memory cache hit
  if (examDetailMemoryCache[examId]) {
    return examDetailMemoryCache[examId];
  }

  // 2. Try Cloudflare Pages static CDN mirror
  try {
    const res = await fetch(`/data/exams/${encodeURIComponent(examId)}.json`, {
      cache: "default",
    });
    if (res.ok) {
      const data: ExamDetailData = await res.json();
      data.fromStaticMirror = true;
      examDetailMemoryCache[examId] = data;
      return data;
    }
  } catch (err) {
    console.warn(`[ExamLoader] Static exam /data/exams/${examId}.json not found or error, trying Supabase...`);
  }

  // 3. Fallback to Supabase
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
