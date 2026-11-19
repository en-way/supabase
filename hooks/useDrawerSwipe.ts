import { useCallback, useEffect, useRef, useState } from "react";
import type React from "react";

export interface UseDrawerSwipeOptions {
  open?: boolean;
  thresholdY?: number;
  ratio?: number;
  dismissDelayMs?: number;
  onDismissHaptic?: () => void;
}

/**
 * Handles interactive downward swipe-to-dismiss touch gestures for bottom sheets/drawers,
 * providing 1:1 drag follow, spring-back on cancel, and smooth slide-out on dismiss.
 */
export function useDrawerSwipe(options: UseDrawerSwipeOptions = {}) {
  const {
    open = true,
    thresholdY = 96,
    ratio = 1.8,
    dismissDelayMs = 200,
    onDismissHaptic,
  } = options;

  const [dragOffsetY, setDragOffsetY] = useState(0);
  const [isDragging, setIsDragging] = useState(false);
  const [isDismissing, setIsDismissing] = useState(false);

  const drawerTouchStartRef = useRef<{ x: number; y: number } | null>(null);
  const dismissTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const hapticRef = useRef(onDismissHaptic);
  hapticRef.current = onDismissHaptic;

  const clearDismissTimer = useCallback(() => {
    if (dismissTimerRef.current !== null) {
      clearTimeout(dismissTimerRef.current);
      dismissTimerRef.current = null;
    }
  }, []);

  useEffect(() => {
    if (!open) {
      clearDismissTimer();
      drawerTouchStartRef.current = null;
      setDragOffsetY(0);
      setIsDragging(false);
      setIsDismissing(false);
    }
  }, [open, clearDismissTimer]);

  useEffect(() => {
    return () => {
      clearDismissTimer();
    };
  }, [clearDismissTimer]);

  const handleDrawerTouchStart = useCallback(
    (e: React.TouchEvent) => {
      if (isDismissing) return;
      if (e.touches.length === 1) {
        drawerTouchStartRef.current = {
          x: e.touches[0].clientX,
          y: e.touches[0].clientY,
        };
        setIsDragging(false);
      }
    },
    [isDismissing]
  );

  const handleDrawerTouchMove = useCallback(
    (e: React.TouchEvent) => {
      if (!drawerTouchStartRef.current || isDismissing) return;
      const touch = e.touches[0];
      if (!touch) return;
      const deltaX = touch.clientX - drawerTouchStartRef.current.x;
      const deltaY = touch.clientY - drawerTouchStartRef.current.y;

      if (deltaY > 0 && deltaY >= Math.abs(deltaX)) {
        setIsDragging(true);
        setDragOffsetY(Math.round(deltaY));
      } else if (deltaY <= 0) {
        setDragOffsetY(0);
      }
    },
    [isDismissing]
  );

  const handleDrawerTouchEnd = useCallback(
    (e: React.TouchEvent, onClose: () => void) => {
      if (!drawerTouchStartRef.current || isDismissing) return;
      const touch = e.changedTouches[0];
      const deltaX = touch.clientX - drawerTouchStartRef.current.x;
      const deltaY = touch.clientY - drawerTouchStartRef.current.y;
      drawerTouchStartRef.current = null;
      setIsDragging(false);

      // Downward swipe >= thresholdY with vertical dominance dismisses the drawer
      if (deltaY >= thresholdY && deltaY > Math.abs(deltaX) * ratio) {
        hapticRef.current?.();
        setIsDismissing(true);
        clearDismissTimer();
        dismissTimerRef.current = setTimeout(() => {
          dismissTimerRef.current = null;
          setIsDismissing(false);
          setDragOffsetY(0);
          onClose();
        }, dismissDelayMs);
      } else {
        setDragOffsetY(0);
      }
    },
    [isDismissing, thresholdY, ratio, dismissDelayMs, clearDismissTimer]
  );

  const panelStyle: React.CSSProperties = isDismissing
    ? {
        transform: "translateY(100%)",
        transition: `transform ${dismissDelayMs}ms cubic-bezier(0.2, 0.8, 0.2, 1)`,
      }
    : isDragging
      ? {
          transform: `translateY(${dragOffsetY}px)`,
          transition: "none",
        }
      : {
          transform: "translateY(0px)",
          transition: "transform 200ms ease-out",
        };

  const backdropStyle: React.CSSProperties = isDismissing
    ? {
        opacity: 0,
        transition: `opacity ${dismissDelayMs}ms ease-out`,
      }
    : isDragging
      ? {
          opacity: Math.max(0.2, 1 - dragOffsetY / 320),
          transition: "none",
        }
      : {
          opacity: 1,
          transition: "opacity 200ms ease-out",
        };

  return {
    dragOffsetY,
    isDragging,
    isDismissing,
    panelStyle,
    backdropStyle,
    handleDrawerTouchStart,
    handleDrawerTouchMove,
    handleDrawerTouchEnd,
  };
}
