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

export default function PresenceProvider({ children }: { children: React.ReactNode }) {
  const [lastTouch, setLastTouch] = React.useState<number>(0);
  const lastTouchRef = useRef<number>(0);

  useEffect(() => {
    let isMounted = true;
    let heartbeatTimer: NodeJS.Timeout | null = null;

    async function touchActivity() {
      if (!isMounted) return;
      // Do not touch if document is in background
      if (typeof document !== "undefined" && document.visibilityState === "hidden") {
        return;
      }

      const { data: { session } } = await supabase.auth.getSession();
      if (!session?.user || !isMounted) return;

      const now = Date.now();
      // Client throttling: only touch if at least 4.5 minutes elapsed since last touch
      if (now - lastTouchRef.current < 4.5 * 60 * 1000) {
        return;
      }

      try {
        lastTouchRef.current = now;
        if (isMounted) setLastTouch(now);
        await supabase.rpc("touch_user_activity");
      } catch (e) {
        // Non-fatal background activity update
      }
    }

    // Touch once on mount if authenticated
    touchActivity();

    // Regular 5-minute interval heartbeat (0 WebSocket long-lived connections)
    heartbeatTimer = setInterval(() => {
      touchActivity();
    }, 5 * 60 * 1000);

    // Visibility change handler: when student returns to tab, touch if > 5 minutes
    const handleVisibilityChange = () => {
      if (document.visibilityState === "visible") {
        touchActivity();
      }
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);

    // Auth state change listener
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === "SIGNED_IN" && session?.user) {
        touchActivity();
      }
    });

    return () => {
      isMounted = false;
      if (heartbeatTimer) clearInterval(heartbeatTimer);
      document.removeEventListener("visibilitychange", handleVisibilityChange);
      subscription.unsubscribe();
    };
  }, []);

  return (
    <PresenceContext.Provider value={{ lastTouch }}>
      {children}
    </PresenceContext.Provider>
  );
}
