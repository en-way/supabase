"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { supabase } from "@/lib/supabase";
import type { AnnouncementType, SystemAnnouncementRow } from "@/types/user";
import {
  Info,
  AlertTriangle,
  AlertCircle,
  X,
  ExternalLink,
  ChevronRight,
} from "lucide-react";

export interface AnnouncementData {
  enabled: boolean;
  text: string;
  type: "info" | "warning" | "alert";
  linkText?: string;
  linkUrl?: string;
  updatedAt?: string;
}

const STORAGE_KEY = "enway_dismissed_announcement_ts";

function getSafeAnnouncementHref(rawUrl?: string): string | null {
  if (!rawUrl) return null;
  const trimmed = rawUrl.trim();
  if (!trimmed) return null;
  if (trimmed.startsWith("/") && !trimmed.startsWith("//") && !trimmed.startsWith("/\\") && !trimmed.includes("\\")) {
    return trimmed;
  }
  try {
    const parsed = new URL(trimmed);
    if (parsed.protocol === "http:" || parsed.protocol === "https:") {
      return parsed.toString();
    }
  } catch {
    return null;
  }
  return null;
}

function normalizeAnnouncementType(raw?: string | null): AnnouncementType {
  if (raw === "warning" || raw === "alert") return raw;
  return "info";
}

interface AnnouncementBannerProps {
  externalData?: SystemAnnouncementRow | null;
}

export default function AnnouncementBanner({ externalData }: AnnouncementBannerProps = {}) {
  const [announcement, setAnnouncement] = useState<AnnouncementData | null>(null);
  const [isDismissed, setIsDismissed] = useState(true);

  const applyAnnouncementData = (data: SystemAnnouncementRow | null) => {
    if (data && data.announcement_enabled && data.announcement_text?.trim()) {
      const item: AnnouncementData = {
        enabled: Boolean(data.announcement_enabled),
        text: data.announcement_text.trim(),
        type: normalizeAnnouncementType(data.announcement_type),
        linkText: data.announcement_link_text?.trim() || "",
        linkUrl: data.announcement_link_url?.trim() || "",
        updatedAt: data.announcement_updated_at || "",
      };

      setAnnouncement(item);

      const dismissedTs = localStorage.getItem(STORAGE_KEY);
      if (dismissedTs && dismissedTs === item.updatedAt) {
        setIsDismissed(true);
      } else {
        setIsDismissed(false);
      }
    } else {
      setAnnouncement(null);
      setIsDismissed(true);
    }
  };

  useEffect(() => {
    if (externalData !== undefined) {
      applyAnnouncementData(externalData);
    }
  }, [externalData]);

  useEffect(() => {
    async function loadAnnouncement() {
      if (externalData !== undefined) return;
      try {
        const { data, error } = await supabase
          .from("system_settings")
          .select(
            "announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at"
          )
          .eq("id", 1)
          .maybeSingle();

        if (error || !data) return;
        applyAnnouncementData(data);
      } catch (err) {
        console.warn("[Announcement] Failed to fetch announcement:", err);
      }
    }

    if (externalData === undefined) {
      loadAnnouncement();
    }

    const handleReopen = () => setIsDismissed(false);
    const handleUpdated = async () => {
      if (externalData !== undefined) return;
      try {
        const { data } = await supabase
          .from("system_settings")
          .select(
            "announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at"
          )
          .eq("id", 1)
          .maybeSingle();
        if (data) applyAnnouncementData(data);
      } catch {}
    };

    window.addEventListener("enway_reopen_announcement", handleReopen);
    if (externalData === undefined) {
      window.addEventListener("enway_announcement_updated", handleUpdated);
    }
    return () => {
      window.removeEventListener("enway_reopen_announcement", handleReopen);
      if (externalData === undefined) {
        window.removeEventListener("enway_announcement_updated", handleUpdated);
      }
    };
  }, [externalData]);

  const handleDismiss = () => {
    if (announcement?.updatedAt) {
      try {
        localStorage.setItem(STORAGE_KEY, announcement.updatedAt);
      } catch {}
    }
    setIsDismissed(true);
    window.dispatchEvent(new CustomEvent("enway_announcement_dismissed"));
  };

  if (!announcement || !announcement.enabled || isDismissed) {
    return null;
  }

  const themeStyles = {
    info: {
      wrapper: "bg-info-soft border-b border-info/20 text-info",
      icon: <Info className="w-3.5 h-3.5 text-info shrink-0" />,
      btn: "bg-info text-primary-fg hover:opacity-90",
      closeBtn: "text-info/70 hover:text-info hover:bg-surface/40",
    },
    warning: {
      wrapper: "bg-warning-soft border-b border-warning/20 text-warning",
      icon: <AlertTriangle className="w-3.5 h-3.5 text-warning shrink-0" />,
      btn: "bg-warning text-primary-fg hover:opacity-90",
      closeBtn: "text-warning/70 hover:text-warning hover:bg-surface/40",
    },
    alert: {
      wrapper: "bg-danger-soft border-b border-danger/20 text-danger",
      icon: <AlertCircle className="w-3.5 h-3.5 text-danger shrink-0" />,
      btn: "bg-danger text-primary-fg hover:opacity-90",
      closeBtn: "text-danger/70 hover:text-danger hover:bg-surface/40",
    },
  }[announcement.type] || {
    wrapper: "bg-info-soft border-b border-info/20 text-info",
    icon: <Info className="w-3.5 h-3.5 text-info shrink-0" />,
    btn: "bg-info text-primary-fg hover:opacity-90",
    closeBtn: "text-info/70 hover:text-info hover:bg-surface/40",
  };

  const safeLinkHref = getSafeAnnouncementHref(announcement.linkUrl);
  const isExternalLink = Boolean(safeLinkHref && /^https?:\/\//i.test(safeLinkHref));

  return (
    <div
      className={`w-full text-xs transition-colors duration-150 relative z-nav ${themeStyles.wrapper} no-print`}
      role="alert"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-2 flex items-center justify-between gap-3">
        <div className="flex items-center gap-2.5 flex-1 min-w-0">
          <div className="flex items-center shrink-0">{themeStyles.icon}</div>

          <p className="font-medium text-xs leading-relaxed truncate select-text text-fg">
            {announcement.text}
          </p>

          {announcement.linkText && safeLinkHref && (
            <div className="shrink-0 ml-1">
              {isExternalLink ? (
                <a
                  href={safeLinkHref}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-semibold transition-opacity ${themeStyles.btn}`}
                >
                  <span>{announcement.linkText}</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              ) : (
                <Link
                  href={safeLinkHref}
                  className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-semibold transition-opacity ${themeStyles.btn}`}
                >
                  <span>{announcement.linkText}</span>
                  <ChevronRight className="w-3 h-3" />
                </Link>
              )}
            </div>
          )}
        </div>

        <button
          type="button"
          onClick={handleDismiss}
          className={`p-1 rounded-sm transition-colors shrink-0 ${themeStyles.closeBtn}`}
          title="关闭通栏提示（可在导航栏小喇叭随时查看）"
          aria-label="关闭公告横幅"
        >
          <X className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
