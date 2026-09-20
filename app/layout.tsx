import type { Metadata } from "next";
import "./globals.css";
import Navbar from "@/components/Navbar";
import AuthGuard from "@/components/AuthGuard";
import DictionaryPopover from "@/components/DictionaryPopover";

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
    <html lang="zh-CN">
      <body className="min-h-screen bg-slate-50 text-slate-900 flex flex-col antialiased selection:bg-indigo-100 selection:text-indigo-900">
        <AuthGuard>
          <Navbar />
          <main className="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 py-6">
            {children}
          </main>
          <DictionaryPopover />
        </AuthGuard>
      </body>
    </html>
  );
}
