import { defineCollection, z } from 'astro:content';

const projectsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.date(),
    featured: z.boolean().default(false),

    githubUrl: z.string().url(),
    githubStars: z.number().default(0),
    githubOwner: z.string(),
    githubRepo: z.string(),

    category: z.enum([
      'agent-framework',
      'dev-tools',
      'multimodal',
      'code-generation',
      'workflow-automation',
      'data-analysis',
      'other',
    ]),
    tags: z.array(z.string()).default([]),

    editorialScore: z.number().min(1).max(5),
    deploymentRating: z.number().min(1).max(5),
    vibeCodingRating: z.number().min(1).max(5),

    commercialSummary: z.string(),
    vibeCodingPrompt: z.string(),
    pitfallGuide: z.string(),
    affiliateLink: z.string().url().optional(),

    targetAudience: z.array(z.string()).default([]),
    useCases: z.array(z.string()).default([]),
  }),
});

export const collections = {
  projects: projectsCollection,
};
