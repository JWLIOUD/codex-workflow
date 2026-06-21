# Visual hierarchy fix workflow - 2026-06-21

## Background

This task followed the 2026-06-21 visual QA result. The urgent quality issues were:

1. Mobile article listing and series pages showed the main visual too late, so the first impression felt text-heavy.
2. Individual article pages did not have a first-screen topic image, so brand memory and article identity were weaker than expected.

This was handled using the website team workflow mode: route the issue, discuss a solution, execute, validate, then record the result for the next loop.

## AI team assignment

| Role | Responsibility in this task | Output |
| --- | --- | --- |
| Project Manager AI | Own the close loop, split work, confirm scope, and prevent mixing workflow repo with website repo. | Two-repo execution plan and final handoff record. |
| Website Quality Director AI | Define whether the fix should improve perceived quality without overbuilding a new illustration system. | Quality criteria and pass/follow-up decision. |
| Layout Experience AI | Decide mobile-first visual rhythm and first-screen hierarchy. | Put key visuals before text-heavy blocks on mobile. |
| Illustration Planner AI | Decide whether new images are needed now. | Use existing series visuals as short-term topic images; defer unique per-article art. |
| SEO Strategist AI | Preserve existing metadata and avoid unnecessary indexing operations. | Keep OG/social image meaning intact; no Search Console action needed. |
| Web Engineer AI | Implement CSS/template/page changes in `therapist-profile`. | Website commit `6d386ca Improve article visual hierarchy`. |
| Brand Quality Reviewer AI | Validate screenshots and judge visual result against the quality criteria. | Visual QA screenshots and pass/follow-up notes. |

## Decision

The team chose a conservative implementation:

- Use existing series artwork instead of generating new article-specific images immediately.
- On mobile article listing and series pages, move the main visual above the text block so the first viewport has a stronger brand signal.
- On individual article pages, add a topic image directly after the title and before the description.
- Keep desktop hierarchy stable: title remains primary, image supports the article rather than replacing the reading flow.
- Avoid Search Console indexing requests because this is a presentation and asset hierarchy update, not a new-indexing event.

This solves the urgent quality issue while keeping future per-article illustration work available as a separate content/visual production track.

## Website implementation

Repo: `therapist-profile`

Commit:

```text
6d386ca Improve article visual hierarchy
```

Changed areas:

- `articles.css`
  - Mobile article listing now presents the hero visual before the text column.
  - Mobile crop uses `16 / 10` to make the first-screen image feel intentional.
  - The secondary author card is hidden on mobile to reduce first-screen clutter.
- `series.css`
  - Mobile series pages now present the series visual before the text column.
  - Mobile crop uses `16 / 10`.
  - The secondary series note is hidden on mobile to keep the first view visual-led.
- `article.css`
  - Added `.article-hero-media` for a first-screen topic image on article pages.
- `articles/*.html`
  - Added one topic image block to each article page.
  - Uses existing mobile and desktop WebP assets.
- `tools/generate_articles.py`
  - Updated the article template so generated article pages keep the new topic image block.
- `articles.html` and formal `series/*.html`
  - Updated CSS cache-busting version to `20260621-visual-qa-1`.

## Validation

Local checks:

- `git diff --check` passed before the website commit.
- Confirmed 25 article pages include `article-hero-media`.
- Confirmed checked pages no longer reference the old `20260613` CSS query for the modified article/series surfaces.

Visual QA screenshots:

```text
WorkFlow/project/YucheinHomePage/docs/project/visual-fix-screenshots-2026-06-21/
```

Screenshots captured:

- `articles-local-mobile.png`
- `articles-local-desktop.png`
- `series-workplace-local-mobile.png`
- `series-workplace-local-desktop.png`
- `article-addiction-01-local-mobile.png`
- `article-addiction-01-local-desktop.png`

Formal site checks:

| URL | HTTP | New CSS version | Article hero media | Mobile image source |
| --- | --- | --- | --- | --- |
| `https://yuchienpsy.com/articles.html` | 200 | yes | not applicable | yes |
| `https://yuchienpsy.com/series/workplace.html` | 200 | yes | not applicable | yes |
| `https://yuchienpsy.com/articles/addiction-01.html` | 200 | yes | yes | yes |

## Quality result

Status: PASS with follow-up.

What improved:

- Mobile article listing now gives a warmer visual signal before the text-heavy area.
- Mobile series page now starts with the series visual, so the first impression is less plain.
- Individual article pages now have a topic image in the first reading area, improving article identity and brand memory.
- Existing image assets remain consistent with the current website style.

Remaining follow-up:

- P2: Plan unique per-article topic images for high-priority articles.
- P2: Define crop rules for each article image type before generating or uploading new art.
- P3: Add a reusable QA checklist for mobile first-viewport visual balance after future content updates.

## Close-loop notes

The issue is resolved for the current urgent quality concern. The next loop should not reopen this as a layout bug unless screenshots show regression. Future work should move into the visual content production workflow:

1. Pick priority articles.
2. Write image briefs.
3. Generate or design topic images.
4. Crop for desktop, mobile, Open Graph, and article body use.
5. Run visual QA before publishing.
