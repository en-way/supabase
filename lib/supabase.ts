import { createClient } from "@supabase/supabase-js";
import { sentinelFetch } from "@/lib/quotaSentinel";

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || "https://pghybspsjtzihpzpahcf.supabase.co";
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBnaHlic3BzanR6aWhwenBhaGNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk3NjQ2OTgsImV4cCI6MjEwNTM0MDY5OH0.64uRYk9fCvrEfn4ifhk-PSd1ypGjVz_PTiHwgBPiHpM";

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    persistSession: true,
    autoRefreshToken: true,
  },
  global: {
    fetch: sentinelFetch,
  },
});
