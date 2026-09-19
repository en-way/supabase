"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { BookOpen, KeyRound, User, Sparkles, CheckCircle2, AlertCircle } from "lucide-react";

export default function LoginPage() {
  const router = useRouter();
  const [isRegister, setIsRegister] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");
  const [successMsg, setSuccessMsg] = useState("");

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

    setLoading(true);
    // Use internal standard email mapping to satisfy Supabase Auth
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

        if (data.session) {
          setSuccessMsg("注册成功！即将进入系统...");
          setTimeout(() => router.push("/"), 800);
        } else {
          // In case email confirm is somehow triggered on Supabase
          setSuccessMsg("注册成功！正在为你自动登录...");
          const { error: signInErr } = await supabase.auth.signInWithPassword({
            email: internalEmail,
            password,
          });
          if (signInErr) throw signInErr;
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

        router.push("/");
      }
    } catch (err: any) {
      setErrorMsg(err.message || "操作失败，请稍后重试");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen -mt-6 flex flex-col justify-center items-center px-4 bg-gradient-to-b from-slate-50 to-indigo-50/40">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-xl border border-slate-200/80 p-8">
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
            onClick={() => { setIsRegister(true); setErrorMsg(""); }}
            className={`py-2 text-sm font-semibold rounded-lg transition-all ${
              isRegister ? "bg-white text-indigo-700 shadow-sm" : "text-slate-500 hover:text-slate-800"
            }`}
          >
            快速注册
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
            disabled={loading}
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
            <span>纯用户名安全注册 · 首位注册用户将自动晋升超级管理员</span>
          </p>
        </div>
      </div>
    </div>
  );
}
