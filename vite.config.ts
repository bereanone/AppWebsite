import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  base: "/AppWebsite/",  // 👈 ensures assets load correctly on GitHub Pages
});
