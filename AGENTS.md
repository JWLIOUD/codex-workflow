# Codex Agent Instructions

This is a cross-Mac / Windows Codex workflow repository for maintaining `yuchienpsy.com` and related project operations.

## Core Rules

- Before changing files, run `git status -sb`.
- Preserve user changes. Do not revert unrelated work.
- Keep long-term project knowledge in `docs/`, `workflows/`, or `WorkFlow/project/YucheinHomePage/docs/`.
- Keep role-specific prompts in `prompts/`.
- Keep Windows automation notes in `windows-automation/`.
- Do not write secrets, API keys, tokens, cookies, auth files, browser credentials, or private local state into this repo.
- Do not commit `.codex/`, `.agents/`, `.env`, `node_modules/`, build output, caches, or local browser/session state.
- Treat `therapist-profile/` as a separate website source repository unless the user explicitly asks to work inside that repo.
- When a task is complete, summarize changed files, verification performed, and any remaining risks.
- Remind the user when local changes still need commit or push.

## Project Context

The active website project is:

- Site: `https://yuchienpsy.com/`
- Website source repo: `therapist-profile/` when cloned next to this workflow repo
- Main workflow docs: `WorkFlow/project/YucheinHomePage/docs/project/`

Priority project files:

- `WorkFlow/project/YucheinHomePage/docs/project/README.md`
- `WorkFlow/project/YucheinHomePage/docs/project/search-performance.md`
- `WorkFlow/project/YucheinHomePage/docs/project/todo.md`
- `WorkFlow/project/YucheinHomePage/docs/project/release-log.md`
- `WorkFlow/project/YucheinHomePage/docs/project/test-report.md`
- `WorkFlow/project/YucheinHomePage/docs/project/requirements.md`

## Windows Automation Guidance

If a task benefits from long-running availability, propose moving it to Windows Codex automations or thread automations.

Good candidates:

- Search Console indexing follow-up
- weekly search-performance reports
- scheduled sitemap or HTTP checks
- periodic test/build verification
- monitoring `todo.md` for stale tasks

Automation prompts must include:

- exact target URLs or files
- what to record
- where to write results
- rules to avoid repeated quota usage
- completion criteria

For Search Console indexing tasks, never request indexing again when URL Inspection already shows:

- `已要求建立索引`
- `網址在 Google 服務中`
- `網頁已編入索引`

In those cases, record the status only.
