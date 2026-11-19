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
        <h3 className="text-base font-bold text-fg">题库试卷总览</h3>
        <button
          onClick={onSwitchToImport}
          className="px-3.5 py-2 rounded-xl bg-primary hover:opacity-95 text-primary-fg text-xs font-bold flex items-center space-x-1.5 shadow-sm"
        >
          <Plus className="w-3.5 h-3.5" />
          <span>导入新试卷</span>
        </button>
      </div>

      <div className="bg-surface rounded-2xl border border-border overflow-hidden shadow-sm">
        {/* Desktop Table View */}
        <div className="hidden md:block overflow-x-auto">
          <table className="w-full text-left text-xs text-fg">
            <thead className="bg-surface-2 border-b border-border text-fg-muted font-semibold">
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
            <tbody className="divide-y divide-border">
              {exams.map((e) => {
                const isPendingUpload = e.approval_status === "pending_upload";
                const isPendingDelete = e.approval_status === "pending_delete";
                const isRejected = e.approval_status === "rejected";

                return (
                  <tr key={e.id} className="hover:bg-surface-2 transition-colors">
                    <td className="p-4 font-bold text-fg max-w-xs truncate">{e.title}</td>
                    <td className="p-4 uppercase font-semibold text-primary">{e.category_id}</td>
                    <td className="p-4 text-fg-muted">
                      {e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题
                    </td>
                    <td className="p-4">{e.total_score}分 / {e.pass_score}分</td>
                    <td className="p-4">
                      {isPendingUpload ? (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-warning-soft text-warning border border-transparent flex items-center w-fit space-x-1">
                          <Clock className="w-3 h-3" />
                          <span>待超管审批</span>
                        </span>
                      ) : isPendingDelete ? (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-danger-soft text-danger border border-transparent flex items-center w-fit space-x-1">
                          <Trash2 className="w-3 h-3" />
                          <span>申请删除中</span>
                        </span>
                      ) : isRejected ? (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-surface-2 text-fg-muted">
                          已驳回
                        </span>
                      ) : (
                        <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-success-soft text-success border border-transparent">
                          已通过
                        </span>
                      )}
                    </td>
                    <td className="p-4">
                      <span
                        className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                          e.is_published
                            ? "bg-success-soft text-success border border-transparent"
                            : "bg-surface-2 text-fg-muted"
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
                          className="inline-flex items-center space-x-1 px-2.5 py-1 text-xs font-semibold text-primary bg-primary-soft hover:bg-indigo-100 rounded-lg border border-primary/30 transition-colors"
                        >
                          <FileEdit className="w-3.5 h-3.5" />
                          <span>修改材料/JSON</span>
                        </button>
                      )}
                      {isSuperAdmin && (
                        <button
                          onClick={() => onTogglePublish(e)}
                          title={e.is_published ? "点击下架隐藏" : "点击上架公开"}
                          className="p-1.5 text-fg-subtle hover:text-indigo-600 rounded-lg transition-colors"
                        >
                          {e.is_published ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                        </button>
                      )}
                      <button
                        onClick={() => onDeleteExam(e)}
                        title={isSuperAdmin ? "彻底物理删除" : "申请删除(需超管审批)"}
                        className="p-1.5 text-fg-subtle hover:text-rose-600 rounded-lg transition-colors"
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
        <div className="md:hidden divide-y divide-border">
          {exams.length === 0 ? (
            <div className="p-8 text-center text-xs text-fg-subtle">暂无试卷记录</div>
          ) : (
            exams.map((e) => {
              const isPendingUpload = e.approval_status === "pending_upload";
              const isPendingDelete = e.approval_status === "pending_delete";
              const isRejected = e.approval_status === "rejected";

              return (
                <div key={e.id} className="p-4 space-y-3">
                  <div className="flex items-start justify-between gap-2">
                    <div className="font-bold text-sm text-fg leading-snug">{e.title}</div>
                    <span className="uppercase text-[10px] font-bold px-2 py-0.5 rounded bg-primary-soft text-primary border border-primary/30 shrink-0">
                      {e.category_id}
                    </span>
                  </div>

                  <div className="flex flex-wrap items-center gap-2 text-xs text-fg-muted">
                    <span>{e.passages?.[0]?.count || 0} 篇 / {e.questions?.[0]?.count || 0} 题</span>
                    <span>•</span>
                    <span>满分 {e.total_score} / 及格 {e.pass_score}</span>
                  </div>

                  <div className="flex flex-wrap items-center gap-2">
                    {isPendingUpload ? (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-warning-soft text-warning border border-transparent flex items-center space-x-1">
                        <Clock className="w-3 h-3" />
                        <span>待超管审批</span>
                      </span>
                    ) : isPendingDelete ? (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-danger-soft text-danger border border-transparent flex items-center space-x-1">
                        <Trash2 className="w-3 h-3" />
                        <span>申请删除中</span>
                      </span>
                    ) : isRejected ? (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-surface-2 text-fg-muted">
                        已驳回
                      </span>
                    ) : (
                      <span className="px-2 py-0.5 rounded-md font-bold text-[10px] bg-success-soft text-success border border-transparent">
                        已通过
                      </span>
                    )}

                    <span
                      className={`px-2 py-0.5 rounded-md font-bold text-[10px] ${
                        e.is_published
                          ? "bg-success-soft text-success border border-transparent"
                          : "bg-surface-2 text-fg-muted"
                      }`}
                    >
                      {e.is_published ? "公开可见" : "隐藏未发布"}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 pt-1 border-t border-border">
                    {(isSuperAdmin || (e.approval_status !== "approved" && !e.is_published)) && (
                      <button
                        onClick={() => onOpenEdit(e)}
                        className="flex-1 py-1.5 px-2.5 text-xs font-semibold text-primary bg-primary-soft hover:bg-indigo-100 rounded-lg border border-primary/30 flex items-center justify-center space-x-1 transition-colors"
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
                            ? "bg-surface-2 text-fg-muted border-border"
                            : "bg-success-soft text-success border-success/30"
                        }`}
                        title={e.is_published ? "下架隐藏" : "上架公开"}
                      >
                        {e.is_published ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
                      </button>
                    )}
                    <button
                      onClick={() => onDeleteExam(e)}
                      className="p-2 text-danger bg-danger-soft hover:bg-rose-100 rounded-lg border border-danger/30 transition-colors"
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
