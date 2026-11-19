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

  // Lock body scroll when modal is active
  useEffect(() => {
    if (!isOpen) return;
    const originalOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = originalOverflow;
    };
  }, [isOpen]);

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
      className="fixed inset-0 z-modal bg-overlay/60 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in duration-150 overflow-y-auto overscroll-contain"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <div className="bg-surface rounded-3xl border border-border p-6 shadow-pop w-full max-w-lg max-h-[85dvh] flex flex-col animate-in zoom-in-95 duration-150">
        <div className="flex items-center justify-between pb-4 border-b border-border">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-primary-soft text-primary border border-primary/25">
              <Keyboard className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-fg">PC 端键盘快捷键速查</h3>
              <p className="text-xs text-fg-subtle">
                双手不离键盘，极速作答与全真研习
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-full bg-surface-2 text-fg-muted hover:text-fg transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        <div className="py-4 space-y-4 max-h-[60dvh] overflow-y-auto overscroll-contain pr-1">
          {shortcutGroups.map((group, gIdx) => (
            <div key={gIdx} className="space-y-2">
              <h4 className="text-[11px] font-bold text-fg-subtle uppercase tracking-wider">
                {group.title}
              </h4>
              <div className="space-y-1.5 bg-surface-2/80 p-3 rounded-2xl border border-border">
                {group.items.map((item, idx) => (
                  <div
                    key={idx}
                    className="flex items-center justify-between py-1 text-xs"
                  >
                    <span className="text-fg font-medium">{item.desc}</span>
                    <div className="flex items-center gap-1 font-mono shrink-0">
                      {item.keys.map((k, kIdx) => (
                        <kbd
                          key={kIdx}
                          className="px-2 py-0.5 rounded-lg bg-surface border border-border text-fg text-xs font-bold shadow-1"
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

        <div className="pt-3 border-t border-border flex items-center justify-between text-xs text-fg-subtle">
          <span>提示：输入框聚焦时快捷键自动暂停</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-primary text-primary-fg font-bold shadow-1 hover:opacity-95 transition-opacity"
          >
            我知道了 (Esc)
          </button>
        </div>
      </div>
    </div>
  );
}
