"use client";

import { useState, useEffect, useRef } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import type { User as AuthUser } from "@supabase/supabase-js";
import type { UserProfile, SystemAnnouncementRow } from "@/types/user";
import {
  clearLocalData,
  uploadBackupToCloud,
  setLastLocalUserId,
} from "@/lib/storage";
import { clearPendingSubmissionTasks } from "@/lib/submissionQueue";
import { useDismiss } from "@/hooks/useDismiss";
import { Modal } from "@/components/ui/Modal";
import { BottomSheet } from "@/components/ui/BottomSheet";
import { Button } from "@/components/ui/Button";
import {
  BookOpen,
  User,
  LogOut,
  Shield,
  FileText,
  AlertCircle,
  Bookmark,
  CloudUpload,
  Trash2,
  X,
  Megaphone,
  ChevronRight,
  Sun,
  Moon,
} from "lucide-react";
import AnnouncementBanner from "@/components/AnnouncementBanner";

function getSafeAnnouncementHref(rawUrl?: string | null): string | null {
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

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<AuthUser | null>(null);
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);

  const [isDark, setIsDark] = useState(false);

  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [isLoggingOut, setIsLoggingOut] = useState(false);
  const [showMobileUserMenu, setShowMobileUserMenu] = useState(false);

  const [activeAnnouncement, setActiveAnnouncement] = useState<SystemAnnouncementRow | null>(null);
  const [showAnnouncementDetail, setShowAnnouncementDetail] = useState(false);
  const announcementRef = useRef<HTMLDivElement>(null);

  useDismiss(showAnnouncementDetail, () => setShowAnnouncementDetail(false), announcementRef);

  useEffect(() => {
    const isDarkMode = document.documentElement.classList.contains("dark");
    setIsDark(isDarkMode);
  }, []);

  const toggleTheme = () => {
    const nextIsDark = !isDark;
    setIsDark(nextIsDark);
    if (nextIsDark) {
      document.documentElement.classList.add("dark");
      try {
        localStorage.setItem("enway_theme", "dark");
      } catch {}
    } else {
      document.documentElement.classList.remove("dark");
      try {
        localStorage.setItem("enway_theme", "light");
      } catch {}
    }
  };

  useEffect(() => {
    let isMounted = true;
    const NAV_ANNOUNCEMENT_CACHE_KEY = "enway_cached_nav_announcement";
    const NAV_PROFILE_CACHE_PREFIX = "enway_cached_nav_profile_";
    const NAV_CACHE_TTL = 60 * 60 * 1000;

    async function loadAnnouncement(forceRefresh = false) {
      if (!forceRefresh && typeof window !== "undefined") {
        try {
          const raw = sessionStorage.getItem(NAV_ANNOUNCEMENT_CACHE_KEY);
          if (raw) {
            const { data, timestamp } = JSON.parse(raw);
            if (Date.now() - timestamp < NAV_CACHE_TTL) {
              if (!isMounted) return;
              if (data && data.announcement_enabled && data.announcement_text?.trim()) {
                setActiveAnnouncement(data);
              } else {
                setActiveAnnouncement(null);
              }
              return;
            }
          }
        } catch {}
      }

      try {
        const { data } = await supabase
          .from("system_settings")
          .select(
            "announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at"
          )
          .eq("id", 1)
          .maybeSingle();

        if (typeof window !== "undefined") {
          try {
            sessionStorage.setItem(
              NAV_ANNOUNCEMENT_CACHE_KEY,
              JSON.stringify({ data, timestamp: Date.now() })
            );
          } catch {}
        }

        if (!isMounted) return;
        if (data && data.announcement_enabled && data.announcement_text?.trim()) {
          setActiveAnnouncement(data);
        } else {
          setActiveAnnouncement(null);
        }
      } catch {}
    }
    loadAnnouncement();

    let isFetchingUser = false;
    let pendingReload = false;
    let pendingForce = false;

    async function loadUser(forceRefresh = false) {
      if (!isMounted) return;
      if (isFetchingUser) {
        pendingReload = true;
        if (forceRefresh) pendingForce = true;
        return;
      }
      isFetchingUser = true;
      try {
        const {
          data: { session },
        } = await supabase.auth.getSession();
        if (!isMounted) return;
        const currentUser = session?.user || null;
        setUser(currentUser);

        if (currentUser) {
          const profileCacheKey = `${NAV_PROFILE_CACHE_PREFIX}${currentUser.id}`;
          if (!forceRefresh && typeof window !== "undefined") {
            try {
              const cached = sessionStorage.getItem(profileCacheKey);
              if (cached) {
                const { data, timestamp } = JSON.parse(cached);
                if (Date.now() - timestamp < NAV_CACHE_TTL) {
                  if (isMounted) setProfile(data);
                  return;
                }
              }
            } catch {}
          }

          const { data } = await supabase
            .from("profiles")
            .select("id, username, nickname, role")
            .eq("id", currentUser.id)
            .maybeSingle();

          if (!isMounted) return;
          if (data) {
            const profileRow = data as UserProfile;
            setProfile(profileRow);
            if (typeof window !== "undefined") {
              try {
                sessionStorage.setItem(
                  profileCacheKey,
                  JSON.stringify({ data: profileRow, timestamp: Date.now() })
                );
              } catch {}
            }
          } else if (currentUser.user_metadata) {
            const fallbackProfile: UserProfile = {
              id: currentUser.id,
              username: String(currentUser.user_metadata.username || currentUser.email?.split("@")[0] || "user"),
              nickname: currentUser.user_metadata.nickname || currentUser.user_metadata.username || null,
              role: "student",
            };
            setProfile(fallbackProfile);
            if (typeof window !== "undefined") {
              try {
                sessionStorage.setItem(
                  profileCacheKey,
                  JSON.stringify({ data: fallbackProfile, timestamp: Date.now() })
                );
              } catch {}
            }
          }
        } else {
          setProfile(null);
        }
      } catch (e) {
        if (isMounted) {
          console.error("Error loading user profile", e);
        }
      } finally {
        isFetchingUser = false;
        if (isMounted) {
          setLoading(false);
          if (pendingReload) {
            const nextForce = pendingForce;
            pendingReload = false;
            pendingForce = false;
            loadUser(nextForce);
          }
        }
      }
    }
    loadUser();

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((event, session) => {
      if (!isMounted) return;
      if (session?.user) {
        setUser(session.user);
        if (event === "SIGNED_IN" || event === "USER_UPDATED") {
          loadUser(true);
        }
      } else {
        setUser(null);
        setProfile(null);
      }
    });

    const handleProfileUpdate = () => {
      loadUser(true);
    };
    const handleAnnouncementUpdate = () => {
      loadAnnouncement(true);
    };

    window.addEventListener("enway_profile_updated", handleProfileUpdate);
    window.addEventListener("enway_announcement_updated", handleAnnouncementUpdate);

    return () => {
      isMounted = false;
      subscription.unsubscribe();
      window.removeEventListener("enway_profile_updated", handleProfileUpdate);
      window.removeEventListener("enway_announcement_updated", handleAnnouncementUpdate);
    };
  }, []);

  const cleanupLocalSessionData = () => {
    clearLocalData("all");
    clearPendingSubmissionTasks();
    setLastLocalUserId(null);
    if (typeof window !== "undefined") {
      try {
        localStorage.removeItem("enway_last_presence_touch");
      } catch {}
      try {
        sessionStorage.removeItem("enway_cached_nav_announcement");
        sessionStorage.removeItem("enway_last_silent_backup");
        Object.keys(sessionStorage).forEach((k) => {
          if (k.startsWith("enway_cached_nav_profile_")) {
            sessionStorage.removeItem(k);
          }
        });
      } catch {}
    }
  };

  const handleConfirmLogout = async (backupFirst: boolean) => {
    setIsLoggingOut(true);
    try {
      if (backupFirst) {
        const uploadRes = await uploadBackupToCloud();
        if (!uploadRes.success) {
          const confirmForce = window.confirm(
            `⚠️ 学习档案同步至云端未成功（原因: ${uploadRes.error || "网络波动/未完成"}）。\n\n如果此时退出，本终端未同步的学习记录将被清除并可能丢失。\n\n是否仍然强制退出？`
          );
          if (!confirmForce) {
            setIsLoggingOut(false);
            return;
          }
        }
      }
      cleanupLocalSessionData();
      await supabase.auth.signOut();
      setShowLogoutModal(false);
      router.push("/login");
    } catch (err: unknown) {
      console.error("Logout error", err);
      const errMessage = err instanceof Error ? err.message : "网络异常";
      const confirmForce = window.confirm(
        `⚠️ 登出过程遇到异常（${errMessage}）。是否强制清除本地数据并退出？`
      );
      if (!confirmForce) {
        setIsLoggingOut(false);
        return;
      }
      cleanupLocalSessionData();
      await supabase.auth.signOut();
      setShowLogoutModal(false);
      router.push("/login");
    } finally {
      setIsLoggingOut(false);
    }
  };

  const isLoginPage =
    pathname === "/login" || pathname === "/login/" || pathname?.startsWith("/login");
  if (isLoginPage) return null;

  const isAnyAdmin = profile?.role === "admin" || profile?.role === "super_admin";
  const safeAnnouncementHref = getSafeAnnouncementHref(activeAnnouncement?.announcement_link_url);
  const displayName = profile?.nickname || profile?.username || "学员";
  const avatarInitial = displayName[0]?.toUpperCase() || "U";

  return (
    <>
      <AnnouncementBanner externalData={activeAnnouncement} />
      <header className="sticky top-0 z-nav w-full border-b border-border bg-surface/90 backdrop-blur-md transition-colors duration-150">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between h-16">
          {/* Brand Logo + Desktop Nav */}
          <div className="flex items-center gap-7">
            <Link href="/" className="flex items-center gap-2.5 group">
              <div className="w-8 h-8 rounded-md bg-primary text-primary-fg flex items-center justify-center font-bold shadow-1 group-hover:bg-primary-hover transition-colors duration-150">
                <BookOpen className="w-4 h-4" />
              </div>
              <div className="flex flex-col">
                <span className="text-base font-bold tracking-tight text-fg leading-none group-hover:text-primary transition-colors">
                  ENWAY
                </span>
                <span className="text-[10px] text-fg-subtle font-medium tracking-wider mt-0.5">
                  真题研习 · 全真模考
                </span>
              </div>
            </Link>

            <nav className="hidden md:flex items-center gap-1 bg-surface-2 p-1 rounded-md border border-border">
              <Link
                href="/"
                className={`px-3 py-1.5 rounded-sm text-xs font-semibold transition-colors duration-150 ${
                  pathname === "/"
                    ? "bg-surface text-primary shadow-1"
                    : "text-fg-muted hover:text-fg hover:bg-surface/60"
                }`}
              >
                <span className="flex items-center gap-1.5">
                  <FileText className="w-3.5 h-3.5 opacity-80" />
                  <span>真题大厅</span>
                </span>
              </Link>

              <Link
                href="/mistakes"
                className={`px-3 py-1.5 rounded-sm text-xs font-semibold transition-colors duration-150 ${
                  pathname.startsWith("/mistakes")
                    ? "bg-surface text-primary shadow-1"
                    : "text-fg-muted hover:text-fg hover:bg-surface/60"
                }`}
              >
                <span className="flex items-center gap-1.5">
                  <AlertCircle className="w-3.5 h-3.5 text-warning opacity-90" />
                  <span>智能错题集</span>
                </span>
              </Link>

              <Link
                href="/vocabulary"
                className={`px-3 py-1.5 rounded-sm text-xs font-semibold transition-colors duration-150 ${
                  pathname.startsWith("/vocabulary")
                    ? "bg-surface text-primary shadow-1"
                    : "text-fg-muted hover:text-fg hover:bg-surface/60"
                }`}
              >
                <span className="flex items-center gap-1.5">
                  <Bookmark className="w-3.5 h-3.5 text-primary opacity-90" />
                  <span>核心词汇库</span>
                </span>
              </Link>

              {isAnyAdmin && (
                <Link
                  href="/admin"
                  className={`px-3 py-1.5 rounded-sm text-xs font-semibold transition-colors duration-150 ${
                    pathname.startsWith("/admin")
                      ? "bg-primary-soft text-primary-soft-fg shadow-1"
                      : "text-primary hover:bg-primary-soft/60"
                  }`}
                >
                  <span className="flex items-center gap-1.5">
                    <Shield className="w-3.5 h-3.5" />
                    <span>考务与题库</span>
                  </span>
                </Link>
              )}
            </nav>
          </div>

          {/* Right Actions */}
          <div className="flex items-center gap-2">
            {/* Theme Toggle */}
            <button
              type="button"
              onClick={toggleTheme}
              title={isDark ? "切换为暖纸浅色模式" : "切换为护眼深炭模式"}
              aria-label={isDark ? "切换为暖纸浅色模式" : "切换为护眼深炭模式"}
              className="p-2 rounded-md border border-border bg-surface text-fg-muted hover:text-fg hover:bg-surface-2 shadow-1 active:scale-[0.96] transition-colors duration-150"
            >
              {isDark ? (
                <Sun className="w-4 h-4 text-warning" />
              ) : (
                <Moon className="w-4 h-4 text-primary" />
              )}
            </button>

            {/* Sitewide Announcement Megaphone */}
            {activeAnnouncement?.announcement_enabled &&
              activeAnnouncement?.announcement_text?.trim() && (
                <div ref={announcementRef} className="relative">
                  <button
                    type="button"
                    onClick={() => setShowAnnouncementDetail((prev) => !prev)}
                    aria-expanded={showAnnouncementDetail}
                    aria-label="查看全站公告"
                    className={`relative p-2 rounded-md border transition-colors duration-150 ${
                      showAnnouncementDetail
                        ? "bg-primary text-primary-fg border-primary shadow-1"
                        : "bg-surface border-border text-fg-muted hover:text-fg hover:bg-surface-2 shadow-1"
                    }`}
                    title="全站公告通知"
                  >
                    <Megaphone className="w-4 h-4" />
                    <span className="absolute -top-0.5 -right-0.5 h-2 w-2 rounded-full bg-warning ring-2 ring-surface" />
                  </button>

                  {showAnnouncementDetail && (
                    <div
                      role="dialog"
                      aria-label="全站公告详情"
                      className="fixed inset-x-3 top-[calc(var(--nav-h)+0.5rem)] sm:absolute sm:inset-x-auto sm:right-0 sm:top-auto sm:mt-2 sm:w-[22rem] sm:max-w-[calc(100vw-1.5rem)] bg-surface border border-border rounded-lg shadow-pop p-4 text-fg z-dropdown animate-in fade-in zoom-in-95 duration-150 text-left"
                    >
                      <div className="flex items-center justify-between border-b border-border pb-2.5 mb-3">
                        <div className="flex items-center gap-2">
                          <div className="w-7 h-7 rounded-sm bg-primary-soft text-primary-soft-fg flex items-center justify-center">
                            <Megaphone className="w-4 h-4" />
                          </div>
                          <div>
                            <h4 className="text-xs font-bold text-fg">全站公告</h4>
                            <span className="text-[10px] text-fg-subtle">来自超级管理员</span>
                          </div>
                        </div>
                        <button
                          type="button"
                          onClick={() => setShowAnnouncementDetail(false)}
                          aria-label="关闭公告详情"
                          className="p-1 rounded-sm text-fg-subtle hover:text-fg hover:bg-surface-2 transition-colors"
                        >
                          <X className="w-4 h-4" />
                        </button>
                      </div>

                      <div className="text-xs font-medium text-fg leading-relaxed whitespace-pre-wrap select-text bg-surface-2 p-3 rounded-md border border-border mb-3">
                        {activeAnnouncement.announcement_text}
                      </div>

                      <div className="flex items-center justify-between pt-1">
                        <button
                          type="button"
                          onClick={() => {
                            window.dispatchEvent(new CustomEvent("enway_reopen_announcement"));
                            setShowAnnouncementDetail(false);
                          }}
                          className="text-[11px] text-fg-muted hover:text-primary font-semibold hover:underline"
                        >
                          在顶部重新展示横幅
                        </button>

                        {activeAnnouncement.announcement_link_text && safeAnnouncementHref && (
                          <a
                            href={safeAnnouncementHref}
                            target={/^https?:\/\//i.test(safeAnnouncementHref) ? "_blank" : undefined}
                            rel="noopener noreferrer"
                            className="px-3 py-1 bg-primary hover:bg-primary-hover text-primary-fg rounded-md text-xs font-semibold flex items-center gap-1 shadow-1 transition-colors"
                          >
                            <span>{activeAnnouncement.announcement_link_text}</span>
                            <ChevronRight className="w-3.5 h-3.5" />
                          </a>
                        )}
                      </div>
                    </div>
                  )}
                </div>
              )}

            {loading ? (
              <div className="h-9 w-20 bg-surface-2 animate-pulse rounded-md" />
            ) : user ? (
              <>
                {/* Desktop User Pill + Logout */}
                <div className="hidden md:flex items-center gap-1.5">
                  <Link
                    href="/profile"
                    className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-surface border border-border hover:border-border-strong shadow-1 transition-colors duration-150"
                  >
                    <div className="w-5 h-5 rounded-full bg-primary text-primary-fg flex items-center justify-center text-[10px] font-bold">
                      {avatarInitial}
                    </div>
                    <div className="flex items-center gap-1.5">
                      <span className="text-xs font-semibold text-fg leading-tight truncate max-w-[140px]">
                        {displayName}
                      </span>
                      {profile?.role === "super_admin" && (
                        <span className="text-[10px] text-fg-muted font-mono">超管</span>
                      )}
                      {profile?.role === "admin" && (
                        <span className="text-[10px] text-fg-muted font-mono">管理</span>
                      )}
                    </div>
                  </Link>

                  <button
                    type="button"
                    onClick={() => setShowLogoutModal(true)}
                    title="安全退出系统"
                    aria-label="安全退出系统"
                    className="p-2 text-fg-subtle hover:text-danger hover:bg-danger-soft rounded-full transition-colors"
                  >
                    <LogOut className="w-4 h-4" />
                  </button>
                </div>

                {/* Mobile User Trigger (opens BottomSheet with /admin access for admins) */}
                <button
                  type="button"
                  onClick={() => setShowMobileUserMenu(true)}
                  aria-label="打开账户菜单"
                  className="md:hidden flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-surface border border-border shadow-1 active:scale-[0.97] transition-transform"
                >
                  <div className="w-5 h-5 rounded-full bg-primary text-primary-fg flex items-center justify-center text-[10px] font-bold">
                    {avatarInitial}
                  </div>
                  <span className="text-xs font-semibold text-fg max-w-[72px] truncate">
                    {displayName}
                  </span>
                </button>
              </>
            ) : (
              <Link
                href="/login"
                className="px-4 py-1.5 bg-primary hover:bg-primary-hover text-primary-fg text-xs font-semibold rounded-full shadow-1 active:scale-[0.98] transition-colors duration-150"
              >
                考生登录 / 注册
              </Link>
            )}
          </div>
        </div>
      </header>

      {/* Mobile User Menu BottomSheet */}
      <BottomSheet
        open={showMobileUserMenu}
        onClose={() => setShowMobileUserMenu(false)}
        title={displayName}
        subtitle={
          profile?.role === "super_admin"
            ? "超级管理员"
            : profile?.role === "admin"
            ? "考务管理员"
            : "研习学员"
        }
      >
        <div className="space-y-2">
          <Link
            href="/profile"
            onClick={() => setShowMobileUserMenu(false)}
            className="flex items-center justify-between p-3 rounded-md bg-surface-2 hover:bg-surface-3 border border-border transition-colors"
          >
            <span className="flex items-center gap-2.5 text-sm font-semibold text-fg">
              <User className="w-4 h-4 text-primary" />
              <span>个人中心与云端归档</span>
            </span>
            <ChevronRight className="w-4 h-4 text-fg-subtle" />
          </Link>

          {isAnyAdmin && (
            <Link
              href="/admin"
              onClick={() => setShowMobileUserMenu(false)}
              className="flex items-center justify-between p-3 rounded-md bg-primary-soft border border-primary/20 text-primary-soft-fg transition-colors"
            >
              <span className="flex items-center gap-2.5 text-sm font-semibold">
                <Shield className="w-4 h-4" />
                <span>考务与题库管理台</span>
              </span>
              <ChevronRight className="w-4 h-4" />
            </Link>
          )}

          <button
            type="button"
            onClick={() => {
              toggleTheme();
            }}
            className="w-full flex items-center justify-between p-3 rounded-md bg-surface-2 hover:bg-surface-3 border border-border transition-colors"
          >
            <span className="flex items-center gap-2.5 text-sm font-semibold text-fg">
              {isDark ? <Sun className="w-4 h-4 text-warning" /> : <Moon className="w-4 h-4 text-primary" />}
              <span>{isDark ? "切换为暖纸浅色模式" : "切换为护眼深炭模式"}</span>
            </span>
          </button>

          <button
            type="button"
            onClick={() => {
              setShowMobileUserMenu(false);
              setShowLogoutModal(true);
            }}
            className="w-full flex items-center justify-between p-3 rounded-md bg-danger-soft text-danger border border-danger/20 transition-colors"
          >
            <span className="flex items-center gap-2.5 text-sm font-semibold">
              <LogOut className="w-4 h-4" />
              <span>安全退出系统</span>
            </span>
          </button>
        </div>
      </BottomSheet>

      {/* Logout Confirmation Dialog */}
      <Modal
        open={showLogoutModal}
        onClose={() => {
          if (!isLoggingOut) setShowLogoutModal(false);
        }}
        disableClose={isLoggingOut}
        maxWidthClass="max-w-sm"
        title="安全退出系统"
        subtitle="学习档案云端同步与终端隔离"
      >
        <div className="space-y-4">
          <p className="text-xs text-fg-muted leading-relaxed">
            为保障考场环境与个人学习进度安全，退出时将清除本终端本地缓存。请选择退出方式：
          </p>

          <div className="space-y-2">
            <Button
              variant="primary"
              className="w-full"
              loading={isLoggingOut}
              onClick={() => handleConfirmLogout(true)}
            >
              {!isLoggingOut && <CloudUpload className="w-4 h-4" />}
              <span>同步档案至云端并退出</span>
            </Button>

            <Button
              variant="secondary"
              className="w-full"
              disabled={isLoggingOut}
              onClick={() => handleConfirmLogout(false)}
            >
              <Trash2 className="w-3.5 h-3.5 text-fg-muted" />
              <span>仅清除本地缓存退出</span>
            </Button>

            <Button
              variant="ghost"
              size="sm"
              className="w-full"
              disabled={isLoggingOut}
              onClick={() => setShowLogoutModal(false)}
            >
              取消返回
            </Button>
          </div>
        </div>
      </Modal>
    </>
  );
}
