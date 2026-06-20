# 專案協作中心

此資料夾是網站現況分析 AI、需求分析 AI、插畫家 AI、網頁工程 AI、
網頁測試 AI 與使用者共同使用的唯一交接來源。

## 文件索引

| 文件 | 用途 | 主要維護角色 |
|---|---|---|
| `handoff.md` | 提供各角色快速掌握本次專欄更新目標、規則與執行順序 | 需求分析 AI |
| `site-inventory.md` | 保存目前頁面、功能、內容、資產、問題與重複需求檢查 | 網站現況分析 AI |
| `content-review.md` | 保存疑似錯字、語句與來源問題及使用者決議 | 需求分析 AI |
| `illustration-brief.md` | 保存已確認的圖片目的、構圖、尺寸與視覺限制 | 需求分析 AI |
| `illustration-assets.md` | 保存正式圖片路徑、尺寸、替代文字與工程使用方式 | 插畫家 AI |
| `release-log.md` | 保存每次網站正式上線的時間、需求及影響頁面 | 網頁工程 AI／使用者 |
| `search-performance.md` | 保存 Search Console 基準與更新前後流量影響 | 網站現況分析 AI |
| `meeting-notes.md` | 保存每次需求討論、決議及待確認問題 | 需求分析 AI |
| `requirements.md` | 保存經使用者確認的正式需求與驗收條件 | 需求分析 AI |
| `todo.md` | 保存尚未完成、進行中及受阻的工作 | 需求分析 AI／網頁工程 AI |
| `done.md` | 保存已實作且通過驗收的工作 | 網頁測試 AI |
| `implementation-log.md` | 保存程式修改、技術決策與工程自測結果 | 網頁工程 AI |
| `test-report.md` | 保存需求驗收、問題紀錄與回歸測試結果 | 網頁測試 AI |

## AI 角色文件

| 文件 | 角色 |
|---|---|
| `../ai-roles/current-state-analyst.md` | 網站現況分析 AI |
| `../ai-roles/requirements-analyst.md` | 需求分析 AI |
| `../ai-roles/illustrator.md` | 插畫家 AI |
| `../ai-roles/web-engineer.md` | 網頁工程 AI |
| `../ai-roles/web-tester.md` | 網頁測試 AI |

## 工作流程

1. 網站現況分析 AI 盤點網站，將結果寫入 `site-inventory.md`，並建立 Search Console 流量基準。
2. 需求分析 AI 先閱讀現況報告，將討論內容寫入 `meeting-notes.md`。
3. 需求分析 AI 對照 `CAP-xxx`，判斷需求是沿用、修改、取代或新增功能。
4. 尚未確認的內容保留為「提案」或「待確認」，不得交付開發。
5. 使用者確認後，需求分析 AI 將內容寫入 `requirements.md`，並分配 `REQ-xxx` 編號。
6. 每項正式需求拆成 `TASK-xxx`，加入 `todo.md`。
7. 需要新圖片時，需求分析 AI 建立 `ILL-REQ-xxx` 並寫入 `illustration-brief.md`。
8. 插畫家 AI 產生圖片、放入網站專案，並在 `illustration-assets.md` 記錄 `ILL-ASSET-xxx` 與路徑。
9. 使用者或需求分析 AI 完成視覺確認後，素材狀態改為「可供工程使用」。
10. 網頁工程 AI 只實作狀態為「已確認」的需求及「可供工程使用」的圖片，並更新 `todo.md` 與 `implementation-log.md`。
11. 網頁測試 AI 依 `requirements.md` 的驗收條件測試，將結果寫入 `test-report.md`。
12. 通過驗收的工作從 `todo.md` 移至 `done.md`；失敗項目建立 `BUG-xxx` 並退回對應角色。
13. 正式上線後建立 `REL-xxx` 更新紀錄，並在固定觀察節點更新 `search-performance.md`。

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
