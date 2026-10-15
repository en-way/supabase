"use client";

import React, { useEffect } from "react";
import { Keyboard, X, ArrowLeft, ArrowRight, ArrowUp, ArrowDown, BookOpen, Bookmark, Maximize2, HelpCircle } from "lucide-react";

interface KeyboardShortcutsModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function KeyboardShortcutsModal({
  isOpen,
  onClose,
}: KeyboardShortcutsModalProps) {
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const shortcutGroups = [
    {
      title: "选项与作答",
      items: [
        { keys: ["A", "B", "C", "D"], desc: "直接选择对应选项（新题型支持 E/F/G）" },
      ],
    },
    {
      title: "翻题与文章滚动",
      items: [
        { keys: ["←", "J"], desc: "上一题（自动切换篇章并置顶）" },
        { keys: ["→", "K"], desc: "下一题" },
        { keys: ["↑", "↓"], desc: "平滑向上 / 向下滚动左侧阅读篇章" },
      ],
    },
    {
      title: "考场研习工具",
      items: [
        { keys: ["M", "Tab"], desc: "打开 / 关闭全卷答题卡" },
        { keys: ["F"], desc: "收藏 / 取消收藏当前试题" },
        { keys: ["Z"], desc: "开启 / 退出沉浸专注全屏模式 (Zen Mode)" },
      ],
    },
    {
      title: "全局辅助",
      items: [
        { keys: ["?", "H"], desc: "打开本快捷键速查卡" },
        { keys: ["Esc"], desc: "关闭任何浮层、抽屉或退出专注模式" },
      ],
    },
  ];

  return (
    <div
      className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in duration-150"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <div className="bg-white dark:bg-[#11131a] rounded-3xl border border-black/[0.08] dark:border-cyan-500/25 p-6 shadow-2xl w-full max-w-lg flex flex-col animate-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-zinc-800">
          <div className="flex items-center space-x-2.5">
            <div className="p-2 rounded-xl bg-emerald-50 dark:bg-cyan-950/40 text-emerald-700 dark:text-cyber-300 border border-emerald-200/50 dark:border-cyan-500/20">
              <Keyboard className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-stone-900 dark:text-zinc-100">
                PC 端键盘快捷键速查
              </h3>
              <p className="text-xs text-stone-400 dark:text-zinc-500">
                双手不离键盘，极速作答与全真研习
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-full bg-stone-100 dark:bg-zinc-800 text-stone-400 hover:text-stone-700 dark:hover:text-zinc-200 transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Shortcuts List */}
        <div className="py-4 space-y-4 max-h-[60vh] overflow-y-auto pr-1">
          {shortcutGroups.map((group, gIdx) => (
            <div key={gIdx} className="space-y-2">
              <h4 className="text-[11px] font-bold text-stone-400 dark:text-zinc-500 uppercase tracking-wider">
                {group.title}
              </h4>
              <div className="space-y-1.5 bg-stone-50/70 dark:bg-zinc-900/60 p-3 rounded-2xl border border-black/[0.03] dark:border-cyan-500/10">
                {group.items.map((item, idx) => (
                  <div
                    key={idx}
                    className="flex items-center justify-between py-1 text-xs"
                  >
                    <span className="text-stone-700 dark:text-zinc-300 font-medium">
                      {item.desc}
                    </span>
                    <div className="flex items-center space-x-1 font-mono shrink-0">
                      {item.keys.map((k, kIdx) => (
                        <kbd
                          key={kIdx}
                          className="px-2 py-0.5 rounded-lg bg-white dark:bg-zinc-800 border border-stone-200 dark:border-zinc-700 text-stone-800 dark:text-zinc-200 text-xs font-bold shadow-subtle"
                        >
                          {k}
                        </kbd>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="pt-3 border-t border-stone-100 dark:border-zinc-800 flex items-center justify-between text-xs text-stone-400 dark:text-zinc-500">
          <span>提示：输入框聚焦时快捷键自动暂停</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-emerald-700 dark:bg-cyber-500 text-white dark:text-[#090a0f] font-bold shadow-subtle hover:bg-emerald-800 dark:hover:bg-cyber-400 transition-colors"
          >
            我知道了 (Esc)
          </button>
        </div>
      </div>
    </div>
  );
}
