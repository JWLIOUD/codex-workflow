# Codex Workflow Repository

This repository stores the Codex workflow, project notes, role handoffs, prompts, and operating rules used to maintain `yuchienpsy.com`.

It is intended to be shared across Mac and Windows so work can continue from another machine without losing project context.

## What This Repo Contains

- `AGENTS.md`: operating rules for Codex when working in this repo.
- `WorkFlow/project/YucheinHomePage/`: current project knowledge for the psychology website.
- `docs/`: general long-lived documentation and project indexes.
- `workflows/`: reusable work procedures and checklists.
- `prompts/`: reusable prompts for role-based Codex work.
- `scripts/`: safe helper scripts, if added later.
- `windows-automation/`: notes for using Windows 11 as the long-running automation host.
- `archive/`: old or superseded workflow notes.

## What This Repo Excludes

This repo intentionally does not track:

- the website source repo `therapist-profile/`
- raw article draft files in `專欄文章/`
- Codex local state such as `.codex/` or `.agents/`
- credentials, tokens, cookies, `.env` files, caches, build output, or dependencies

The website source should continue to be managed through its own GitHub repository.

## Windows 11 Setup

On Windows 11, install:

- Git for Windows
- GitHub CLI (`gh`)
- Codex App
- A browser logged into the Google account that owns Search Console

Clone this workflow repo:

```powershell
git clone <GITHUB_REPO_URL>
cd <REPO_FOLDER>
```

Clone the website repo separately next to it:

```powershell
git clone <WEBSITE_REPO_URL> therapist-profile
```

Recommended Windows folder layout:

```text
Codex/
  codex-workflow/
  therapist-profile/
```

## Codex Startup Order

When starting work from Windows, ask Codex to read these first:

1. `AGENTS.md`
2. `README.md`
3. `WorkFlow/project/YucheinHomePage/docs/project/README.md`
4. `WorkFlow/project/YucheinHomePage/docs/project/search-performance.md`
5. `WorkFlow/project/YucheinHomePage/docs/project/todo.md`
6. `WorkFlow/project/YucheinHomePage/docs/project/release-log.md`
7. `WorkFlow/project/YucheinHomePage/docs/project/test-report.md`

## Updating Workflow Documents

Use these conventions:

- Long-term rules go in `AGENTS.md`, `docs/`, or `workflows/`.
- Project-specific records go in `WorkFlow/project/YucheinHomePage/docs/project/`.
- Role prompts go in `prompts/`.
- Windows automation notes go in `windows-automation/`.
- Superseded notes go in `archive/`.

Before committing:

```bash
git status -sb
git diff --stat
```

## Windows as the Automation Host

Use Windows 11 for tasks that benefit from long uptime:

- Search Console follow-up checks
- scheduled site status reviews
- weekly search-performance updates
- periodic test/build runs
- monitoring docs such as `todo.md` and `search-performance.md`

Keep secrets out of this repo. Store credentials in the Windows user account, browser profile, or a dedicated secret manager.
