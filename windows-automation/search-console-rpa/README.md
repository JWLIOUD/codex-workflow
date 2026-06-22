# Search Console RPA runbook

This is the short-term automation path for Request indexing.

Use this only because Codex/Chrome extension can claim the Search Console tab but cannot read or interact with `https://search.google.com` content. The RPA should operate the visible Windows UI, not the browser DOM.

## Recommended tool

Power Automate Desktop.

Alternative tools:

- AutoHotkey v2
- UI.Vision RPA

## Daily cap

- Process at most one URL per day.
- Stop immediately after one successful Request indexing action.
- Stop immediately on quota exceeded.

## Inputs

Queue:

```text
C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-queue.md
```

First target status:

- `pending-inspection`
- `quota-blocked`

## Power Automate Desktop flow

1. Launch or focus Chrome.
2. Confirm a Search Console tab is already open:
   - `https://search.google.com/search-console?resource_id=sc-domain:yuchienpsy.com`
3. If the tab is not open, open it and stop for that run; do not continue to URL Inspection on the same run.
4. Read the first actionable URL from `search-console-indexing-queue.md`.
5. Click the URL Inspection search field.
6. Paste the target URL.
7. Press Enter.
8. Wait until Search Console result text is visible.
9. Branch:
   - If page is on Google / indexed: record `indexed`.
   - If indexing was already requested: record `already-requested`.
   - If not indexed and Request indexing is available: click Request indexing.
   - If quota exceeded appears: record `quota-blocked` and stop.
   - If URL is blocked by noindex, robots, canonical mismatch, or not indexable: record `not-indexable` with reason.
10. Write the result to a local text file for Codex to import:

```text
C:\Users\roy81\Documents\Codex\.local\search-console-rpa-result.md
```

11. Stop the flow.

## Output format

```markdown
### Search Console RPA indexing run: YYYY-MM-DD HH:mm

- URL inspected:
- Search Console result:
- Live test result:
- Action:
- Quota result:
- Queue update:
- Notes:
```

## Safety rules

- Never submit more than one Request indexing action per day.
- Never submit a URL already marked `google-visible`, `indexed`, or `already-requested`.
- Never submit `talks.html` until its indexing decision is resolved.
- Never store Google passwords, cookies, or browser credentials in this repo.
