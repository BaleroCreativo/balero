---
name: blog-post-writer
description: Writes and structures long-form blog posts, creates tutorial outlines, and optimizes content for SEO with cover image generation. Use when the user asks to write a blog post, article, how-to guide, tutorial, technical writeup, thought leadership piece, or long-form content.
license: Adaptiert von langchain-ai/deepagents (MIT) — Tool-Aufrufe (task/researcher, generate_image) auf Claude Code Äquivalente umgestellt.
---

# Blog Post Writing Skill

## Research First (Recommended)

Before writing a blog post, research the topic:

1. Use the `Agent` tool with `subagent_type: "Explore"` or `"general-purpose"` for codebase/internal context, or `WebSearch`/`WebFetch` for external topics.
2. Save findings to `research/<slug>.md` if the research is substantial enough to reuse.
3. Read the findings before writing.

## Output Structure

```
blogs/
└── <slug>/
    ├── post.md        # The blog post content
    └── hero.png        # Optional: cover image
```

Example: A post about "AI Agents in 2025" → `blogs/ai-agents-2025/`

## Blog Post Structure

Every blog post should follow this structure:

### 1. Hook (Opening)
- Start with a compelling question, statistic, or statement
- Make the reader want to continue
- Keep it to 2-3 sentences

### 2. Context (The Problem)
- Explain why this topic matters
- Describe the problem or opportunity
- Connect to the reader's experience

### 3. Main Content (The Solution)
- Break into 3-5 main sections with H2 headers
- Each section covers one key point
- Include code examples, diagrams, or screenshots where helpful
- Use bullet points for lists

### 4. Practical Application
- Show how to apply the concepts
- Include step-by-step instructions if applicable
- Provide code snippets or templates

### 5. Conclusion & CTA
- Summarize key takeaways (3 bullets max)
- End with a clear call-to-action
- Link to related resources

## Cover Image Generation

A cover image strengthens most posts. Use whatever image-generation capability is available in this environment — e.g. the `gemini-image-gen` skill, an Adobe Firefly MCP tool if connected, or another configured image tool. If none is available, skip the image rather than blocking on it. Save it to `blogs/<slug>/hero.png`.

### Writing Effective Image Prompts

Structure your prompt with these elements:

1. **Subject**: What is the main focus? Be specific and concrete.
2. **Style**: Art direction (minimalist, isometric, flat design, 3D render, watercolor, etc.)
3. **Composition**: How elements are arranged (centered, rule of thirds, symmetrical)
4. **Color palette**: Specific colors or mood (warm earth tones, cool blues and purples, high contrast)
5. **Lighting/Atmosphere**: Soft diffused light, dramatic shadows, golden hour, neon glow
6. **Technical details**: Aspect ratio considerations, negative space for text overlay

### Example Prompts

**For a technical blog post:**
```
Isometric 3D illustration of interconnected glowing cubes representing AI agents, each cube has subtle circuit patterns. Cubes connected by luminous data streams. Deep navy background (#0a192f) with electric blue (#64ffda) and soft purple (#c792ea) accents. Clean minimal style, lots of negative space at top for title. Professional tech aesthetic.
```

**For a tutorial/how-to:**
```
Clean flat illustration of hands typing on a keyboard with abstract code symbols floating upward, transforming into lightbulbs and gears. Warm gradient background from soft coral to light peach. Friendly, approachable style. Centered composition with space for text overlay.
```

**For thought leadership:**
```
Abstract visualization of a human silhouette profile merging with geometric neural network patterns. Split composition - organic watercolor texture on left transitioning to clean vector lines on right. Muted sage green and warm terracotta color scheme. Contemplative, forward-thinking mood.
```

## SEO Considerations

- Include the main keyword in the title and first paragraph
- Use the keyword naturally 3-5 times throughout
- Keep the title under 60 characters
- Write a meta description (150-160 characters)

## Quality Checklist

Before finishing:
- [ ] Post saved to `blogs/<slug>/post.md`
- [ ] Hero image generated at `blogs/<slug>/hero.png` (if a suitable tool is available)
- [ ] Hook grabs attention in first 2 sentences
- [ ] Each section has a clear purpose
- [ ] Conclusion summarizes key points
- [ ] CTA tells reader what to do next
