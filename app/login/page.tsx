"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import {
  clearLocalData,
  downloadBackupFromCloud,
  reconcileLearningState,
  touchUserActivityThrottled,
  getLastLocalUserId,
  setLastLocalUserId,
  getLastReconcileTimestamp,
  setLastReconcileTimestamp,
  setLoginSyncInProgress,
} from "@/lib/storage";
import { clearPendingSubmissionTasks } from "@/lib/submissionQueue";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Spinner } from "@/components/ui/Feedback";
import { Input } from "@/components/ui/Field";
import { Modal } from "@/components/ui/Modal";
import {
  KeyRound,
  User,
  Sparkles,
  CheckCircle2,
  AlertCircle,
  Users,
  Lock,
  HelpCircle,
} from "lucide-react";

const KNOWN_STATIC_ROUTES = /^\/(mistakes|vocabulary|profile|exam|practice|login|admin)$/;

function normalizeRouteTrailingSlash(pathname: string): string {
  return KNOWN_STATIC_ROUTES.test(pathname) ? `${pathname}/` : pathname;
}

function getSafeRedirectTarget(): string {
  if (typeof window === "undefined") return "/";
  try {
    const params = new URLSearchParams(window.location.search);
    const r = params.get("redirect");
    if (!r) return "/";

    if (r.startsWith("//") || r.startsWith("/\\") || r.includes("\\")) {
      return "/";
    }

    const parsed = new URL(r, window.location.origin);
    if (parsed.origin !== window.location.origin) {
      return "/";
    }

    if (
      parsed.pathname === "/login" ||
      parsed.pathname === "/login/" ||
      parsed.pathname.startsWith("/login")
    ) {
      return "/";
    }

    return normalizeRouteTrailingSlash(parsed.pathname) + parsed.search;
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

  const [showForgotModal, setShowForgotModal] = useState(false);
  const [forgotUsername, setForgotUsername] = useState("");
  const [forgotNewPassword, setForgotNewPassword] = useState("");
  const [forgotConfirmPassword, setForgotConfirmPassword] = useState("");
  const [forgotLoading, setForgotLoading] = useState(false);
  const [forgotNotice, setForgotNotice] = useState<{
    type: "success" | "error";
    text: string;
  } | null>(null);

  const [settings, setSettings] = useState<{
    maxStudentsLimit: number;
    registrationEnabled: boolean;
    currentStudentCount?: number;
    isFull?: boolean;
  } | null>(null);

  useEffect(() => {
    let isMounted = true;
    async function loadSettings() {
      try {
        const { data: quotaData, error: rpcErr } = await supabase.rpc(
          "get_registration_quota_status"
        );
        if (!isMounted) return;

        if (!rpcErr && quotaData && typeof quotaData === "object") {
          setSettings({
            maxStudentsLimit: Number(quotaData.max_students_limit || 0),
            registrationEnabled: Boolean(quotaData.registration_enabled),
            currentStudentCount: Number(quotaData.current_student_count || 0),
            isFull: Boolean(quotaData.is_full),
          });
          return;
        }

        const { data: setRow } = await supabase
          .from("system_settings")
          .select("max_students_limit, registration_enabled")
          .eq("id", 1)
          .maybeSingle();

        if (!isMounted) return;
        if (setRow) {
          setSettings({
            maxStudentsLimit: Number(setRow.max_students_limit || 0),
            registrationEnabled: Boolean(setRow.registration_enabled),
            currentStudentCount: 0,
            isFull: false,
          });
        }
      } catch (err) {
        if (isMounted) {
          console.error("Error loading system settings:", err);
        }
      }
    }
    loadSettings();
    return () => {
      isMounted = false;
    };
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

    if (isRegister) {
      if (settings?.registrationEnabled === false) {
        setErrorMsg("系统当前已暂停新用户注册，请联系管理员。");
        return;
      }
      if (settings?.isFull) {
        setErrorMsg(
          `注册人数已达系统上限（${settings.maxStudentsLimit}人），暂不开放新注册。`
        );
        return;
      }
    }

    setLoading(true);
    setRetryStatus("");
    const internalEmail = `${cleanUsername}@enway.com`;

    const isRateLimitAuthError = (
      err: { status?: number; message?: string } | null | undefined
    ): boolean => {
      if (!err) return false;
      const has429Status = "status" in err && err.status === 429;
      const msg = (err.message || "").toLowerCase();
      return (
        has429Status ||
        msg.includes("rate limit") ||
        msg.includes("too many requests")
      );
    };

    const signInWithBackoff = async (
      email: string,
      pass: string,
      maxRetries = 3
    ) => {
      for (let attempt = 1; attempt <= maxRetries; attempt++) {
        const res = await supabase.auth.signInWithPassword({
          email,
          password: pass,
        });
        if (!res.error) return res;
        if (isRateLimitAuthError(res.error) && attempt < maxRetries) {
          const delay = Math.floor(
            1000 * Math.pow(1.5, attempt) + Math.random() * 800
          );
          setRetryStatus(`登录高峰安全排队中 (第 ${attempt}/${maxRetries} 次)...`);
          await new Promise((r) => setTimeout(r, delay));
          continue;
        }
        return res;
      }
      return {
        data: { user: null, session: null },
        error: { message: "登录请求超时，请稍后重试", status: 408 } as {
          message: string;
          status?: number;
        },
      };
    };

    const signUpWithBackoff = async (
      email: string,
      pass: string,
      options: { data?: { username: string; nickname: string } },
      maxRetries = 3
    ) => {
      for (let attempt = 1; attempt <= maxRetries; attempt++) {
        const res = await supabase.auth.signUp({
          email,
          password: pass,
          options,
        });
        if (!res.error) return res;
        if (isRateLimitAuthError(res.error) && attempt < maxRetries) {
          const delay = Math.floor(
            1000 * Math.pow(1.5, attempt) + Math.random() * 800
          );
          setRetryStatus(`注册服务高峰排队中 (第 ${attempt}/${maxRetries} 次)...`);
          await new Promise((r) => setTimeout(r, delay));
          continue;
        }
        return res;
      }
      return {
        data: { user: null, session: null },
        error: { message: "注册请求超时，请稍后重试", status: 408 } as {
          message: string;
          status?: number;
        },
      };
    };

    const clearCrossAccountClientCaches = () => {
      clearLocalData("all");
      clearPendingSubmissionTasks();
      try {
        localStorage.removeItem("enway_last_presence_touch");
      } catch {}
      try {
        sessionStorage.removeItem("enway_last_silent_backup");
        Object.keys(sessionStorage).forEach((k) => {
          if (k.startsWith("enway_cached_nav_profile_")) {
            sessionStorage.removeItem(k);
          }
        });
      } catch {}
    };

    try {
      setLoginSyncInProgress(true);
      if (isRegister) {
        const { data, error } = await signUpWithBackoff(internalEmail, password, {
          data: {
            username: cleanUsername,
            nickname: cleanUsername,
          },
        });

        if (error) {
          if (error.message.includes("User already registered")) {
            throw new Error("该用户名/学号已被注册，请直接登录");
          }
          throw error;
        }

        let activeSession = data?.session || null;
        if (!activeSession) {
          const { data: signInData, error: signInErr } = await signInWithBackoff(
            internalEmail,
            password
          );
          if (signInErr) throw signInErr;
          activeSession = signInData?.session || null;
        }

        const activeUser =
          activeSession?.user ||
          (await supabase.auth.getSession()).data.session?.user ||
          null;
        if (!activeUser) {
          throw new Error("注册已完成但未能建立登录会话，请切换登录页面直接登录");
        }

        clearCrossAccountClientCaches();
        setLastLocalUserId(activeUser.id);

        try {
          await touchUserActivityThrottled();
        } catch {}

        setSuccessMsg("注册成功！正在进入系统...");
        const targetUrl = getSafeRedirectTarget();
        setLoginSyncInProgress(false);
        router.replace(targetUrl);
      } else {
        const { data: signInData, error } = await signInWithBackoff(
          internalEmail,
          password
        );

        if (error) {
          if (error.message.includes("Invalid login credentials")) {
            throw new Error("用户名或密码错误，请核对后重试");
          }
          throw error;
        }

        const signedInUserId =
          signInData?.user?.id ||
          signInData?.session?.user?.id ||
          (await supabase.auth.getSession()).data.session?.user?.id ||
          null;

        const prevUserId = getLastLocalUserId();
        if (signedInUserId && prevUserId && prevUserId !== signedInUserId) {
          clearCrossAccountClientCaches();
        }
        if (signedInUserId) {
          setLastLocalUserId(signedInUserId);
        }

        setSuccessMsg("登录成功，正在从云端对象存储同步并校对存档...");

        try {
          await touchUserActivityThrottled();
        } catch {}

        try {
          const downloadRes = await downloadBackupFromCloud();
          if (downloadRes.success) {
            console.log("云端档案同步完成");
          }

          const lastRecon = getLastReconcileTimestamp(signedInUserId);
          if (Date.now() - lastRecon > 7 * 24 * 60 * 60 * 1000) {
            try {
              const recon = await reconcileLearningState();
              if (recon.completed) {
                setLastReconcileTimestamp(signedInUserId, Date.now());
              }
            } catch (reconErr) {
              console.warn("Reconcile skipped/failed:", reconErr);
            }
          }
        } catch (syncErr) {
          console.warn("Cloud backup pull or reconcile skipped/empty:", syncErr);
        }

        const targetUrl = getSafeRedirectTarget();
        setLoginSyncInProgress(false);
        router.replace(targetUrl);
      }
    } catch (err: unknown) {
      const errMsg =
        err instanceof Error
          ? err.message
          : typeof err === "object" && err !== null && "message" in err
            ? String((err as { message?: unknown }).message || "")
            : "";
      setErrorMsg(errMsg || "操作失败，请稍后重试");
    } finally {
      setLoginSyncInProgress(false);
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
      const { data, error } = await supabase.rpc(
        "submit_unauthenticated_password_reset_request",
        {
          input_username: uname,
          new_plain_password: forgotNewPassword,
        }
      );

      if (error) throw error;

      setForgotNotice({
        type: "success",
        text:
          data?.message ||
          "已成功提交重置密码申请！请联系超级管理员审批，审批通过后即可使用新密码登录。",
      });
      setForgotNewPassword("");
      setForgotConfirmPassword("");
    } catch (err: unknown) {
      const errMsg =
        err instanceof Error
          ? err.message
          : typeof err === "object" && err !== null && "message" in err
            ? String((err as { message?: unknown }).message || "")
            : "";
      setForgotNotice({
        type: "error",
        text: errMsg || "提交重置密码申请失败，请稍后重试",
      });
    } finally {
      setForgotLoading(false);
    }
  };

  const isRegistrationBlocked =
    settings && (!settings.registrationEnabled || settings.isFull);

  return (
    <div className="min-h-[calc(100dvh-5rem)] flex flex-col justify-center items-center px-4 py-8">
      <Card className="w-full max-w-md p-7 sm:p-8 shadow-2">
        <div className="text-center mb-7">
          <div className="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-primary text-primary-fg shadow-1 mb-3.5 tracking-tight font-black font-reading text-lg">
            EW
          </div>
          <h1 className="text-xl font-bold text-fg tracking-tight">
            Enway 在线英语平台
          </h1>
          <p className="text-xs text-fg-muted mt-1">
            全国统考硕士研招 · 考研英语一与英语二历年全真真题研习
          </p>
        </div>

        {settings && !settings.registrationEnabled && (
          <div className="mb-4 p-3 bg-warning-soft border border-warning/30 rounded-xl flex items-center gap-2 text-xs text-fg">
            <Lock className="w-4 h-4 text-warning shrink-0" />
            <span>系统已由管理员暂停新学员注册，已注册学员可正常登录。</span>
          </div>
        )}
        {settings && settings.isFull && (
          <div className="mb-4 p-3 bg-warning-soft border border-warning/30 rounded-xl flex items-center gap-2 text-xs text-fg">
            <Users className="w-4 h-4 text-warning shrink-0" />
            <span>
              注册学员已达到系统设定的最大人数上限（{settings.maxStudentsLimit}人），暂不开放新注册。
            </span>
          </div>
        )}

        <div className="grid grid-cols-2 gap-1 p-1 bg-surface-2 border border-border rounded-xl mb-5">
          <button
            type="button"
            onClick={() => {
              setIsRegister(false);
              setErrorMsg("");
            }}
            className={`py-2 text-xs font-semibold rounded-lg transition-colors ${
              !isRegister
                ? "bg-surface text-fg shadow-1"
                : "text-fg-muted hover:text-fg"
            }`}
          >
            学员登录
          </button>
          <button
            type="button"
            disabled={Boolean(isRegistrationBlocked)}
            onClick={() => {
              setIsRegister(true);
              setErrorMsg("");
            }}
            className={`py-2 text-xs font-semibold rounded-lg transition-colors ${
              isRegister
                ? "bg-surface text-fg shadow-1"
                : isRegistrationBlocked
                  ? "text-fg-subtle opacity-50 cursor-not-allowed"
                  : "text-fg-muted hover:text-fg"
            }`}
          >
            快速注册 {isRegistrationBlocked && " (已满)"}
          </button>
        </div>

        {errorMsg && (
          <div className="mb-4 p-3 rounded-xl bg-danger-soft border border-danger/30 text-danger text-xs flex items-center gap-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>{errorMsg}</span>
          </div>
        )}
        {successMsg && (
          <div className="mb-4 p-3 rounded-xl bg-success-soft border border-success/30 text-success text-xs flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            <span>{successMsg}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-medium text-fg mb-1.5">
              用户名 / 学号
            </label>
            <div className="relative">
              <User className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-fg-subtle pointer-events-none" />
              <Input
                compact
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="例如: student01 或 20240901"
                className="pl-10"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-fg mb-1.5">
              密码
            </label>
            <div className="relative">
              <KeyRound className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-fg-subtle pointer-events-none" />
              <Input
                compact
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="至少 6 位密码"
                className="pl-10"
              />
            </div>
          </div>

          <Button
            type="submit"
            disabled={loading || (isRegister && Boolean(isRegistrationBlocked))}
            className="w-full mt-2"
          >
            {loading ? (
              <span className="inline-flex items-center gap-2">
                <Spinner className="w-4 h-4 text-primary-fg" />
                <span>
                  {retryStatus || (isRegister ? "正在处理注册..." : "安全登录中...")}
                </span>
              </span>
            ) : (
              <span>{isRegister ? "立即完成注册" : "安全登录系统"}</span>
            )}
          </Button>
        </form>

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
              className="text-xs text-fg-muted hover:text-primary transition-colors inline-flex items-center gap-1"
            >
              <HelpCircle className="w-3.5 h-3.5" />
              <span>忘记密码？申请重置</span>
            </button>
          </div>
        )}

        <div className="mt-6 pt-5 border-t border-border text-center">
          <p className="text-[11px] text-fg-subtle leading-relaxed flex items-center justify-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-primary shrink-0" />
            <span>登录自动同步云端做题快照 · 退出彻底隔离设备本地数据</span>
          </p>
        </div>
      </Card>

      <Modal
        open={showForgotModal}
        onClose={() => setShowForgotModal(false)}
        title="申请重置密码"
      >
        <div className="space-y-3.5">
          <div className="p-3 rounded-xl bg-warning-soft border border-warning/30 text-[11px] text-fg leading-relaxed">
            为保护个人做题进度与数据安全，系统实行<strong>自主申请审批制</strong>
            。提交后将生成不可逆密文存入审批流，超级管理员审核通过后新密码即可生效。
          </div>

          {forgotNotice && (
            <div
              className={`p-3 rounded-xl text-xs flex items-start gap-2 border ${
                forgotNotice.type === "success"
                  ? "bg-success-soft border-success/30 text-success"
                  : "bg-danger-soft border-danger/30 text-danger"
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

          <form onSubmit={handleForgotSubmit} className="space-y-3.5">
            <div>
              <label className="block text-xs font-medium text-fg mb-1">
                账号用户名 / 学号
              </label>
              <Input
                compact
                type="text"
                required
                value={forgotUsername}
                onChange={(e) => setForgotUsername(e.target.value)}
                placeholder="请输入您的账号用户名"
              />
            </div>

            <div>
              <label className="block text-xs font-medium text-fg mb-1">
                期望设置的新密码
              </label>
              <Input
                compact
                type="password"
                required
                value={forgotNewPassword}
                onChange={(e) => setForgotNewPassword(e.target.value)}
                placeholder="至少 6 位密码"
              />
            </div>

            <div>
              <label className="block text-xs font-medium text-fg mb-1">
                确认期望新密码
              </label>
              <Input
                compact
                type="password"
                required
                value={forgotConfirmPassword}
                onChange={(e) => setForgotConfirmPassword(e.target.value)}
                placeholder="再次输入新密码"
              />
            </div>

            <div className="pt-2 flex items-center justify-end gap-2">
              <Button
                type="button"
                variant="secondary"
                size="sm"
                onClick={() => setShowForgotModal(false)}
              >
                关闭
              </Button>
              <Button type="submit" size="sm" disabled={forgotLoading}>
                {forgotLoading && <Spinner className="w-3.5 h-3.5 text-primary-fg" />}
                <span>{forgotLoading ? "正在提交..." : "提交改密申请"}</span>
              </Button>
            </div>
          </form>
        </div>
      </Modal>
    </div>
  );
}
