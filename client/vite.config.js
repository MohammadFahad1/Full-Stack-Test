import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Every request to /api is forwarded to the backend on port 3001.
// This means no CORS setup is needed.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:3001",
    },
  },
});
