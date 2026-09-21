"use client";

import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";

export default function PresenceProvider({ children }: { children: React.ReactNode }) {
  const [sessionUser, setSessionUser] = useState<any>(null);

  useEffect(() => {
    let activeChannel: any = null;
    let isMounted = true;

    async function initPresence() {
      const { data: { session } } = await supabase.auth.getSession();
      if (!isMounted) return;

      if (!session?.user) {
        setSessionUser(null);
        return;
      }

      setSessionUser(session.user);

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

      channel.subscribe(async (status) => {
        if (status === "SUBSCRIBED" && isMounted) {
          await channel.track({
            user_id: session.user.id,
            username,
            online_at: new Date().toISOString(),
          });
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
          activeChannel.untrack();
          supabase.removeChannel(activeChannel);
          activeChannel = null;
        }
        setSessionUser(null);
      }
    });

    return () => {
      isMounted = false;
      subscription.unsubscribe();
      if (activeChannel) {
        activeChannel.untrack();
        supabase.removeChannel(activeChannel);
      }
    };
  }, []);

  return <>{children}</>;
}
