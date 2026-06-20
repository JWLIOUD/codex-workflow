# 專案總管 v2 派工路由

此文件定義 `yuchienpsy.com` 專案總管 AI 的 v2 派工規則。v2 的核心是把需求分成「討論、開發、維運、混合」四種模式，並在每種模式中建立明確的 close loop。

## 啟動順序

每次開始前：

1. 在會修改的 repo 執行 `git status -sb`。
2. 閱讀 `AGENTS.md`、專案 `README.md`、`project-manager.md`。
3. 閱讀 `todo.md`、`requirements.md`、`decision-board.md`。
4. 視任務讀取 `search-performance.md`、`release-log.md`、`test-report.md`、`implementation-log.md`。

## 四種模式

### 1. 需求討論模式

使用時機：

- 目標不明確。
- 需要文案、定位、SEO、視覺或內容策略決策。
- 可能影響專業形象、使用者期待、心理健康表述或法律/危機邊界。

角色順序：

1. 專案總管 AI
2. 需求分析 AI
3. 使用者風險分析 AI
4. 專業形象分析 AI
5. 必要時加入網頁工程 AI 評估可行性

完成條件：

- `meeting-notes.md` 有討論紀錄。
- `requirements.md` 有已確認需求，或 `decision-board.md` 有待使用者決策項。
- 不明確內容不得交付工程。

### 2. 開發模式

使用時機：

- 新增或修改網站功能、頁面、文案、SEO、圖片、sitemap、robots。
- 修正已確認 bug。
- 更新可驗收的網站原始碼。

角色順序：

1. 專案總管 AI
2. 需求分析 AI，若需求尚未正式化
3. 網頁工程 AI
4. 網頁測試 AI
5. 維運監控 AI，若影響搜尋或正式站觀察

完成條件：

- 工程修改完成。
- `implementation-log.md` 有紀錄。
- `test-report.md` 有驗收結果。
- 通過驗收後才能更新 `done.md`。
- 若已上線，更新 `release-log.md` 與 `search-performance.md`。

### 3. 維運模式

使用時機：

- 檢查 Search Console、索引、sitemap、robots、HTTP 狀態。
- 每週流量更新。
- 正式站健康檢查。
- 上線後觀察節點。

角色順序：

1. 專案總管 AI
2. 維運監控 AI
3. 網站現況分析 AI
4. 網頁測試 AI，若需要驗收證據

完成條件：

- `search-performance.md` 或 `test-report.md` 有紀錄。
- 異常若需要改程式，轉混合模式。

### 4. 混合模式

使用時機：

- 一開始像維運檢查，但發現需求缺口或工程 bug。
- 一開始像 bug，但需要先證明現況。
- Search Console 或正式站問題不確定是外部延遲、設定問題或網站問題。

角色順序：

1. 維運監控 AI 或網站現況分析 AI 先蒐證。
2. 若是需求不明，轉需求討論模式。
3. 若是工程缺口，轉開發模式。
4. 修正後回到維運或測試驗收。

完成條件：

- 現況證據、原因判讀與後續模式都被記錄。
- 不得未蒐證就直接改網站。

## 高風險升級條件

遇到以下情況，必須先回到需求討論模式，不得直接開發：

- 專業形象、心理健康表述、診斷、療效、危機或法律風險。
- 可能讓使用者誤解服務承諾或緊急支援能力。
- 對首頁定位、合作入口或個案期待有重大影響。
- 使用者需要在多個價值取捨中做選擇。

## 總管回報格式

- 模式分類。
- 派工角色。
- 讀取證據。
- 已完成事項。
- 驗收結果。
- 文件更新。
- 是否 commit / push。
- 是否需要使用者決策或 Search Console 操作。
