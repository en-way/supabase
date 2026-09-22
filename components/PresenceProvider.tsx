"use client";

import React, { createContext, useContext, useEffect, useRef } from "react";
import { supabase } from "@/lib/supabase";

interface PresenceContextType {
  lastTouch: number;
}

const PresenceContext = createContext<PresenceContextType>({
  lastTouch: 0,
});

export const usePresence = () => useContext(PresenceContext);

// 全局跨标签页与全局组件共享的打点时间戳 key
export const PRESENCE_STORAGE_KEY = "enway_last_presence_touch";
// 节流与打点间隔：提升至 20 分钟（1,200 秒），阈值 18 分钟
const HEARTBEAT_INTERVAL_MS = 20 * 60 * 1000;
const THROTTLE_THRESHOLD_MS = 18 * 60 * 1000;
// 用户键鼠操作判定静默挂机阈值：10 分钟
const USER_IDLE_TIMEOUT_MS = 10 * 60 * 1000;

/**
 * 供登录、交卷、云备份等关键节点显式调用，共享打点时间，避免后续心跳重复打点
 */
export function markActivityTouched() {
  if (typeof window !== "undefined") {
    try {
      localStorage.setItem(PRESENCE_STORAGE_KEY, String(Date.now()));
    } catch {}
  }
}

export default function PresenceProvider({ children }: { children: React.ReactNode }) {
  const [lastTouch, setLastTouch] = React.useState<number>(0);
  const lastUserActionRef = useRef<number>(Date.now());

  useEffect(() => {
    let isMounted = true;
    let heartbeatTimer: NodeJS.Timeout | null = null;

    // 1. 监听物理键鼠操作，确认学员是否真正活跃（非挂机空耗）
    const recordUserAction = () => {
      lastUserActionRef.current = Date.now();
    };

    window.addEventListener("mousemove", recordUserAction, { passive: true });
    window.addEventListener("keydown", recordUserAction, { passive: true });
    window.addEventListener("touchstart", recordUserAction, { passive: true });
    window.addEventListener("scroll", recordUserAction, { passive: true });

    async function touchActivity() {
      if (!isMounted) return;

      // 门禁 A：页面在后台标签页或已最小化，坚决不打点
      if (typeof document !== "undefined" && document.visibilityState === "hidden") {
        return;
      }

      // 门禁 B：用户超过 10 分钟无任何按键或鼠标移动，判定为离开挂机，直接休眠！
      const now = Date.now();
      if (now - lastUserActionRef.current > USER_IDLE_TIMEOUT_MS) {
        return;
      }

      // 门禁 C：跨标签页及跨操作全局节流（检查 localStorage）
      let lastGlobalTouch = 0;
      try {
        lastGlobalTouch = Number(localStorage.getItem(PRESENCE_STORAGE_KEY) || "0");
      } catch {}

      if (now - lastGlobalTouch < THROTTLE_THRESHOLD_MS) {
        return;
      }

      // 门禁 D：仅在已登录且拥有有效 Session 时才发起轻量打点
      const { data: { session } } = await supabase.auth.getSession();
      if (!session?.user || !isMounted) return;

      try {
        // 先行占位写入，彻底阻断其他标签页并发同时发起请求
        markActivityTouched();
        if (isMounted) setLastTouch(now);

        await supabase.rpc("touch_user_activity");
      } catch (e) {
        // 后台打点异常不阻断业务
      }
    }

    // 挂载时延时 2 秒初次打点（避开冷启动资源争抢）
    const initialTimer = setTimeout(() => {
      touchActivity();
    }, 2000);

    // 每 20 分钟执行一次心跳检测
    heartbeatTimer = setInterval(() => {
      touchActivity();
    }, HEARTBEAT_INTERVAL_MS);

    // 页面切回前台时，若已满 20 分钟才触发一次
    const handleVisibilityChange = () => {
      if (document.visibilityState === "visible") {
        touchActivity();
      }
    };
    document.addEventListener("visibilitychange", handleVisibilityChange);

    return () => {
      isMounted = false;
      clearTimeout(initialTimer);
      if (heartbeatTimer) clearInterval(heartbeatTimer);
      window.removeEventListener("mousemove", recordUserAction);
      window.removeEventListener("keydown", recordUserAction);
      window.removeEventListener("touchstart", recordUserAction);
      window.removeEventListener("scroll", recordUserAction);
      document.removeEventListener("visibilitychange", handleVisibilityChange);
    };
  }, []);

  return (
    <PresenceContext.Provider value={{ lastTouch }}>
      {children}
    </PresenceContext.Provider>
  );
}
