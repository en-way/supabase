"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { supabase } from "@/lib/supabase";
import { 
  Info, 
  AlertTriangle, 
  AlertCircle, 
  X, 
  ExternalLink, 
  ChevronRight,
  Megaphone
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

export default function AnnouncementBanner() {
  const [announcement, setAnnouncement] = useState<AnnouncementData | null>(null);
  const [isDismissed, setIsDismissed] = useState(true);

  useEffect(() => {
    async function loadAnnouncement() {
      try {
        const { data, error } = await supabase
          .from("system_settings")
          .select("announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at")
          .eq("id", 1)
          .maybeSingle();

        if (error || !data) return;

        if (data.announcement_enabled && data.announcement_text?.trim()) {
          const item: AnnouncementData = {
            enabled: Boolean(data.announcement_enabled),
            text: data.announcement_text.trim(),
            type: (data.announcement_type as any) || "info",
            linkText: data.announcement_link_text?.trim() || "",
            linkUrl: data.announcement_link_url?.trim() || "",
            updatedAt: data.announcement_updated_at || "",
          };

          setAnnouncement(item);

          // Check if user previously dismissed this exact version
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
      } catch (err) {
        console.warn("[Announcement] Failed to fetch announcement:", err);
      }
    }

    loadAnnouncement();

    // Listen for custom broadcast events when announcement is updated or reopened from Navbar
    const handleReopen = () => setIsDismissed(false);
    window.addEventListener("enway_reopen_announcement", handleReopen);
    window.addEventListener("enway_announcement_updated", loadAnnouncement);
    return () => {
      window.removeEventListener("enway_reopen_announcement", handleReopen);
      window.removeEventListener("enway_announcement_updated", loadAnnouncement);
    };
  }, []);

  const handleDismiss = () => {
    if (announcement?.updatedAt) {
      try {
        localStorage.setItem(STORAGE_KEY, announcement.updatedAt);
      } catch {}
    }
    setIsDismissed(true);
    // Notify Navbar that top banner is collapsed (so it can display the folded horn icon)
    window.dispatchEvent(new CustomEvent("enway_announcement_dismissed"));
  };

  if (!announcement || !announcement.enabled || isDismissed) {
    return null;
  }

  // Theme styling based on level (modern muted palette in light, glowing cyber neon in dark)
  const themeStyles = {
    info: {
      wrapper: "bg-blue-50/70 dark:bg-cyan-950/40 border-b border-blue-100/80 dark:border-cyan-500/20 text-blue-900 dark:text-cyan-200",
      badge: "bg-blue-600 dark:bg-cyan-500 text-white dark:text-[#090a0f]",
      icon: <Info className="w-3.5 h-3.5 text-blue-600 dark:text-cyan-400 shrink-0" />,
      btn: "bg-blue-600 hover:bg-blue-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-[#090a0f] shadow-subtle",
      closeBtn: "text-blue-400 dark:text-cyan-400 hover:text-blue-800 dark:hover:text-cyan-200 hover:bg-blue-100/60 dark:hover:bg-cyan-900/40",
    },
    warning: {
      wrapper: "bg-amber-50/70 dark:bg-amber-950/40 border-b border-amber-100/80 dark:border-amber-500/20 text-amber-900 dark:text-amber-200",
      badge: "bg-amber-600 dark:bg-amber-500 text-white dark:text-[#090a0f]",
      icon: <AlertTriangle className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400 shrink-0" />,
      btn: "bg-amber-600 hover:bg-amber-700 dark:bg-amber-500 dark:hover:bg-amber-400 text-white dark:text-[#090a0f] shadow-subtle",
      closeBtn: "text-amber-400 dark:text-amber-400 hover:text-amber-800 dark:hover:text-amber-200 hover:bg-amber-100/60 dark:hover:bg-amber-900/40",
    },
    alert: {
      wrapper: "bg-rose-50/70 dark:bg-rose-950/40 border-b border-rose-100/80 dark:border-rose-500/20 text-rose-900 dark:text-rose-200",
      badge: "bg-rose-600 dark:bg-rose-500 text-white dark:text-[#090a0f]",
      icon: <AlertCircle className="w-3.5 h-3.5 text-rose-600 dark:text-rose-400 shrink-0" />,
      btn: "bg-rose-600 hover:bg-rose-700 dark:bg-rose-500 dark:hover:bg-rose-400 text-white dark:text-[#090a0f] shadow-subtle",
      closeBtn: "text-rose-400 dark:text-rose-400 hover:text-rose-800 dark:hover:text-rose-200 hover:bg-rose-100/60 dark:hover:bg-rose-900/40",
    },
  }[announcement.type] || {
    wrapper: "bg-blue-50/70 dark:bg-cyan-950/40 border-b border-blue-100/80 dark:border-cyan-500/20 text-blue-900 dark:text-cyan-200",
    badge: "bg-blue-600 dark:bg-cyan-500 text-white dark:text-[#090a0f]",
    icon: <Info className="w-3.5 h-3.5 text-blue-600 dark:text-cyan-400 shrink-0" />,
    btn: "bg-blue-600 hover:bg-blue-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-[#090a0f] shadow-subtle",
    closeBtn: "text-blue-400 dark:text-cyan-400 hover:text-blue-800 dark:hover:text-cyan-200 hover:bg-blue-100/60 dark:hover:bg-cyan-900/40",
  };

  const isExternalLink = announcement.linkUrl?.startsWith("http");

  return (
    <div
      className={`w-full text-xs transition-all duration-200 relative z-50 ${themeStyles.wrapper} no-print`}
      role="alert"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-2 flex items-center justify-between gap-3">
        <div className="flex items-center space-x-2.5 flex-1 min-w-0">
          <div className="flex items-center space-x-1 shrink-0">
            {themeStyles.icon}
          </div>

          <p className="font-medium text-xs leading-relaxed truncate select-text">
            {announcement.text}
          </p>

          {announcement.linkText && announcement.linkUrl && (
            <div className="shrink-0 ml-2">
              {isExternalLink ? (
                <a
                  href={announcement.linkUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold transition-colors ${themeStyles.btn}`}
                >
                  <span>{announcement.linkText}</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              ) : (
                <Link
                  href={announcement.linkUrl}
                  className={`inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold transition-colors ${themeStyles.btn}`}
                >
                  <span>{announcement.linkText}</span>
                  <ChevronRight className="w-3 h-3" />
                </Link>
              )}
            </div>
          )}
        </div>

        {/* Close / Dismiss Button */}
        <button
          onClick={handleDismiss}
          className={`p-1 rounded-md transition-colors shrink-0 ${themeStyles.closeBtn}`}
          title="关闭通栏提示（可在导航栏小喇叭随时查看）"
        >
          <X className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
