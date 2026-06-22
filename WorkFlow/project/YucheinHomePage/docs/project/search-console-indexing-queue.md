# Search Console indexing queue - 2026-06-22

This queue tracks indexable pages for `yuchienpsy.com`.

Source:

- Local sitemap: `C:\Users\roy81\Documents\Codex\therapist-profile\sitemap.xml`
- Public Google check: 2026-06-22 `site:` and exact URL searches
- Search Console history: `search-performance.md`

## Queue rules

- Do not request indexing for `google-visible`, `indexed`, `already-requested`, or `not-indexable` URLs.
- Process `pending-inspection` and `quota-blocked` URLs first.
- Stop after one successful Request indexing action per day.
- Stop immediately if quota is exceeded.
- Update the `Last checked` and `Notes` columns after every inspection.

## URL queue

| Priority | URL | Status | Last checked | Notes |
|---:|---|---|---|---|
| 0 | `https://yuchienpsy.com/` | google-visible | 2026-06-22 | Public Google result found; Search Console previously indexed. Do not re-request. |
| 0 | `https://yuchienpsy.com/articles.html` | google-visible | 2026-06-22 | Public Google result found; Search Console previously indexed. Do not re-request. |
| 0 | `https://yuchienpsy.com/series/addiction.html` | google-visible | 2026-06-22 | Public Google result found. Do not re-request unless Search Console contradicts. |
| 0 | `https://yuchienpsy.com/series/workplace.html` | google-visible | 2026-06-22 | Public Google result found. Do not re-request unless Search Console contradicts. |
| 0 | `https://yuchienpsy.com/series/boundary.html` | google-visible | 2026-06-22 | Public Google result found. Do not re-request unless Search Console contradicts. |
| 0 | `https://yuchienpsy.com/series/self-care.html` | google-visible | 2026-06-22 | Public Google result found. Do not re-request unless Search Console contradicts. |
| 0 | `https://yuchienpsy.com/series/insights.html` | google-visible | 2026-06-22 | Public Google result found. Do not re-request unless Search Console contradicts. |
| 0 | `https://yuchienpsy.com/articles/addiction-01.html` | google-visible | 2026-06-22 | Public Google result found; Search Console previously indexed/requested. Do not re-request. |
| 0 | `https://yuchienpsy.com/articles/boundary-01.html` | google-visible | 2026-06-22 | Public Google result found after prior request. Do not re-request. |
| 0 | `https://yuchienpsy.com/articles/workplace-01.html` | google-visible | 2026-06-22 | Public Google result found. Do not re-request unless Search Console contradicts. |
| 1 | `https://yuchienpsy.com/articles/self-care-07.html` | quota-blocked | 2026-06-22 | First retry target. Prior Search Console result: discovered, not indexed; Request indexing failed due quota. 2026-06-22 22:14 automation could not inspect because browser policy blocked Search Console access; no indexing request made. 2026-06-22 22:28 automation found Chrome extension control available, but browser security policy blocked Search Console navigation; no inspection or indexing request made. |
| 2 | `https://yuchienpsy.com/articles/love-and-imperfection.html` | pending-inspection | 2026-06-20 | Prior Search Console result: not on Google; skipped because quota was already exceeded. |
| 3 | `https://yuchienpsy.com/articles/addiction-02.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 4 | `https://yuchienpsy.com/articles/addiction-03.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 5 | `https://yuchienpsy.com/articles/addiction-04.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 6 | `https://yuchienpsy.com/articles/addiction-05.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 7 | `https://yuchienpsy.com/articles/addiction-06.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 8 | `https://yuchienpsy.com/articles/addiction-07.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 9 | `https://yuchienpsy.com/articles/boundary-02.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 10 | `https://yuchienpsy.com/articles/boundary-03.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 11 | `https://yuchienpsy.com/articles/boundary-04.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 12 | `https://yuchienpsy.com/articles/boundary-05.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 13 | `https://yuchienpsy.com/articles/boundary-06.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 14 | `https://yuchienpsy.com/articles/boundary-07.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 15 | `https://yuchienpsy.com/articles/post-election-self-care.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 16 | `https://yuchienpsy.com/articles/relationship-control.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 17 | `https://yuchienpsy.com/articles/workplace-02.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 18 | `https://yuchienpsy.com/articles/workplace-03.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 19 | `https://yuchienpsy.com/articles/workplace-05.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 20 | `https://yuchienpsy.com/articles/workplace-06.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 21 | `https://yuchienpsy.com/articles/workplace-07.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |
| 22 | `https://yuchienpsy.com/articles/workplace-08.html` | pending-inspection | 2026-06-22 | Public exact Google search found no result. |

## Special cases outside the sitemap queue

| URL | Status | Reason |
|---|---|---|
| `https://yuchienpsy.com/talks.html` | needs-user-decision | Public Google currently shows the page, but prior Search Console notes say live test detected `noindex`. If this page should be searchable, remove `noindex` and add it to sitemap first. |
| `https://yuchienpsy.com/series/addiction-01.html` | not-indexable | Local file exists but is not in sitemap; likely not a canonical public content page. Do not submit unless website repo confirms intent. |
