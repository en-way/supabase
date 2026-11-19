import { useEffect, useRef, type RefObject } from "react";

/**
 * Dismisses a floating surface on outside pointer down or Escape key press.
 */
export function useDismiss(
  open: boolean,
  onDismiss: () => void,
  refs: RefObject<HTMLElement | null> | Array<RefObject<HTMLElement | null>>
): void {
  const onDismissRef = useRef(onDismiss);
  onDismissRef.current = onDismiss;

  const refsRef = useRef(refs);
  refsRef.current = refs;

  useEffect(() => {
    if (!open) return;

    const handlePointerDown = (e: MouseEvent | TouchEvent) => {
      const target = e.target as Node | null;
      if (!target) return;

      const list = Array.isArray(refsRef.current) ? refsRef.current : [refsRef.current];
      const clickedInside = list.some((r) => r.current && r.current.contains(target));
      if (!clickedInside) {
        onDismissRef.current();
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onDismissRef.current();
      }
    };

    document.addEventListener("mousedown", handlePointerDown);
    document.addEventListener("touchstart", handlePointerDown, { passive: true });
    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("mousedown", handlePointerDown);
      document.removeEventListener("touchstart", handlePointerDown);
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [open]);
}
