import { resolve } from 'node:path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        brhc: resolve(__dirname, 'brhc.html'),
        studybible: resolve(__dirname, 'studybible.html'),
        downloads: resolve(__dirname, 'downloads.html'),
        usermanual: resolve(__dirname, 'usermanual.html'),
      },
    },
  },
})
