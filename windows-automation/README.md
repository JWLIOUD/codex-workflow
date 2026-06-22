# Windows Automation Host

Windows 11 can be used as the long-running host for Codex maintenance work because it is less likely to sleep, disconnect, or interrupt scheduled follow-up tasks.

## Good Uses

- Periodically check repo status.
- Periodically run tests or build checks.
- Monitor important files such as:
  - `WorkFlow/project/YucheinHomePage/docs/project/todo.md`
  - `WorkFlow/project/YucheinHomePage/docs/project/search-performance.md`
  - `WorkFlow/project/YucheinHomePage/docs/project/release-log.md`
- Run Search Console follow-up checks.
- Use Codex automations or thread automations for scheduled tracking.

## Recommended Setup

1. Install Git for Windows.
2. Install GitHub CLI.
3. Install Codex App.
4. Clone this workflow repo.
5. Clone the website source repo separately.
6. Keep the browser logged into Google Search Console.
7. Configure Windows power settings to avoid sleep during automation windows.

## Suggested Folder Layout

```text
C:\Users\<you>\Documents\Codex\
  codex-workflow\
  therapist-profile\
```

## Automation Rules

- Keep secrets outside Git.
- Write results into Markdown files under `WorkFlow/project/YucheinHomePage/docs/project/`.
- Do not repeatedly request Search Console indexing for URLs that are already indexed or already requested.
- If an automation hits a quota limit, record the result and retry on a later schedule.
- When a temporary automation finishes its task, restore or delete it so it does not keep running unnecessarily.

## Example Automation Task

Search Console indexing follow-up:

- inspect target URLs
- skip already indexed or already requested URLs
- request indexing only for eligible URLs
- update `search-performance.md`
- stop if quota is exceeded

Project-specific automation spec:

- `WorkFlow/project/YucheinHomePage/docs/project/search-console-indexing-automation.md`
- `WorkFlow/project/YucheinHomePage/docs/project/search-console-indexing-queue.md`
