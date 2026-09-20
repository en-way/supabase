import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        primary: {
          50: "#eef2ff",
          100: "#e0e7ff",
          200: "#c7d2fe",
          300: "#a5b4fc",
          400: "#818cf8",
          500: "#6366f1",
          600: "#4f46e5",
          700: "#4338ca",
          800: "#3730a3",
          900: "#312e81",
        },
      },
      boxShadow: {
        "subtle": "0 1px 2px rgba(0, 0, 0, 0.03), 0 1px 1px rgba(0, 0, 0, 0.02)",
        "card": "0 1px 3px rgba(0, 0, 0, 0.02), 0 6px 16px rgba(0, 0, 0, 0.02)",
        "card-hover": "0 12px 32px -8px rgba(0, 0, 0, 0.07), 0 4px 12px rgba(0, 0, 0, 0.02)",
        "float": "0 20px 40px -12px rgba(0, 0, 0, 0.1), 0 8px 16px -4px rgba(0, 0, 0, 0.03)",
        "pill": "0 2px 8px -2px rgba(0, 0, 0, 0.06), 0 1px 4px -1px rgba(0, 0, 0, 0.04)",
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
