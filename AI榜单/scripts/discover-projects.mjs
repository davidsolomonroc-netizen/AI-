// 每周自动发现 AI 项目脚本
// 通过 GitHub API 搜索热门 AI 项目，用 AI 分析后生成内容

import fs from 'fs';
import path from 'path';

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const AI_API_KEY = process.env.AI_API_KEY;
const AI_API_URL = process.env.AI_API_URL || 'https://api.deepseek.com/v1/chat/completions';
const AI_MODEL = process.env.AI_MODEL || 'deepseek-chat';

const PROJECTS_DIR = 'src/content/projects';

// -------------------- 工具函数 --------------------

function getDateNDaysAgo(n) {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().split('T')[0];
}

function slugify(name) {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 60);
}

async function githubFetch(url) {
  const res = await fetch(url, {
    headers: { Authorization: `Bearer ${GITHUB_TOKEN}` },
  });
  if (!res.ok) throw new Error(`GitHub API ${res.status}: ${url}`);
  return res.json();
}

// -------------------- 第一步：发现新项目 --------------------

async function discoverTrendingRepos() {
  const since = getDateNDaysAgo(7);

  // 搜索 AI 相关热门项目
  const queries = [
    `topic:ai created:>=${since} stars:>50`,
    `topic:llm created:>=${since} stars:>50`,
    `topic:agent created:>=${since} stars:>50`,
    `topic:artificial-intelligence created:>=${since} stars:>100`,
  ];

  const seen = new Set();
  const repos = [];

  for (const query of queries) {
    try {
      const data = await githubFetch(
        `https://api.github.com/search/repositories?q=${encodeURIComponent(query)}&sort=stars&order=desc&per_page=15`
      );
      for (const item of data.items || []) {
        const key = `${item.owner.login}/${item.name}`;
        if (!seen.has(key)) {
          seen.add(key);
          repos.push(item);
        }
      }
    } catch (e) {
      console.warn(`搜索失败: ${query}`, e.message);
    }
  }

  // 按星数排序，取前 15 个
  repos.sort((a, b) => b.stargazers_count - a.stargazers_count);
  return repos.slice(0, 15);
}

// -------------------- 第二步：读取已有项目 --------------------

function loadExistingSlugs() {
  if (!fs.existsSync(PROJECTS_DIR)) return new Set();
  const files = fs.readdirSync(PROJECTS_DIR).filter(f => f.endsWith('.md'));
  return new Set(files);
}

// -------------------- 第三步：获取 README --------------------

async function getReadme(owner, repo) {
  try {
    const res = await fetch(
      `https://api.github.com/repos/${owner}/${repo}/readme`,
      {
        headers: {
          Authorization: `Bearer ${GITHUB_TOKEN}`,
          Accept: 'application/vnd.github.raw+json',
        },
      }
    );
    if (res.ok) {
      const text = await res.text();
      return text.slice(0, 3000); // 取前 3000 字符
    }
    return '';
  } catch {
    return '';
  }
}

// -------------------- 第四步：AI 分析 --------------------

async function analyzeWithAI(repo, readme) {
  const systemPrompt = `你是一个 AI 开源项目分析师。请分析这个 GitHub 项目，用中文输出 JSON。

评分标准：
- editorialScore (1-5): 项目的创新性、社区活跃度、代码质量
- deploymentRating (1-5): 非技术用户能否在 10 分钟内跑通（5=一行命令搞定）
- vibeCodingRating (1-5): 是否适合用 Claude Code/Cursor 集成使用

输出严格 JSON 格式（不要 markdown 代码块）：`;

  const userPrompt = `项目名称: ${repo.full_name}
描述: ${repo.description || '无'}
星数: ${repo.stargazers_count}
语言: ${repo.language || 'N/A'}
Topics: ${(repo.topics || []).join(', ')}
README 摘要: ${readme.slice(0, 2000)}

请输出 JSON:
{
  "title": "中文项目名（简洁有力）",
  "description": "20字以内的一句话描述",
  "category": "agent-framework | dev-tools | multimodal | code-generation | workflow-automation | data-analysis | other",
  "tags": ["最多4个英文标签"],
  "editorialScore": 4,
  "deploymentRating": 3,
  "vibeCodingRating": 4,
  "commercialSummary": "2-3句话面向非技术读者：解决什么业务问题，适合谁用",
  "vibeCodingPrompt": "给 Claude Code 使用的具体 Prompt，一步步说明如何用这个项目搭一个实际应用",
  "pitfallGuide": "3-5条避坑要点，每行用\\\\n分隔"
}`;

  // 尝试 AI API
  if (AI_API_KEY) {
    try {
      const res = await fetch(AI_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${AI_API_KEY}`,
        },
        body: JSON.stringify({
          model: AI_MODEL,
          messages: [
            { role: 'system', content: systemPrompt },
            { role: 'user', content: userPrompt },
          ],
          temperature: 0.7,
          max_tokens: 2000,
        }),
      });

      if (res.ok) {
        const data = await res.json();
        const content = data.choices?.[0]?.message?.content || '';
        // 尝试解析 JSON
        const jsonMatch = content.match(/\{[\s\S]*\}/);
        if (jsonMatch) {
          return JSON.parse(jsonMatch[0]);
        }
      }
    } catch (e) {
      console.warn(`AI API 调用失败: ${e.message}`);
    }
  }

  // 无 AI Key 或 API 失败时，生成模板
  return generateFallback(repo);
}

// -------------------- 第五步：模板兜底 --------------------

function generateFallback(repo) {
  const topics = repo.topics || [];
  let category = 'other';
  if (topics.some(t => ['agent', 'agents', 'ai-agent', 'autonomous'].includes(t))) category = 'agent-framework';
  else if (topics.some(t => ['cli', 'dev-tools', 'developer-tools', 'terminal'].includes(t))) category = 'dev-tools';
  else if (topics.some(t => ['multimodal', 'vision', 'image', 'video', 'audio', 'speech'].includes(t))) category = 'multimodal';
  else if (topics.some(t => ['code-generation', 'coding', 'programming'].includes(t))) category = 'code-generation';
  else if (topics.some(t => ['workflow', 'automation', 'pipeline'].includes(t))) category = 'workflow-automation';
  else if (topics.some(t => ['data', 'analytics', 'database'].includes(t))) category = 'data-analysis';

  // 用 repo 语言和星数估算评分
  const stars = repo.stargazers_count;
  const score = stars > 5000 ? 4 : stars > 1000 ? 3 : 2;

  return {
    title: repo.name.replace(/[-_]/g, ' '),
    description: (repo.description || '一个值得关注的开源项目').slice(0, 60),
    category,
    tags: topics.slice(0, 4),
    editorialScore: Math.min(score + 1, 5),
    deploymentRating: score,
    vibeCodingRating: score + 1,
    commercialSummary: `${repo.description || repo.name} 是 GitHub 上近期热门的开源项目，获得了 ${stars} 颗星。值得 AI 开发者关注和使用。`,
    vibeCodingPrompt: `探索 ${repo.name} 的功能和用法。请帮我：1) 阅读项目文档了解核心功能 2) 搭建一个 demo 3) 测试主要特性`,
    pitfallGuide: '1. 建议先阅读官方文档了解项目架构\n2. 注意检查依赖版本兼容性\n3. 生产环境使用前建议充分测试',
  };
}

// -------------------- 第六步：生成 Markdown --------------------

function generateMarkdown(repo, analysis) {
  const now = new Date().toISOString().split('T')[0];
  const tags = (analysis.tags || []).map(t => `"${t.trim()}"`).join(', ');

  return `---
title: "${analysis.title}"
description: "${analysis.description}"
publishDate: ${now}
featured: false
githubUrl: "https://github.com/${repo.full_name}"
githubStars: ${repo.stargazers_count}
githubOwner: "${repo.owner.login}"
githubRepo: "${repo.name}"
category: "${analysis.category}"
tags: [${tags}]
editorialScore: ${analysis.editorialScore || 3}
deploymentRating: ${analysis.deploymentRating || 3}
vibeCodingRating: ${analysis.vibeCodingRating || 3}
commercialSummary: "${(analysis.commercialSummary || '').replace(/"/g, '\\"')}"
vibeCodingPrompt: "${(analysis.vibeCodingPrompt || '').replace(/"/g, '\\"')}"
pitfallGuide: "${(analysis.pitfallGuide || '').replace(/"/g, '\\"')}"
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。${repo.description || ''}

> GitHub: [${repo.full_name}](https://github.com/${repo.full_name}) | ⭐ ${repo.stargazers_count} | ${repo.language || '多种语言'}
`;
}

// -------------------- 主流程 --------------------

async function main() {
  console.log('🔍 开始自动发现 AI 项目...');

  // 1. 发现新项目
  const repos = await discoverTrendingRepos();
  console.log(`  发现 ${repos.length} 个项目`);

  // 2. 去重
  const existing = loadExistingSlugs();
  let newCount = 0;

  for (const repo of repos) {
    const slug = slugify(repo.name);
    const filename = `${slug}.md`;

    if (existing.has(filename)) {
      console.log(`  ⏭ 已存在: ${repo.full_name}`);
      continue;
    }

    console.log(`  📥 分析: ${repo.full_name} (★${repo.stargazers_count})`);

    // 3. 获取 README
    const readme = await getReadme(repo.owner.login, repo.name);

    // 4. AI 分析
    const analysis = await analyzeWithAI(repo, readme);

    // 5. 生成文件
    const markdown = generateMarkdown(repo, analysis);
    const filePath = path.join(PROJECTS_DIR, filename);
    fs.writeFileSync(filePath, markdown, 'utf-8');

    console.log(`  ✅ 已生成: ${filename} (${analysis.title})`);
    newCount++;

    // 避免请求过快
    await new Promise(r => setTimeout(r, 1000));
  }

  console.log(`\n🎉 完成！新增 ${newCount} 个项目`);
}

main().catch(console.error);
