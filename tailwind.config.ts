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
        background: "var(--background)",
        foreground: "var(--foreground)",
        // Living Nature light mode accents
        nature: {
          50: "#f0fdf4",
          100: "#dcfce7",
          200: "#bbf7d0",
          300: "#86efac",
          400: "#4ade80",
          500: "#22c55e",
          600: "#16a34a",
          700: "#15803d",
          800: "#166534",
          900: "#14532d",
        },
        // Cyber Void dark mode accents
        cyber: {
          50: "#ecfeff",
          100: "#cffafe",
          200: "#a5f3fc",
          300: "#67e8f9",
          400: "#22d3ee",
          500: "#06b6d4",
          600: "#0891b2",
          700: "#0e7490",
          800: "#155e75",
          900: "#164e63",
          950: "#083344",
        },
      },
      boxShadow: {
        "subtle": "0 1px 2px rgba(0, 0, 0, 0.03), 0 1px 1px rgba(0, 0, 0, 0.02)",
        "card": "0 1px 3px rgba(0, 0, 0, 0.02), 0 6px 16px rgba(0, 0, 0, 0.02)",
        "card-hover": "0 12px 32px -8px rgba(0, 0, 0, 0.07), 0 4px 12px rgba(0, 0, 0, 0.02)",
        "float": "0 20px 40px -12px rgba(0, 0, 0, 0.1), 0 8px 16px -4px rgba(0, 0, 0, 0.03)",
        "pill": "0 2px 8px -2px rgba(0, 0, 0, 0.06), 0 1px 4px -1px rgba(0, 0, 0, 0.04)",
        "glow-cyan": "0 0 20px -3px rgba(6, 182, 212, 0.25)",
        "glow-emerald": "0 0 20px -3px rgba(16, 185, 129, 0.25)",
      },
      transitionTimingFunction: {
        "spring": "cubic-bezier(0.16, 1, 0.3, 1)",
        "bounce-subtle": "cubic-bezier(0.34, 1.56, 0.64, 1)",
      },
    },
  },
  plugins: [],
};
export default config;
