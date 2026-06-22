# 專案協作中心

此資料夾是專案總管 AI、網站現況分析 AI、需求分析 AI、插畫家 AI、網頁工程 AI、
網頁測試 AI 與使用者共同使用的唯一交接來源。

## 文件索引

| 文件 | 用途 | 主要維護角色 |
|---|---|---|
| `handoff.md` | 提供各角色快速掌握本次專欄更新目標、規則與執行順序 | 需求分析 AI |
| `site-inventory.md` | 保存目前頁面、功能、內容、資產、問題與重複需求檢查 | 網站現況分析 AI |
| `content-review.md` | 保存疑似錯字、語句與來源問題及使用者決議 | 需求分析 AI |
| `illustration-brief.md` | 保存已確認的圖片目的、構圖、尺寸與視覺限制 | 需求分析 AI |
| `illustration-assets.md` | 保存正式圖片路徑、尺寸、替代文字與工程使用方式 | 插畫家 AI |
| `brand-style-guide.md` | 保存網站長期品牌氣質、色彩、文案、SEO 與品質原則 | 網站品質總監 AI |
| `visual-content-system.md` | 保存主視覺、系列圖、文章圖、講座圖與裁切規格 | 插圖企劃 AI |
| `release-log.md` | 保存每次網站正式上線的時間、需求及影響頁面 | 網頁工程 AI／使用者 |
| `search-performance.md` | 保存 Search Console 基準與更新前後流量影響 | 網站現況分析 AI |
| `search-console-indexing-automation.md` | 保存每日 URL Inspection 與 Request indexing 自動化規格 | 專案總管 AI／網站現況分析 AI |
| `search-console-indexing-queue.md` | 保存 Search Console 索引追蹤 URL 佇列與每日處理狀態 | 網站現況分析 AI |
| `meeting-notes.md` | 保存每次需求討論、決議及待確認問題 | 需求分析 AI |
| `requirements.md` | 保存經使用者確認的正式需求與驗收條件 | 需求分析 AI |
| `todo.md` | 保存尚未完成、進行中及受阻的工作 | 需求分析 AI／網頁工程 AI |
| `decision-board.md` | 保存總管層級的進行中、下一步、待決策與高風險事項 | 專案總管 AI |
| `done.md` | 保存已實作且通過驗收的工作 | 網頁測試 AI |
| `implementation-log.md` | 保存程式修改、技術決策與工程自測結果 | 網頁工程 AI |
| `test-report.md` | 保存需求驗收、問題紀錄與回歸測試結果 | 網頁測試 AI |
| `quality-audit-2026-06-21.md` | 保存網站品質管理團隊補驗收結果、限制與後續品質任務 | 網站品質總監 AI |
| `visual-hierarchy-fix-2026-06-21.md` | 保存 2026-06-21 文章與系列頁主視覺層級修正的派工、執行與驗收 close loop | 專案總管 AI／品牌一致性 QA AI |

## AI 角色文件

| 文件 | 角色 |
|---|---|
| `../ai-roles/project-manager.md` | 專案總管 AI |
| `../ai-roles/website-quality-director.md` | 網站品質總監 AI |
| `../ai-roles/content-editor.md` | 內容編輯 AI |
| `../ai-roles/seo-strategist.md` | SEO 策略 AI |
| `../ai-roles/layout-experience-ai.md` | 版面體驗 AI |
| `../ai-roles/illustration-planner.md` | 插圖企劃 AI |
| `../ai-roles/talks-collaboration-content-ai.md` | 講座合作內容 AI |
| `../ai-roles/brand-quality-reviewer.md` | 品牌一致性 QA AI |
| `../ai-roles/current-state-analyst.md` | 網站現況分析 AI |
| `../ai-roles/requirements-analyst.md` | 需求分析 AI |
| `../ai-roles/user-risk-analyst.md` | 使用者風險分析 AI |
| `../ai-roles/professional-brand-analyst.md` | 專業形象分析 AI |
| `../ai-roles/operations-maintenance-ai.md` | 維運監控 AI |
| `../ai-roles/illustrator.md` | 插畫家 AI |
| `../ai-roles/web-engineer.md` | 網頁工程 AI |
| `../ai-roles/web-tester.md` | 網頁測試 AI |

## 工作流程

1. 專案總管 AI 接收使用者需求，先依 v2 路由判斷為需求討論模式、開發模式、維運模式或混合模式。
2. 明確工作由專案總管 AI 依任務性質直接派給合適角色，並規劃執行、驗收、回饋、修正、收斂的 close loop。
3. 需要討論的需求先交給需求分析 AI；若涉及使用者期待或專業形象，加入使用者風險分析 AI 與專業形象分析 AI。
4. 若需求涉及網站質感、圖片、文案、SEO、講座合作或主視覺，啟動網站品質管理團隊。
5. 需求分析 AI 對照 `CAP-xxx`，判斷需求是沿用、修改、取代或新增功能。
6. 尚未確認的內容保留為「提案」或「待確認」，不得交付開發。
7. 使用者確認後，需求分析 AI 將內容寫入 `requirements.md`，並分配 `REQ-xxx` 編號。
8. 每項正式需求拆成 `TASK-xxx`，加入 `todo.md`。
9. 網站現況分析 AI 盤點網站，將結果寫入 `site-inventory.md`，並建立或更新 Search Console 流量基準。
10. 需要新圖片時，插圖企劃 AI 建立 `ILL-REQ-xxx` 並寫入 `illustration-brief.md`。
11. 插畫家 AI 產生圖片、放入網站專案，並在 `illustration-assets.md` 記錄 `ILL-ASSET-xxx` 與路徑。
12. 使用者或需求分析 AI 完成視覺確認後，素材狀態改為「可供工程使用」。
13. 網頁工程 AI 只實作狀態為「已確認」的需求及「可供工程使用」的圖片，並更新 `todo.md` 與 `implementation-log.md`。
14. 網頁測試 AI 依 `requirements.md` 的驗收條件測試，將結果寫入 `test-report.md`。
15. 品牌一致性 QA AI 驗收圖文、SEO、排版、裁切與整體品牌氣質；未通過時回派對應角色。
16. 通過驗收的工作從 `todo.md` 移至 `done.md`；失敗項目建立 `BUG-xxx` 並退回對應角色。
17. 正式上線後建立 `REL-xxx` 更新紀錄，並在固定觀察節點更新 `search-performance.md`。
18. 專案總管 AI 維護 `decision-board.md`，同步進行中、下一步、待決策與高風險事項。

## 狀態定義

- `提案`：仍在討論，不可開發。
- `待確認`：規格已整理，等待使用者確認。
- `已確認`：可交付工程 AI。
- `進行中`：工程 AI 正在實作。
- `待驗收`：工程完成，等待測試。
- `受阻`：缺少資訊或存在無法繼續的問題。
- `已完成`：實作完成且測試通過。

## 編號規則

- 既有頁面：`PAGE-001`
- 既有功能：`CAP-001`
- 現況觀察：`OBS-001`
- 正式更新：`REL-YYYYMMDD-01`
- 流量分析：`IMPACT-YYYYMMDD-01`
- 正式需求：`REQ-001`
- 工程待辦：`TASK-001`
- 測試問題：`BUG-001`
- 圖片需求：`ILL-REQ-001`
- 圖片素材：`ILL-ASSET-001`
- 會議紀錄：`MTG-YYYYMMDD-01`

所有待辦、實作紀錄、測試結果與完成紀錄都必須引用相關需求編號。

## 交接原則

- `requirements.md` 是正式需求的唯一依據。
- `site-inventory.md` 是現況基準，但不是正式需求。
- 建立新需求前必須檢查相關 `CAP-xxx`、既有需求、待辦與完成紀錄。
- 會議中的想法若未獲確認，不得直接進入工程階段。
- 需求有變更時，先更新會議紀錄與正式需求，再修改程式。
- 圖片需求以 `illustration-brief.md` 為準；圖片路徑以 `illustration-assets.md` 為準。
- 工程 AI 不得使用仍處於「待視覺確認」或「退回修改」的素材。
- 不刪除歷史決議；被取代的內容應標示日期與原因。
- `done.md` 只收錄已通過測試的項目，不等同於「工程師已寫完」。
