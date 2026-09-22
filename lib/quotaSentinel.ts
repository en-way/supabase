/**
 * Enway Client Quota Sentinel (客户端配额熔断守护哨兵)
 * 
 * 核心目标：在前端构建一道主动自愈与防刷防火墙，拦截由于未预料的死循环、
 * 恶性高频重渲染或脚本恶意请求导致的 Supabase 50 万次/月免费配额瞬时耗尽。
 * 
 * 特性：
 * 1. 10 秒滑动窗口速率监测（Sliding Window Rate-Limiter）
 * 2. 双层自适应熔断：
 *    - 10s 内 > 12 次：软限削峰排队（自适应指数退避延迟 300~1000ms）
 *    - 10s 内 > 25 次：硬断路器熔断（直接阻断非特权 API 30 秒，0 网络消耗）
 * 3. 特权白名单豁免：登出（/auth/v1/logout）与关键考场交卷绝对不阻断
 * 4. 每日与会话调用度量统计持久化
 * 5. 全局事件通知（enway_sentinel_alert），联动学员端胶囊与管理看板
 */

export type CircuitBreakerState = "CLOSED" | "OPEN" | "HALF_OPEN";

export interface SentinelStats {
  date: string;
  totalRequests: number;
  throttledRequests: number;
  trippedCount: number;
  blockedRequests: number;
  lastTrippedAt?: string;
}

export interface SentinelAlertDetail {
  state: CircuitBreakerState;
  remainingCooldownSeconds: number;
  currentWindowRps: number;
  stats: SentinelStats;
}

// 阈值配置
const WINDOW_MS = 10_000; // 10秒滑动窗口
const SOFT_LIMIT = 12;    // 软限阈值（开始排队退避）
const HARD_LIMIT = 25;    // 硬限阈值（触发断路熔断）
const COOLDOWN_MS = 30_000; // 熔断冷却时长 30 秒

const STATS_STORAGE_KEY = "enway_sentinel_stats";

// 内存滑动窗口与状态机
let requestTimestamps: number[] = [];
let circuitState: CircuitBreakerState = "CLOSED";
let cooldownExpiresAt = 0;
let cooldownTimer: any = null;

// 内存持久化后备（供 SSR 或 Node 运行时使用）
let memoryStats: SentinelStats = {
  date: new Date().toISOString().slice(0, 10),
  totalRequests: 0,
  throttledRequests: 0,
  trippedCount: 0,
  blockedRequests: 0,
};

// 获取今日统计
export function getSentinelStats(): SentinelStats {
  const todayStr = new Date().toISOString().slice(0, 10);
  if (typeof window === "undefined") {
    if (memoryStats.date !== todayStr) {
      memoryStats = {
        date: todayStr,
        totalRequests: 0,
        throttledRequests: 0,
        trippedCount: 0,
        blockedRequests: 0,
      };
    }
    return memoryStats;
  }

  try {
    const raw = localStorage.getItem(STATS_STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed.date === todayStr) {
        memoryStats = parsed;
        return parsed;
      }
    }
  } catch {}

  const initial: SentinelStats = {
    date: todayStr,
    totalRequests: 0,
    throttledRequests: 0,
    trippedCount: 0,
    blockedRequests: 0,
  };
  saveSentinelStats(initial);
  return initial;
}

function saveSentinelStats(stats: SentinelStats) {
  memoryStats = stats;
  if (typeof window === "undefined") return;
  try {
    localStorage.setItem(STATS_STORAGE_KEY, JSON.stringify(stats));
  } catch {}
}

function mutateStats(updater: (stats: SentinelStats) => void) {
  const stats = getSentinelStats();
  updater(stats);
  saveSentinelStats(stats);
}

// 派发状态更新事件
function emitSentinelAlert() {
  if (typeof window === "undefined") return;
  const now = Date.now();
  const remaining = Math.max(0, Math.ceil((cooldownExpiresAt - now) / 1000));
  const recentCount = getActiveWindowCount(now);
  const detail: SentinelAlertDetail = {
    state: circuitState,
    remainingCooldownSeconds: remaining,
    currentWindowRps: Number((recentCount / (WINDOW_MS / 1000)).toFixed(1)),
    stats: getSentinelStats(),
  };

  window.dispatchEvent(new CustomEvent("enway_sentinel_alert", { detail }));
}

// 计算滑动窗口内请求数
function getActiveWindowCount(now: number): number {
  const cutoff = now - WINDOW_MS;
  requestTimestamps = requestTimestamps.filter((t) => t > cutoff);
  return requestTimestamps.length;
}

// 触发熔断断路
function tripCircuitBreaker() {
  circuitState = "OPEN";
  cooldownExpiresAt = Date.now() + COOLDOWN_MS;
  mutateStats((s) => {
    s.trippedCount += 1;
    s.lastTrippedAt = new Date().toISOString();
  });

  emitSentinelAlert();

  if (cooldownTimer) clearTimeout(cooldownTimer);
  cooldownTimer = setTimeout(() => {
    circuitState = "HALF_OPEN";
    emitSentinelAlert();
  }, COOLDOWN_MS);
}

// 手动或自动重置哨兵状态
export function resetSentinelState() {
  circuitState = "CLOSED";
  cooldownExpiresAt = 0;
  requestTimestamps = [];
  if (cooldownTimer) clearTimeout(cooldownTimer);
  emitSentinelAlert();
}

/**
 * 判断请求是否属于特权豁免通道（例如账号安全登出、正式交卷）
 */
function isExemptRequest(input: RequestInfo | URL, init?: RequestInit): boolean {
  try {
    const urlStr = typeof input === "string" ? input : input instanceof URL ? input.href : input.url;
    // 1. 退出登录接口
    if (urlStr.includes("/auth/v1/logout")) {
      return true;
    }
    // 2. 携带了高优先级标头的关键请求
    const headers = init?.headers;
    if (headers) {
      if (headers instanceof Headers) {
        if (headers.get("x-enway-priority") === "high") return true;
      } else if (Array.isArray(headers)) {
        if (headers.some(([k, v]) => k.toLowerCase() === "x-enway-priority" && v === "high")) return true;
      } else if (typeof headers === "object") {
        if ((headers as Record<string, string>)["x-enway-priority"] === "high") return true;
      }
    }
  } catch {}
  return false;
}

/**
 * 专供 Supabase client 使用的全局 fetch 拦截代理
 */
export async function sentinelFetch(
  input: RequestInfo | URL,
  init?: RequestInit
): Promise<Response> {
  const now = Date.now();
  const isExempt = isExemptRequest(input, init);

  // 1. 如果断路器处于 OPEN 状态
  if (circuitState === "OPEN") {
    if (now >= cooldownExpiresAt) {
      // 冷却期满，转为半开嗅探状态
      circuitState = "HALF_OPEN";
      emitSentinelAlert();
    } else if (!isExempt) {
      // 拦截并阻断请求，直接返回合成的 429 响应，杜绝物理打到 Supabase 云端
      mutateStats((s) => {
        s.blockedRequests += 1;
      });
      emitSentinelAlert();

      const remainingSec = Math.ceil((cooldownExpiresAt - now) / 1000);
      return new Response(
        JSON.stringify({
          error: "Client Quota Sentinel Tripped",
          message: `客户端流量防刷保护生效中：检测到异常高频请求，已暂时挂起网络同步（还剩 ${remainingSec} 秒）。`,
          sentinel_blocked: true,
        }),
        {
          status: 429,
          headers: {
            "Content-Type": "application/json",
            "Retry-After": String(remainingSec),
          },
        }
      );
    }
  }

  // 2. 记录请求与滑动窗口速率监测（豁免请求不计入惩罚窗口）
  if (!isExempt) {
    getActiveWindowCount(now);
    requestTimestamps.push(now);
    const windowCount = requestTimestamps.length;

    // 二级硬熔断：10s 内请求超 25 次
    if (windowCount > HARD_LIMIT) {
      console.warn(
        `[Sentinel] ⚠️ 触发断路器硬熔断！10秒内发起 ${windowCount} 次 API 请求，进入 30 秒保护冷静期。`
      );
      tripCircuitBreaker();

      return new Response(
        JSON.stringify({
          error: "Client Quota Sentinel Tripped",
          message: "客户端检测到异常死循环或脚本请求，已启动防爆熔断保护，暂停云端通信 30 秒。",
          sentinel_blocked: true,
        }),
        {
          status: 429,
          headers: {
            "Content-Type": "application/json",
            "Retry-After": "30",
          },
        }
      );
    }

    // 一级软限削峰：10s 内请求超 12 次，执行微排队退避延迟
    if (windowCount > SOFT_LIMIT) {
      mutateStats((s) => {
        s.throttledRequests += 1;
      });
      const excess = windowCount - SOFT_LIMIT;
      const backoffMs = Math.min(1000, excess * 150 + Math.floor(Math.random() * 100));
      await new Promise((resolve) => setTimeout(resolve, backoffMs));
    }
  }

  // 3. 执行物理网络请求
  try {
    const res = await fetch(input, init);
    mutateStats((s) => {
      s.totalRequests += 1;
    });

    // 如果半开嗅探请求成功，断路器安全闭合
    if (circuitState === "HALF_OPEN") {
      circuitState = "CLOSED";
      emitSentinelAlert();
    }

    return res;
  } catch (err) {
    mutateStats((s) => {
      s.totalRequests += 1;
    });
    throw err;
  }
}

/**
 * 快捷读取当前断路器状态
 */
export function getCircuitBreakerState(): {
  state: CircuitBreakerState;
  remainingCooldown: number;
  recentRps: number;
} {
  const now = Date.now();
  const count = getActiveWindowCount(now);
  const remaining = Math.max(0, Math.ceil((cooldownExpiresAt - now) / 1000));
  return {
    state: circuitState,
    remainingCooldown: remaining,
    recentRps: Number((count / (WINDOW_MS / 1000)).toFixed(1)),
  };
}
