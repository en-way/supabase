export type UserRole = "student" | "admin" | "super_admin";

export interface UserProfile {
  id: string;
  username: string;
  nickname?: string | null;
  avatar_url?: string | null;
  role: UserRole;
  created_at?: string;
  updated_at?: string;
  last_active_at?: string | null;
}

export type AnnouncementType = "info" | "warning" | "alert";

export interface SystemAnnouncementRow {
  announcement_enabled?: boolean | null;
  announcement_text?: string | null;
  announcement_type?: string | null;
  announcement_link_text?: string | null;
  announcement_link_url?: string | null;
  announcement_updated_at?: string | null;
}

export interface PasswordResetRequestRecord {
  id: string;
  user_id?: string;
  username?: string;
  nickname?: string | null;
  role?: UserRole;
  status: "pending" | "approved" | "rejected" | "canceled";
  created_at: string;
  reviewed_at?: string | null;
  review_note?: string | null;
}
