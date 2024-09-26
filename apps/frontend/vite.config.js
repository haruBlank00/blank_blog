import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/scripts/main.ts'),
      },
      output: {
        entryFileNames: 'script.js',
        chunkFileNames: 'script.js',
        assetFileNames: ({ name }) => {
          if (name && name.endsWith('.css')) {
            return 'style.css';
          }
          return '[name].[ext]';
        },
      },
    },
    outDir: './static/frontend/assets',
    emptyOutDir: true,
  },
  css: {
    postcss: './postcss.config.js',
  },
  server: {
    port: 3000,
  },
});
