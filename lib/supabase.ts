import { createClient } from "@supabase/supabase-js";
import { sentinelFetch } from "@/lib/quotaSentinel";

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || "https://pghybspsjtzihpzpahcf.supabase.co";
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBnaHlic3BzanR6aWhwenBhaGNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk3NjQ2OTgsImV4cCI6MjEwNTM0MDY5OH0.64uRYk9fCvrEfn4ifhk-PSd1ypGjVz_PTiHwgBPiHpM";

/**
 * 0-WebSocket 极致配额保护桩（Stub）
 * 彻底阻断 Phoenix Socket 传输层实例化原生 WebSocket，
 * 确保全站实时并发连接数锁定为绝对的 0 / 200 (0%)。
 */
class BlockedRealtimeTransport {
  static CONNECTING = 0;
  static OPEN = 1;
  static CLOSING = 2;
  static CLOSED = 3;

  readyState = BlockedRealtimeTransport.CLOSED;

  constructor() {
    if (process.env.NODE_ENV !== "production") {
      console.warn("[QuotaArmor] Realtime WebSocket is permanently blocked to enforce 0/200 connection quota.");
    }
  }

  close() {}
  send() {}
  addEventListener() {}
  removeEventListener() {}
}

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    persistSession: true,
    autoRefreshToken: true,
  },
  global: {
    fetch: sentinelFetch,
  },
  realtime: {
    transport: BlockedRealtimeTransport as any,
    timeout: 0,
    heartbeatIntervalMs: 0,
  },
});

// 客户端层二次加固：封禁 channel 创建与主动 connect
(supabase as any).channel = (channelName: string) => {
  console.warn(
    `[QuotaArmor] Blocked supabase.channel("${channelName}"): Enway operates on a strict 0-WebSocket architecture.`
  );
  return {
    subscribe: (cb?: (status: string) => void) => {
      if (cb) cb("TIMED_OUT");
      return { unsubscribe: () => Promise.resolve("ok") };
    },
    on: () => ({
      subscribe: (cb?: (status: string) => void) => {
        if (cb) cb("TIMED_OUT");
        return { unsubscribe: () => Promise.resolve("ok") };
      },
    }),
    unsubscribe: () => Promise.resolve("ok"),
  };
};

if (supabase.realtime) {
  supabase.realtime.connect = () => {
    console.warn("[QuotaArmor] Blocked supabase.realtime.connect(): WebSocket connections are forbidden.");
  };
}
