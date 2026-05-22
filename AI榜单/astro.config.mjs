import { defineConfig } from 'astro/config';
import tailwind from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://ai-leaderboard.pages.dev',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwind()],
  },
  output: 'static',
});
