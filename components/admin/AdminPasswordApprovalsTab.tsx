import { Check, CheckCircle2, RefreshCw, X } from "lucide-react";
import type { PasswordResetRequestRecord } from "@/types/user";

interface AdminPasswordApprovalsTabProps {
  passwordRequests: PasswordResetRequestRecord[];
  loadingPwdRequests: boolean;
  reviewNotes: Record<string, string>;
  processingRequestId: string | null;
  onRefresh: () => void;
  onChangeReviewNote: (requestId: string, note: string) => void;
  onReviewPassword: (requestId: string, approve: boolean) => void;
}

export function AdminPasswordApprovalsTab({
  passwordRequests,
  loadingPwdRequests,
  reviewNotes,
  processingRequestId,
  onRefresh,
  onChangeReviewNote,
  onReviewPassword,
}: AdminPasswordApprovalsTabProps) {
  const pendingPasswordRequests = passwordRequests.filter((r) => r.status === "pending");
  const historyPasswordRequests = passwordRequests.filter((r) => r.status !== "pending");

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <div className="flex items-center space-x-2">
            <h3 className="text-base font-bold text-fg">密码审批工作台</h3>
            <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-warning-soft text-warning border border-warning/30">
              全员自主申请制
            </span>
          </div>
          <p className="text-xs text-fg-muted mt-0.5">
            学员在登录页提交「找回密码」或个人中心提交改密申请，均生成不可逆密文汇聚于此等待超级管理员核准
          </p>
        </div>
        <button
          onClick={onRefresh}
          disabled={loadingPwdRequests}
          className="p-2 text-fg-muted hover:bg-surface-2 rounded-xl transition-colors disabled:opacity-50"
          title="刷新审批队列"
        >
          <RefreshCw className={`w-4 h-4 ${loadingPwdRequests ? "animate-spin" : ""}`} />
        </button>
      </div>

      {/* Pending Section */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <h4 className="text-xs font-bold text-fg flex items-center space-x-1.5">
            <span>待审核改密申请</span>
            <span className="px-1.5 py-0.2 rounded-full bg-amber-500 text-white text-[10px] font-bold">
              {pendingPasswordRequests.length}
            </span>
          </h4>
        </div>

        {pendingPasswordRequests.length === 0 ? (
          <div className="text-center py-12 bg-surface rounded-2xl border border-dashed border-slate-300">
            <CheckCircle2 className="w-10 h-10 text-emerald-400 mx-auto mb-2.5" />
            <p className="text-fg-muted font-bold text-sm">当前暂无待审核的密码重置申请</p>
            <p className="text-xs text-fg-subtle mt-1">学员在登录页或个人中心发起申请后，将实时出现在这里</p>
          </div>
        ) : (
          <div className="grid gap-3.5">
            {pendingPasswordRequests.map((req) => {
              const isProcessing = processingRequestId === req.id;
              return (
                <div
                  key={req.id}
                  className="p-5 bg-surface rounded-2xl border border-border shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4"
                >
                  <div className="space-y-1.5">
                    <div className="flex items-center space-x-2">
                      <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-warning-soft text-warning border border-warning/30">
                        待审批
                      </span>
                      <span className="text-xs font-mono font-bold text-primary">
                        {req.username}
                      </span>
                      {req.nickname && (
                        <span className="text-xs text-fg-muted font-medium">
                          ({req.nickname})
                        </span>
                      )}
                      <span className="text-[10px] px-1.5 py-0.5 rounded bg-surface-2 text-fg-muted font-mono">
                        {req.role === "admin" ? "🛡️ 管理员" : "🎓 学员"}
                      </span>
                    </div>
                    <p className="text-xs text-fg-muted">
                      提交时间: {new Date(req.created_at).toLocaleString()} · 目标哈希: 10轮 bcrypt 安全密文 (0 明文暴露)
                    </p>
                    <div className="pt-1">
                      <input
                        type="text"
                        placeholder="审批批注 (选填，例如：身份已确认/予以通过)"
                        value={reviewNotes[req.id] || ""}
                        onChange={(e) => onChangeReviewNote(req.id, e.target.value)}
                        className="w-full sm:w-80 px-2.5 py-1 text-xs bg-surface-2 border border-border rounded-lg text-fg placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                      />
                    </div>
                  </div>

                  <div className="flex items-center space-x-2 shrink-0">
                    <button
                      onClick={() => onReviewPassword(req.id, true)}
                      disabled={isProcessing}
                      className="px-4 py-2 bg-primary hover:opacity-95 disabled:opacity-50 text-primary-fg rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-colors"
                    >
                      <Check className="w-3.5 h-3.5" />
                      <span>{isProcessing ? "处理中..." : "通过生效"}</span>
                    </button>
                    <button
                      onClick={() => onReviewPassword(req.id, false)}
                      disabled={isProcessing}
                      className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 disabled:opacity-50 text-danger rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition-colors"
                    >
                      <X className="w-3.5 h-3.5" />
                      <span>驳回</span>
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* History Section */}
      {historyPasswordRequests.length > 0 && (
        <div className="space-y-3 pt-4 border-t border-border">
          <h4 className="text-xs font-bold text-fg">
            最近审批历史 ({historyPasswordRequests.length})
          </h4>
          <div className="bg-surface rounded-2xl border border-border overflow-hidden shadow-sm">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-fg">
                <thead className="bg-surface-2 border-b border-border text-fg-muted font-semibold">
                  <tr>
                    <th className="p-3.5">用户名</th>
                    <th className="p-3.5">角色</th>
                    <th className="p-3.5">申请时间</th>
                    <th className="p-3.5">状态</th>
                    <th className="p-3.5">审核批注</th>
                    <th className="p-3.5">审核时间</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-border">
                  {historyPasswordRequests.slice(0, 20).map((h) => (
                    <tr key={h.id}>
                      <td className="p-3.5 font-mono font-bold text-fg">
                        {h.username} {h.nickname && <span className="font-normal text-slate-500">({h.nickname})</span>}
                      </td>
                      <td className="p-3.5">
                        <span className="text-[10px] px-1.5 py-0.5 rounded bg-surface-2 font-mono">
                          {h.role}
                        </span>
                      </td>
                      <td className="p-3.5 text-fg-muted font-mono text-[11px]">
                        {new Date(h.created_at).toLocaleString()}
                      </td>
                      <td className="p-3.5">
                        <span
                          className={`px-2 py-0.5 rounded-md text-[10px] font-bold ${
                            h.status === "approved"
                              ? "bg-success-soft text-success"
                              : h.status === "rejected"
                              ? "bg-danger-soft text-danger"
                              : "bg-surface-2 text-fg-muted"
                          }`}
                        >
                          {h.status === "approved" ? "✅ 已批准" : h.status === "rejected" ? "❌ 已驳回" : "已撤回"}
                        </span>
                      </td>
                      <td className="p-3.5 text-fg-muted text-[11px]">{h.review_note || "--"}</td>
                      <td className="p-3.5 text-fg-muted font-mono text-[11px]">
                        {h.reviewed_at ? new Date(h.reviewed_at).toLocaleString() : "--"}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
