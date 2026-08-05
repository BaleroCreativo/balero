---
name: social-media-post
description: Drafts engaging social media posts, writes hooks, suggests hashtags, creates thread structures, and generates companion images. Use when the user asks to write a LinkedIn post, tweet, Twitter/X thread, social media caption, social post, or repurpose content for social platforms.
license: Adaptiert von langchain-ai/deepagents (MIT) — Tool-Aufrufe (task/researcher, generate_image) auf Claude Code Äquivalente umgestellt.
---

# Social Media Content Skill

## Research First (Recommended)

Before writing any social media content, research the topic:

1. Use the `Agent` tool with `subagent_type: "Explore"` or `"general-purpose"` for codebase/internal context, or `WebSearch`/`WebFetch` for external topics.
2. Save findings to `research/<slug>.md` if the research is substantial enough to reuse.
3. Read the findings before writing the post.

## Output Structure

**LinkedIn posts:**
```
linkedin/
└── <slug>/
    ├── post.md        # The post content
    └── image.png      # Optional: companion visual
```

**Twitter/X threads:**
```
tweets/
└── <slug>/
    ├── thread.md      # The thread content
    └── image.png      # Optional: companion visual
```

Example: A LinkedIn post about "prompt engineering" → `linkedin/prompt-engineering/`

## Platform Guidelines

### LinkedIn

**Format:**
- 1,300 character limit (show more after ~210 chars)
- First line is crucial - make it hook
- Use line breaks for readability
- 3-5 hashtags at the end

**Tone:**
- Professional but personal
- Share insights and learnings
- Ask questions to drive engagement
- Use "I" and share experiences

**Structure:**
```
[Hook - 1 compelling line]

[Empty line]

[Context - why this matters]

[Empty line]

[Main insight - 2-3 short paragraphs]

[Empty line]

[Call to action or question]

#hashtag1 #hashtag2 #hashtag3
```

### Twitter/X

**Format:**
- 280 character limit per tweet
- Threads for longer content (use 1/🧵 format)
- No more than 2 hashtags per tweet

**Thread Structure:**
```
1/🧵 [Hook - the main insight]

2/ [Supporting point 1]

3/ [Supporting point 2]

4/ [Example or evidence]

5/ [Conclusion + CTA]
```

## Image Generation

A companion image strengthens most posts. Use whatever image-generation capability is available in this environment — e.g. the `gemini-image-gen` skill, an Adobe Firefly MCP tool if connected, or another configured image tool. If none is available, skip the image rather than blocking on it.

### Social Image Best Practices

Social images need to work at small sizes in crowded feeds:
- **Bold, simple compositions** - one clear focal point
- **High contrast** - stands out when scrolling
- **No text in image** - too small to read, platforms add their own
- **Square or 4:5 ratio** - works across platforms

### Writing Effective Prompts

Include these elements:

1. **Single focal point**: One clear subject, not a busy scene
2. **Bold style**: Vibrant colors, strong shapes, high contrast
3. **Simple background**: Solid color, gradient, or subtle texture
4. **Mood/energy**: Match the post tone (inspiring, urgent, thoughtful)

### Example Prompts

**For an insight/tip post:**
```
Single glowing lightbulb floating against a deep purple gradient background, lightbulb made of interconnected golden geometric lines, rays of soft light emanating outward. Minimal, striking, high contrast. Square composition.
```

**For announcements/news:**
```
Abstract rocket ship made of colorful geometric shapes launching upward with a trail of particles. Bright coral and teal color scheme against clean white background. Energetic, celebratory mood. Bold flat illustration style.
```

**For thought-provoking content:**
```
Two overlapping translucent circles, one blue one orange, creating a glowing intersection in the center. Represents collaboration or intersection of ideas. Dark charcoal background, soft ethereal glow. Minimalist and contemplative.
```

## Content Types

### Announcement Posts
- Lead with the news
- Explain the impact
- Include link or next step

### Insight Posts
- Share one specific learning
- Explain the context briefly
- Make it actionable

### Question Posts
- Ask a genuine question
- Provide your take first
- Keep it focused on one topic

## Quality Checklist

Before finishing:
- [ ] Post saved to `linkedin/<slug>/post.md` or `tweets/<slug>/thread.md`
- [ ] Image generated alongside the post (if a suitable tool is available)
- [ ] First line hooks attention
- [ ] Content fits platform limits
- [ ] Tone matches platform norms
- [ ] Has clear CTA or question
- [ ] Hashtags are relevant (not generic)
