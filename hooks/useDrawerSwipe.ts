import { useCallback, useRef } from "react";
import type React from "react";

export interface UseDrawerSwipeOptions {
  thresholdY?: number;
  ratio?: number;
  onDismissHaptic?: () => void;
}

/**
 * Handles downward swipe-to-dismiss touch gestures for bottom sheets/drawers.
 */
export function useDrawerSwipe(options: UseDrawerSwipeOptions = {}) {
  const { thresholdY = 150, ratio = 2.0, onDismissHaptic } = options;
  const drawerTouchStartRef = useRef<{ x: number; y: number } | null>(null);
  const hapticRef = useRef(onDismissHaptic);
  hapticRef.current = onDismissHaptic;

  const handleDrawerTouchStart = useCallback((e: React.TouchEvent) => {
    if (e.touches.length === 1) {
      drawerTouchStartRef.current = {
        x: e.touches[0].clientX,
        y: e.touches[0].clientY,
      };
    }
  }, []);

  const handleDrawerTouchEnd = useCallback(
    (e: React.TouchEvent, onClose: () => void) => {
      if (!drawerTouchStartRef.current) return;
      const deltaX = e.changedTouches[0].clientX - drawerTouchStartRef.current.x;
      const deltaY = e.changedTouches[0].clientY - drawerTouchStartRef.current.y;
      drawerTouchStartRef.current = null;

      // Downward swipe >= thresholdY with vertical dominance dismisses the drawer
      if (deltaY >= thresholdY && deltaY > Math.abs(deltaX) * ratio) {
        hapticRef.current?.();
        onClose();
      }
    },
    [thresholdY, ratio]
  );

  return { handleDrawerTouchStart, handleDrawerTouchEnd };
}
