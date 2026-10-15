"use client";

import React, { useState, useEffect, useRef, useCallback } from "react";
import { Columns, Split, Layout } from "lucide-react";

interface SplitPaneProps {
  leftPane: React.ReactNode;
  rightPane: React.ReactNode;
  storageKey?: string;
  defaultRatio?: number; // percentage for left pane (e.g. 60)
  minRatio?: number;
  maxRatio?: number;
  isZenMode?: boolean;
  className?: string;
}

export default function SplitPane({
  leftPane,
  rightPane,
  storageKey = "enway_split_ratio",
  defaultRatio = 60,
  minRatio = 35,
  maxRatio = 80,
  isZenMode = false,
  className = "",
}: SplitPaneProps) {
  const [leftRatio, setLeftRatio] = useState<number>(defaultRatio);
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // Load persisted ratio from localStorage
  useEffect(() => {
    try {
      const saved = localStorage.getItem(storageKey);
      if (saved) {
        const parsed = parseFloat(saved);
        if (!isNaN(parsed) && parsed >= minRatio && parsed <= maxRatio) {
          setLeftRatio(parsed);
        }
      }
    } catch {}
  }, [storageKey, minRatio, maxRatio]);

  const updateRatio = useCallback(
    (newRatio: number) => {
      const clamped = Math.max(minRatio, Math.min(maxRatio, newRatio));
      setLeftRatio(clamped);
      try {
        localStorage.setItem(storageKey, clamped.toFixed(1));
      } catch {}
    },
    [minRatio, maxRatio, storageKey]
  );

  // Mouse Drag Handler
  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  useEffect(() => {
    if (!isDragging) return;

    const handleMouseMove = (e: MouseEvent) => {
      if (!containerRef.current) return;
      const rect = containerRef.current.getBoundingClientRect();
      const clientX = e.clientX;
      const newRatio = ((clientX - rect.left) / rect.width) * 100;
      updateRatio(newRatio);
    };

    const handleMouseUp = () => {
      setIsDragging(false);
    };

    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("mouseup", handleMouseUp);
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none";

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
      document.body.style.cursor = "";
      document.body.style.userSelect = "";
    };
  }, [isDragging, updateRatio]);

  return (
    <div className={`space-y-2.5 ${className}`}>
      {/* PC Split Ratio Quick Controls (Hidden on mobile) */}
      <div className="hidden lg:flex items-center justify-between text-xs text-stone-500 dark:text-zinc-400 px-1">
        <div className="flex items-center space-x-1.5 font-medium">
          <Split className="w-3.5 h-3.5 text-stone-400 dark:text-zinc-500" />
          <span>分栏比例:</span>
          <span className="font-mono font-bold text-stone-700 dark:text-zinc-200">
            {Math.round(leftRatio)}% : {100 - Math.round(leftRatio)}%
          </span>
        </div>

        <div className="flex items-center space-x-1 bg-stone-100 dark:bg-zinc-800/80 p-0.5 rounded-lg border border-black/[0.04] dark:border-cyan-500/15">
          <button
            type="button"
            onClick={() => updateRatio(50)}
            title="对称平衡 (5:5 均分左右视野)"
            className={`px-2 py-0.5 rounded text-[11px] font-medium transition-all ${
              Math.round(leftRatio) === 50
                ? "bg-white dark:bg-zinc-700 text-stone-900 dark:text-zinc-100 shadow-sm font-bold"
                : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
            }`}
          >
            5:5 对称
          </button>
          <button
            type="button"
            onClick={() => updateRatio(60)}
            title="黄金标准 (6:4 适中文本与题目对照)"
            className={`px-2 py-0.5 rounded text-[11px] font-medium transition-all ${
              Math.round(leftRatio) === 60
                ? "bg-white dark:bg-zinc-700 text-stone-900 dark:text-zinc-100 shadow-sm font-bold"
                : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
            }`}
          >
            6:4 标准
          </button>
          <button
            type="button"
            onClick={() => updateRatio(70)}
            title="宽幅研读 (7:3 宽幅文章大屏精读)"
            className={`px-2 py-0.5 rounded text-[11px] font-medium transition-all ${
              Math.round(leftRatio) === 70
                ? "bg-white dark:bg-zinc-700 text-stone-900 dark:text-zinc-100 shadow-sm font-bold"
                : "text-stone-500 dark:text-zinc-400 hover:text-stone-800 dark:hover:text-zinc-200"
            }`}
          >
            7:3 宽阅读
          </button>
          <span className="text-[10px] text-stone-400 dark:text-zinc-500 px-1 border-l border-stone-200 dark:border-zinc-700">
            可拖拽中轴线
          </span>
        </div>
      </div>

      {/* Main Container */}
      <div
        ref={containerRef}
        className={`relative w-full ${isDragging ? "select-none" : ""}`}
      >
        {/* Desktop Split View (Screen >= lg) */}
        <div className="hidden lg:flex w-full items-start gap-0">
          {/* Left Pane */}
          <div
            style={{ width: `${leftRatio}%` }}
            className="shrink-0 transition-[width] duration-75"
          >
            {leftPane}
          </div>

          {/* Draggable Divider Handle */}
          <div
            onMouseDown={handleMouseDown}
            onDoubleClick={() => updateRatio(defaultRatio)}
            title="按住鼠标拖拽微调分栏宽度，双击恢复默认 6:4"
            className="w-4 shrink-0 -mx-1 group relative flex items-center justify-center cursor-col-resize self-stretch z-10 select-none py-4"
          >
            {/* Visual Line */}
            <div
              className={`w-1 h-full rounded-full transition-all duration-150 ${
                isDragging
                  ? "bg-emerald-600 dark:bg-cyber-400 w-1.5 shadow-glow-cyan"
                  : "bg-transparent group-hover:bg-emerald-500/40 dark:group-hover:bg-cyan-500/40"
              }`}
            />
            {/* Grip Dots */}
            <div
              className={`absolute top-1/2 -translate-y-1/2 w-3.5 h-7 rounded-full bg-white dark:bg-zinc-800 border border-black/10 dark:border-cyan-500/30 shadow-md flex items-center justify-center transition-all ${
                isDragging
                  ? "scale-110 border-emerald-600 dark:border-cyber-400 text-emerald-600 dark:text-cyber-400"
                  : "group-hover:scale-105 text-stone-400 dark:text-zinc-500"
              }`}
            >
              <div className="flex flex-col space-y-0.5">
                <span className="w-0.5 h-0.5 rounded-full bg-current" />
                <span className="w-0.5 h-0.5 rounded-full bg-current" />
                <span className="w-0.5 h-0.5 rounded-full bg-current" />
              </div>
            </div>
          </div>

          {/* Right Pane */}
          <div
            style={{ width: `${100 - leftRatio}%` }}
            className="shrink-0 transition-[width] duration-75 pl-1"
          >
            {rightPane}
          </div>
        </div>

        {/* Mobile / Tablet Fallback (< lg) */}
        <div className="block lg:hidden w-full">
          <div className="w-full space-y-5">
            {leftPane}
            {rightPane}
          </div>
        </div>
      </div>
    </div>
  );
}
