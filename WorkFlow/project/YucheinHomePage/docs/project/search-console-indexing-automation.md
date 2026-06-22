# Search Console indexing automation - 2026-06-22

## Status

Automation request: daily URL Inspection and indexing follow-up for `yuchienpsy.com`.

Implementation status:

- Created in Codex Automations by the user on 2026-06-22.
- Automation ID: `yuchien-search-console-indexing-follow-up`
- Schedule shown in Codex: daily at 09:30.
- This file remains the operating contract for the scheduled task.

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

1. Read this file, `search-console-indexing-queue.md`, and `search-performance.md`.
2. Run `git status -sb` before any edit.
3. Find the first URL whose status is `pending-inspection` or `quota-blocked`.
4. Check browser availability using the execution rules below.
5. Open Search Console and confirm the active property is `sc-domain:yuchienpsy.com` or `https://yuchienpsy.com/`.
6. Confirm sitemap status for `https://yuchienpsy.com/sitemap.xml`.
7. Run URL Inspection for the selected URL.
8. Apply the decision rules below.
9. Update `search-console-indexing-queue.md` and `search-performance.md` with the result.
10. Stop after one successful Request indexing action, or immediately after a quota error.

## Browser execution rules

Search Console URL Inspection depends on the logged-in browser UI. The daily task must not rediscover the browser strategy from scratch.

Use this fixed browser policy:

1. Use the logged-in Chrome extension/browser session as the only valid browser path for Search Console.
2. First list open Chrome tabs and claim an existing Search Console tab whose URL starts with `https://search.google.com/search-console`.
3. Do not open a new `https://search.google.com` tab and do not navigate an existing tab to Search Console. The 2026-06-22 immediate run showed that direct navigation to Search Console can be blocked by browser security policy, while claiming an already-open Search Console tab works.
4. If no Search Console tab is already open, stop the run immediately and record a blocked-run log that asks the user to keep Search Console open before the next run.
5. If Chrome extension control is unavailable, stop the run immediately.
6. Do not fall back to the in-app browser for `https://search.google.com/`; the 2026-06-22 immediate run showed that Search Console is blocked there by browser security policy.
7. Do not retry browser setup with renamed variables, reset loops, or alternate browser surfaces after the known blocked condition appears.
8. When browser access is unavailable, do not inspect the URL, do not request indexing, do not change the queue status except adding a blocked-run note, and append one blocked run entry to `search-performance.md`.
9. A blocked browser run does not consume Search Console quota.

Blocked browser log wording:

```text
URL Inspection result: Not completed; no claimable already-open Search Console tab was available, or Chrome extension/Search Console browser access was unavailable.
Action: Skipped; no Request indexing action was attempted.
Quota result: No quota consumed.
Queue update: status unchanged; blocked-run note appended.
```

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

The Codex automation should continue to use the prompt below as its operating instruction.

```text
Every day at 09:30 Asia/Taipei, continue Search Console indexing follow-up for yuchienpsy.com.

Use property sc-domain:yuchienpsy.com, or https://yuchienpsy.com/ if the domain property is unavailable.

Read:
- C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-automation.md
- C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-queue.md
- C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-performance.md

Run one Search Console URL Inspection batch:
1. Run git status -sb.
2. Read the queue and select only the first URL marked pending-inspection or quota-blocked.
3. Use only the logged-in Chrome extension/browser session for Search Console.
4. List open Chrome tabs and claim an existing tab whose URL starts with https://search.google.com/search-console. Do not navigate to search.google.com yourself.
5. If Chrome extension control is unavailable, or no already-open Search Console tab can be claimed, stop immediately. Do not fall back to the in-app browser for search.google.com. Record one blocked-run log and leave the queue status unchanged except for a note.
6. Confirm Search Console login and property.
7. Do not request indexing if the URL is already indexed, already requested, not indexable, noindex, google-visible, or canonicalized elsewhere.
8. Request indexing only when the URL is not indexed, not already requested, live test says Google can index it, and Search Console allows the request.
9. Stop immediately after one successful Request indexing action.
10. Stop immediately if Search Console shows quota exceeded.
11. Update search-console-indexing-queue.md and search-performance.md with the exact result.
12. Do not modify website source files.
13. Do not commit unless explicitly asked in that run.
```
