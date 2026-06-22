# Search Console indexing automation - 2026-06-22

## Status

Automation request: daily URL Inspection and indexing follow-up for `yuchienpsy.com`.

Implementation status:

- Codex `automation_update` tool was not available in the current session, so the actual Codex scheduled task could not be created from this turn.
- This file defines the automation contract that must be used when Codex Automations are available again.
- Until the scheduled task is confirmed in the Codex app, this is a manual/runbook-backed automation specification, not proof that the daily job is already firing.

## Goal

Make every indexable page on `https://yuchienpsy.com/` discoverable through Google Search while avoiding:

- duplicate Request indexing actions,
- wasting daily Search Console quota,
- requesting indexing for pages that should not be indexed,
- repeated submissions for pages that are already indexed or already requested.

## Schedule

- Frequency: daily
- Preferred time: 09:30 Asia/Taipei
- Runtime host: Windows 11 Codex host
- Required browser state: Google Search Console logged in
- Required property:
  - `sc-domain:yuchienpsy.com`
  - fallback acceptable property: `https://yuchienpsy.com/`

## Sitemap source

Primary sitemap:

```text
https://yuchienpsy.com/sitemap.xml
```

Local source reference:

```text
C:\Users\roy81\Documents\Codex\therapist-profile\sitemap.xml
```

The queue file for this project is:

```text
WorkFlow/project/YucheinHomePage/docs/project/search-console-indexing-queue.md
```

## Daily algorithm

Each daily run must follow this exact order.

1. Open Search Console and confirm the active property is `sc-domain:yuchienpsy.com` or `https://yuchienpsy.com/`.
2. Confirm sitemap status for `https://yuchienpsy.com/sitemap.xml`.
3. Read `search-console-indexing-queue.md`.
4. Find the first URL whose status is `pending-inspection` or `quota-blocked`.
5. Run URL Inspection for that URL.
6. Apply the decision rules below.
7. Update `search-console-indexing-queue.md` and `search-performance.md` with the result.
8. Stop after one successful Request indexing action, or immediately after a quota error.

## Decision rules

Do not click Request indexing when any of these is true:

- URL Inspection says the URL is on Google.
- Page indexing says the page is indexed.
- Search Console says indexing has already been requested.
- The page is not intended to be indexed.
- The page has `noindex`.
- The inspected URL is not the canonical URL selected by Google and the selected canonical is acceptable.
- Search Console shows a quota error.

Only click Request indexing when all of these are true:

- URL is intended to be indexed.
- URL is not currently indexed.
- URL Inspection does not say indexing has already been requested.
- Live test says Google can index the page.
- Search Console allows the action.
- The URL is the canonical URL that should appear in Google.

Quota rule:

- If quota is exceeded, stop the run immediately.
- Mark the URL as `quota-blocked`.
- Do not try the next URL on the same day.

Daily cap:

- Maximum one successful Request indexing action per run.
- If several URLs only need inspection and no request, record them only if inspected.

## Status vocabulary

Use only these status values in the queue:

- `google-visible`: found through public Google search.
- `indexed`: Search Console says URL is on Google / page is indexed.
- `already-requested`: Search Console says indexing was already requested.
- `pending-inspection`: needs URL Inspection.
- `request-sent`: Request indexing was clicked successfully.
- `quota-blocked`: Request indexing was attempted or needed, but quota stopped the run.
- `not-indexable`: page should not be submitted because of `noindex`, canonical mismatch, redirect, or intentional exclusion.
- `needs-user-decision`: page purpose conflicts with current SEO rules.

## Required log format

Append each run to `search-performance.md` using this shape:

```markdown
### Search Console daily indexing automation: YYYY-MM-DD HH:mm

- Executor: Search Console automation AI
- Property: `sc-domain:yuchienpsy.com`
- Sitemap status:
- URL inspected:
- URL Inspection result:
- Live test result:
- Action:
- Quota result:
- Queue update:
- Next URL:
- Notes:
```

## Current constraints

- Search Console does not provide a public API for triggering Request indexing for ordinary web pages, so this workflow depends on the logged-in browser UI.
- Public Google `site:` checks are useful evidence, but they do not replace Search Console URL Inspection.
- `talks.html` is currently treated as a special case. Prior notes say it had `noindex`; if the user wants the talks page intentionally searchable, the website repo must first remove `noindex` and add it back to sitemap before any indexing request.

## Immediate next action

When Codex Automations tooling is available, create a daily scheduled automation using the prompt below.

```text
Every day at 09:30 Asia/Taipei, continue Search Console indexing follow-up for yuchienpsy.com.

Use property sc-domain:yuchienpsy.com, or https://yuchienpsy.com/ if the domain property is unavailable.

Read:
- C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-automation.md
- C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-queue.md
- C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-performance.md

Run one Search Console URL Inspection batch:
1. Confirm Search Console login and property.
2. Check the first queue URL marked pending-inspection or quota-blocked.
3. Do not request indexing if the URL is already indexed, already requested, not indexable, noindex, or canonicalized elsewhere.
4. Request indexing only when the URL is not indexed, not already requested, live test says Google can index it, and Search Console allows the request.
5. Stop immediately after one successful Request indexing action.
6. Stop immediately if Search Console shows quota exceeded.
7. Update search-console-indexing-queue.md and search-performance.md with the exact result.
8. Do not modify website source files.
9. Do not commit unless explicitly asked in that run.
```
