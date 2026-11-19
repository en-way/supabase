import { useEffect, useRef } from "react";

/**
 * Guards keyboard shortcuts against modifier combos, IME composition, and editable targets.
 */
export function isEditableKeyboardEvent(e: KeyboardEvent): boolean {
  const target = e.target as HTMLElement | null;
  return Boolean(
    e.ctrlKey ||
      e.metaKey ||
      e.altKey ||
      e.isComposing ||
      target instanceof HTMLInputElement ||
      target instanceof HTMLTextAreaElement ||
      target?.isContentEditable ||
      target?.closest?.("input, textarea, [contenteditable='true']")
  );
}

/**
 * Attaches a global keydown listener guarded against inputs, textareas, IME composition, and editable elements.
 */
export function useKeyboardGuard(
  handler: (e: KeyboardEvent) => void,
  enabled = true
): void {
  const handlerRef = useRef(handler);
  handlerRef.current = handler;

  useEffect(() => {
    if (!enabled) return;

    const listener = (e: KeyboardEvent) => {
      if (isEditableKeyboardEvent(e)) {
        return;
      }
      handlerRef.current(e);
    };

    window.addEventListener("keydown", listener);
    return () => window.removeEventListener("keydown", listener);
  }, [enabled]);
}
