# Power Automate Desktop flow - Search Console indexing

This checklist describes how to build the short-term Windows RPA flow for Google Search Console Request indexing.

Goal:

- Inspect one queued URL per run.
- Request indexing only when eligible.
- Stop after one successful request.
- Stop immediately on quota exceeded.
- Write a result file for Codex to import.

## Prerequisites

Before building the flow:

1. Install Power Automate Desktop.
2. Open Chrome with the Google account that owns `sc-domain:yuchienpsy.com`.
3. Open Search Console:

```text
https://search.google.com/search-console?resource_id=sc-domain:yuchienpsy.com
```

4. Keep Chrome visible on the Windows desktop.
5. Set Windows power settings so the machine does not sleep during the scheduled window.
6. Confirm the queue file exists:

```text
C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-queue.md
```

7. Confirm the local output folder exists or create it:

```text
C:\Users\roy81\Documents\Codex\.local\
```

Do not store Google passwords, cookies, or OAuth tokens in the workflow repo.

## Flow variables

Create these variables in Power Automate Desktop:

| Variable | Example value |
|---|---|
| `QueuePath` | `C:\Users\roy81\Documents\Codex\codex-workflow\WorkFlow\project\YucheinHomePage\docs\project\search-console-indexing-queue.md` |
| `ResultPath` | `C:\Users\roy81\Documents\Codex\.local\search-console-rpa-result.md` |
| `SearchConsoleUrl` | `https://search.google.com/search-console?resource_id=sc-domain:yuchienpsy.com` |
| `TargetUrl` | empty at start |
| `RunTimestamp` | empty at start |
| `RunStatus` | empty at start |
| `SearchConsoleResult` | empty at start |
| `ActionTaken` | empty at start |
| `QuotaResult` | empty at start |
| `Notes` | empty at start |

## Flow actions

### 1. Initialize

1. Action: `Get current date and time`
   - Save to: `RunTimestamp`
2. Action: `Set variable`
   - `RunStatus = Started`
3. Action: `If file exists`
   - File: `%QueuePath%`
   - If no: write result file with `Queue file missing`, then stop.

### 2. Read the first actionable URL

Power Automate Desktop has limited Markdown parsing. Use the simplest stable rule:

1. Action: `Read text from file`
   - File path: `%QueuePath%`
   - Store content in: `QueueText`
2. Action: `Split text`
   - Text: `%QueueText%`
   - Standard delimiter: New line
   - Store in: `QueueLines`
3. Action: `For each`
   - Value to iterate: `%QueueLines%`
   - Current item: `CurrentLine`
4. Inside loop, add condition:
   - If `%CurrentLine%` contains `| pending-inspection |`
   - Or `%CurrentLine%` contains `| quota-blocked |`
5. If matched:
   - Extract URL between the first pair of backticks.
   - Set `TargetUrl`.
   - Exit loop.

Extraction option:

- Use action `Parse text` with regular expression:

```text
`([^`]+)`
```

- Save the first match to `TargetUrl`.

6. After loop:
   - If `TargetUrl` is empty, write result file with `No actionable URL`, then stop.

### 3. Focus Chrome and Search Console

1. Action: `Attach to running Chrome`
   - Attach to existing instance.
2. Action: `Go to web page`
   - URL: `%SearchConsoleUrl%`
   - Use only if Search Console is not already visible.
   - If navigation triggers login or security challenge, stop and write blocked result.
3. Action: `Wait for web page content`
   - Wait for text: `URL 檢查` or `URL inspection`
   - Timeout: 30 seconds.

If this wait fails:

- Set `RunStatus = Blocked`
- Set `Notes = Search Console page not available or not logged in`
- Write result file.
- Stop.

### 4. Open URL Inspection

Use the most stable method available in your Chrome language.

Option A: Search field is visible in the top bar.

1. Action: `Click UI element in window`
   - Target the URL Inspection search field.
2. Action: `Populate text field in window`
   - Text: `%TargetUrl%`
3. Action: `Send keys`
   - Keys: `{Enter}`

Option B: Search field cannot be targeted reliably.

1. Action: `Send keys`
   - Keys: `Ctrl+L`
2. Action: `Populate text field in window`
   - Text: `https://search.google.com/search-console/inspect?resource_id=sc-domain:yuchienpsy.com&id=%TargetUrl%`
3. Action: `Send keys`
   - Keys: `{Enter}`

If Search Console changes URL format, prefer Option A.

### 5. Wait for inspection result

1. Action: `Wait`
   - 5 seconds.
2. Action: `Wait for web page content`
   - Wait for one of:
     - `網址在 Google 服務中`
     - `URL is on Google`
     - `網址不在 Google 服務中`
     - `URL is not on Google`
     - `已要求建立索引`
     - `Indexing requested`
     - `超過配額`
     - `Quota exceeded`
   - Timeout: 90 seconds.

If timeout:

- Set `RunStatus = Blocked`
- Set `SearchConsoleResult = Inspection result timed out`
- Set `ActionTaken = Skipped`
- Set `QuotaResult = Unknown`
- Write result file.
- Stop.

### 6. Branch by visible result

Evaluate visible page text in this order.

#### Case A: already indexed

If page contains:

- `網址在 Google 服務中`
- or `URL is on Google`
- or `網頁已編入索引`
- or `Page is indexed`

Then:

- `RunStatus = Completed`
- `SearchConsoleResult = Indexed / URL is on Google`
- `ActionTaken = Skipped - already indexed`
- `QuotaResult = No quota consumed`
- Write result file.
- Stop.

#### Case B: already requested

If page contains:

- `已要求建立索引`
- or `Indexing requested`

Then:

- `RunStatus = Completed`
- `SearchConsoleResult = Already requested`
- `ActionTaken = Skipped - already requested`
- `QuotaResult = No quota consumed`
- Write result file.
- Stop.

#### Case C: quota exceeded

If page contains:

- `超過配額`
- or `Quota exceeded`

Then:

- `RunStatus = Quota blocked`
- `SearchConsoleResult = Not indexed or request attempted`
- `ActionTaken = Stopped - quota exceeded`
- `QuotaResult = Quota exceeded`
- Write result file.
- Stop.

#### Case D: not indexable

If page contains:

- `noindex`
- `robots`
- `重新導向`
- `redirect`
- `Alternate page with proper canonical tag`
- `Google 選取的標準網址` and it is not the inspected URL

Then:

- `RunStatus = Completed`
- `SearchConsoleResult = Not indexable or canonicalized elsewhere`
- `ActionTaken = Skipped - not eligible`
- `QuotaResult = No quota consumed`
- Write result file.
- Stop.

#### Case E: not indexed and request is available

If page contains:

- `網址不在 Google 服務中`
- or `URL is not on Google`

And Request indexing button is visible/enabled:

1. Action: `Click UI element in window`
   - Button: `要求建立索引` or `Request indexing`
2. Wait for processing.
3. If success text appears:
   - `RunStatus = Completed`
   - `SearchConsoleResult = Not indexed; request accepted`
   - `ActionTaken = Request indexing submitted`
   - `QuotaResult = One request consumed`
4. If quota appears:
   - `RunStatus = Quota blocked`
   - `SearchConsoleResult = Request blocked by quota`
   - `ActionTaken = Stopped - quota exceeded`
   - `QuotaResult = Quota exceeded`
5. Write result file.
6. Stop.

## Result file

Write exactly one Markdown block to:

```text
C:\Users\roy81\Documents\Codex\.local\search-console-rpa-result.md
```

Template:

```markdown
### Search Console RPA indexing run: %RunTimestamp%

- URL inspected: `%TargetUrl%`
- Search Console result: %SearchConsoleResult%
- Live test result: Not separately run by RPA unless visible in Search Console
- Action: %ActionTaken%
- Quota result: %QuotaResult%
- Queue update: Pending Codex import
- Notes: %Notes%
```

## Codex import step

After the RPA flow finishes, ask Codex:

```text
總管AI 匯入 Search Console RPA 結果
```

Codex should then:

1. Read `C:\Users\roy81\Documents\Codex\.local\search-console-rpa-result.md`.
2. Update `search-console-indexing-queue.md`.
3. Append the run to `search-performance.md`.
4. Commit and push `codex-workflow`.

## Scheduling

Use Windows Task Scheduler or Power Automate cloud schedule to run once per day.

Recommended time:

```text
09:30 Asia/Taipei
```

If the flow hits quota, keep the next run scheduled for the following day.

## QA checklist

Before enabling unattended daily runs:

- [ ] Run once with Power Automate Desktop open and visible.
- [ ] Confirm it reads the correct first queue URL.
- [ ] Confirm it stops if Search Console is not logged in.
- [ ] Confirm it does not request indexing for an already indexed URL.
- [ ] Confirm it writes the result file.
- [ ] Confirm Codex can import the result file.
- [ ] Confirm no credential, cookie, token, or browser state file is committed.
