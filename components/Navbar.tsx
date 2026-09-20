"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import { 
  uploadBackupToCloud, 
  clearLocalData 
} from "@/lib/storage";
import { 
  BookOpen, 
  FileText, 
  AlertCircle, 
  Bookmark, 
  Shield, 
  LogOut,
  CloudUpload,
  Trash2,
  X,
  Loader2,
  Megaphone,
  ExternalLink,
  ChevronRight,
  Info,
  AlertTriangle
} from "lucide-react";
import AnnouncementBanner from "@/components/AnnouncementBanner";

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  // Logout Confirmation Dialog State
  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  // Sitewide announcement dropdown state
  const [activeAnnouncement, setActiveAnnouncement] = useState<any>(null);
  const [showAnnouncementDetail, setShowAnnouncementDetail] = useState(false);

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
          const { data, error } = await supabase
            .from("profiles")
            .select("*")
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
  }, [pathname]);

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
      <AnnouncementBanner />
      <header className="sticky top-0 z-40 w-full border-b border-black/[0.06] bg-white/80 backdrop-blur-xl transition-all duration-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between h-16">
          {/* Brand Logo */}
          <div className="flex items-center space-x-7">
            <Link href="/" className="flex items-center space-x-2.5 group">
              <div className="w-8 h-8 rounded-xl bg-zinc-900 text-white flex items-center justify-center font-bold shadow-subtle group-hover:bg-indigo-600 transition-colors duration-200">
                <BookOpen className="w-4 h-4" />
              </div>
              <div className="flex flex-col">
                <span className="text-base font-black tracking-tight text-zinc-900 leading-none group-hover:text-indigo-600 transition-colors">
                  ENWAY
                </span>
                <span className="text-[10px] text-zinc-400 font-medium tracking-wider mt-0.5">
                  真题研习 · 全真模考
                </span>
              </div>
            </Link>

            {/* Navigation Links (Micro-capsule style) */}
            <nav className="hidden md:flex items-center space-x-1 bg-zinc-100/70 p-1 rounded-xl border border-black/[0.03]">
              <Link
                href="/"
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
                  pathname === "/" 
                    ? "bg-white text-zinc-950 shadow-subtle" 
                    : "text-zinc-600 hover:text-zinc-950 hover:bg-white/60"
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
                    ? "bg-white text-zinc-950 shadow-subtle" 
                    : "text-zinc-600 hover:text-zinc-950 hover:bg-white/60"
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
                    ? "bg-white text-zinc-950 shadow-subtle" 
                    : "text-zinc-600 hover:text-zinc-950 hover:bg-white/60"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <Bookmark className="w-3.5 h-3.5 text-emerald-500 opacity-80" />
                  <span>核心词汇库</span>
                </span>
              </Link>

              {isAnyAdmin && (
                <Link
                  href="/admin"
                  className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-150 ${
                    pathname.startsWith("/admin") 
                      ? "bg-purple-50 text-purple-800 shadow-subtle" 
                      : "text-purple-600 hover:text-purple-900 hover:bg-purple-50/50"
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

          {/* User Status / Actions */}
          <div className="flex items-center space-x-2">
            {/* Sitewide Announcement Megaphone (Folded Access) */}
            {activeAnnouncement?.announcement_enabled && activeAnnouncement?.announcement_text?.trim() && (
              <div className="relative">
                <button
                  onClick={() => setShowAnnouncementDetail(!showAnnouncementDetail)}
                  className={`relative p-2 rounded-xl border transition-all duration-150 ${
                    showAnnouncementDetail
                      ? "bg-zinc-900 text-white border-zinc-900 shadow-subtle"
                      : "bg-white border-black/[0.06] text-zinc-600 hover:text-zinc-950 hover:border-black/[0.12] shadow-subtle"
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
                  <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white/95 backdrop-blur-2xl rounded-2xl shadow-float border border-black/[0.08] p-4 text-zinc-900 z-50 animate-in fade-in zoom-in-95 duration-150 text-left">
                    <div className="flex items-center justify-between border-b border-zinc-100 pb-2.5 mb-3">
                      <div className="flex items-center space-x-2">
                        <div className="w-7 h-7 rounded-lg bg-zinc-100 text-zinc-800 flex items-center justify-center font-bold">
                          <Megaphone className="w-4 h-4" />
                        </div>
                        <div>
                          <h4 className="text-xs font-bold text-zinc-900">全站公告</h4>
                          <span className="text-[10px] text-zinc-400">来自超级管理员</span>
                        </div>
                      </div>
                      <button
                        onClick={() => setShowAnnouncementDetail(false)}
                        className="p-1 rounded-lg text-zinc-400 hover:text-zinc-700 hover:bg-zinc-100 transition-colors"
                      >
                        <X className="w-4 h-4" />
                      </button>
                    </div>

                    <div className="text-xs font-medium text-zinc-800 leading-relaxed whitespace-pre-wrap select-text bg-zinc-50/80 p-3 rounded-xl border border-black/[0.04] mb-3">
                      {activeAnnouncement.announcement_text}
                    </div>

                    <div className="flex items-center justify-between pt-1">
                      <button
                        onClick={() => {
                          window.dispatchEvent(new CustomEvent("enway_reopen_announcement"));
                          setShowAnnouncementDetail(false);
                        }}
                        className="text-[11px] text-zinc-600 hover:text-zinc-900 font-semibold hover:underline"
                      >
                        在顶部重新展示横幅
                      </button>

                      {activeAnnouncement.announcement_link_text && activeAnnouncement.announcement_link_url && (
                        <a
                          href={activeAnnouncement.announcement_link_url}
                          target={activeAnnouncement.announcement_link_url.startsWith("http") ? "_blank" : undefined}
                          rel="noopener noreferrer"
                          className="px-3 py-1 bg-zinc-900 hover:bg-zinc-800 text-white rounded-lg text-xs font-bold flex items-center space-x-1 shadow-subtle transition-all"
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
              <div className="h-8 w-20 bg-zinc-100 animate-pulse rounded-lg" />
            ) : user ? (
              <div className="flex items-center space-x-1.5">
                <Link
                  href="/profile"
                  className="flex items-center space-x-2 px-3 py-1.5 rounded-full bg-white border border-black/[0.06] hover:border-black/[0.14] shadow-subtle hover:shadow-card transition-all duration-150"
                >
                  <div className="w-5 h-5 rounded-full bg-zinc-900 text-white flex items-center justify-center text-[10px] font-bold">
                    {profile?.nickname?.[0] || profile?.username?.[0] || "U"}
                  </div>
                  <div className="text-left flex items-center space-x-1.5">
                    <span className="text-xs font-semibold text-zinc-900 leading-tight">
                      {profile?.nickname || profile?.username}
                    </span>
                    <span className="text-[10px] text-zinc-400 font-mono leading-tight">
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
                  className="p-2 text-zinc-400 hover:text-rose-600 hover:bg-rose-50/80 rounded-full transition-colors"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            ) : (
              <Link
                href="/login"
                className="px-4 py-1.5 bg-zinc-900 hover:bg-zinc-800 text-white text-xs font-bold rounded-full shadow-subtle hover:shadow-card active:scale-[0.98] transition-all duration-150"
              >
                考生登录 / 注册
              </Link>
            )}
          </div>
        </div>
      </header>

      {/* Logout Confirmation Dialog (Local data clearance & backup) */}
      {showLogoutModal && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-md flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-white/95 backdrop-blur-2xl rounded-2xl max-w-sm w-full p-6 shadow-float border border-black/[0.08] space-y-4">
            <div className="flex items-start justify-between">
              <div className="flex items-center space-x-3 text-zinc-900">
                <div className="w-9 h-9 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center font-bold">
                  <LogOut className="w-4 h-4" />
                </div>
                <div>
                  <h3 className="font-bold text-sm text-zinc-900">安全退出系统</h3>
                  <p className="text-[11px] text-zinc-400">学习档案云端同步与终端隔离</p>
                </div>
              </div>
              <button
                onClick={() => setShowLogoutModal(false)}
                disabled={isLoggingOut}
                className="text-zinc-400 hover:text-zinc-700 p-1 rounded-lg transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <p className="text-xs text-zinc-600 leading-relaxed">
              为保障考场环境与个人学习进度安全，退出时将清除本终端本地缓存。请选择退出方式：
            </p>

            <div className="space-y-2 pt-1">
              <button
                onClick={() => handleConfirmLogout(true)}
                disabled={isLoggingOut}
                className="w-full py-2.5 px-4 bg-zinc-900 hover:bg-zinc-800 text-white rounded-xl text-xs font-bold shadow-subtle flex items-center justify-center space-x-2 transition-all duration-150 active:scale-[0.98] disabled:opacity-50"
              >
                {isLoggingOut ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <>
                    <CloudUpload className="w-4 h-4 text-zinc-300" />
                    <span>同步档案至云端并退出</span>
                  </>
                )}
              </button>

              <button
                onClick={() => handleConfirmLogout(false)}
                disabled={isLoggingOut}
                className="w-full py-2.5 px-4 bg-zinc-100 hover:bg-zinc-200/80 text-zinc-700 rounded-xl text-xs font-semibold flex items-center justify-center space-x-2 transition-all duration-150 disabled:opacity-50"
              >
                <Trash2 className="w-3.5 h-3.5 text-zinc-400" />
                <span>仅清除本地缓存退出</span>
              </button>

              <button
                onClick={() => setShowLogoutModal(false)}
                disabled={isLoggingOut}
                className="w-full py-1.5 text-xs font-medium text-zinc-400 hover:text-zinc-700 text-center transition-colors"
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
