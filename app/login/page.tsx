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
  Lock,
  X,
  HelpCircle
} from "lucide-react";

function getSafeRedirectTarget(): string {
  if (typeof window === "undefined") return "/";
  try {
    const params = new URLSearchParams(window.location.search);
    const r = params.get("redirect");
    if (!r) return "/";

    // 1. Prevent backslash / protocol-relative open redirect attacks
    if (r.startsWith("//") || r.startsWith("/\\") || r.includes("\\")) {
      return "/";
    }

    // 2. Validate strict same-origin via standard URL parser
    const parsed = new URL(r, window.location.origin);
    if (parsed.origin !== window.location.origin) {
      return "/";
    }

    // 3. Prevent infinite redirect loop back to login
    if (parsed.pathname === "/login" || parsed.pathname === "/login/" || parsed.pathname.startsWith("/login")) {
      return "/";
    }

    return parsed.pathname + parsed.search;
  } catch {
    return "/";
  }
}

export default function LoginPage() {
  const router = useRouter();
  const [isRegister, setIsRegister] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [retryStatus, setRetryStatus] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const [successMsg, setSuccessMsg] = useState("");

  // Forgot password modal state
  const [showForgotModal, setShowForgotModal] = useState(false);
  const [forgotUsername, setForgotUsername] = useState("");
  const [forgotNewPassword, setForgotNewPassword] = useState("");
  const [forgotConfirmPassword, setForgotConfirmPassword] = useState("");
  const [forgotLoading, setForgotLoading] = useState(false);
  const [forgotNotice, setForgotNotice] = useState<{ type: "success" | "error"; text: string } | null>(null);

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
              .select("id", { count: "exact", head: true })
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
    setRetryStatus("");
    // Use internal standard email mapping to satisfy Supabase GoTrue Auth
    const internalEmail = `${cleanUsername}@enway.com`;

    // Resilient Auth helpers with jittered exponential backoff for 429 rate limit
    const signInWithBackoff = async (email: string, pass: string, maxRetries = 3) => {
      for (let attempt = 1; attempt <= maxRetries; attempt++) {
        const res = await supabase.auth.signInWithPassword({
          email,
          password: pass,
        });
        if (!res.error) return res;
        const err = res.error;
        const isRateLimit = (err as any)?.status === 429 || 
          err.message?.toLowerCase().includes("rate limit") || 
          err.message?.toLowerCase().includes("too many requests");
        if (isRateLimit && attempt < maxRetries) {
          const delay = Math.floor(1000 * Math.pow(1.5, attempt) + Math.random() * 800);
          setRetryStatus(`登录高峰安全排队中 (第 ${attempt}/${maxRetries} 次)...`);
          await new Promise((r) => setTimeout(r, delay));
          continue;
        }
        return res;
      }
      return { data: { user: null, session: null }, error: new Error("登录请求超时，请稍后重试") as any };
    };

    const signUpWithBackoff = async (email: string, pass: string, options: any, maxRetries = 3) => {
      for (let attempt = 1; attempt <= maxRetries; attempt++) {
        const res = await supabase.auth.signUp({
          email,
          password: pass,
          options,
        });
        if (!res.error) return res;
        const err = res.error;
        const isRateLimit = (err as any)?.status === 429 || 
          err.message?.toLowerCase().includes("rate limit") || 
          err.message?.toLowerCase().includes("too many requests");
        if (isRateLimit && attempt < maxRetries) {
          const delay = Math.floor(1000 * Math.pow(1.5, attempt) + Math.random() * 800);
          setRetryStatus(`注册服务高峰排队中 (第 ${attempt}/${maxRetries} 次)...`);
          await new Promise((r) => setTimeout(r, delay));
          continue;
        }
        return res;
      }
      return { data: { user: null, session: null }, error: new Error("注册请求超时，请稍后重试") as any };
    };

    try {
      if (isRegister) {
        const { data, error } = await signUpWithBackoff(
          internalEmail,
          password,
          {
            data: {
              username: cleanUsername,
              nickname: cleanUsername,
            },
          }
        );

        if (error) {
          if (error.message.includes("User already registered")) {
            throw new Error("该用户名/学号已被注册，请直接登录");
          }
          throw error;
        }

        // Clean local state for newly registered user
        clearLocalData("all");

        const targetUrl = getSafeRedirectTarget();

        // Touch active timestamp
        try {
          await supabase.rpc("touch_user_activity");
        } catch {}

        if (data?.session) {
          setSuccessMsg("注册成功！正在为您初始化学习数据...");
          setTimeout(() => router.push(targetUrl), 600);
        } else {
          // If auto sign-in is needed
          const { error: signInErr } = await signInWithBackoff(
            internalEmail,
            password
          );
          if (signInErr) throw signInErr;
          setSuccessMsg("注册成功！正在进入系统...");
          router.push(targetUrl);
        }
      } else {
        const { error } = await signInWithBackoff(
          internalEmail,
          password
        );

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

          // 🛡️ Free Quota Protection: 7-day throttle on automatic reconciliation
          const LAST_RECON_KEY = "enway_last_reconcile_ts";
          let lastRecon = 0;
          try {
            lastRecon = Number(localStorage.getItem(LAST_RECON_KEY) || "0");
          } catch {}

          if (Date.now() - lastRecon > 7 * 24 * 60 * 60 * 1000) {
            try {
              localStorage.setItem(LAST_RECON_KEY, String(Date.now()));
              await reconcileLearningState();
            } catch (reconErr) {
              console.warn("Reconcile skipped/failed:", reconErr);
            }
          }
        } catch (syncErr) {
          console.warn("Cloud backup pull or reconcile skipped/empty:", syncErr);
        }

        router.push(getSafeRedirectTarget());
      }
    } catch (err: any) {
      setErrorMsg(err.message || "操作失败，请稍后重试");
    } finally {
      setLoading(false);
    }
  };

  const handleForgotSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setForgotNotice(null);

    const uname = forgotUsername.trim();
    if (!uname) {
      setForgotNotice({ type: "error", text: "请输入用户名或学号" });
      return;
    }
    if (forgotNewPassword.length < 6) {
      setForgotNotice({ type: "error", text: "新密码长度至少需要 6 位" });
      return;
    }
    if (forgotNewPassword !== forgotConfirmPassword) {
      setForgotNotice({ type: "error", text: "两次输入的新密码不一致" });
      return;
    }

    try {
      setForgotLoading(true);
      const { data, error } = await supabase.rpc("submit_unauthenticated_password_reset_request", {
        input_username: uname,
        new_plain_password: forgotNewPassword,
      });

      if (error) throw error;

      setForgotNotice({
        type: "success",
        text: data?.message || "已成功提交重置密码申请！请联系超级管理员审批，审批通过后即可使用新密码登录。",
      });
      setForgotNewPassword("");
      setForgotConfirmPassword("");
    } catch (err: any) {
      setForgotNotice({
        type: "error",
        text: err.message || "提交重置密码申请失败，请稍后重试",
      });
    } finally {
      setForgotLoading(false);
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
            全国统考硕士研招 · 考研英语一与英语二历年全真真题研习
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
              <div className="flex items-center space-x-2">
                <div className="w-4 h-4 border-2 border-white dark:border-[#090a0f] border-t-transparent rounded-full animate-spin" />
                <span>{retryStatus || (isRegister ? "正在处理注册..." : "安全登录中...")}</span>
              </div>
            ) : (
              <span>{isRegister ? "立即完成注册" : "安全登录系统"}</span>
            )}
          </button>
        </form>

        {/* Forgot password trigger */}
        {!isRegister && (
          <div className="mt-3 flex justify-end">
            <button
              type="button"
              onClick={() => {
                setShowForgotModal(true);
                setForgotNotice(null);
                setForgotUsername(username);
                setForgotNewPassword("");
                setForgotConfirmPassword("");
              }}
              className="text-xs text-stone-500 hover:text-emerald-700 dark:text-zinc-400 dark:hover:text-cyber-400 transition-colors inline-flex items-center space-x-1"
            >
              <HelpCircle className="w-3.5 h-3.5" />
              <span>忘记密码？申请重置</span>
            </button>
          </div>
        )}

        {/* Tip / Notes */}
        <div className="mt-6 pt-5 border-t border-stone-100 dark:border-zinc-800 text-center">
          <p className="text-[11px] text-stone-400 dark:text-zinc-500 leading-relaxed flex items-center justify-center space-x-1.5">
            <Sparkles className="w-3.5 h-3.5 text-emerald-600 dark:text-cyber-400" />
            <span>登录自动同步云端做题快照 · 退出彻底隔离设备本地数据</span>
          </p>
        </div>
      </div>

      {/* Forgot Password Modal */}
      {showForgotModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in">
          <div className="w-full max-w-md bg-white dark:bg-[#11131a] rounded-2xl shadow-2xl border border-black/[0.08] dark:border-cyan-500/25 p-6 relative transition-colors duration-300">
            {/* Modal Header */}
            <div className="flex items-center justify-between pb-3 border-b border-stone-100 dark:border-zinc-800">
              <div className="flex items-center space-x-2">
                <div className="p-1.5 rounded-lg bg-emerald-100 dark:bg-cyan-950 text-emerald-800 dark:text-cyan-400">
                  <KeyRound className="w-4 h-4" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-stone-900 dark:text-zinc-100">申请重置密码</h3>
                  <p className="text-[11px] text-stone-400 dark:text-zinc-500">全员自主申请制 · 超级管理员后台审批</p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setShowForgotModal(false)}
                className="p-1 text-stone-400 hover:text-stone-600 dark:hover:text-zinc-200 rounded-lg hover:bg-stone-100 dark:hover:bg-zinc-800 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Explanation banner */}
            <div className="mt-3.5 p-3 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200/80 dark:border-amber-500/30 text-[11px] text-amber-900 dark:text-amber-300 leading-relaxed">
              为保护个人做题进度与数据安全，系统实行<strong>自主申请审批制</strong>。提交后将生成不可逆密文存入审批流，超级管理员审核通过后新密码即可生效。
            </div>

            {/* Notice banner */}
            {forgotNotice && (
              <div
                className={`mt-3 p-3 rounded-xl text-xs flex items-start space-x-2 ${
                  forgotNotice.type === "success"
                    ? "bg-emerald-50/80 dark:bg-emerald-950/40 border border-emerald-200/80 dark:border-emerald-500/30 text-emerald-800 dark:text-emerald-300"
                    : "bg-rose-50/80 dark:bg-rose-950/40 border border-rose-200/80 dark:border-rose-500/30 text-rose-700 dark:text-rose-300"
                }`}
              >
                {forgotNotice.type === "success" ? (
                  <CheckCircle2 className="w-4 h-4 shrink-0 mt-0.5" />
                ) : (
                  <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />
                )}
                <span className="flex-1">{forgotNotice.text}</span>
              </div>
            )}

            {/* Form */}
            <form onSubmit={handleForgotSubmit} className="mt-4 space-y-3.5">
              <div>
                <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                  账号用户名 / 学号
                </label>
                <input
                  type="text"
                  required
                  value={forgotUsername}
                  onChange={(e) => setForgotUsername(e.target.value)}
                  placeholder="请输入您的账号用户名"
                  className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                  期望设置的新密码
                </label>
                <input
                  type="password"
                  required
                  value={forgotNewPassword}
                  onChange={(e) => setForgotNewPassword(e.target.value)}
                  placeholder="至少 6 位密码"
                  className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-stone-700 dark:text-zinc-300 mb-1">
                  确认期望新密码
                </label>
                <input
                  type="password"
                  required
                  value={forgotConfirmPassword}
                  onChange={(e) => setForgotConfirmPassword(e.target.value)}
                  placeholder="再次输入新密码"
                  className="w-full px-3.5 py-2 bg-stone-50 dark:bg-zinc-900 border border-stone-200 dark:border-zinc-800 rounded-xl text-xs text-stone-900 dark:text-zinc-100 placeholder:text-stone-400 dark:placeholder:text-zinc-500 focus:outline-none focus:ring-2 focus:ring-emerald-700/10 dark:focus:ring-cyan-500/20 focus:border-emerald-600 dark:focus:border-cyan-400"
                />
              </div>

              <div className="pt-2 flex items-center justify-end space-x-2">
                <button
                  type="button"
                  onClick={() => setShowForgotModal(false)}
                  className="px-3.5 py-2 rounded-xl text-xs text-stone-600 dark:text-zinc-400 hover:bg-stone-100 dark:hover:bg-zinc-800 transition-colors"
                >
                  关闭
                </button>
                <button
                  type="submit"
                  disabled={forgotLoading}
                  className="px-4 py-2 bg-emerald-700 dark:bg-cyber-500 hover:bg-emerald-800 dark:hover:bg-cyber-400 disabled:opacity-50 text-white dark:text-[#090a0f] text-xs font-bold rounded-xl shadow-sm dark:shadow-glow-cyan transition-all flex items-center space-x-1.5"
                >
                  {forgotLoading && (
                    <div className="w-3.5 h-3.5 border-2 border-white dark:border-[#090a0f] border-t-transparent rounded-full animate-spin" />
                  )}
                  <span>{forgotLoading ? "正在提交..." : "提交改密申请"}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
