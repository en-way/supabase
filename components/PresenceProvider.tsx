"use client";

import React, { createContext, useContext, useEffect, useState, useMemo } from "react";
import { supabase } from "@/lib/supabase";

interface PresenceContextType {
  onlineUserIds: Set<string>;
  onlineCount: number;
}

const PresenceContext = createContext<PresenceContextType>({
  onlineUserIds: new Set(),
  onlineCount: 0,
});

export const usePresence = () => useContext(PresenceContext);

export default function PresenceProvider({ children }: { children: React.ReactNode }) {
  const [onlineUserIds, setOnlineUserIds] = useState<Set<string>>(new Set());

  useEffect(() => {
    let activeChannel: any = null;
    let isMounted = true;

    async function initPresence() {
      const { data: { session } } = await supabase.auth.getSession();
      if (!isMounted) return;

      if (!session?.user) {
        setOnlineUserIds(new Set());
        return;
      }

      // Fetch minimal profile to enrich presence state
      let username = session.user.email?.split("@")[0] || "user";
      try {
        const { data: profile } = await supabase
          .from("profiles")
          .select("username, nickname, role")
          .eq("id", session.user.id)
          .maybeSingle();
        if (profile?.username) username = profile.username;
      } catch (e) {
        // fallback to email prefix
      }

      // 🛡️ Free Quota Guard: Connect to WebSocket presence ONLY for authenticated users
      const channel = supabase.channel("online-presence", {
        config: {
          presence: {
            key: session.user.id,
          },
        },
      });

      // ⚡️ CRITICAL: Register presence callback BEFORE calling subscribe() to prevent
      // "cannot add 'presence' callbacks for realtime:online-presence after 'subscribe()'"
      channel.on("presence", { event: "sync" }, () => {
        if (!isMounted) return;
        const state = channel.presenceState();
        const userIds = new Set<string>();
        for (const key in state) {
          const presences = state[key] as any[];
          for (const p of presences) {
            if (p?.user_id) userIds.add(p.user_id);
          }
        }
        setOnlineUserIds(userIds);
      });

      channel.subscribe(async (status) => {
        if (status === "SUBSCRIBED" && isMounted) {
          try {
            await channel.track({
              user_id: session.user.id,
              username,
              online_at: new Date().toISOString(),
            });
          } catch (err) {
            console.warn("Presence track error (non-fatal):", err);
          }
        }
      });

      activeChannel = channel;
    }

    initPresence();

    // Listen to auth state changes
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === "SIGNED_IN" && session?.user) {
        initPresence();
      } else if (event === "SIGNED_OUT") {
        if (activeChannel) {
          try {
            activeChannel.untrack();
            supabase.removeChannel(activeChannel);
          } catch {}
          activeChannel = null;
        }
        setOnlineUserIds(new Set());
      }
    });

    return () => {
      isMounted = false;
      subscription.unsubscribe();
      if (activeChannel) {
        try {
          activeChannel.untrack();
          supabase.removeChannel(activeChannel);
        } catch {}
      }
    };
  }, []);

  const value = useMemo(
    () => ({
      onlineUserIds,
      onlineCount: onlineUserIds.size,
    }),
    [onlineUserIds]
  );

  return (
    <PresenceContext.Provider value={value}>
      {children}
    </PresenceContext.Provider>
  );
}
