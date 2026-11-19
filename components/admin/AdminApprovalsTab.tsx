import { Check, CheckCircle2, RefreshCw, Trash2, X } from "lucide-react";
import type { ExamRecord } from "@/types/exam";
import type { ExamApprovalActionType } from "./types";

interface AdminApprovalsTabProps {
  pendingExams: ExamRecord[];
  onRefresh: () => void;
  onApprovalAction: (examId: string, actionType: ExamApprovalActionType) => void;
}

export function AdminApprovalsTab({
  pendingExams,
  onRefresh,
  onApprovalAction,
}: AdminApprovalsTabProps) {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">试卷待审批大厅</h3>
          <p className="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">
            普通管理员提交的新试卷与删除申请，需在此由超级管理员核准
          </p>
        </div>
        <button
          onClick={onRefresh}
          className="p-2 text-slate-500 dark:text-zinc-400 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-xl transition-colors"
          title="刷新待审列表"
        >
          <RefreshCw className="w-4 h-4" />
        </button>
      </div>

      {pendingExams.length === 0 ? (
        <div className="text-center py-16 bg-white dark:bg-[#11131a] rounded-2xl border border-dashed border-slate-300 dark:border-zinc-800">
          <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
          <p className="text-slate-600 dark:text-zinc-300 font-bold text-sm">当前暂无待审批的试卷申请</p>
          <p className="text-xs text-slate-400 dark:text-zinc-500 mt-1">
            普通管理员提交的上传或删除将会实时出现在这里
          </p>
        </div>
      ) : (
        <div className="grid gap-4">
          {pendingExams.map((item) => {
            const isUpload = item.approval_status === "pending_upload";
            return (
              <div
                key={item.id}
                className="p-5 bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-cyan-500/20 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4"
              >
                <div className="space-y-1.5">
                  <div className="flex items-center space-x-2">
                    <span
                      className={`px-2.5 py-0.5 rounded-md text-[10px] font-bold ${
                        isUpload
                          ? "bg-amber-100 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-transparent dark:border-amber-500/30"
                          : "bg-rose-100 dark:bg-rose-950/40 text-rose-800 dark:text-rose-300 border border-transparent dark:border-rose-500/30"
                      }`}
                    >
                      {isUpload ? "📤 新试卷上传待审" : "🗑️ 申请删除试卷待审"}
                    </span>
                    <span className="text-xs font-mono font-bold text-indigo-600 dark:text-cyan-400 uppercase">
                      {item.category_id}
                    </span>
                    <span className="text-xs text-slate-400 dark:text-zinc-500">年份: {item.year}</span>
                  </div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-zinc-100">{item.title}</h4>
                  <p className="text-xs text-slate-500 dark:text-zinc-400">
                    篇章: {item.passages?.[0]?.count || 0} 篇 · 包含客观题: {item.questions?.[0]?.count || 0} 道 · 提交时间:{" "}
                    {item.created_at ? new Date(item.created_at).toLocaleString() : "--"}
                  </p>
                </div>

                <div className="flex items-center space-x-2 shrink-0">
                  {isUpload ? (
                    <>
                      <button
                        onClick={() => onApprovalAction(item.id, "approve_upload")}
                        className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-colors"
                      >
                        <Check className="w-3.5 h-3.5" />
                        <span>批准发布上架</span>
                      </button>
                      <button
                        onClick={() => onApprovalAction(item.id, "reject_upload")}
                        className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-200 rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition-colors"
                      >
                        <X className="w-3.5 h-3.5" />
                        <span>驳回上传</span>
                      </button>
                    </>
                  ) : (
                    <>
                      <button
                        onClick={() => onApprovalAction(item.id, "approve_delete")}
                        className="px-3.5 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-xl text-xs font-bold flex items-center space-x-1.5 shadow-sm transition-colors"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                        <span>批准彻底删除</span>
                      </button>
                      <button
                        onClick={() => onApprovalAction(item.id, "reject_delete")}
                        className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-200 rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition-colors"
                      >
                        <X className="w-3.5 h-3.5" />
                        <span>驳回删除申请</span>
                      </button>
                    </>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
