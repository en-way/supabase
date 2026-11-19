/**
 * Enway Durable Offline Submission & Retry Queue (持久化离线交卷与重试队列)
 * 
 * 核心目标：
 * 1. 杜绝 500 人高并发突发（如 22:00 晚自习交卷）时，由于网络瞬断、PostgREST 429 限流
 *    或 503 临时繁忙导致学员答题卡与考试成绩在客户端被丢弃。
 * 2. 在物理发送前，优先将交卷任务落盘写入 localStorage 持久化保障槽。
 * 3. 采用 Full Jitter 指数退避重试算法与 online/visibilitychange 自愈唤醒机制。
 */

import { supabase } from "./supabase";
import { uploadBackupToCloud } from "./storage";
import { runWithHighPriority } from "./quotaSentinel";
import type { SubmissionTaskPayload } from "@/types/storage";

export interface SubmissionTask {
  id: string;
  type: "exam_result" | "cloud_backup";
  payload: SubmissionTaskPayload;
  attempts: number;
  lastError?: string;
  createdAt: string;
  nextRetryAt: number;
}

const STORAGE_QUEUE_KEY = "enway_offline_submission_tasks";
let isFlushing = false;
let flushTimer: ReturnType<typeof setTimeout> | null = null;

// 读取队列中的待处理任务
export function getPendingSubmissionTasks(): SubmissionTask[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(STORAGE_QUEUE_KEY);
    if (!raw) return [];
    const tasks: SubmissionTask[] = JSON.parse(raw);
    return Array.isArray(tasks) ? tasks : [];
  } catch {
    return [];
  }
}

// 保存队列到本地
function savePendingSubmissionTasks(tasks: SubmissionTask[]) {
  if (typeof window === "undefined") return;
  try {
    if (tasks.length === 0) {
      localStorage.removeItem(STORAGE_QUEUE_KEY);
    } else {
      localStorage.setItem(STORAGE_QUEUE_KEY, JSON.stringify(tasks));
    }
  } catch (err) {
    console.warn("[SubmissionQueue] Failed to persist tasks:", err);
  }
}

/**
 * 清理本地挂起的离线交卷与备份任务（供安全退出或跨账号切换调用）
 */
export function clearPendingSubmissionTasks() {
  if (flushTimer) {
    clearTimeout(flushTimer);
    flushTimer = null;
  }
  savePendingSubmissionTasks([]);
}

/**
 * 压入待提交任务并持久化落盘，返回任务 ID
 */
export function enqueueSubmissionTask(
  type: SubmissionTask["type"],
  payload: SubmissionTaskPayload
): string {
  const taskId = `task_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;

  const tasks = getPendingSubmissionTasks();
  // 相同 examId 的未完成交卷任务或同类 cloud_backup 任务进行替换去重，继承退避进度
  const payloadExamId =
    typeof payload === "object" && payload !== null && "examId" in payload
      ? (payload as { examId?: unknown }).examId
      : undefined;
  const isSameTask = (t: SubmissionTask) => {
    if (type === "exam_result") {
      const existingExamId =
        typeof t.payload === "object" && t.payload !== null && "examId" in t.payload
          ? (t.payload as { examId?: unknown }).examId
          : undefined;
      return t.type === "exam_result" && existingExamId === payloadExamId;
    }
    return t.type === "cloud_backup";
  };
  const existingTask = tasks.find(isSameTask);
  const newTask: SubmissionTask = {
    id: taskId,
    type,
    payload,
    attempts: existingTask ? existingTask.attempts : 0,
    createdAt: existingTask ? existingTask.createdAt : new Date().toISOString(),
    nextRetryAt: existingTask ? existingTask.nextRetryAt : Date.now(),
  };
  const filtered = tasks.filter((t) => !isSameTask(t));
  filtered.push(newTask);
  savePendingSubmissionTasks(filtered);

  // 异步触发非阻塞队列刷新（带 0~1500ms 随机微抖动）
  const jitterMs = Math.floor(Math.random() * 1500);
  setTimeout(() => {
    flushSubmissionQueue();
  }, jitterMs);

  return taskId;
}

/**
 * 调度执行离线队列刷新
 */
export async function flushSubmissionQueue(): Promise<{
  processed: number;
  failed: number;
}> {
  if (isFlushing || typeof window === "undefined") {
    return { processed: 0, failed: 0 };
  }
  if (typeof navigator !== "undefined" && !navigator.onLine) {
    return { processed: 0, failed: 0 };
  }

  isFlushing = true;
  let processed = 0;
  let failed = 0;

  try {
    const tasks = getPendingSubmissionTasks();
    if (tasks.length === 0) {
      return { processed: 0, failed: 0 };
    }

    const now = Date.now();
    const remainingTasks: SubmissionTask[] = [];

    for (const task of tasks) {
      // 若尚未到达重试冷静期，保留并在稍后重试
      if (now < task.nextRetryAt) {
        remainingTasks.push(task);
        continue;
      }

      // 预检登录态：若未登录，直接挂起任务并延后重试，绝不调用 RPC 造成无效网络轰炸
      try {
        const { data: { session } } = await supabase.auth.getSession();
        if (!session?.user) {
          // 未登录状态：延长退避至 10 分钟，等待重新登录事件唤醒
          task.nextRetryAt = Date.now() + 10 * 60 * 1000;
          remainingTasks.push(task);
          continue;
        }
      } catch {
        task.nextRetryAt = Date.now() + 60 * 1000;
        remainingTasks.push(task);
        continue;
      }

      try {
        if (task.type === "exam_result") {
          // 1. 尝试执行云端备份同步（启用高优先级豁免通道；活跃打点由 uploadBackupToCloud 节流完成）
          const backupRes = await runWithHighPriority(() => uploadBackupToCloud());
          if (!backupRes.success) {
            if (backupRes.error?.includes("未登录")) {
              // User is logged out — delay 10 minutes without burning retry budget
              task.nextRetryAt = Date.now() + 10 * 60 * 1000;
              remainingTasks.push(task);
              continue;
            }
            throw new Error(backupRes.error);
          }
          processed += 1;
        } else if (task.type === "cloud_backup") {
          const backupRes = await uploadBackupToCloud();
          if (!backupRes.success) {
            if (backupRes.error?.includes("未登录")) {
              task.nextRetryAt = Date.now() + 10 * 60 * 1000;
              remainingTasks.push(task);
              continue;
            }
            throw new Error(backupRes.error);
          }
          processed += 1;
        }
      } catch (err: unknown) {
        failed += 1;
        task.attempts += 1;
        task.lastError = err instanceof Error ? err.message : String(err);

        // Full Jitter 指数退避: 常规上限 60s；连续失败 >= 10 次降频至 5 分钟
        const baseDelay =
          task.attempts >= 10
            ? 300_000
            : Math.min(60_000, 1000 * Math.pow(2, Math.min(task.attempts, 6)));
        const jitter = Math.floor(Math.random() * 2000);
        task.nextRetryAt = Date.now() + baseDelay + jitter;

        remainingTasks.push(task);
      }
    }

    savePendingSubmissionTasks(remainingTasks);

    // 若仍有未完成任务，预约下一次自动检查
    if (remainingTasks.length > 0) {
      const nextWakeup = Math.min(
        ...remainingTasks.map((t) => Math.max(1000, t.nextRetryAt - Date.now()))
      );
      if (flushTimer) clearTimeout(flushTimer);
      flushTimer = setTimeout(() => {
        flushSubmissionQueue();
      }, Math.max(2000, nextWakeup));
    }
  } finally {
    isFlushing = false;
  }

  return { processed, failed };
}

// 自动挂载网络恢复与页面可见性监听
if (typeof window !== "undefined") {
  window.addEventListener("online", () => {
    flushSubmissionQueue();
  });

  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") {
      flushSubmissionQueue();
    }
  });

  // 监听用户登录事件：登录成功后立即重设未完成任务的冷静期并主动刷新队列
  supabase.auth.onAuthStateChange((event, session) => {
    if (event === "SIGNED_IN" && session?.user) {
      const pending = getPendingSubmissionTasks();
      if (pending.length > 0) {
        pending.forEach((t) => {
          t.nextRetryAt = Date.now();
        });
        savePendingSubmissionTasks(pending);
        flushSubmissionQueue();
      }
    }
  });

  // 页面加载 3 秒后尝试静默刷新一次残留队列
  setTimeout(() => {
    flushSubmissionQueue();
  }, 3000);
}
