"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import { 
  BookOpen, 
  FileText, 
  AlertCircle, 
  Bookmark, 
  User, 
  Shield, 
  LogOut 
} from "lucide-react";

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

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
            // Fallback to metadata if DB row pending
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

  const handleLogout = async () => {
    await supabase.auth.signOut();
    router.push("/login");
  };

  if (pathname === "/login") return null;

  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between h-16">
        {/* Brand Logo */}
        <div className="flex items-center space-x-6">
          <Link href="/" className="flex items-center space-x-2">
            <div className="w-9 h-9 rounded-xl bg-indigo-600 flex items-center justify-center text-white font-bold shadow-md shadow-indigo-200">
              <BookOpen className="w-5 h-5" />
            </div>
            <div className="flex flex-col">
              <span className="text-lg font-black tracking-tight text-slate-900 leading-none">
                ENWAY
              </span>
              <span className="text-xs text-indigo-600 font-medium tracking-wide">
                英语刷题与模考
              </span>
            </div>
          </Link>

          {/* Navigation Links */}
          <nav className="hidden md:flex items-center space-x-1">
            <Link
              href="/"
              className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                pathname === "/" 
                  ? "bg-indigo-50 text-indigo-700" 
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              <span className="flex items-center space-x-1.5">
                <FileText className="w-4 h-4" />
                <span>试卷大厅</span>
              </span>
            </Link>

            <Link
              href="/mistakes"
              className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                pathname.startsWith("/mistakes") 
                  ? "bg-indigo-50 text-indigo-700" 
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              <span className="flex items-center space-x-1.5">
                <AlertCircle className="w-4 h-4 text-amber-500" />
                <span>错题本</span>
              </span>
            </Link>

            <Link
              href="/vocabulary"
              className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                pathname.startsWith("/vocabulary") 
                  ? "bg-indigo-50 text-indigo-700" 
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              <span className="flex items-center space-x-1.5">
                <Bookmark className="w-4 h-4 text-emerald-500" />
                <span>生词本</span>
              </span>
            </Link>

            {profile?.role === "admin" && (
              <Link
                href="/admin"
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                  pathname.startsWith("/admin") 
                    ? "bg-purple-50 text-purple-700" 
                    : "text-purple-600 hover:text-purple-900 hover:bg-purple-50/50"
                }`}
              >
                <span className="flex items-center space-x-1.5">
                  <Shield className="w-4 h-4" />
                  <span>管理后台</span>
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
                    {profile?.role === "admin" ? "👑 管理员" : "学号:" + (profile?.username || "")}
                  </span>
                </div>
              </Link>

              <button
                onClick={handleLogout}
                title="退出登录"
                className="p-2 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors"
              >
                <LogOut className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <Link
              href="/login"
              className="px-4 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-medium rounded-lg shadow-sm transition-colors"
            >
              登录 / 注册
            </Link>
          )}
        </div>
      </div>
    </header>
  );
}
