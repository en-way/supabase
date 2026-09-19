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
  Loader2
} from "lucide-react";

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  // Logout Confirmation Dialog State
  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  useEffect(() => {
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

    return () => {
      subscription.unsubscribe();
      window.removeEventListener("enway_profile_updated", handleProfileUpdate);
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
      <header className="sticky top-0 z-40 w-full border-b border-slate-200 bg-white/90 backdrop-blur">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between h-16">
          {/* Brand Logo */}
          <div className="flex items-center space-x-6">
            <Link href="/" className="flex items-center space-x-2.5">
              <div className="w-9 h-9 rounded-xl bg-indigo-600 flex items-center justify-center text-white font-bold shadow-md shadow-indigo-200">
                <BookOpen className="w-5 h-5" />
              </div>
              <div className="flex flex-col">
                <span className="text-lg font-black tracking-tight text-slate-900 leading-none">
                  ENWAY
                </span>
                <span className="text-[11px] text-indigo-600 font-semibold tracking-wide mt-0.5">
                  真题研习与全真模考
                </span>
              </div>
            </Link>

            {/* Navigation Links */}
            <nav className="hidden md:flex items-center space-x-1">
              <Link
                href="/"
                className={`px-3.5 py-1.5 rounded-lg text-sm font-semibold transition-colors ${
                  pathname === "/" 
                    ? "bg-indigo-50 text-indigo-700" 
                    : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <FileText className="w-4 h-4" />
                  <span>真题大厅</span>
                </span>
              </Link>

              <Link
                href="/mistakes"
                className={`px-3.5 py-1.5 rounded-lg text-sm font-semibold transition-colors ${
                  pathname.startsWith("/mistakes") 
                    ? "bg-indigo-50 text-indigo-700" 
                    : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <AlertCircle className="w-4 h-4 text-amber-500" />
                  <span>智能错题集</span>
                </span>
              </Link>

              <Link
                href="/vocabulary"
                className={`px-3.5 py-1.5 rounded-lg text-sm font-semibold transition-colors ${
                  pathname.startsWith("/vocabulary") 
                    ? "bg-indigo-50 text-indigo-700" 
                    : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <Bookmark className="w-4 h-4 text-emerald-500" />
                  <span>核心词汇库</span>
                </span>
              </Link>

              {isAnyAdmin && (
                <Link
                  href="/admin"
                  className={`px-3.5 py-1.5 rounded-lg text-sm font-semibold transition-colors ${
                    pathname.startsWith("/admin") 
                      ? "bg-purple-50 text-purple-700" 
                      : "text-purple-600 hover:text-purple-900 hover:bg-purple-50/50"
                  }`}
                >
                  <span className="flex items-center space-x-1.5">
                    <Shield className="w-4 h-4" />
                    <span>考务与题库管理</span>
                  </span>
                </Link>
              )}
            </nav>
          </div>

          {/* User Status / Actions */}
          <div className="flex items-center space-x-3">
            {loading ? (
              <div className="h-8 w-20 bg-slate-100 animate-pulse rounded-lg" />
            ) : user ? (
              <div className="flex items-center space-x-2">
                <Link
                  href="/profile"
                  className="flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200/80 hover:bg-slate-100 transition-colors"
                >
                  <div className="w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs font-bold">
                    {profile?.nickname?.[0] || profile?.username?.[0] || "U"}
                  </div>
                  <div className="text-left">
                    <span className="text-xs font-semibold text-slate-800 block leading-tight">
                      {profile?.nickname || profile?.username}
                    </span>
                    <span className="text-[10px] text-slate-500 block leading-tight">
                      {profile?.role === "super_admin" 
                        ? "👑 超级管理员" 
                        : profile?.role === "admin" 
                        ? "🛡️ 管理员" 
                        : "考号:" + (profile?.username || "")}
                    </span>
                  </div>
                </Link>

                <button
                  onClick={() => setShowLogoutModal(true)}
                  title="安全退出系统"
                  className="p-2 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            ) : (
              <Link
                href="/login"
                className="px-4 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold rounded-lg shadow-sm transition-colors"
              >
                考生登录 / 注册
              </Link>
            )}
          </div>
        </div>
      </header>

      {/* Logout Confirmation Dialog (Local data clearance & backup) */}
      {showLogoutModal && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in duration-150">
          <div className="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border border-slate-200 space-y-4">
            <div className="flex items-start justify-between">
              <div className="flex items-center space-x-3 text-slate-900">
                <div className="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center font-bold">
                  <LogOut className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-base">安全退出确认</h3>
                  <p className="text-xs text-slate-400">学习档案云端同步与终端隔离</p>
                </div>
              </div>
              <button
                onClick={() => setShowLogoutModal(false)}
                disabled={isLoggingOut}
                className="text-slate-400 hover:text-slate-600 p-1"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <p className="text-xs text-slate-600 leading-relaxed">
              为保障考场环境与个人学习进度安全，退出时将清除本终端本地缓存。请选择退出方式：
            </p>

            <div className="space-y-2 pt-2">
              <button
                onClick={() => handleConfirmLogout(true)}
                disabled={isLoggingOut}
                className="w-full py-2.5 px-4 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold shadow-sm shadow-indigo-200 flex items-center justify-center space-x-2 transition-colors disabled:opacity-50"
              >
                {isLoggingOut ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <>
                    <CloudUpload className="w-4 h-4" />
                    <span>同步档案至云端并安全退出</span>
                  </>
                )}
              </button>

              <button
                onClick={() => handleConfirmLogout(false)}
                disabled={isLoggingOut}
                className="w-full py-2.5 px-4 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-semibold flex items-center justify-center space-x-2 transition-colors disabled:opacity-50"
              >
                <Trash2 className="w-4 h-4 text-slate-500" />
                <span>直接清除本地缓存退出</span>
              </button>

              <button
                onClick={() => setShowLogoutModal(false)}
                disabled={isLoggingOut}
                className="w-full py-2 text-xs font-medium text-slate-500 hover:text-slate-700 text-center"
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
