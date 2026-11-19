import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class",
  content: [
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        bg: "rgb(var(--bg) / <alpha-value>)",
        surface: {
          DEFAULT: "rgb(var(--surface) / <alpha-value>)",
          2: "rgb(var(--surface-2) / <alpha-value>)",
          3: "rgb(var(--surface-3) / <alpha-value>)",
        },
        border: {
          DEFAULT: "rgb(var(--border) / <alpha-value>)",
          strong: "rgb(var(--border-strong) / <alpha-value>)",
        },
        fg: {
          DEFAULT: "rgb(var(--fg) / <alpha-value>)",
          muted: "rgb(var(--fg-muted) / <alpha-value>)",
          subtle: "rgb(var(--fg-subtle) / <alpha-value>)",
        },
        primary: {
          DEFAULT: "rgb(var(--primary) / <alpha-value>)",
          hover: "rgb(var(--primary-hover) / <alpha-value>)",
          fg: "rgb(var(--primary-fg) / <alpha-value>)",
          soft: "rgb(var(--primary-soft) / <alpha-value>)",
          "soft-fg": "rgb(var(--primary-soft-fg) / <alpha-value>)",
        },
        success: {
          DEFAULT: "rgb(var(--success) / <alpha-value>)",
          soft: "rgb(var(--success-soft) / <alpha-value>)",
        },
        danger: {
          DEFAULT: "rgb(var(--danger) / <alpha-value>)",
          soft: "rgb(var(--danger-soft) / <alpha-value>)",
        },
        warning: {
          DEFAULT: "rgb(var(--warning) / <alpha-value>)",
          soft: "rgb(var(--warning-soft) / <alpha-value>)",
        },
        info: {
          DEFAULT: "rgb(var(--info) / <alpha-value>)",
          soft: "rgb(var(--info-soft) / <alpha-value>)",
        },
        hl: {
          yellow: "var(--hl-yellow)",
          green: "var(--hl-green)",
        },
        overlay: "var(--overlay)",
        background: "rgb(var(--bg) / <alpha-value>)",
        foreground: "rgb(var(--fg) / <alpha-value>)",
      },
      fontFamily: {
        sans: ["var(--font-sans)"],
        reading: ["var(--font-reading)"],
        mono: ["var(--font-mono)"],
      },
      borderRadius: {
        sm: "6px",
        md: "10px",
        lg: "14px",
        xl: "18px",
      },
      boxShadow: {
        1: "0 1px 2px rgb(35 31 26 / 0.06)",
        2: "0 4px 14px -4px rgb(35 31 26 / 0.12)",
        pop: "0 12px 32px -8px rgb(35 31 26 / 0.2)",
        // Temporary compatibility shadows (all non-glowing)
        subtle: "0 1px 2px rgb(35 31 26 / 0.06)",
        card: "0 1px 3px rgb(35 31 26 / 0.05), 0 4px 12px rgb(35 31 26 / 0.04)",
        "card-hover": "0 8px 24px -6px rgb(35 31 26 / 0.12), 0 2px 6px rgb(35 31 26 / 0.05)",
        float: "0 12px 32px -8px rgb(35 31 26 / 0.2)",
        pill: "0 2px 8px -2px rgb(35 31 26 / 0.08)",
        "glow-cyan": "0 1px 3px rgb(35 31 26 / 0.08)",
        "glow-emerald": "0 1px 3px rgb(35 31 26 / 0.08)",
      },
      zIndex: {
        base: "0",
        sticky: "20",
        nav: "30",
        dropdown: "40",
        backdrop: "50",
        sheet: "55",
        modal: "60",
        selection: "65",
        popover: "70",
        toast: "80",
        blocking: "90",
      },
      transitionTimingFunction: {
        spring: "cubic-bezier(0.16, 1, 0.3, 1)",
        "bounce-subtle": "cubic-bezier(0.34, 1.56, 0.64, 1)",
      },
    },
  },
  plugins: [],
};
export default config;
