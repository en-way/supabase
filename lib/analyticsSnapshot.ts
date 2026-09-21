import { supabase } from "./supabase";

export interface AnalyticsSnapshot {
  totalStudents: number;
  totalAdmins: number;
  totalExams: number;
  examsByCategory: Record<string, number>;
  totalBackups: number;
  generatedAt: string;
}

const SNAPSHOT_PATH = "admin-analytics/snapshot.json";

/**
 * Loads dashboard analytics snapshot directly from 1GB Storage Bucket.
 * ⚡ Zero DB CPU load, 0 complex SQL aggregations.
 */
export async function fetchAnalyticsSnapshot(): Promise<{
  snapshot: AnalyticsSnapshot | null;
  fromStorage: boolean;
}> {
  try {
    const { data: fileBlob, error } = await supabase.storage
      .from("user-backups")
      .download(SNAPSHOT_PATH);

    if (!error && fileBlob) {
      const text = await fileBlob.text();
      if (text) {
        const parsed = JSON.parse(text) as AnalyticsSnapshot;
        return { snapshot: parsed, fromStorage: true };
      }
    }
  } catch (err) {
    console.warn("[Analytics] Snapshot miss in Storage, falling back to compute:", err);
  }

  // If miss or error, compute on-demand
  return { snapshot: null, fromStorage: false };
}

/**
 * Computes platform analytics and persists the pre-rendered snapshot into Storage Bucket.
 */
export async function refreshAnalyticsSnapshot(): Promise<AnalyticsSnapshot | null> {
  try {
    const [profilesRes, examsRes, backupsRes] = await Promise.all([
      supabase.from("profiles").select("role"),
      supabase.from("exams").select("category_id"),
      supabase.from("user_backups").select("user_id", { count: "exact", head: true }),
    ]);

    let students = 0;
    let admins = 0;
    if (profilesRes.data) {
      for (const p of profilesRes.data) {
        if (p.role === "student") students++;
        else if (p.role === "admin" || p.role === "super_admin") admins++;
      }
    }

    const byCategory: Record<string, number> = {};
    if (examsRes.data) {
      for (const e of examsRes.data) {
        byCategory[e.category_id] = (byCategory[e.category_id] || 0) + 1;
      }
    }

    const snapshot: AnalyticsSnapshot = {
      totalStudents: students,
      totalAdmins: admins,
      totalExams: examsRes.data?.length || 0,
      examsByCategory: byCategory,
      totalBackups: backupsRes.count || 0,
      generatedAt: new Date().toISOString(),
    };

    // Upload snapshot to Storage Bucket
    const blob = new Blob([JSON.stringify(snapshot, null, 2)], {
      type: "application/json",
    });

    await supabase.storage
      .from("user-backups")
      .upload(SNAPSHOT_PATH, blob, {
        contentType: "application/json",
        upsert: true,
      });

    return snapshot;
  } catch (err) {
    console.error("[Analytics] Failed to refresh snapshot:", err);
    return null;
  }
}
