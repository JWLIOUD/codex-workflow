# 開發、維運與混合模式工作流

此文件補足專案總管 v2 的實際執行順序，讓網站更新與長期維運可以在同一套 close loop 中運作。

## 開發模式

### 入口條件

- 使用者要求新增或修改網站內容、功能、SEO、圖片或頁面。
- `todo.md` 已有明確 `TASK-xxx`。
- 測試或維運發現明確工程 bug。

### 必讀

- `requirements.md`
- `todo.md`
- `implementation-log.md`
- `test-report.md`
- 相關角色文件

### 步驟

1. 確認需求是否已正式化。
2. 若未正式化，先交需求分析 AI。
3. 網頁工程 AI 實作最小可驗收修改。
4. 網頁測試 AI 依驗收條件檢查。
5. 驗收失敗時建立或更新 `BUG-xxx`，回工程修正。
6. 驗收通過後更新 `done.md`。
7. 若有正式上線，更新 `release-log.md`。
8. 若影響搜尋，交維運監控 AI 更新 `search-performance.md`。

### 完成定義

- 需求、實作、測試與狀態文件一致。
- 相關 repo 狀態清楚。
- 使用者知道是否已 commit / push。

## 維運模式

### 入口條件

- 使用者要求檢查狀態、Search Console、索引、sitemap、robots、正式站或週報。
- 排程或自動化需要更新紀錄。
- 上線後觀察節點到期。

### 必讀

- `search-performance.md`
- `release-log.md`
- `test-report.md`
- `workflows/search-console-indexing.md`

### 步驟

1. 確認檢查範圍與資料來源。
2. 收集證據，例如 HTTP 狀態、sitemap URL 數、robots、Search Console 狀態。
3. 判讀是否正常、觀察中或異常。
4. 記錄到 `search-performance.md` 或 `test-report.md`。
5. 若只是外部延遲或 Search Console 配額，記錄並排下次追蹤。
6. 若發現網站工程缺口，轉混合模式。

### 完成定義

- 狀態有證據。
- 異常有下一步。
- 沒有重複浪費 Search Console indexing 配額。

## 混合模式

### 入口條件

- 維運檢查發現可能是網站 bug。
- 網站 bug 可能其實是需求或內容策略問題。
- 使用者反映問題，但原因尚未確認。

### 步驟

1. 先蒐證，不直接修改。
2. 判斷問題類型：
   - 外部延遲或配額：留在維運模式。
   - 需求不明：轉需求討論模式。
   - 工程缺口：轉開發模式。
   - 驗收不足：交網頁測試 AI 補驗收。
3. 轉入對應模式後，完成該模式 close loop。
4. 回到 `decision-board.md` 或 `todo.md` 更新狀態。

### 完成定義

- 原因已分類。
- 後續角色明確。
- 文件已收斂，不靠聊天記憶當唯一依據。
