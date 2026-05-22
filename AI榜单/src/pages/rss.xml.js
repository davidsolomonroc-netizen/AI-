import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const projects = await getCollection('projects');
  const sorted = projects.sort((a, b) => b.data.publishDate.getTime() - a.data.publishDate.getTime());

  return rss({
    title: 'AI 榜单 - 每周 AI 开源项目推荐',
    description: '发现最适合 AI 开发者和 Vibe Coding 用户的开源项目 — 每周精选推荐',
    site: context.site,
    language: 'zh-cn',
    items: sorted.map((project) => ({
      title: project.data.title,
      description: project.data.commercialSummary,
      pubDate: project.data.publishDate,
      link: `/projects/${project.slug}/`,
    })),
  });
}
