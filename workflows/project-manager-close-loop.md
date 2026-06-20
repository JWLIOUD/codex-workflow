# 專案總管 Close Loop 工作流程

此流程供專案總管 AI 管理 `yuchienpsy.com` 的需求、工程、驗收、回饋與 Search Console 追蹤。

## 1. 啟動檢查

1. 閱讀 `AGENTS.md`、`README.md` 與專案 `README.md`。
2. 閱讀 `docs/ai-roles/project-manager.md`。
3. 閱讀 `todo.md`、`requirements.md`、`handoff.md`。
4. 視任務需要閱讀 `test-report.md`、`implementation-log.md`、`release-log.md`、`search-performance.md`。
5. 在會修改的 repo 執行 `git status -sb`。

## 2. 任務分流

### 明確任務

若使用者已明確指定工作，且可制定驗收條件：

1. 確認是否已有 `REQ-xxx` 或 `TASK-xxx`。
2. 沒有任務時，補入 `todo.md`。
3. 指派合適角色。
4. 進入執行階段。

### 需討論任務

若目標、內容、風險或驗收條件未明：

1. 指派需求分析 AI。
2. 將討論寫入 `meeting-notes.md`。
3. 使用者確認後寫入 `requirements.md`。
4. 拆成 `TASK-xxx` 寫入 `todo.md`。
5. 再由總管 AI 派工。

## 3. 派工

| 工作 | 角色 | 必要輸出 |
|---|---|---|
| 現況、流量、索引 | 網站現況分析 AI | `site-inventory.md`、`search-performance.md` |
| 需求、文案、策略、驗收條件 | 需求分析 AI | `meeting-notes.md`、`requirements.md`、`todo.md` |
| 圖像需求與素材 | 插畫家 AI | `illustration-brief.md`、`illustration-assets.md` |
| 網站實作 | 網頁工程 AI | website repo、`implementation-log.md` |
| 回歸驗收 | 網頁測試 AI | `test-report.md`、`done.md` |
| 跨角色收斂 | 專案總管 AI | `todo.md`、`handoff.md`、回報 |

## 4. 執行

1. 工程或文件修改前確認 repo 狀態。
2. 僅修改任務必要範圍。
3. 避免把 workflow repo 與 website repo 混 commit。
4. 執行後更新對應紀錄文件。

## 5. 驗收

依任務性質選擇驗收方式：

- 文件任務：檢查索引、連結、狀態、編號一致。
- 網站任務：檢查本地預覽、響應式、連結、metadata、主控台、必要時正式站。
- Search Console 任務：檢查 property、sitemap、URL Inspection 狀態與配額規則。
- 內容任務：確認已引用正式需求與使用者決議。

驗收失敗時：

1. 建立或更新 `BUG-xxx`。
2. 指派回對應角色。
3. 修正後重新驗收。

## 6. 收斂

驗收通過後：

1. 將任務狀態更新為已完成或移入 `done.md`。
2. 若有上線，更新 `release-log.md`。
3. 若影響搜尋，更新 `search-performance.md`。
4. 若有工程修改，更新 `implementation-log.md`。
5. 若形成長期規則，更新角色文件、workflow 或 prompt。

## 7. 使用者回報

每次完成後回報：

- 修改檔案。
- 變更 repo。
- 驗收結果。
- 是否 commit。
- 是否 push。
- 是否需要使用者確認。
- 是否需要 Search Console 操作。
