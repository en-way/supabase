import { Clock, Eye, EyeOff, FileEdit, Plus, Trash2 } from "lucide-react";
import type { ExamRecord } from "@/types/exam";

interface AdminExamsTabProps {
  exams: ExamRecord[];
  isSuperAdmin: boolean;
  onOpenEdit: (exam: ExamRecord) => void;
  onTogglePublish: (exam: ExamRecord) => void;
  onDeleteExam: (exam: ExamRecord) => void;
  onSwitchToImport: () => void;
}

export function AdminExamsTab({
  exams,
  isSuperAdmin,
  onOpenEdit,
  onTogglePublish,
  onDeleteExam,
  onSwitchToImport,
}: AdminExamsTabProps) {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-base font-bold text-slate-900 dark:text-zinc-100">题库试卷总览</h3>
        <button
          onClick={onSwitchToImport}
          className="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 dark:bg-cyan-500 dark:hover:bg-cyan-400 text-white dark:text-zinc-950 text-xs font-bold flex items-center space-x-1.5 shadow-sm"
        >
          <Plus className="w-3.5 h-3.5" />
          <span>导入新试卷</span>
        </button>
      </div>

      <div className="bg-white dark:bg-[#11131a] rounded-2xl border border-slate-200 dark:border-cyan-500/20 overflow-hidden shadow-sm">
        {/* Desktop Table View */}
        <div className="hidden md:block overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-700 dark:text-zinc-300">
            <thead className="bg-slate-50 dark:bg-zinc-900/80 border-b border-slate-200 dark:border-zinc-800 text-slate-500 dark:text-zinc-400 font-semibold">
              <tr>
                <th className="p-4">试卷标题</th>
                <th className="p-4">科目</th>
                <th className="p-4">篇章 / 题数</th>
                <th className="p-4">满分 / 及格</th>
                <th className="p-4">审核状态</th>
                <th className="p-4">上架状态</th>
                <th className="p-4 text-right">操作</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 dark:divide-zinc-800">
              {exams.map((e) => {
                const isPendingUpload = e.approval_status === "pending_upload";
                const isPendingDelete = e.approval_status === "pending_delete";
                const isRejected = e.approval_status === "rejected";

                return (
                  <tr key={e.id} className="hover:bg-slate-50/60 dark:hover:bg-zinc-800/40 transition-colors">
                    <td className="p-4 font-bold text-slate-900 dark:text-zinc-100 max-w-xs truncate">{e.title}</td>
                    <td className="p-4 uppercase font-semibold text-indigo-600 dark:text-cyan-400">{e.category_id}</td>
                    <td className="p-4 text-slate-500 dark:text-zinc-400">
                      {e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题
                    </td>
                    <td className="p-4">{e.total_score}分 / {e.pass_score}分</td>
                    <td className="p-4">
                      {isPendingUpload ? (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-amber-100 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-transparent dark:border-amber-500/30 flex items-center w-fit space-x-1">
                          <Clock className="w-3 h-3" />
                          <span>待超管审批</span>
                        </span>
                      ) : isPendingDelete ? (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-rose-100 dark:bg-rose-950/40 text-rose-800 dark:text-rose-300 border border-transparent dark:border-rose-500/30 flex items-center w-fit space-x-1">
                          <Trash2 className="w-3 h-3" />
                          <span>申请删除中</span>
                        </span>
                      ) : isRejected ? (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400">
                          已驳回
                        </span>
                      ) : (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-emerald-100 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border border-transparent dark:border-emerald-500/30">
                          已通过
                        </span>
                      )}
                    </td>
                    <td className="p-4">
                      <span
                        className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                          e.is_published
                            ? "bg-emerald-100 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-transparent dark:border-emerald-500/30"
                            : "bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400"
                        }`}
                      >
                        {e.is_published ? "公开可见" : "隐藏未发布"}
                      </span>
                    </td>
                    <td className="p-4 text-right space-x-2 whitespace-nowrap">
                      {(isSuperAdmin || (e.approval_status !== "approved" && !e.is_published)) && (
                        <button
                          onClick={() => onOpenEdit(e)}
                          title="修改材料、题目与完整 JSON 文件"
                          className="inline-flex items-center space-x-1 px-2.5 py-1 text-xs font-semibold text-indigo-600 dark:text-cyan-400 bg-indigo-50 dark:bg-cyan-950/40 hover:bg-indigo-100 dark:hover:bg-cyan-900/50 rounded-lg border border-indigo-200/50 dark:border-cyan-500/30 transition-colors"
                        >
                          <FileEdit className="w-3.5 h-3.5" />
                          <span>修改材料/JSON</span>
                        </button>
                      )}
                      {isSuperAdmin && (
                        <button
                          onClick={() => onTogglePublish(e)}
                          title={e.is_published ? "点击下架隐藏" : "点击上架公开"}
                          className="p-1.5 text-slate-400 dark:text-zinc-500 hover:text-indigo-600 dark:hover:text-cyan-400 rounded-lg transition-colors"
                        >
                          {e.is_published ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                        </button>
                      )}
                      <button
                        onClick={() => onDeleteExam(e)}
                        title={isSuperAdmin ? "彻底物理删除" : "申请删除(需超管审批)"}
                        className="p-1.5 text-slate-400 dark:text-zinc-500 hover:text-rose-600 dark:hover:text-rose-400 rounded-lg transition-colors"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        {/* Mobile Exam Card List */}
        <div className="md:hidden divide-y divide-slate-100 dark:divide-zinc-800/80">
          {exams.length === 0 ? (
            <div className="p-8 text-center text-xs text-slate-400 dark:text-zinc-500">暂无试卷记录</div>
          ) : (
            exams.map((e) => {
              const isPendingUpload = e.approval_status === "pending_upload";
              const isPendingDelete = e.approval_status === "pending_delete";
              const isRejected = e.approval_status === "rejected";

              return (
                <div key={e.id} className="p-4 space-y-3">
                  <div className="flex items-start justify-between gap-2">
                    <div className="font-bold text-sm text-slate-900 dark:text-zinc-100 leading-snug">{e.title}</div>
                    <span className="uppercase text-[10px] font-bold px-2 py-0.5 rounded bg-indigo-50 dark:bg-cyan-950/60 text-indigo-600 dark:text-cyan-400 border border-indigo-200/50 dark:border-cyan-500/30 shrink-0">
                      {e.category_id}
                    </span>
                  </div>

                  <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 dark:text-zinc-400">
                    <span>{e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题</span>
                    <span>•</span>
                    <span>满分 {e.total_score} / 及格 {e.pass_score}</span>
                  </div>

                  <div className="flex flex-wrap items-center gap-2">
                    {isPendingUpload ? (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-amber-100 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-transparent dark:border-amber-500/30 flex items-center space-x-1">
                        <Clock className="w-3 h-3" />
                        <span>待超管审批</span>
                      </span>
                    ) : isPendingDelete ? (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-rose-100 dark:bg-rose-950/40 text-rose-800 dark:text-rose-300 border border-transparent dark:border-rose-500/30 flex items-center space-x-1">
                        <Trash2 className="w-3 h-3" />
                        <span>申请删除中</span>
                      </span>
                    ) : isRejected ? (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400">
                        已驳回
                      </span>
                    ) : (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-emerald-100 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border border-transparent dark:border-emerald-500/30">
                        已通过
                      </span>
                    )}

                    <span
                      className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                        e.is_published
                          ? "bg-emerald-100 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-transparent dark:border-emerald-500/30"
                          : "bg-slate-100 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400"
                      }`}
                    >
                      {e.is_published ? "公开可见" : "隐藏未发布"}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 pt-1 border-t border-slate-100 dark:border-zinc-800/60">
                    {(isSuperAdmin || (e.approval_status !== "approved" && !e.is_published)) && (
                      <button
                        onClick={() => onOpenEdit(e)}
                        className="flex-1 py-1.5 px-2.5 text-xs font-semibold text-indigo-600 dark:text-cyan-400 bg-indigo-50 dark:bg-cyan-950/40 hover:bg-indigo-100 dark:hover:bg-cyan-900/50 rounded-lg border border-indigo-200/50 dark:border-cyan-500/30 flex items-center justify-center space-x-1 transition-colors"
                      >
                        <FileEdit className="w-3.5 h-3.5" />
                        <span>修改JSON</span>
                      </button>
                    )}
                    {isSuperAdmin && (
                      <button
                        onClick={() => onTogglePublish(e)}
                        className={`p-2 rounded-lg text-xs font-semibold border transition-colors flex items-center justify-center ${
                          e.is_published
                            ? "bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-300 border-slate-200 dark:border-zinc-700"
                            : "bg-emerald-50 dark:bg-emerald-950/40 text-emerald-600 dark:text-emerald-400 border-emerald-200/60 dark:border-emerald-500/30"
                        }`}
                        title={e.is_published ? "下架隐藏" : "上架公开"}
                      >
                        {e.is_published ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
                      </button>
                    )}
                    <button
                      onClick={() => onDeleteExam(e)}
                      className="p-2 text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/30 hover:bg-rose-100 dark:hover:bg-rose-950/50 rounded-lg border border-rose-200/50 dark:border-rose-500/30 transition-colors"
                      title={isSuperAdmin ? "彻底物理删除" : "申请删除(需超管审批)"}
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              );
            })
          )}
        </div>
      </div>
    </div>
  );
}
