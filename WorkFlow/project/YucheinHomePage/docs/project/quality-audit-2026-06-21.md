# 網站品質管理團隊補驗收報告（2026-06-21）

## 驗收範圍

- 網站 repo：`therapist-profile`
- 線上站：`https://yuchienpsy.com/`
- 抽查頁面：首頁、文章列表、職場系列頁、成癮單篇文章、講座頁、sitemap、robots。

## 本輪限制

- 已完成：線上 HTTP 狀態、SEO metadata、sitemap/robots、本地 HTML/CSS、圖片尺寸與 WebP 容量檢查。
- 未完成：瀏覽器截圖人工視覺比對。Windows headless Chrome/Edge DevTools endpoint 未成功啟動。
- 因此本輪可判斷「規格與流程是否正確」，但「最後畫面是否完全符合美感」需下一輪用實際截圖補驗收。

## 技術與 SEO 結果

| URL | HTTP | robots | canonical | 結論 |
|---|---:|---|---|---|
| `/` | 200 | `index, follow` | `https://yuchienpsy.com/` | PASS |
| `/articles.html` | 200 | `index, follow` | `https://yuchienpsy.com/articles.html` | PASS |
| `/series/workplace.html` | 200 | `index, follow` | `https://yuchienpsy.com/series/workplace.html` | PASS |
| `/articles/addiction-01.html` | 200 | `index, follow` | `https://yuchienpsy.com/articles/addiction-01.html` | PASS |
| `/talks.html` | 200 | `noindex, follow` | `https://yuchienpsy.com/` | 現況 PASS，未來需重構 |
| `/sitemap.xml` | 200 | - | - | PASS |
| `/robots.txt` | 200 | - | - | PASS |

補充：

- sitemap 內列出的 URL 在本地 repo 都有對應檔案。
- `talks.html` 目前不在 sitemap，且設定 `noindex, follow`，符合「講座合作尚未重新獨立」的現況。
- 若後續要讓講座合作成為可索引頁，必須建立新需求，同步處理 canonical、robots、sitemap、title、description、OG image 與主視覺。

## 圖片與裁切結果

目前圖片系統符合新版品質規格：

| 類型 | 尺寸 | 用途 | 結論 |
|---|---:|---|---|
| 文章列表 hero 桌機 | `1600x900` | `/articles.html` 首屏主視覺 | PASS |
| 文章列表 hero 手機 | `900x1125` | `/articles.html` 手機主視覺 | PASS |
| 系列圖桌機 | `1600x900` | 系列卡片、系列頁桌機 | PASS |
| 系列圖手機 | `900x900` | 手機系列卡片、系列頁 hero | PASS |

WebP 圖片約 `64KB` 到 `183KB`，適合正式網站使用。PNG 檔案較大，應保留為來源或社群預覽素材，工程載入優先使用 WebP。

CSS 規則已確認：

- 文章列表系列卡片：桌機 `16 / 9`，手機 `1 / 1`
- 系列頁 hero：手機 `1 / 1`，桌機 `16 / 9`
- 圖片使用 `object-fit: cover`

品質結論：

- 技術裁切規格：PASS
- 裝置比例配置：PASS
- 主體是否被裁切影響觀感：需下一輪截圖人工確認

## 分角色驗收

### 網站品質總監 AI

狀態：PASS with follow-up。

目前網站氣質穩定：溫暖、柔和、可信任、不過度銷售。首頁真人照搭配柔和插圖，文章區以系列插圖建立一致性，方向正確。

修改方向：

- 講座合作未來重新獨立時，應維持心理師品牌的安定與專業，不要做成一般商業銷售頁。
- 建議為講座合作建立專用主視覺，不長期只沿用 headshot。

### 內容編輯 AI

狀態：PASS。

首頁、文章列表與抽查單篇文章語氣一致，偏故事型與陪伴型，沒有過度承諾療效。

修改方向：

- 未來講座頁文案應拆成：合作主題、適合單位、合作形式、邀約方式、實際活動或示意素材。
- CTA 要清楚，但避免過度銷售化。

### SEO 策略 AI

狀態：PASS，講座頁待決策。

可索引頁已有 title、description、canonical、robots。`talks.html` 目前 noindex 是合理現況。

修改方向：

- 若講座合作要成為搜尋入口，需建立 `REQ` 後再改，不應單點修改 metadata。
- 單篇文章目前共用系列 OG image，短期可接受；若要提升分享質感，應規劃每篇文章自己的主題圖。

### 版面體驗 AI

狀態：PASS，待補截圖。

BUG-005 修正後，系列卡片與系列頁圖片比例已有手機/桌機分流規則。

修改方向：

- 下一輪用實際截圖檢查：首頁、文章列表、系列頁、單篇文章、講座頁。
- 重點看 CTA 是否擠壓、圖片是否遮擋文字、卡片高度是否過長、手機首屏是否能看見下一段線索。

### 插圖企劃 AI

狀態：PASS。

目前已有 `ill-001` 文章列表 hero，以及 `ill-002` 至 `ill-006` 系列主題圖。

修改方向：

- 單篇文章主題圖不應直接大量複製系列圖，需先決定採「系列母圖 + 單篇變體」或「每篇獨立圖」。
- 每張新圖都應先建立 `ILL-REQ-xxx`，包含用途、比例、主體、安全區、情緒、禁用元素與 alt。

### 講座合作內容 AI

狀態：待需求討論。

目前 `talks.html` 可讀但不是獨立 SEO 頁。若重新獨立講座合作，應作為新專案切片處理。

建議工作包：

- `REQ-talks-landing`：講座合作頁重新獨立
- `REQ-talks-visual-system`：講座合作主視覺與活動示意圖
- `REQ-talks-seo`：講座合作 SEO 與 sitemap
- `REQ-talks-proof-assets`：實際活動照片、合作單位或講座主題素材清單

### 品牌一致性 QA AI

狀態：PASS with follow-up。

目前沒有必須立即修的品牌一致性阻斷項。系列圖尺寸、命名、alt 方向與文案氣質整體一致。

待補確認：

- 實際截圖人工視覺比對
- 首頁真人照與插圖在手機版的視覺平衡
- 講座頁未來獨立後的主視覺一致性

## 總結

目前網站可維持上線，不需要立即 hotfix。

建議新增追蹤任務：

| ID | 任務 | 負責角色 | 優先級 |
|---|---|---|---|
| `QA-IMG-001` | 補做手機/桌機截圖人工視覺比對 | 品牌一致性 QA AI、版面體驗 AI | P1 |
| `QA-TALKS-001` | 討論講座合作是否重新獨立成可索引頁 | 需求分析 AI、講座合作內容 AI、SEO 策略 AI | P2 |
| `QA-SEO-001` | 評估單篇文章是否需要獨立主題圖與 OG image | SEO 策略 AI、插圖企劃 AI | P2 |
| `QA-VIS-001` | 建立未來圖片裁切驗收清單與截圖欄位 | 插圖企劃 AI、品牌一致性 QA AI | P2 |

## 需要使用者確認

1. 講座合作頁是否要重新獨立並可被 Google 索引。
2. 單篇文章是否要逐篇製作自己的主題圖，或先維持系列圖策略。
3. 下一輪是否用實機或瀏覽器截圖補做最後視覺 QA。
