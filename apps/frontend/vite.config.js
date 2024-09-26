import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/scripts/main.ts'), 
      },
    },
    outDir: './static/frontend',
    emptyOutDir: true,
  },
  server: {
    port: 3000,
  },
});
