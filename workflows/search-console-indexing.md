# Search Console Indexing Workflow

Use this workflow when checking or requesting indexing for `yuchienpsy.com`.

## Preconditions

- Browser is logged into the Google account that owns Search Console.
- Search Console property is either `sc-domain:yuchienpsy.com` or `https://yuchienpsy.com/`.
- Sitemap is `https://yuchienpsy.com/sitemap.xml`.

## Steps

1. Check `https://yuchienpsy.com/robots.txt`.
2. Check `https://yuchienpsy.com/sitemap.xml`.
3. Confirm sitemap status in Search Console.
4. Run URL Inspection for target URLs.
5. Record:
   - URL status
   - Page indexing status
   - Referring sitemap
   - Last crawl
   - Crawled as
   - Crawl allowed
   - Page fetch
   - Indexing allowed
   - User-declared canonical
   - Google-selected canonical
6. Request indexing only when appropriate.
7. Update `WorkFlow/project/YucheinHomePage/docs/project/search-performance.md`.

## Quota Protection

Do not request indexing if URL Inspection already shows any of these:

- `已要求建立索引`
- `網址在 Google 服務中`
- `網頁已編入索引`

Only request indexing when:

- the URL is not indexed,
- it has not already been requested,
- Search Console allows the action,
- and the page is intended to be indexed.

If Search Console shows quota exceeded, stop requesting more URLs that day and record the blocked state.
