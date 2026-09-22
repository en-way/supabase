import type { Metadata } from "next";
import "./globals.css";
import Navbar from "@/components/Navbar";
import AuthGuard from "@/components/AuthGuard";
import PresenceProvider from "@/components/PresenceProvider";
import DictionaryPopover from "@/components/DictionaryPopover";
import NetworkStatusIndicator from "@/components/NetworkStatusIndicator";
import SentinelAlertCapsule from "@/components/SentinelAlertCapsule";

export const metadata: Metadata = {
  title: "Enway - 在线英语刷题与全真模考系统",
  description: "面向大学英语四六级与考研英语的专业级在线刷题、全真模考、智能错题本与生词学习平台",
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
            __html: `(function(){try{var t=localStorage.getItem('enway_theme')||(window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');if(t==='dark'){document.documentElement.classList.add('dark');}else{document.documentElement.classList.remove('dark');}}catch(e){}})();`,
          }}
        />
      </head>
      <body className="min-h-screen bg-background text-foreground flex flex-col antialiased selection:bg-nature-200 selection:text-nature-900 dark:selection:bg-cyber-500/30 dark:selection:text-cyber-200">
        <NetworkStatusIndicator />
        <SentinelAlertCapsule />
        <AuthGuard>
          <PresenceProvider>
            <Navbar />
            <main className="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 py-6">
              {children}
            </main>
            <DictionaryPopover />
          </PresenceProvider>
        </AuthGuard>
      </body>
    </html>
  );
}
