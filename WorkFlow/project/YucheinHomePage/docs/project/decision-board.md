# 專案決策看板

此文件由專案總管 AI 維護，用來收斂跨角色狀態、下一步與需要使用者決策的事項。它不取代 `todo.md`、`requirements.md` 或 `done.md`，而是提供一頁式總覽。

## 使用規則

- 明確任務仍寫入 `todo.md`。
- 已確認需求仍寫入 `requirements.md`。
- 已驗收完成項目仍寫入 `done.md`。
- 本文件只保存總管層級的進行中、下一步、待決策與風險。
- 每次重大切換工作模式時，總管 AI 應檢查是否需要更新本文件。

## 進行中

- Search Console 索引與流量觀察仍需依 `search-performance.md` 追蹤。
- 2026-06-22：每日 Search Console URL Inspection 自動化規格與 URL 佇列已建立；使用者已在 Codex Automations 建立每日 09:30 排程，ID：`yuchien-search-console-indexing-follow-up`。

## 已完成

- 2026-06-20：建立並推送專案總管 AI v1 工作流。
- 2026-06-21：建立專案總管 AI v2 架構文件，整合需求討論、開發、維運與混合模式。
- 2026-06-21：依開發模式修正 BUG-005，`articles.html#series` 手機系列卡片圖片比例本地與正式站回歸 PASS。

## 下一步

- Search Console 配額恢復後，依 `search-console-indexing-automation.md` 與 `search-console-indexing-queue.md` 每日接續索引追蹤。
- 下一次每日自動化執行後，確認是否成功更新 `search-console-indexing-queue.md` 與 `search-performance.md`。
- 檢查 `todo.md` 與 `test-report.md` 中待驗收/已完成狀態是否需要一致化整理。

## 需要使用者決策

- 是否優先恢復 Search Console 索引追蹤。
- 是否要把 v2 的「使用者風險分析 AI」與「專業形象分析 AI」納入每次首頁/文案/SEO 改動的必跑流程。

## 高風險事項

- 心理健康、法律、危機、診斷或療效相關文字不得直接進入工程，必須先走需求討論模式。
- Search Console 顯示已要求建立索引、網址在 Google 服務中或網頁已編入索引時，不得重複 Request indexing。
- workflow repo 與 website repo 不得混在同一個 commit。
