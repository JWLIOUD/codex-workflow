# Search Console API automation

This folder supports the medium-term indexing monitor for `yuchienpsy.com`.

It uses official Google Search Console APIs for:

- URL Inspection indexed-status checks.
- Sitemap submission.

It does not perform Search Console UI Request indexing. Google does not provide an ordinary-page API for that action.

## Official API boundaries

- URL Inspection API can inspect the indexed status of a URL in Google Search Console.
- URL Inspection API cannot test the live URL and cannot press Request indexing.
- Google Indexing API is limited to job posting pages and livestreaming video pages, so it should not be used for this psychology article site.
- Sitemaps API can submit the sitemap URL to Search Console.

References:

- URL Inspection API: `https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect`
- Sitemaps submit API: `https://developers.google.com/webmaster-tools/v1/sitemaps/submit`
- Indexing API limits: `https://developers.google.com/search/apis/indexing-api/v3/quickstart`

## Local setup

Do not commit credentials or tokens.

1. Create an OAuth Desktop client in Google Cloud.
2. Download the OAuth client secret JSON locally.
3. Set:

```powershell
$env:GSC_OAUTH_CLIENT_SECRET="C:\Users\roy81\Documents\Codex\.local\gsc-oauth-client.json"
$env:GSC_TOKEN_PATH="C:\Users\roy81\Documents\Codex\.local\gsc-token.json"
```

4. Install dependencies in a local venv:

```powershell
py -m venv C:\Users\roy81\Documents\Codex\.venv-gsc
C:\Users\roy81\Documents\Codex\.venv-gsc\Scripts\pip install -r C:\Users\roy81\Documents\Codex\codex-workflow\windows-automation\search-console-api\requirements.txt
```

## Inspect the first queue URL

```powershell
C:\Users\roy81\Documents\Codex\.venv-gsc\Scripts\python `
  C:\Users\roy81\Documents\Codex\codex-workflow\windows-automation\search-console-api\inspect_queue.py
```

The script prints a Markdown log block. Review it before appending to:

```text
WorkFlow/project/YucheinHomePage/docs/project/search-performance.md
```

## Submit sitemap

```powershell
C:\Users\roy81\Documents\Codex\.venv-gsc\Scripts\python `
  C:\Users\roy81\Documents\Codex\codex-workflow\windows-automation\search-console-api\submit_sitemap.py
```
