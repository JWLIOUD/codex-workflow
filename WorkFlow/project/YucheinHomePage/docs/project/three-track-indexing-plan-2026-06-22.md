# Three-track indexing plan - 2026-06-22

## Decision

Run all three indexing tracks together:

1. Short-term: Windows RPA for Search Console Request indexing.
2. Medium-term: official Search Console API monitor.
3. Long-term: strengthen internal links and sitemap signals.

## Track B - short-term Windows RPA

Goal: automate the visible Search Console UI because Request indexing is only available in the Search Console browser UI for this site.

Implementation status:

- RPA runbook created:
  - `windows-automation/search-console-rpa/README.md`
- Daily limit:
  - at most one successful Request indexing action.
- Current blocker:
  - Codex Chrome extension can claim Search Console tabs but cannot read/control Search Console page content.
- Recommended executor:
  - Power Automate Desktop on the Windows 11 host.

## Track A - medium-term Search Console API

Goal: monitor indexed status without relying on the Search Console UI.

Implementation status:

- API scripts created:
  - `windows-automation/search-console-api/inspect_queue.py`
  - `windows-automation/search-console-api/submit_sitemap.py`
  - `windows-automation/search-console-api/requirements.txt`
- Credentials are intentionally excluded from Git.

API boundary:

- URL Inspection API can check indexed status.
- Sitemap API can submit sitemap.
- API cannot press Request indexing.
- Google Indexing API is not suitable for the psychology article pages because Google's official scope is JobPosting and livestream BroadcastEvent pages.

## Track C - long-term site signal strengthening

Goal: reduce dependence on manual Request indexing by improving Google discovery signals.

Website implementation status:

- Homepage article entry now links to the formal workplace and boundary series pages instead of placeholder links.
- Homepage now adds direct links to priority queue articles:
  - `articles/self-care-07.html`
  - `articles/love-and-imperfection.html`
  - `articles/addiction-02.html`
- Sitemap `lastmod` updated for homepage and the two highest-priority queue URLs:
  - `https://yuchienpsy.com/`
  - `https://yuchienpsy.com/articles/self-care-07.html`
  - `https://yuchienpsy.com/articles/love-and-imperfection.html`

Website commit:

```text
9f1bf90 Strengthen article discovery links
```

## Next operating loop

Daily:

1. RPA attempts one Request indexing action only if Search Console UI is controllable.
2. API monitor checks indexed status for the first actionable queue URL.
3. Queue and `search-performance.md` are updated.

Weekly:

1. Review which article URLs are still not visible on Google.
2. Add or rotate homepage/series links toward unresolved priority URLs.
3. Re-submit sitemap through the API after meaningful internal-link or sitemap changes.
