import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  optimizeDeps: {
    include: ['jwt-decode']
  },
  // server: {
  //   hmr: {
  //     overlay: false
  //   }
  // },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      // 'jwt-decode': 'jwt-decode/build/esm/index.js',

    },
  },
})
