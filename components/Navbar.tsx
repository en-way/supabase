"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { 
  clearLocalData, 
  uploadBackupToCloud 
} from "@/lib/storage";
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
  Loader2,
  Megaphone,
  ChevronRight,
  Sun,
  Moon
} from "lucide-react";
import AnnouncementBanner from "@/components/AnnouncementBanner";

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  // Theme State
  const [isDark, setIsDark] = useState(false);

  // Logout Confirmation Dialog State
  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  // Sitewide announcement dropdown state
  const [activeAnnouncement, setActiveAnnouncement] = useState<any>(null);
  const [showAnnouncementDetail, setShowAnnouncementDetail] = useState(false);

  // Initialize theme state from html class
  useEffect(() => {
    const isDarkMode = document.documentElement.classList.contains("dark");
    setIsDark(isDarkMode);
  }, []);

  const toggleTheme = () => {
    const nextIsDark = !isDark;
    setIsDark(nextIsDark);
    if (nextIsDark) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("enway_theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("enway_theme", "light");
    }
  };

  useEffect(() => {
    async function loadAnnouncement() {
      try {
        const { data } = await supabase
          .from("system_settings")
          .select("announcement_enabled, announcement_text, announcement_type, announcement_link_text, announcement_link_url, announcement_updated_at")
          .eq("id", 1)
          .maybeSingle();
        if (data && data.announcement_enabled && data.announcement_text?.trim()) {
          setActiveAnnouncement(data);
        } else {
          setActiveAnnouncement(null);
        }
      } catch {}
    }
    loadAnnouncement();

    async function loadUser() {
      try {
        const { data: { user } } = await supabase.auth.getUser();
        setUser(user);
        if (user) {
          const { data } = await supabase
            .from("profiles")
            .select("id, username, nickname, role")
            .eq("id", user.id)
            .maybeSingle();
          if (data) {
            setProfile(data);
          } else if (user.user_metadata) {
            setProfile({
              username: user.user_metadata.username || user.email?.split("@")[0],
              nickname: user.user_metadata.nickname || user.user_metadata.username,
              role: "student",
            });
          }
        }
      } catch (e) {
        console.error("Error loading user profile", e);
      } finally {
        setLoading(false);
      }
    }
    loadUser();

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_, session) => {
      if (session?.user) {
        setUser(session.user);
        loadUser();
      } else {
        setUser(null);
        setProfile(null);
      }
    });

    const handleProfileUpdate = () => {
      loadUser();
    };
    window.addEventListener("enway_profile_updated", handleProfileUpdate);
    window.addEventListener("enway_announcement_updated", loadAnnouncement);

    return () => {
      subscription.unsubscribe();
      window.removeEventListener("enway_profile_updated", handleProfileUpdate);
      window.removeEventListener("enway_announcement_updated", loadAnnouncement);
    };
  }, []);

  // Execute logout with optional cloud backup and local cache clearance
  const handleConfirmLogout = async (backupFirst: boolean) => {
    setIsLoggingOut(true);
    try {
      if (backupFirst) {
        await uploadBackupToCloud();
      }
      // Strictly clear local device data per user request to isolate accounts
      clearLocalData("all");
      await supabase.auth.signOut();
      setShowLogoutModal(false);
      router.push("/login");
    } catch (err) {
      console.error("Logout error", err);
      // Fallback
      clearLocalData("all");
      await supabase.auth.signOut();
      setShowLogoutModal(false);
      router.push("/login");
    } finally {
      setIsLoggingOut(false);
    }
  };

  if (pathname === "/login") return null;

  const isAnyAdmin = profile?.role === "admin" || profile?.role === "super_admin";

  return (
    <>
      <AnnouncementBanner externalData={activeAnnouncement} />
      <header className="sticky top-0 z-40 w-full border-b border-black/[0.06] dark:border-cyan-500/15 bg-white/80 dark:bg-[#090a0f]/80 backdrop-blur-xl transition-all duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between h-16">
          {/* Brand Logo */}
          <div className="flex items-center space-x-7">
            <Link href="/" className="flex items-center space-x-2.5 group">
              <div className="w-8 h-8 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] flex items-center justify-center font-bold shadow-subtle dark:shadow-glow-cyan group-hover:scale-105 transition-all duration-200">
                <BookOpen className="w-4 h-4" />
              </div>
              <div className="flex flex-col">
                <span className="text-base font-black tracking-tight text-stone-900 dark:text-zinc-100 leading-none group-hover:text-emerald-700 dark:group-hover:text-cyber-400 transition-colors">
                  ENWAY
                </span>
                <span className="text-[10px] text-stone-400 dark:text-zinc-500 font-medium tracking-wider mt-0.5">
                  真题研习 · 全真模考
                </span>
              </div>
            </Link>

            {/* Navigation Links (Micro-capsule style) */}
            <nav className="hidden md:flex items-center space-x-1 bg-stone-100/80 dark:bg-zinc-900/80 p-1 rounded-xl border border-black/[0.04] dark:border-cyan-500/20">
              <Link
                href="/"
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
                  pathname === "/" 
                    ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-subtle dark:shadow-glow-cyan" 
                    : "text-stone-600 dark:text-zinc-400 hover:text-stone-950 dark:hover:text-zinc-100 hover:bg-white/60 dark:hover:bg-zinc-800/50"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <FileText className="w-3.5 h-3.5 opacity-70" />
                  <span>真题大厅</span>
                </span>
              </Link>

              <Link
                href="/mistakes"
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
                  pathname.startsWith("/mistakes") 
                    ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-subtle dark:shadow-glow-cyan" 
                    : "text-stone-600 dark:text-zinc-400 hover:text-stone-950 dark:hover:text-zinc-100 hover:bg-white/60 dark:hover:bg-zinc-800/50"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <AlertCircle className="w-3.5 h-3.5 text-amber-500 opacity-80" />
                  <span>智能错题集</span>
                </span>
              </Link>

              <Link
                href="/vocabulary"
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
                  pathname.startsWith("/vocabulary") 
                    ? "bg-white dark:bg-zinc-800 text-emerald-800 dark:text-cyber-300 shadow-subtle dark:shadow-glow-cyan" 
                    : "text-stone-600 dark:text-zinc-400 hover:text-stone-950 dark:hover:text-zinc-100 hover:bg-white/60 dark:hover:bg-zinc-800/50"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <Bookmark className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400 opacity-80" />
                  <span>核心词汇库</span>
                </span>
              </Link>

              {isAnyAdmin && (
                <Link
                  href="/admin"
                  className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
                    pathname.startsWith("/admin") 
                      ? "bg-purple-50 dark:bg-purple-950/50 text-purple-800 dark:text-purple-300 shadow-subtle" 
                      : "text-purple-600 dark:text-purple-400 hover:text-purple-900 dark:hover:text-purple-200 hover:bg-purple-50/50 dark:hover:bg-purple-950/30"
                  }`}
                >
                  <span className="flex items-center space-x-1.5">
                    <Shield className="w-3.5 h-3.5" />
                    <span>考务与题库</span>
                  </span>
                </Link>
              )}
            </nav>
          </div>

          {/* User Status / Theme Switch / Actions */}
          <div className="flex items-center space-x-2">
            {/* Theme Toggle Capsule Button */}
            <button
              type="button"
              onClick={toggleTheme}
              title={isDark ? "切换为晨曦自然明亮模式" : "切换为深空极光科幻模式"}
              className="p-2 rounded-xl border border-black/[0.06] dark:border-cyan-500/25 bg-white dark:bg-[#11131a] text-stone-600 dark:text-cyber-400 hover:text-stone-950 dark:hover:text-cyber-200 shadow-subtle hover:shadow-card active:scale-[0.96] transition-all duration-200"
            >
              {isDark ? (
                <Sun className="w-4 h-4 text-amber-400 transition-transform duration-300 rotate-0" />
              ) : (
                <Moon className="w-4 h-4 text-emerald-700 transition-transform duration-300 rotate-0" />
              )}
            </button>

            {/* Sitewide Announcement Megaphone (Folded Access) */}
            {activeAnnouncement?.announcement_enabled && activeAnnouncement?.announcement_text?.trim() && (
              <div className="relative">
                <button
                  onClick={() => setShowAnnouncementDetail(!showAnnouncementDetail)}
                  className={`relative p-2 rounded-xl border transition-all duration-150 ${
                    showAnnouncementDetail
                      ? "bg-stone-900 dark:bg-cyber-500 text-white dark:text-[#090a0f] border-stone-900 dark:border-cyber-400 shadow-subtle"
                      : "bg-white dark:bg-[#11131a] border-black/[0.06] dark:border-cyan-500/25 text-stone-600 dark:text-zinc-400 hover:text-stone-950 dark:hover:text-cyber-300 shadow-subtle"
                  }`}
                  title="全站公告通知"
                >
                  <Megaphone className="w-4 h-4" />
                  <span className="absolute -top-0.5 -right-0.5 flex h-2 w-2">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2 w-2 bg-amber-500"></span>
                  </span>
                </button>

                {showAnnouncementDetail && (
                  <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white/95 dark:bg-[#11131a]/95 backdrop-blur-2xl rounded-2xl shadow-float border border-black/[0.08] dark:border-cyan-500/25 p-4 text-stone-900 dark:text-zinc-100 z-50 animate-in fade-in zoom-in-95 duration-150 text-left">
                    <div className="flex items-center justify-between border-b border-stone-100 dark:border-zinc-800 pb-2.5 mb-3">
                      <div className="flex items-center space-x-2">
                        <div className="w-7 h-7 rounded-lg bg-stone-100 dark:bg-zinc-800 text-stone-800 dark:text-cyber-400 flex items-center justify-center font-bold">
                          <Megaphone className="w-4 h-4" />
                        </div>
                        <div>
                          <h4 className="text-xs font-bold text-stone-900 dark:text-zinc-100">全站公告</h4>
                          <span className="text-[10px] text-stone-400 dark:text-zinc-500">来自超级管理员</span>
                        </div>
                      </div>
                      <button
                        onClick={() => setShowAnnouncementDetail(false)}
                        className="p-1 rounded-lg text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-300 hover:bg-stone-100 dark:hover:bg-zinc-800 transition-colors"
                      >
                        <X className="w-4 h-4" />
                      </button>
                    </div>

                    <div className="text-xs font-medium text-stone-800 dark:text-zinc-200 leading-relaxed whitespace-pre-wrap select-text bg-stone-50/80 dark:bg-zinc-900/80 p-3 rounded-xl border border-black/[0.04] dark:border-cyan-500/10 mb-3">
                      {activeAnnouncement.announcement_text}
                    </div>

                    <div className="flex items-center justify-between pt-1">
                      <button
                        onClick={() => {
                          window.dispatchEvent(new CustomEvent("enway_reopen_announcement"));
                          setShowAnnouncementDetail(false);
                        }}
                        className="text-[11px] text-stone-600 dark:text-zinc-400 hover:text-emerald-700 dark:hover:text-cyber-400 font-semibold hover:underline"
                      >
                        在顶部重新展示横幅
                      </button>

                      {activeAnnouncement.announcement_link_text && activeAnnouncement.announcement_link_url && (
                        <a
                          href={activeAnnouncement.announcement_link_url}
                          target={activeAnnouncement.announcement_link_url.startsWith("http") ? "_blank" : undefined}
                          rel="noopener noreferrer"
                          className="px-3 py-1 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] rounded-lg text-xs font-bold flex items-center space-x-1 shadow-subtle transition-all"
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
              <div className="h-8 w-20 bg-stone-100 dark:bg-zinc-800 animate-pulse rounded-lg" />
            ) : user ? (
              <div className="flex items-center space-x-1.5">
                <Link
                  href="/profile"
                  className="flex items-center space-x-2 px-3 py-1.5 rounded-full bg-white dark:bg-[#11131a] border border-black/[0.06] dark:border-cyan-500/25 hover:border-black/[0.14] dark:hover:border-cyan-500/50 shadow-subtle hover:shadow-card transition-all duration-150"
                >
                  <div className="w-5 h-5 rounded-full bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] flex items-center justify-center text-[10px] font-bold">
                    {profile?.nickname?.[0] || profile?.username?.[0] || "U"}
                  </div>
                  <div className="text-left flex items-center space-x-1.5">
                    <span className="text-xs font-semibold text-stone-900 dark:text-zinc-100 leading-tight">
                      {profile?.nickname || profile?.username}
                    </span>
                    <span className="text-[10px] text-stone-400 dark:text-zinc-500 font-mono leading-tight">
                      {profile?.role === "super_admin" 
                        ? "👑 超管" 
                        : profile?.role === "admin" 
                        ? "🛡️ 管理" 
                        : ""}
                    </span>
                  </div>
                </Link>

                <button
                  onClick={() => setShowLogoutModal(true)}
                  title="安全退出系统"
                  className="p-2 text-stone-400 dark:text-zinc-500 hover:text-rose-600 hover:bg-rose-50/80 dark:hover:bg-rose-950/40 rounded-full transition-colors"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            ) : (
              <Link
                href="/login"
                className="px-4 py-1.5 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] text-xs font-bold rounded-full shadow-subtle hover:shadow-card active:scale-[0.98] transition-all duration-150"
              >
                考生登录 / 注册
              </Link>
            )}
          </div>
        </div>
      </header>

      {/* Logout Confirmation Dialog (Local data clearance & backup) */}
      {showLogoutModal && (
        <div className="fixed inset-0 z-50 bg-black/40 dark:bg-black/70 backdrop-blur-md flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-white/95 dark:bg-[#11131a]/95 backdrop-blur-2xl rounded-2xl max-w-sm w-full p-6 shadow-float border border-black/[0.08] dark:border-cyan-500/25 space-y-4">
            <div className="flex items-start justify-between">
              <div className="flex items-center space-x-3 text-stone-900 dark:text-zinc-100">
                <div className="w-9 h-9 rounded-xl bg-amber-50 dark:bg-amber-950/50 text-amber-600 dark:text-amber-400 flex items-center justify-center font-bold">
                  <LogOut className="w-4 h-4" />
                </div>
                <div>
                  <h3 className="font-bold text-sm text-stone-900 dark:text-zinc-100">安全退出系统</h3>
                  <p className="text-[11px] text-stone-400 dark:text-zinc-500">学习档案云端同步与终端隔离</p>
                </div>
              </div>
              <button
                onClick={() => setShowLogoutModal(false)}
                disabled={isLoggingOut}
                className="text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-300 p-1 rounded-lg transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <p className="text-xs text-stone-600 dark:text-zinc-400 leading-relaxed">
              为保障考场环境与个人学习进度安全，退出时将清除本终端本地缓存。请选择退出方式：
            </p>

            <div className="space-y-2 pt-1">
              <button
                onClick={() => handleConfirmLogout(true)}
                disabled={isLoggingOut}
                className="w-full py-2.5 px-4 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 text-white dark:text-[#090a0f] rounded-xl text-xs font-bold shadow-subtle flex items-center justify-center space-x-2 transition-all duration-150 active:scale-[0.98] disabled:opacity-50"
              >
                {isLoggingOut ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <>
                    <CloudUpload className="w-4 h-4 text-emerald-100 dark:text-[#090a0f]" />
                    <span>同步档案至云端并退出</span>
                  </>
                )}
              </button>

              <button
                onClick={() => handleConfirmLogout(false)}
                disabled={isLoggingOut}
                className="w-full py-2.5 px-4 bg-stone-100 dark:bg-zinc-800 hover:bg-stone-200/80 dark:hover:bg-zinc-700 text-stone-700 dark:text-zinc-300 rounded-xl text-xs font-semibold flex items-center justify-center space-x-2 transition-all duration-150 disabled:opacity-50"
              >
                <Trash2 className="w-3.5 h-3.5 text-stone-400 dark:text-zinc-500" />
                <span>仅清除本地缓存退出</span>
              </button>

              <button
                onClick={() => setShowLogoutModal(false)}
                disabled={isLoggingOut}
                className="w-full py-1.5 text-xs font-medium text-stone-400 dark:text-zinc-500 hover:text-stone-700 dark:hover:text-zinc-300 text-center transition-colors"
              >
                取消返回
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
