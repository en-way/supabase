"use client";

import { useCallback, useEffect, useRef, useState } from "react";

export type ReaderLineHeight = 1.65 | 1.8 | 2.0;

const FONT_SIZE_KEY = "enway_exam_font_size";
const LINE_HEIGHT_KEY = "enway_reader_line_height";
const LEGACY_SCALE_KEY = "enway_font_scale";

export function triggerHaptic(pattern: number | number[] = 10): void {
  if (typeof window !== "undefined" && "vibrate" in navigator) {
    try {
      navigator.vibrate(pattern);
    } catch {}
  }
}

export function useReaderPrefs() {
  const [fontSize, setFontSizeState] = useState<number>(16);
  const [lineHeight, setLineHeightState] = useState<ReaderLineHeight>(1.8);
  const fontSizeRef = useRef<number>(fontSize);
  fontSizeRef.current = fontSize;

  useEffect(() => {
    try {
      const savedSize = localStorage.getItem(FONT_SIZE_KEY);
      if (savedSize) {
        const num = Number.parseInt(savedSize, 10);
        if (!Number.isNaN(num) && num >= 13 && num <= 22) {
          fontSizeRef.current = num;
          setFontSizeState(num);
        }
      } else {
        const legacyScale = localStorage.getItem(LEGACY_SCALE_KEY);
        if (legacyScale === "medium") setFontSizeState(17);
        else if (legacyScale === "large") setFontSizeState(19);
      }

      const savedLh = localStorage.getItem(LINE_HEIGHT_KEY);
      if (savedLh === "1.65" || savedLh === "1.8" || savedLh === "2") {
        setLineHeightState(Number(savedLh) as ReaderLineHeight);
      }
    } catch {}
  }, []);

  const updateFontSize = useCallback(
    (valOrUpdater: number | ((prev: number) => number)) => {
      const next =
        typeof valOrUpdater === "function"
          ? valOrUpdater(fontSizeRef.current)
          : valOrUpdater;
      const clamped = Math.max(13, Math.min(22, next));
      fontSizeRef.current = clamped;
      setFontSizeState(clamped);
      try {
        localStorage.setItem(FONT_SIZE_KEY, String(clamped));
      } catch {}
      triggerHaptic(8);
    },
    []
  );

  const cycleLineHeight = useCallback(() => {
    setLineHeightState((prev) => {
      const next: ReaderLineHeight =
        prev === 1.65 ? 1.8 : prev === 1.8 ? 2.0 : 1.65;
      try {
        localStorage.setItem(LINE_HEIGHT_KEY, String(next));
      } catch {}
      triggerHaptic(8);
      return next;
    });
  }, []);

  return {
    fontSize,
    lineHeight,
    updateFontSize,
    cycleLineHeight,
  };
}
