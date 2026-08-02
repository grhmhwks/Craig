import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          const normalized = id.replaceAll("\\", "/");
          if (!normalized.includes("/node_modules/")) return undefined;
          if (
            /\/node_modules\/(react|react-dom|scheduler)\//.test(normalized)
          ) {
            return "react";
          }
          if (normalized.includes("/node_modules/katex/")) return "math";
          if (
            normalized.includes("markdown") ||
            normalized.includes("remark") ||
            normalized.includes("rehype") ||
            normalized.includes("unified") ||
            normalized.includes("micromark")
          ) {
            return "markdown";
          }
          return undefined;
        },
      },
    },
  },
  server: {
    host: "127.0.0.1",
    port: 5173,
    proxy: {
      "/api": "http://127.0.0.1:8000",
    },
  },
});
