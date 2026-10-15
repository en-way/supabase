import "./globals.css";
import Navbar from "@/components/Navbar";
import AuthGuard from "@/components/AuthGuard";
import PresenceProvider from "@/components/PresenceProvider";
import DictionaryPopover from "@/components/DictionaryPopover";
import NetworkStatusIndicator from "@/components/NetworkStatusIndicator";
import SentinelAlertCapsule from "@/components/SentinelAlertCapsule";
import MobileTabBar from "@/components/MobileTabBar";

import type { Metadata, Viewport } from "next";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  viewportFit: "cover",
  themeColor: "#0f172a",
};

export const metadata: Metadata = {
  title: {
    default: "Enway 考研英语 · 历年真题沉浸式研习系统",
    template: "%s | Enway 考研英语",
  },
  description: "面向全国硕士研究生统一招生考试英语（英语一 / 英语二）的权威专业级历年真题研习、分栏双读、全真限时模考与官方黄皮书精解平台",
  keywords: ["考研英语", "考研英语一", "考研英语二", "考研真题", "真题模考", "在线刷题", "黄皮书精解", "智能错题本"],
  manifest: "/manifest.json",
  appleWebApp: {
    capable: true,
    statusBarStyle: "black-translucent",
    title: "考研英语",
  },
  icons: {
    icon: "/icon.svg",
    apple: "/icon.svg",
  },
  openGraph: {
    title: "Enway 考研英语 · 历年真题沉浸式研习系统",
    description: "全国硕士研究生统一招生考试英语（英语一 / 英语二）权威历年真题研习与全真模考系统",
    siteName: "Enway 考研英语",
    locale: "zh_CN",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN" suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var t=localStorage.getItem('enway_theme')||(window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');if(t==='dark'){document.documentElement.classList.add('dark');}else{document.documentElement.classList.remove('dark');}}catch(e){}if(typeof window!=='undefined'){window.addEventListener('error',function(e){var m=(e&&e.message)?e.message:'';if(m.indexOf('Loading chunk')!==-1||m.indexOf('Failed to fetch dynamically imported module')!==-1){var l=Number(sessionStorage.getItem('enway_chunk_reload_ts')||'0');if(Date.now()-l>8000){sessionStorage.setItem('enway_chunk_reload_ts',String(Date.now()));window.location.reload();}}});window.addEventListener('unhandledrejection',function(e){var m=(e&&e.reason)?(e.reason.message||String(e.reason)):'';if(m.indexOf('Loading chunk')!==-1||m.indexOf('Failed to fetch dynamically imported module')!==-1){var l=Number(sessionStorage.getItem('enway_chunk_reload_ts')||'0');if(Date.now()-l>8000){sessionStorage.setItem('enway_chunk_reload_ts',String(Date.now()));window.location.reload();}}});}})();`,
          }}
        />
      </head>
      <body className="min-h-screen bg-background text-foreground flex flex-col antialiased selection:bg-nature-200 selection:text-nature-900 dark:selection:bg-cyber-500/30 dark:selection:text-cyber-200">
        <NetworkStatusIndicator />
        <SentinelAlertCapsule />
        <AuthGuard>
          <PresenceProvider>
            <Navbar />
            <main className="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 pt-4 sm:pt-6 pb-24 md:pb-6">
              {children}
            </main>
            <MobileTabBar />
            <DictionaryPopover />
          </PresenceProvider>
        </AuthGuard>
      </body>
    </html>
  );
}
