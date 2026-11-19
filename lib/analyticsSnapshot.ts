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
        if (
          parsed &&
          typeof parsed === "object" &&
          typeof parsed.totalStudents === "number" &&
          typeof parsed.totalExams === "number"
        ) {
          return { snapshot: parsed, fromStorage: true };
        }
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
  const [studentsRes, adminsRes, examsRes, backupsRes] = await Promise.all([
    supabase.from("profiles").select("id", { count: "exact", head: true }).eq("role", "student"),
    supabase.from("profiles").select("id", { count: "exact", head: true }).in("role", ["admin", "super_admin"]),
    supabase.from("exams").select("category_id"),
    supabase.from("user_backups").select("user_id", { count: "exact", head: true }),
  ]);

  if (studentsRes.error) {
    throw new Error(`查询学员总数失败: ${studentsRes.error.message}`);
  }
  if (adminsRes.error) {
    throw new Error(`查询管理员总数失败: ${adminsRes.error.message}`);
  }
  if (examsRes.error) {
    throw new Error(`查询试卷统计失败: ${examsRes.error.message}`);
  }
  if (backupsRes.error) {
    throw new Error(`查询云端备份数失败: ${backupsRes.error.message}`);
  }

  const byCategory: Record<string, number> = {};
  if (examsRes.data) {
    for (const e of examsRes.data) {
      byCategory[e.category_id] = (byCategory[e.category_id] ?? 0) + 1;
    }
  }

  const snapshot: AnalyticsSnapshot = {
    totalStudents: studentsRes.count ?? 0,
    totalAdmins: adminsRes.count ?? 0,
    totalExams: examsRes.data?.length ?? 0,
    examsByCategory: byCategory,
    totalBackups: backupsRes.count ?? 0,
    generatedAt: new Date().toISOString(),
  };

  // Upload snapshot to Storage Bucket
  const blob = new Blob([JSON.stringify(snapshot, null, 2)], {
    type: "application/json",
  });

  const { error: uploadError } = await supabase.storage
    .from("user-backups")
    .upload(SNAPSHOT_PATH, blob, {
      contentType: "application/json",
      upsert: true,
    });

  if (uploadError) {
    throw new Error(`上传统计快照失败: ${uploadError.message}`);
  }

  return snapshot;
}
