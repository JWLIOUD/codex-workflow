# 需求交接：心衛中心原刊連結與搜尋結果網站名稱

- 建立日期：2026-06-14
- 需求角色：需求分析 AI
- 工程評估角色：網頁工程師 AI
- 現狀分析角色：現狀分析 AI
- 來源：使用者提出「每篇專題文章原刊於台北市社區心理衛生中心網頁，希望個人網站文章逐篇連到對應頁面」；另附 Google 搜尋「黃郁倩」結果截圖。
- 狀態：已完成實作並完成來源連結實際驗證。25 篇文章皆已確認台北市社區心理衛生中心原刊 URL，來源頁皆可開啟且內容對應文章主題，並已加入文章頁來源卡片與 JSON-LD `isBasedOn`。

## 需求摘要

每篇 `/articles/{slug}.html` 文章頁需顯示一個穩定、清楚、方便維護的「原刊來源」連結，連至台北市社區心理衛生中心該篇文章的對應頁面。連結需讓讀者知道文章並非任意轉載，也讓搜尋引擎理解作者與原刊出處的可信脈絡。

同時，需修正 Google 搜尋結果中本站第二筆顯示「yuchienpsy.com」而不是更理想的網站名稱問題。這不是單純畫面錯誤，而是 Google 尚未採用或尚未能穩定辨識本站 site name。

## 目前網站狀態

- 文章頁由 `/Users/liuzhewei/Documents/Codex/therapist-profile/tools/generate_articles.py` 統一產生。
- 文章詳頁模板位置：`article_page()`。
- 目前每篇文章已有：
  - `<title>`
  - `<meta name="description">`
  - `<link rel="canonical">`
  - Open Graph / Twitter metadata
  - `Article` JSON-LD
  - `BreadcrumbList` JSON-LD
- 目前每篇文章尚未有：
  - 原刊來源連結
  - 外部來源 URL 資料表
  - `Article.sameAs` 或 `Article.isBasedOn` 等可追溯外部來源欄位
- 首頁目前已有：
  - title：`黃郁倩 諮商心理師｜理解你的感受，陪伴你找到力量`
  - description
  - `LocalBusiness` JSON-LD
  - `FAQPage` JSON-LD
- 首頁目前尚未有：
  - `WebSite` JSON-LD 的 `name` / `alternateName`
  - `og:site_name`

## 工程師 AI 評估：來源連結放置方式

### 建議做法

不要逐篇手動修改 HTML。應在產生器中建立結構化來源資料，再由模板統一輸出。

建議新增一個資料結構，例如：

```python
ARTICLE_SOURCE_LINKS = {
    "addiction-01": {
        "label": "台北市社區心理衛生中心原刊文章",
        "url": "https://...",
    },
}
```

或獨立成 JSON 檔：

```json
{
  "addiction-01": {
    "label": "台北市社區心理衛生中心原刊文章",
    "url": "https://..."
  }
}
```

若後續會持續新增文章，較推薦 JSON 檔，讓非工程角色也能維護；若目前只是一批 25 篇，先放 Python 常數也可以。

### 顯示位置

建議放在正文結束後、內容聲明前，樣式接近資訊卡：

```html
<aside class="article-source" aria-label="文章原刊來源">
  <strong>原刊來源</strong>
  <p>本文原刊於台北市社區心理衛生中心心理健康專欄。</p>
  <a href="..." target="_blank" rel="noopener noreferrer">前往原刊頁面</a>
</aside>
```

理由：

- 不干擾讀者閱讀正文。
- 比放在頁首更不會把讀者太早導出本站。
- 比藏在頁尾更清楚，能補強文章可信度。
- 可用 `aria-label` 提高語意清楚度。

### 連結文字

建議統一使用：

`原刊於台北市社區心理衛生中心心理健康專欄：前往原刊頁面`

不建議只寫「點我」、「連結」或裸網址，因為可讀性與可及性較差。

### 外連屬性

建議：

```html
target="_blank" rel="noopener noreferrer"
```

不建議加 `nofollow`。如果這是正式、可信、相關的政府／公部門來源，保留正常外連即可。

### 結構化資料

每篇文章的 `Article` JSON-LD 可增加外部來源欄位，建議由工程師依實作可行性二擇一：

- `sameAs`: 原刊頁與本站文章是同一篇文章的另一個公開位置。
- `isBasedOn`: 若本站文章有調整、改寫、刪修或重新排版，則用此欄位表達「基於原刊內容」較保守。

在目前情境中，若本站文章內容基本等同原刊，建議使用 `sameAs`；若後續本站會修正錯字、調整段落或刪改求助資訊，建議使用 `isBasedOn`，避免宣稱完全相同。

## 現狀分析 AI 評估：來源連結對流量的影響

### 可能正面影響

- 增加文章可信度：公部門原刊來源可補強專業與權威感，對心理健康類內容尤其重要。
- 改善使用者信任：讀者看到原刊單位後，較容易理解文章是正式專欄，不只是個人網站自說自話。
- 有助於搜尋引擎理解作者脈絡：本站、作者、外部原刊平台之間的關係更清楚。
- 若心衛中心頁面本身也能連回本站，效果會更好，因為會形成雙向關聯與權威背書。

### 可能限制

- 單向連出去本身不保證排名上升。
- 若使用者太早被導到外站，可能降低本站停留與轉換，所以來源連結不建議放在文章頁首。
- 若原刊頁也被 Google 視為同一內容，兩站可能競爭同一篇文章的排名；但加上清楚 canonical 與來源語意，可以降低混亂。
- 若原刊頁無法公開存取、網址不穩、或日後改版失效，會造成壞連結，需要定期驗收。

### SEO 判斷

整體評估：正面，但屬於「可信度與語意清楚」的長期幫助，不是立即流量暴增工具。

最理想狀態：

1. 本站文章頁保留自己的 canonical。
2. 本站顯示原刊來源連結。
3. JSON-LD 補上 `sameAs` 或 `isBasedOn`。
4. 心衛中心原刊頁若能標示作者名稱並連回本站或作者介紹頁，效果最佳。

## Google 搜尋結果顯示問題

### 使用者觀察

搜尋「黃郁倩」時，第一筆外部網站顯示：

- 網站名稱：陪伴心理諮商體系
- URL：`acmate-group.com`
- 標題：黃郁倩心理師

本站顯示：

- 網站名稱：`yuchienpsy.com`
- URL：`yuchienpsy.com`
- 標題：黃郁倩諮商心理師｜關於我

使用者期待本站也能像第一筆一樣顯示「網站名稱 + 網頁標題」，而不是 domain。

### 判斷原因

Google 搜尋結果最上方的小字是 site name，不一定等於 `<title>`。本站目前 title 與 metadata 有寫好，但缺少明確的 `WebSite` 結構化資料與 `og:site_name`，Google 因此可能直接用 domain `yuchienpsy.com` 當作 site name。

此外，截圖中本站搜尋結果標題是「黃郁倩諮商心理師｜關於我」，但目前本地首頁 `<title>` 是「黃郁倩 諮商心理師｜理解你的感受，陪伴你找到力量」。這代表 Google 顯示的結果可能仍是舊版快取、錨點內容判斷，或 Google 自行改寫標題。此問題不一定能立即修正，但可以提高 Google 採用正確名稱的機率。

### 建議修正

首頁 `<head>` 增加：

```html
<meta property="og:site_name" content="黃郁倩 諮商心理師">
```

首頁 JSON-LD 增加：

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "黃郁倩 諮商心理師",
  "alternateName": "郁倩心理師",
  "url": "https://yuchienpsy.com/"
}
```

也可在文章頁、系列頁、專欄首頁補上 `og:site_name`，讓全站社群與搜尋語意一致。

### 搜尋結果期待

短期期待：

- 小字 site name 從 `yuchienpsy.com` 逐步變成「黃郁倩 諮商心理師」。
- 搜尋標題較穩定顯示首頁 title 或更合理的品牌標題。

注意：Google 不保證立即採用網站指定的 site name 或 title，通常需要重新抓取與一段時間觀察。

## 使用者確認結果

- [x] Google site name 使用「黃郁倩 諮商心理師」。
- [x] 使用者授權逐篇比對台北市社區心理衛生中心原刊頁面。
- [x] 來源連結放在正文後、內容聲明前。
- [x] 連結文字使用「前往原刊頁面」。
- [x] 因本站文章已有部分錯字、法規與求助資訊修正，JSON-LD 採用較保守的 `isBasedOn`。

## 原刊 URL 比對結果

### 已確認並已實作

| 本站文章 | 心衛中心原刊 URL |
|---|---|
| `/articles/addiction-01.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=3D674DEEAF3F73B0` |
| `/articles/addiction-02.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=50CE07A385B3B612` |
| `/articles/addiction-03.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=91D7F977E87FE3C0` |
| `/articles/addiction-04.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=2AC1351402564E6B` |
| `/articles/addiction-05.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=7829AAB9690E36B0` |
| `/articles/addiction-06.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=F39940A76ABD4498` |
| `/articles/addiction-07.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=CFB4198B850ECC95&sms=F3B948768F07712C&s=365D601A67285EFA` |
| `/articles/boundary-01.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=F26D9EDCC2B987E6` |
| `/articles/workplace-01.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=D75FD5A60B0A944B` |
| `/articles/workplace-02.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=83E456DAA4866B05` |
| `/articles/workplace-03.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=2B82BF204E79233B` |
| `/articles/workplace-05.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=C055A3C111939DB9` |
| `/articles/workplace-06.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=C67BFD2F8898DF6C` |
| `/articles/workplace-07.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=312E5B8E5F0F7D30` |
| `/articles/workplace-08.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=AAC728154AF14339&sms=D7C906BCBC57377D&s=E64DEAEEB3B3458A` |
| `/articles/boundary-02.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=CC74D12A815F9F4E` |
| `/articles/boundary-03.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=95320434A94A30CD` |
| `/articles/boundary-04.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=3C978A675DB273BE` |
| `/articles/boundary-05.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=8A65A282F0636702` |
| `/articles/boundary-06.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=57AFE5383F1DBAB9` |
| `/articles/boundary-07.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=5E95684569241C17` |
| `/articles/relationship-control.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=AFF5047157696D81` |
| `/articles/love-and-imperfection.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=160B9C4672BF2849&sms=D9970CDAAAA49C91&s=AF62ED96775EB103` |
| `/articles/self-care-07.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=117760319DAB664F&sms=0D9C3FAA1367281C&s=C552C927A56FFAA4` |
| `/articles/post-election-self-care.html` | `https://mental-health.gov.taipei/News_Content.aspx?n=A526AC306CCFCE21&sms=69F6D3EF07A1110E&s=5F05187A8CB988F0` |

## 來源連結驗收補充

- 2026-06-14 驗收工程師 AI 發現：不能只檢查文章頁「有沒有來源連結」，必須逐一開啟來源 URL，確認官方頁面不是 404，且頁面標題或正文能對應本站文章。
- 原本由現狀分析 AI 先行比對的 16 篇 URL 實測皆為 404；已依使用者建議的「文章名稱 + 心理衛生中心」搜尋法，以及心衛中心分類頁候選 title 比對，修正為有效 URL。
- 最新驗收結果：25 篇來源 URL 全部回傳 HTTP 200，且官方頁面 title/內容皆命中對應文章關鍵字；目前無需交接需求分析 AI 處理的失效來源連結。
- 後續固定驗收項目：每次新增或更新 `ARTICLE_SOURCE_LINKS` 後，驗收工程師 AI 必須實際開啟來源 URL，檢查 HTTP 狀態與內容對應，不得只檢查 HTML 是否存在連結。

## 文章來源連結驗證與更正 SOP

### 適用時機

以下任一情況發生時，都必須執行此流程：

- 新增文章來源 URL。
- 修改 `tools/generate_articles.py` 中的 `ARTICLE_SOURCE_LINKS`。
- 重新產生文章頁。
- 上線前驗收。
- Search Console 或使用者回報來源連結失效。

### 驗證方法

1. 從 `ARTICLE_SOURCE_LINKS` 取得每篇文章 slug 與心衛中心來源 URL。
2. 逐篇開啟來源 URL，不可只檢查本站 HTML 是否有 `<a href>`。
3. 檢查 HTTP 狀態：
   - `200`：可進入內容對應檢查。
   - `404`、重新導向到錯誤頁、空白頁、或無法連線：視為 FAIL。
4. 檢查官方頁面內容是否對應本站文章：
   - 官方頁面 `<title>` 或正文需包含本站文章的核心標題關鍵字。
   - 不可只因為官方頁面正文的「相關連結」出現文章名稱就判定通過。
   - 若同系列文章互相出現在頁尾相關連結，必須以官方頁面 title 作為主要判斷依據。
5. 檢查本站文章頁：
   - `.article-source` 卡片存在。
   - 畫面連結與 JSON-LD `isBasedOn.url` 完全一致。
   - 外連含 `target="_blank"` 與 `rel="noopener noreferrer"`。
6. 驗收結果需寫入 `test-report.md`：
   - PASS：列出驗證日期、文章數量、檢查方法。
   - FAIL：逐篇列出 slug、本站文章標題、失效 URL、失效原因、建議查找關鍵字。

### 更正方式

若來源 URL 失效或內容不對應，依序使用以下方式修正：

1. 使用 Google 搜尋：
   - 搜尋格式：`文章完整標題 + 心理衛生中心`
   - 例如：`擁抱自己的脆弱也是一種勇敢 心理衛生中心`
   - 優先選擇 `mental-health.gov.taipei/News_Content.aspx` 的官方結果。
2. 若 Google 結果不清楚，改查心衛中心分類頁：
   - 成癮系列：`n=CFB4198B850ECC95&sms=F3B948768F07712C`
   - 職場系列：`n=AAC728154AF14339&sms=D7C906BCBC57377D`
   - 性騷擾／關係界線相關：`n=160B9C4672BF2849&sms=D9970CDAAAA49C91`
   - 心靈雞湯／自我照顧：`n=117760319DAB664F&sms=0D9C3FAA1367281C`
   - 選舉／社會事件壓力：`n=A526AC306CCFCE21&sms=69F6D3EF07A1110E`
3. 從候選頁確認官方頁面 title 是否直接對應文章標題。
4. 將正確 URL 更新到 `tools/generate_articles.py` 的 `ARTICLE_SOURCE_LINKS`。
5. 若找不到可確認的官方 URL：
   - 不可保留原本失效 URL。
   - 不可使用疑似但無法確認對應的 URL。
   - 網頁工程師 AI 應先從 `ARTICLE_SOURCE_LINKS` 移除該篇 slug，或暫時註解該筆資料並標明待補來源。
   - 重新產生文章頁後，該篇文章不應輸出 `.article-source` 來源卡片。
   - 該篇文章的 Article JSON-LD 不應輸出 `isBasedOn`，避免把錯誤來源交給搜尋引擎。
   - 將該篇文章列入「待需求分析確認來源」清單，交接需求分析 AI 後續處理。
6. 重新執行文章產生器：

```bash
/Users/liuzhewei/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/generate_articles.py
```

7. 再次執行來源連結驗證，確認失效項目已修正；若該篇已暫時屏蔽來源，需確認文章頁沒有來源卡片與 `isBasedOn`。
8. 更新本交接文件與 `test-report.md`。

### 網頁工程師 AI 處理規則

當驗收工程師 AI 或使用者回報來源 URL 有問題時，網頁工程師 AI 應依照以下規則處理：

1. 先確認問題類型：
   - URL 404、無法開啟、重新導向錯誤頁。
   - URL 可開啟，但官方頁面 title／正文不是對應文章。
   - 本站畫面來源卡片 URL 與 JSON-LD `isBasedOn.url` 不一致。
2. 若能找到正確官方 URL：
   - 更新 `ARTICLE_SOURCE_LINKS[slug]`。
   - 重新執行 `tools/generate_articles.py`。
   - 確認文章頁來源卡片與 JSON-LD `isBasedOn.url` 已同步更新。
3. 若暫時找不到正確官方 URL：
   - 從 `ARTICLE_SOURCE_LINKS` 移除該篇 slug，讓產生器自動屏蔽該篇來源區塊。
   - 重新執行 `tools/generate_articles.py`。
   - 確認該文章頁沒有 `.article-source`。
   - 確認該文章頁 JSON-LD 沒有 `isBasedOn`。
   - 在交接 MD 中列出：文章 slug、文章標題、失效 URL、已嘗試搜尋方式、目前處理狀態為「來源暫時屏蔽，待需求分析確認」。
4. 不允許的處理：
   - 不可留下已知 404 或內容錯置的來源連結。
   - 不可用其他非官方網站替代心衛中心原刊頁。
   - 不可只改 HTML 而不更新 `ARTICLE_SOURCE_LINKS`，因為文章頁會由產生器重建。
   - 不可只改畫面卡片而忘記 JSON-LD `isBasedOn`。

### 角色分工

- 驗收工程師 AI：
  - 執行逐篇 URL 實測。
  - 整理失效、404、內容不對應清單。
  - 將問題交接需求分析 AI。
- 需求分析 AI：
  - 依「文章標題 + 心理衛生中心」搜尋法尋找正確官方 URL。
  - 判斷候選來源是否真的對應文章。
  - 將確認後的 URL 交接網頁工程師 AI。
- 網頁工程師 AI：
  - 更新 `ARTICLE_SOURCE_LINKS`。
  - 重新產生文章頁。
  - 確認畫面來源卡片與 JSON-LD `isBasedOn` 同步。
  - 若找不到正確官方 URL，先移除該篇 `ARTICLE_SOURCE_LINKS` 對應資料，讓來源卡片與 `isBasedOn` 暫時不輸出，並交接需求分析 AI 補來源。

### 本次修正紀錄

- 原本 16 篇來源 URL 實測為 404。
- 已依上述流程改為有效 URL。
- 2026-06-14 最終驗收：25 篇官方來源 URL 全部 HTTP 200，且 title／正文皆對應本站文章。

## 工程交接

### 建議修改檔案

- `/Users/liuzhewei/Documents/Codex/therapist-profile/tools/generate_articles.py`
- `/Users/liuzhewei/Documents/Codex/therapist-profile/article.css`
- `/Users/liuzhewei/Documents/Codex/therapist-profile/index.html`
- 必要時同步調整：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/articles.html`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/series/*.html`

### 實作步驟

1. 新增文章 slug 對應原刊 URL 的資料來源。
2. `article_page()` 讀取來源 URL。
3. 若該 slug 有來源 URL，輸出 `.article-source` 卡片。
4. `Article` JSON-LD 補上 `sameAs` 或 `isBasedOn`。
5. `article.css` 新增 `.article-source` 樣式。
6. 首頁新增 `WebSite` JSON-LD 與 `og:site_name`。
7. 全站主要頁面可補 `og:site_name`。
8. 重新產生文章頁。
9. 驗收所有外部來源連結可開啟、沒有空連結、沒有錯置文章。

### 驗收標準

- [ ] 25 篇文章若有對應 URL，皆顯示原刊來源卡片。
- [ ] 原刊連結文字清楚，點擊後另開新分頁。
- [ ] 原刊連結使用 `rel="noopener noreferrer"`。
- [ ] 沒有原刊 URL 的文章不輸出空卡片。
- [ ] JSON-LD 合法，且外部來源欄位與畫面連結一致。
- [ ] 首頁包含 `WebSite` JSON-LD。
- [ ] 首頁與主要頁面包含 `og:site_name`。
- [ ] 重新提交 sitemap 後，Search Console 無新增 metadata 或結構化資料錯誤。

## 參考

- Google Search Central：Title links
  - `https://developers.google.com/search/docs/appearance/title-link`
- Google Search Central：Site names
  - `https://developers.google.com/search/docs/appearance/site-names`
- Google Search Central：Make your links crawlable
  - `https://developers.google.com/search/docs/crawling-indexing/links-crawlable`
