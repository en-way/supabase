"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { 
  clearLocalData, 
  downloadBackupFromCloud,
  reconcileLearningState
} from "@/lib/storage";
import { 
  BookOpen, 
  KeyRound, 
  User, 
  Sparkles, 
  CheckCircle2, 
  AlertCircle,
  Users,
  Lock
} from "lucide-react";

export default function LoginPage() {
  const router = useRouter();
  const [isRegister, setIsRegister] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");
  const [successMsg, setSuccessMsg] = useState("");

  // System settings state for quota & registration status
  const [settings, setSettings] = useState<{
    maxStudentsLimit: number;
    registrationEnabled: boolean;
    currentStudentCount?: number;
    isFull?: boolean;
  } | null>(null);

  useEffect(() => {
    async function loadSettings() {
      try {
        const { data: setRow } = await supabase
          .from("system_settings")
          .select("max_students_limit, registration_enabled")
          .eq("id", 1)
          .maybeSingle();

        if (setRow) {
          const limit = Number(setRow.max_students_limit || 0);
          const enabled = Boolean(setRow.registration_enabled);

          let isFull = false;
          let studentCount = 0;
          if (limit > 0) {
            const { count } = await supabase
              .from("profiles")
              .select("*", { count: "exact", head: true })
              .eq("role", "student");
            studentCount = count || 0;
            if (studentCount >= limit) {
              isFull = true;
            }
          }

          setSettings({
            maxStudentsLimit: limit,
            registrationEnabled: enabled,
            currentStudentCount: studentCount,
            isFull,
          });
        }
      } catch (err) {
        console.error("Error loading system settings:", err);
      }
    }
    loadSettings();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg("");
    setSuccessMsg("");

    const cleanUsername = username.trim().toLowerCase();
    if (!cleanUsername) {
      setErrorMsg("请输入用户名或学号");
      return;
    }
    if (!/^[a-zA-Z0-9_-]{3,20}$/.test(cleanUsername)) {
      setErrorMsg("用户名/学号仅支持3~20位字母、数字、下划线或短横线");
      return;
    }
    if (password.length < 6) {
      setErrorMsg("密码至少需要 6 位");
      return;
    }

    // Double check registration settings
    if (isRegister) {
      if (settings?.registrationEnabled === false) {
        setErrorMsg("系统当前已暂停新用户注册，请联系管理员。");
        return;
      }
      if (settings?.isFull) {
        setErrorMsg(`注册人数已达系统上限（${settings.maxStudentsLimit}人），暂不开放新注册。`);
        return;
      }
    }

    setLoading(true);
    // Use internal standard email mapping to satisfy Supabase GoTrue Auth
    const internalEmail = `${cleanUsername}@enway.com`;

    try {
      if (isRegister) {
        const { data, error } = await supabase.auth.signUp({
          email: internalEmail,
          password,
          options: {
            data: {
              username: cleanUsername,
              nickname: cleanUsername,
            },
          },
        });

        if (error) {
          if (error.message.includes("User already registered")) {
            throw new Error("该用户名/学号已被注册，请直接登录");
          }
          throw error;
        }

        // Clean local state for newly registered user
        clearLocalData("all");

        const getRedirectTarget = () => {
          if (typeof window === "undefined") return "/";
          try {
            const params = new URLSearchParams(window.location.search);
            const r = params.get("redirect");
            if (r && r.startsWith("/") && !r.startsWith("//")) return r;
          } catch {}
          return "/";
        };

        const targetUrl = getRedirectTarget();

        // Touch active timestamp
        try {
          await supabase.rpc("touch_user_activity");
        } catch {}

        if (data.session) {
          setSuccessMsg("注册成功！正在为您初始化学习数据...");
          setTimeout(() => router.push(targetUrl), 600);
        } else {
          // If auto sign-in is needed
          const { error: signInErr } = await supabase.auth.signInWithPassword({
            email: internalEmail,
            password,
          });
          if (signInErr) throw signInErr;
          setSuccessMsg("注册成功！正在进入系统...");
          router.push(targetUrl);
        }
      } else {
        const { error } = await supabase.auth.signInWithPassword({
          email: internalEmail,
          password,
        });

        if (error) {
          if (error.message.includes("Invalid login credentials")) {
            throw new Error("用户名或密码错误，请核对后重试");
          }
          throw error;
        }

        setSuccessMsg("登录成功，正在从云端对象存储同步并校对存档...");

        // Touch active timestamp on login
        try {
          await supabase.rpc("touch_user_activity");
        } catch {}

        // Wipe old device cache to prevent account data bleed-through
        clearLocalData("all");

        // Automatically pull latest backup from Supabase Storage and reconcile
        try {
          await downloadBackupFromCloud();
          await reconcileLearningState();
        } catch (syncErr) {
          console.warn("Cloud backup pull or reconcile skipped/empty:", syncErr);
        }

        const getRedirectTarget = () => {
          if (typeof window === "undefined") return "/";
          try {
            const params = new URLSearchParams(window.location.search);
            const r = params.get("redirect");
            if (r && r.startsWith("/") && !r.startsWith("//")) return r;
          } catch {}
          return "/";
        };

        router.push(getRedirectTarget());
      }
    } catch (err: any) {
      setErrorMsg(err.message || "操作失败，请稍后重试");
    } finally {
      setLoading(false);
    }
  };

  const isRegistrationBlocked = 
    settings && (!settings.registrationEnabled || settings.isFull);

  return (
    <div className="min-h-[calc(100vh-4.5rem)] -mt-6 flex flex-col justify-center items-center px-4 relative">
      {/* Background soft ambient radial glow */}
      <div className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-emerald-200/30 dark:bg-cyan-900/20 rounded-full blur-3xl pointer-events-none -z-10 transition-colors duration-300" />

      <div className="w-full max-w-md bg-white dark:bg-[#11131a] rounded-2xl shadow-card border border-black/[0.08] dark:border-cyan-500/25 p-7 sm:p-8 relative transition-colors duration-300">
        {/* Header */}
        <div className="text-center mb-7">
          <div className="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] shadow-sm mb-3.5 tracking-tight font-black font-serif text-lg dark:shadow-glow-cyan">
            EW
          </div>
          <h1 className="text-xl font-bold text-stone-900 dark:text-zinc-100 tracking-tight">
            Enway 在线英语平台
          </h1>
          <p className="text-xs text-stone-500 dark:text-zinc-400 mt-1">
            大学英语四六级 · 考研英语真题模考与逐题精读
          </p>
        </div>

        {/* Quota / Registration Alert Banner */}
        {settings && !settings.registrationEnabled && (
          <div className="mb-4 p-3 bg-amber-50/70 dark:bg-amber-950/40 border border-amber-200/80 dark:border-amber-500/30 rounded-xl flex items-center space-x-2 text-xs text-amber-900 dark:text-amber-300">
            <Lock className="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0" />
            <span>系统已由管理员暂停新学员注册，已注册学员可正常登录。</span>
          </div>
        )}
        {settings && settings.isFull && (
          <div className="mb-4 p-3 bg-amber-50/70 dark:bg-amber-950/40 border border-amber-200/80 dark:border-amber-500/30 rounded-xl flex items-center space-x-2 text-xs text-amber-900 dark:text-amber-300">
            <Users className="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0" />
            <span>注册学员已达到系统设定的最大人数上限（{settings.maxStudentsLimit}人），暂不开放新注册。</span>
          </div>
        )}

        {/* Tab Switcher */}
        <div className="grid grid-cols-2 gap-1 p-1 bg-stone-100 dark:bg-zinc-900 rounded-xl mb-5">
          <button
            type="button"
            onClick={() => { setIsRegister(false); setErrorMsg(""); }}
            className={`py-2 text-xs font-semibold rounded-lg transition-all ${
              !isRegister 
                ? "bg-white dark:bg-zinc-800 text-stone-900 dark:text-cyber-300 shadow-subtle dark:shadow-glow-cyan" 
                : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
            }`}
          >
            学员登录
          </button>
          <button
            type="button"
            disabled={Boolean(isRegistrationBlocked)}
            onClick={() => { setIsRegister(true); setErrorMsg(""); }}
            className={`py-2 text-xs font-semibold rounded-lg transition-all ${
              isRegister 
                ? "bg-white dark:bg-zinc-800 text-stone-900 dark:text-cyber-300 shadow-subtle dark:shadow-glow-cyan" 
                : isRegistrationBlocked 
                ? "text-stone-400 dark:text-zinc-600 cursor-not-allowed" 
                : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
            }`}
          >
            快速注册 {isRegistrationBlocked && " (已满)"}
          </button>
        </div>

        {/* Alerts */}
        {errorMsg && (
          <div className="mb-4 p-3 rounded-xl bg-rose-50/80 dark:bg-rose-950/40 border border-rose-200/80 dark:border-rose-500/30 text-rose-700 dark:text-rose-300 text-xs flex items-center space-x-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>{errorMsg}</span>
          </div>
        )}
        {successMsg && (
          <div className="mb-4 p-3 rounded-xl bg-emerald-50/80 dark:bg-emerald-950/40 border border-emerald-200/80 dark:border-emerald-500/30 text-emerald-700 dark:text-emerald-300 text-xs flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            <span>{successMsg}</span>
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1.5">
              用户名 / 学号
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-stone-400 dark:text-zinc-500">
                <User className="w-4 h-4" />
              </div>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="例如: student01 或 20240901"
                className="w-full pl-10 pr-4 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400 focus:bg-white dark:focus:bg-zinc-950 transition-all"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1.5">
              密码
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-stone-400 dark:text-zinc-500">
                <KeyRound className="w-4 h-4" />
              </div>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="至少 6 位密码"
                className="w-full pl-10 pr-4 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400 focus:bg-white dark:focus:bg-zinc-950 transition-all"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading || (isRegister && Boolean(isRegistrationBlocked))}
            className="w-full mt-2 py-2.5 px-4 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 active:scale-[0.98] disabled:opacity-50 text-white dark:text-[#090a0f] text-xs font-bold rounded-xl shadow-sm dark:shadow-glow-cyan transition-all flex items-center justify-center space-x-2"
          >
            {loading ? (
              <div className="w-4 h-4 border-2 border-white dark:border-[#090a0f] border-t-transparent rounded-full animate-spin" />
            ) : (
              <span>{isRegister ? "立即完成注册" : "安全登录系统"}</span>
            )}
          </button>
        </form>

        {/* Tip / Notes */}
        <div className="mt-6 pt-5 border-t border-stone-100 dark:border-zinc-800 text-center">
          <p className="text-[11px] text-stone-400 dark:text-zinc-500 leading-relaxed flex items-center justify-center space-x-1.5">
            <Sparkles className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
            <span>登录自动同步云端做题快照 · 退出彻底隔离设备本地数据</span>
          </p>
        </div>
      </div>
    </div>
  );
}
