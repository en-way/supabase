import { getCircuitBreakerState } from "@/lib/quotaSentinel";
import type { RawQuestionOptions } from "@/types/exam";
import type { AnnouncementType, UserProfile } from "@/types/user";

export type AdminTab =
  | "exams"
  | "approvals"
  | "pwdApprovals"
  | "import"
  | "users"
  | "settings";

export interface AdminNotice {
  type: "success" | "error";
  text: string;
}

export interface AdminSettingsState {
  maxStudentsLimit: number;
  registrationEnabled: boolean;
}

export interface AdminAnnouncementState {
  enabled: boolean;
  text: string;
  type: AnnouncementType;
  linkText: string;
  linkUrl: string;
  updatedAt: string;
}

export type ExamApprovalActionType =
  | "approve_upload"
  | "reject_upload"
  | "approve_delete"
  | "reject_delete";

export type SentinelStatusState = ReturnType<typeof getCircuitBreakerState>;

export interface EditPassageFormItem {
  id?: string;
  title: string;
  section_type: string;
  content: string;
  sort_order: number;
}

export interface EditExamFormData {
  id: string;
  title: string;
  category_id: string;
  year: number;
  exam_type: string;
  duration_minutes: number;
  total_score: number;
  pass_score: number;
  passages: EditPassageFormItem[];
}

export interface ImportQuestionInput {
  id?: string;
  q_type?: string;
  stem?: string;
  options?: RawQuestionOptions;
  correct_answer?: string;
  explanation?: string;
  points?: number | null;
  sort_order?: number;
}

export interface ImportPassageInput {
  id?: string;
  section_type?: string;
  title?: string;
  content?: string;
  sort_order?: number;
  questions?: ImportQuestionInput[];
}

export interface ImportExamInput {
  title?: string;
  category_id?: string;
  year?: number;
  exam_type?: string;
  duration_minutes?: number;
  total_score?: number;
  pass_score?: number | null;
  passages?: ImportPassageInput[];
}

export type AdminSaveExamRpcResult = {
  passages_count?: number;
  questions_count?: number;
} | null;

export function getAdminErrorMessage(err: unknown, fallback: string): string {
  if (err instanceof Error && err.message) return err.message;
  if (typeof err === "object" && err !== null && "message" in err) {
    const msg = (err as { message?: unknown }).message;
    if (typeof msg === "string" && msg) return msg;
  }
  return fallback;
}

/**
 * 0-WebSocket presence check: 20-minute window aligned with client throttled heartbeat.
 */
export function isUserOnline(
  u: Pick<UserProfile, "last_active_at"> | null | undefined
): boolean {
  if (!u?.last_active_at) return false;
  const diff = Date.now() - new Date(u.last_active_at).getTime();
  return diff >= 0 && diff <= 20 * 60 * 1000;
}

export function formatRelativeTime(isoString?: string | null): string {
  if (!isoString) return "从未在线";
  const date = new Date(isoString);
  const diffMs = Date.now() - date.getTime();
  if (diffMs < 0 || Number.isNaN(diffMs)) return "刚刚 (在线)";
  const diffSec = Math.floor(diffMs / 1000);
  if (diffSec < 60) return "刚刚 (在线)";
  const diffMin = Math.floor(diffSec / 60);
  if (diffMin <= 5) return "刚刚 (在线)";
  if (diffMin < 60) return `${diffMin}分钟前`;
  const diffHour = Math.floor(diffMin / 60);
  if (diffHour < 24) return `${diffHour}小时前`;
  const diffDay = Math.floor(diffHour / 24);
  if (diffDay < 30) return `${diffDay}天前`;
  return date.toLocaleDateString();
}

export function normalizeAnnouncementType(val: unknown): AnnouncementType {
  if (val === "warning" || val === "alert") return val;
  return "info";
}
