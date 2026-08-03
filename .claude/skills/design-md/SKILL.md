---
name: design-md
description: Author, read, and apply DESIGN.md files — a spec for describing a project's visual identity (colors, typography, spacing, shapes, components) as machine-readable tokens plus human-readable rationale. Use this skill when the user wants to define, document, or maintain a design system/brand identity for a project, when a DESIGN.md file exists in the repo and should guide UI work, or when asked to create/lint/validate a DESIGN.md file. Source: https://github.com/google-labs-code/design.md
license: Complete terms in LICENSE.txt (Apache-2.0, Google)
---

DESIGN.md is a format for describing a visual identity so that coding agents can apply it consistently. A DESIGN.md file has two layers:

1. **YAML front matter** — machine-readable design tokens (colors, typography, spacing, rounded corners, components).
2. **Markdown body** — human-readable rationale organized into `##` sections, explaining *why* those values exist and how to apply them.

Full normative spec: `reference/spec.md` (read it before authoring or validating a file — it covers exact section order, token types, and edge-case behavior).

## When to use this skill

- The user asks to create, define, or document a design system / brand identity / style guide for a project.
- A `DESIGN.md` (or similarly named file) already exists in the repo — read it first and apply its tokens/rationale when building or styling UI.
- The user asks to validate, lint, or diff a DESIGN.md file.

## Authoring a DESIGN.md

1. Gather the visual identity: name, a short overview/aesthetic direction, color palette, typography, spacing scale, shape language (corner radius), elevation/depth approach, and any component-specific styling.
2. Write YAML front matter with the token sections that apply: `name`, `description` (optional), `colors`, `typography`, `rounded`, `spacing`, `components`. Only include sections you have real values for — omit the rest (list omissions under `omitted` if intentional).
3. Write the markdown body with `##` sections in this order (skip any that don't apply, but preserve relative order): Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts.
4. Use token references (`{colors.primary}`, `{rounded.md}`, etc.) inside `components` instead of repeating literal values.
5. Keep prose focused on rationale ("why this color/weight/spacing"), not just restating the tokens.

Minimal example:

```md
---
name: Heritage
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 8px
  md: 16px
---

## Overview

Architectural Minimalism meets Journalistic Gravitas.

## Colors

- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Secondary (#6C7278):** Slate for borders, captions, metadata.
- **Neutral (#F7F5F2):** Warm limestone background.
```

## Applying an existing DESIGN.md

When a DESIGN.md file is present in the project, treat its tokens as the source of truth for any UI work: use its exact color/typography/spacing values, follow its shape and elevation guidance, and respect its Do's and Don'ts. Prefer CSS variables or theme config generated from the tokens over hardcoding values.

## Validating / diffing

The reference CLI (`@google/design.md`) can lint a file against the spec (broken token references, WCAG contrast, structural issues) and diff two versions for token/prose regressions. If Node/npx is available:

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN-v1.md DESIGN-v2.md
```

Both commands output structured JSON (`findings`, `summary`, and for diff, `tokens`/`regression`). If npx isn't available or network access is restricted, validate manually against `reference/spec.md`: check section order, confirm every `{token.path}` reference resolves, and check color-on-background contrast ratios (WCAG AA: 4.5:1 for normal text, 3:1 for large text).
