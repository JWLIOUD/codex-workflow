# 工程實作紀錄

網頁工程 AI 應在每次實作後更新此文件，讓測試 AI 能快速掌握修改範圍與測試重點。

## 實作紀錄範本

### DEV-YYYYMMDD-01：實作主題

- 日期：
- 對應需求：REQ-xxx
- 對應待辦：TASK-xxx
- 實作狀態：進行中／待驗收／受阻
- 修改檔案：
- 實作內容：
- 技術決策：
- 未完成項目：
- 已知限制：
- 工程自測：
- 建議測試重點：
- Git 分支：
- Commit：尚未提交／commit SHA

## 實作紀錄

### DEV-20260621-01：BUG-005 手機系列卡片圖片比例修正

- 日期：2026-06-21
- 對應問題：BUG-005
- 對應需求：REQ-003、REQ-004、REQ-007
- 實作狀態：驗收通過
- 修改檔案：`articles.css`
- 實作內容：
  - 將 `articles.html#series` 系列卡片圖片比例控制移到外層 `.series-card-art` 容器。
  - 桌機容器維持 `aspect-ratio: 16 / 9`。
  - 手機 `max-width: 639px` 改由 `.series-card-art` 強制 `aspect-ratio: 1 / 1`。
  - 圖片本身改為 `display: block` 與 `height: 100%`，避免 `<img width="1600" height="900">` 屬性在手機版覆蓋 900x900 圖片比例。
- 技術決策：
  - 不修改插畫素材、不修改 `series.css`，因五個系列頁手機首屏原本已維持 1:1。
  - `articles.html` 已使用 `articles.css?v=20260613-3`，本次不再提高版本號。
- 工程自測：
  - `git diff --check` 通過。
  - 靜態檢查：`articles.html#series` 有 5 個系列卡片與 5 個 `*-mobile-900x900.webp` source。
  - Chrome headless 手機檢查：五張系列卡片 rendered size 皆為 1:1，無水平溢出。
  - Chrome headless 手機逐張滾動檢查：五張系列卡片 `currentSrc` 皆為 `*-mobile-900x900.webp`，natural size 皆為 `900 × 900`。
  - Chrome headless 桌機檢查：系列卡片 rendered ratio 約 1.78，維持 16:9，無水平溢出。
  - Chrome headless 手機檢查五個系列頁：`workplace`、`addiction`、`boundary`、`self-care`、`insights` 首屏圖皆為 1:1，無水平溢出。
- Git 分支：`main`
- Commit：`e400cb1 Fix mobile series card image ratio`

### DEV-20260613-01：心理專欄文章系統

- 日期：2026-06-13
- 對應需求：REQ-001、REQ-002、REQ-003、REQ-004、REQ-005、REQ-006
- 對應待辦：TASK-001、TASK-003、TASK-004、TASK-005、TASK-006
- 實作狀態：待驗收
- 修改檔案：`articles.html`、`articles.css`、`article.css`、`articles/*.html`、`series/*.html`、`tools/generate_articles.py`
- 實作內容：由 Word 原始檔拆分並產製 25 篇文章、5 個分類頁，完成共用導覽、作者資訊、LINE CTA、上一篇／下一篇、延伸閱讀與 SEO 基本標記。
- 技術決策：文章頁統一放在 `/articles/`；舊文章路徑保留無 canonical 的 `noindex` 相容轉址；沒有可靠日期時不輸出日期；只建立有實際內容的分類；保留原文疑似錯字等待確認。
- 未完成項目：TASK-002 錯字逐項討論、TASK-007 SEO 驗收、TASK-008 跨裝置與瀏覽器驗收。
- 已知限制：既有 `talks.html` 缺少 canonical，屬本次專欄範圍外的既知問題。
- 工程自測：25 篇文章數量通過；31 個專欄相關頁面 title、canonical、內部連結與作者署名檢查通過；主要頁面本地 HTTP 回應 200；無 `href="#"`、不存在的主題頁連結或純分隔線段落。
- 建議測試重點：手機長標題換行、系列卡片高度、長文閱讀間距、鍵盤焦點、所有 LINE 外部連結、原文段落與錯字確認。
- Git 分支：`warm-illustration-redesign`
- Commit：尚未提交

### DEV-20260613-02：依驗收報告修正失敗項目

- 日期：2026-06-13
- 對應需求：REQ-004、REQ-005、REQ-006、REQ-007
- 對應待辦：TASK-002、TASK-007、TASK-008
- 實作狀態：待回歸
- 對應問題：BUG-001、BUG-002、BUG-003、BUG-004
- 修改檔案：`tools/generate_articles.py`、`articles.html`、`articles/*.html`、`series/*.html`
- 文件交接：`requirements-handoff-content-review.md`
- 實作內容：
  - 文章頁補齊 Article、BreadcrumbList 與完整 Twitter Card。
  - 系列／分類頁補齊 CollectionPage、BreadcrumbList 與完整 Twitter Card。
  - 專欄首頁將無日期依據的「最新文章／最近更新」改為「延伸閱讀／從這幾篇繼續探索」。
  - 文案疑似錯字與文字決策交接需求分析 AI，不套用未確認修改。
- 技術決策：SEO 欄位由產製工具統一輸出，避免逐頁手動維護；CollectionPage 的 `hasPart` 只列實際存在的文章。
- 未完成項目：BUG-002 需需求分析 AI 完成 `content-review.md`，並與使用者逐項確認。
- 工程自測：
  - 31 個正式頁面 SEO schema 與 Twitter metadata 檢查通過。
  - 32 個含相容頁的站內連結與資產檢查通過。
  - 25 篇正文與 Word 原稿正規化比對通過。
  - 390 與 1440 px 瀏覽器抽查無水平溢出，主控台無錯誤。
- 建議回歸重點：依 `test-report.md` 重測 BUG-001、BUG-003、BUG-004；BUG-002 等待需求分析完成後測試。
- Git 分支：`warm-illustration-redesign`
- Commit：尚未提交

### DEV-20260613-03：套用文案定稿與上線資訊修正

- 日期：2026-06-13
- 對應需求：REQ-002、REQ-003、REQ-005、REQ-006、REQ-007
- 對應待辦：TASK-002、TASK-007、TASK-008
- 實作狀態：待獨立回歸
- 需求依據：`handoff.md`、`content-review.md` 的 Q01–Q41、F01–F04
- 修改檔案：`tools/generate_articles.py`、`article.css`、`articles.css`、
  `articles.html`、`articles/*.html`、`series.css`、`series/*.html`
- 實作內容：
  - 將使用者同意的文字替換、標題格式與中英文間距寫入產製流程。
  - 系列前台名稱改為「自我理解與心理照顧」，保留「心理師的心靈雞湯」副標。
  - 修正 WHO／ICD-11 職業倦怠敘述，AI 研究段落改為初步研究的保守措辭。
  - 25 篇文章各加入一次心理健康科普內容聲明。
  - 移除編輯註記、`[連結]` 佔位符與未確認的私人求助電話。
  - 將報案、保護令及錄音錄影內容改為依個案洽警察、法院或法律專業人員的保守指引。
  - 加入「關懷 e 起來」政府官方連結。
- 查證來源與日期：
  - WHO〈Burn-out an occupational phenomenon〉，查證日期 2026-06-13：
    `https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases`
  - 全國法規資料庫，查證日期 2026-06-13：`https://law.moj.gov.tw/`
  - 衛生福利部 113 保護專線，查證日期 2026-06-13：`https://113.mohw.gov.tw/`
  - 社會安全網「關懷 e 起來」，查證日期 2026-06-13：`https://ecare.mohw.gov.tw/`
  - 內政部警政署，查證日期 2026-06-13：`https://www.npa.gov.tw/`
- 技術決策：
  - 原始 Word 不改寫；所有核准修正由 `generate_articles.py` 可重複產製。
  - 個別保留決議優先於全站格式規則，避免 Q16、Q17、Q20、Q21 被一般格式化修改。
  - 法律段落不提供個案結論，只保留官方求助入口及保守行動指引。
- 工程自測：
  - 重新產製 25 篇文章與 5 個系列／分類頁成功。
  - 25／25 篇文章具有一次內容聲明。
  - 31 個正式頁面的 title、description、canonical、OG、Twitter 完整且唯一。
  - 34 個 HTML 的站內連結與資產無缺檔，JSON-LD 全部可解析。
  - 代表性首頁、文章頁、系列頁於 360、390、768、1024、1440 px
    均無水平溢出或破圖。
  - 手機與桌機視覺抽查通過，瀏覽器主控台無 error／warning。
  - `git diff --check` 通過。
- 已知限制：
  - 依使用者決議，部分研究、統計及影劇引文保留原稿且不增加來源清單。
  - 法律資訊僅核對指定的核心行動範圍，不等同個別法律意見。
- 建議回歸重點：逐項重測 BUG-001 至 BUG-004、所有 `TEXT-xxx` 決議、
  法律求助段落、內容聲明、SEO、站內連結、響應式及 Git 納管。
- Git 分支：`warm-illustration-redesign`
- Commit：尚未提交

### DEV-20260613-04：六張核准插畫接入與上線前驗收修正

- 日期：2026-06-13
- 對應需求：REQ-003、REQ-004、REQ-005
- 對應待辦：插畫素材接入、專欄視覺更新、上線前驗收
- 實作狀態：驗收通過
- 需求依據：`illustration-brief.md`、`illustration-assets.md`
- 修改檔案：`articles.html`、`articles.css`、`series.css`、
  `tools/generate_articles.py`、`articles/*.html`、`series/*.html`、
  `assets/illustrations/*`
- 實作內容：
  - 將 ILL-ASSET-001 接入專欄首頁首屏主視覺、首頁社群圖與 JSON-LD image。
  - 將 ILL-ASSET-002 至 ILL-ASSET-006 接入首頁五個系列卡片與五個系列頁首屏。
  - 25 篇文章依所屬系列改用對應 1600x900 PNG 作為 `og:image`、Twitter image 與 JSON-LD image。
  - 可見頁面圖片優先使用 WebP，並提供手機版 `<source>`。
  - 保留心理師 headshot 作為作者照片，未以插畫取代作者識別。
  - 專欄首頁、系列頁與文章頁 CSS 連結加入 `v=20260613-2`，避免上線後套用舊快取。
- 技術決策：
  - 社群分享圖使用 PNG，以提高平台相容性；頁面可見圖片使用 WebP 降低載入量。
  - 插畫與系列對應寫入 `generate_articles.py`，避免逐篇文章手動維護。
  - 首屏圖使用 `fetchpriority="high"`；系列卡片圖使用 `loading="lazy"`。
- 工程自測：
  - 重新產製 25 篇文章與 5 個系列／分類頁成功。
  - 25 篇文章、5 個系列頁與專欄首頁的插畫路徑、社群圖與 JSON-LD 檢查通過。
  - 1440 px 桌機與 390 px 手機瀏覽器抽查通過，無水平溢出或主控台錯誤。
  - 實測發現並修正圖片高度拉伸問題，於插畫 CSS 加入 `height: auto`。
  - 實測發現並修正 CSS 快取風險，加入版本號。
  - `git diff --check` 與 `git diff --cached --check` 通過。
- 獨立驗收：
  - 第一次驗收發現 25 篇文章頁缺少 `article.css` 版本號，列為 P1。
  - 修正後第二次最小回歸 PASS：25 篇文章、專欄首頁與 5 個正規系列頁均使用版本化 CSS；六張插畫接入、社群圖、JSON-LD 與 whitespace 檢查通過。
- 已知限制：
  - `series/addiction-01.html` 為既有相容頁，不列入 5 個正規系列頁驗收範圍；驗收 AI 未發現 stale `series.css` 引用。
  - `assets/illu-adult.png`、`illu-chair.png`、`illu-chair2.png`、`illu-child.png`
    仍為未追蹤檔案，未被本次頁面引用。
- 建議回歸重點：部署後以正式網址檢查社群分享預覽快取與 Search Console 流量基準。
- Git 分支：`warm-illustration-redesign`
- Commit：尚未提交

### DEV-20260613-05：上線圖片比例回報、rollback 與修正分支

- 日期：2026-06-13
- 對應問題：BUG-005
- 對應交接：`current-state-handoff-image-sizing-20260613.md`
- 實作狀態：待獨立驗收
- Git 狀態：
  - `main` 已推送 rollback commit：`25a9df5`
  - 修正分支：`fix/mobile-series-card-image-ratio`
  - 修正分支已推送到 GitHub
- 實作內容：
  - 依使用者要求，先將 GitHub `main` 的上線來源以安全 revert 方式退回上一版。
  - 建立新分支 `fix/mobile-series-card-image-ratio`，基於 rollback 後的 `main`。
  - 在新分支反轉 rollback，重新帶回專欄與插畫功能，避免未來合併受到已 revert commit 影響。
  - 修正 `articles.html#series` 手機版系列卡片圖片比例。
  - 將 `articles.html` 的 CSS 版本號由 `articles.css?v=20260613-2` 升至
    `articles.css?v=20260613-3`。
- 修改檔案：
  - `articles.css`
  - `articles.html`
- 技術決策：
  - 僅在 `max-width: 639px` 手機斷點將 `.series-card-art img` 改為
    `aspect-ratio: 1 / 1`。
  - 桌機版維持 16:9，以符合桌機素材 `1600 × 900` 與既有卡片設計。
  - 不修改插畫素材、不修改系列頁、不修改文章頁社群圖。
- 工程自測：
  - 靜態檢查通過：`articles.html` 使用 `articles.css?v=20260613-3`。
  - 靜態檢查通過：25 篇文章 JSON-LD 可解析。
  - 手機 `390 × 844` 本地瀏覽器測試：
    - `articles.html#series` 系列卡片載入 `*-mobile-900x900.webp`。
    - 已載入卡片 rendered size 由錯誤情境的約 `356 × 200` 修正為
      `356 × 356`。
    - 無水平溢出。
  - 桌機 `1440 × 1000` 本地瀏覽器測試：
    - 系列卡片載入 `1600 × 900` 桌機 WebP。
    - rendered size 維持 16:9。
    - 無水平溢出。
- 建議驗收重點：
  - 驗收 AI 必須讀取 `current-state-handoff-image-sizing-20260613.md`。
  - 驗收不得只檢查檔案存在，必須量測 `currentSrc`、natural size 與 rendered size。
  - 正式重新上線後，需再以 `https://yuchienpsy.com/articles.html#series`
    做上線網址回歸。
- Commit：
  - `9076277` Reapply "Add article pages and approved illustrations"
  - `d889724` Fix mobile series card image ratio
