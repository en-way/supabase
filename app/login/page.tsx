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

        if (data.session) {
          setSuccessMsg("注册成功！正在为您初始化学习数据...");
          setTimeout(() => router.push("/"), 600);
        } else {
          // If auto sign-in is needed
          const { error: signInErr } = await supabase.auth.signInWithPassword({
            email: internalEmail,
            password,
          });
          if (signInErr) throw signInErr;
          setSuccessMsg("注册成功！正在进入系统...");
          router.push("/");
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

        // Wipe old device cache to prevent account data bleed-through
        clearLocalData("all");

        // Automatically pull latest backup from Supabase Storage and reconcile
        try {
          await downloadBackupFromCloud();
          await reconcileLearningState();
        } catch (syncErr) {
          console.warn("Cloud backup pull or reconcile skipped/empty:", syncErr);
        }

        router.push("/");
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
    <div className="min-h-screen -mt-6 flex flex-col justify-center items-center px-4 bg-gradient-to-b from-slate-50 to-indigo-50/40">
      <div className="w-full max-w-md bg-white rounded-3xl shadow-xl border border-slate-200/80 p-8">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-indigo-600 text-white shadow-lg shadow-indigo-200 mb-4">
            <BookOpen className="w-7 h-7" />
          </div>
          <h1 className="text-2xl font-black text-slate-900 tracking-tight">
            Enway 在线英语平台
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            大学英语四六级 · 考研英语真题模考与刷题
          </p>
        </div>

        {/* Quota / Registration Alert Banner */}
        {settings && !settings.registrationEnabled && (
          <div className="mb-4 p-3 bg-amber-50 border border-amber-200 rounded-xl flex items-center space-x-2 text-xs text-amber-800">
            <Lock className="w-4 h-4 text-amber-600 shrink-0" />
            <span>系统已由管理员暂停新学员注册，已注册学员可正常登录。</span>
          </div>
        )}
        {settings && settings.isFull && (
          <div className="mb-4 p-3 bg-amber-50 border border-amber-200 rounded-xl flex items-center space-x-2 text-xs text-amber-800">
            <Users className="w-4 h-4 text-amber-600 shrink-0" />
            <span>注册学员已达到系统设定的最大人数上限（{settings.maxStudentsLimit}人），暂不开放新注册。</span>
          </div>
        )}

        {/* Tab Switcher */}
        <div className="grid grid-cols-2 gap-1 p-1 bg-slate-100 rounded-xl mb-6">
          <button
            type="button"
            onClick={() => { setIsRegister(false); setErrorMsg(""); }}
            className={`py-2 text-sm font-semibold rounded-lg transition-all ${
              !isRegister ? "bg-white text-indigo-700 shadow-sm" : "text-slate-500 hover:text-slate-800"
            }`}
          >
            学员登录
          </button>
          <button
            type="button"
            disabled={Boolean(isRegistrationBlocked)}
            onClick={() => { setIsRegister(true); setErrorMsg(""); }}
            className={`py-2 text-sm font-semibold rounded-lg transition-all ${
              isRegister 
                ? "bg-white text-indigo-700 shadow-sm" 
                : isRegistrationBlocked 
                ? "text-slate-400 cursor-not-allowed" 
                : "text-slate-500 hover:text-slate-800"
            }`}
          >
            快速注册 {isRegistrationBlocked && " (已满)"}
          </button>
        </div>

        {/* Alerts */}
        {errorMsg && (
          <div className="mb-5 p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-700 text-xs flex items-center space-x-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>{errorMsg}</span>
          </div>
        )}
        {successMsg && (
          <div className="mb-5 p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-700 text-xs flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            <span>{successMsg}</span>
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5">
              用户名 / 学号
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                <User className="w-4 h-4" />
              </div>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="例如: student01 或 20240901"
                className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5">
              密码
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                <KeyRound className="w-4 h-4" />
              </div>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="至少 6 位密码"
                className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading || (isRegister && Boolean(isRegistrationBlocked))}
            className="w-full mt-2 py-3 px-4 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white text-sm font-semibold rounded-xl shadow-md shadow-indigo-200 transition-all flex items-center justify-center space-x-2"
          >
            {loading ? (
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
            ) : (
              <span>{isRegister ? "立即完成注册" : "安全登录系统"}</span>
            )}
          </button>
        </form>

        {/* Tip / Notes */}
        <div className="mt-6 pt-5 border-t border-slate-100 text-center">
          <p className="text-[11px] text-slate-400 leading-relaxed flex items-center justify-center space-x-1">
            <Sparkles className="w-3 h-3 text-indigo-500" />
            <span>登录自动同步云端做题快照 · 退出彻底隔离设备本地数据</span>
          </p>
        </div>
      </div>
    </div>
  );
}
