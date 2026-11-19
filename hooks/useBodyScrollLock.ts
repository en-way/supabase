import { useEffect } from "react";

/**
 * Locks document.body vertical scrolling while a modal or mobile bottom drawer is open.
 */
export function useBodyScrollLock(locked: boolean): void {
  useEffect(() => {
    if (!locked) return;
    const originalOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = originalOverflow;
    };
  }, [locked]);
}
