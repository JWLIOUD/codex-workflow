# 心理專欄回歸驗收報告

## 驗收結論

- 測試日期：2026-06-13
- 測試版本／分支：`warm-illustration-redesign`，尚未提交
- 驗收角色：獨立網頁驗收 AI
- 驗收結論：**PASS，可進入提交或部署前確認**
- P0：0
- P1：0
- P2：0
- BUG-001 至 BUG-004：全部關閉
- 插畫接入上線前驗收：PASS
- 2026-06-13 追加現狀回報：上線後發現 `articles.html#series`
  手機版系列卡片圖片比例不合理，原 PASS 結論需補充修正與回歸。

## 問題回歸

| 問題 | 結果 | 驗收證據 |
|---|---|---|
| BUG-001：SEO／JSON-LD 不完整 | PASS | 31 個正式頁面 metadata 完整；文章包含 Article 與 BreadcrumbList，系列頁包含 CollectionPage 與 BreadcrumbList；JSON-LD 可解析。 |
| BUG-002：文案審閱未完成 | PASS | Q01–Q41、F01–F04 已確認；核准替換寫入產製流程；保留項目、舊錯字及佔位符檢查通過。 |
| BUG-003：必要檔案未納入 Git | PASS | 必要 HTML、CSS、圖片與產製工具均已暫存；網站 repo 未納入 `WorkFlow/`。 |
| BUG-004：「最新文章」無排序依據 | PASS | 已改為「延伸閱讀／從這幾篇繼續探索」，不再暗示時間排序。 |

## 內容驗收

- [x] 25 篇文章均存在且作者署名為「黃郁倩 諮商心理師」。
- [x] 25 篇文章各有一次心理健康科普內容聲明。
- [x] 系列名稱改為「自我理解與心理照顧」，並保留「心理師的心靈雞湯」副標。
- [x] 使用者核准的 `TEXT-xxx` 文字修改均已套用。
- [x] 指定保留原文的項目未被一般格式化誤改。
- [x] WHO／ICD-11 職業倦怠敘述已精確化。
- [x] AI 研究段落已改為「部分初步研究指出」的保守表述。
- [x] 報案、保護令、錄音錄影內容改為保守行動指引。
- [x] 113 與「關懷 e 起來」官方入口已保留。
- [x] `[連結]`、編輯註記及未確認的私人求助電話已移除。

## 技術驗收

- [x] 31 個正式頁面的 title、description、canonical、OG 與 Twitter metadata 完整且唯一。
- [x] canonical、OG URL 與結構化資料 URL 一致。
- [x] 34 個 HTML 的站內連結及資產無缺檔。
- [x] JSON-LD 全部可解析。
- [x] 沒有空白 `href`、`src` 或可見 `href="#"` 文章入口。
- [x] 六張核准插畫已接入專欄首頁、五個系列卡片、五個系列頁與文章社群圖。
- [x] 25 篇文章均使用對應系列 PNG 作為 `og:image`、Twitter image 與 JSON-LD image。
- [x] 專欄首頁、文章頁與系列頁 CSS 連結已加入版本號，避免部署後讀取舊快取。
- [x] 工程抽查首頁、文章頁與系列頁於 360、390、768、1024、1440 px 無水平溢出或破圖。
- [x] 工程瀏覽器抽查主控台無 error／warning。
- [x] `git diff --cached --check` 通過。

## 文章來源外連驗收

- 測試日期：2026-06-14
- 驗收範圍：25 篇文章的「原刊來源」外部連結與 Article JSON-LD `isBasedOn` URL。
- 驗收方法：逐篇直接開啟台北市社區心理衛生中心來源 URL，確認 HTTP 狀態為 200，且官方頁面 title 或正文含對應文章關鍵字。
- 驗收結果：PASS，25 篇全部通過。
- 修正紀錄：原先 16 篇由分類頁初步比對取得的 URL 實測皆為 404；已依「文章名稱 + 心理衛生中心」搜尋法與心衛中心分類頁 title 比對修正。
- 後續必檢：新增或修改來源 URL 時，不得只檢查本站 HTML 是否存在連結；必須實際驗證外部 URL 可開啟且內容對應文章。

## 插畫驗收回歸

| 項目 | 結果 | 驗收證據 |
|---|---|---|
| ILL-001 專欄首頁主視覺 | PASS | `articles.html` 首屏有桌機 WebP、手機 WebP、alt；社群與 JSON-LD image 使用 PNG。 |
| ILL-002 至 ILL-006 系列圖 | PASS | 五個系列卡片與五個正規系列頁皆有對應 `<picture>`、手機 source 與 alt。 |
| 文章社群圖 | PASS | 25 篇文章依系列對應 PNG；JSON-LD 全部可解析。 |
| 圖片版面 | PASS | 圖片 CSS 已加入 `height: auto`，修正原始尺寸造成的高度拉伸風險。 |
| CSS 快取 | PASS | 首頁、文章頁與系列頁皆使用 `?v=20260613-2` 版本化 CSS；第二次獨立回歸通過。 |

## 上線後追加問題

| 問題 | 嚴重度 | 狀態 | 驗收證據 |
|---|---|---|---|
| BUG-005：首頁系列卡片手機版圖片比例過扁 | P1 | PASS | 2026-06-21 修正 `articles.css`。Chrome headless 手機逐張滾動檢查五張系列卡片皆載入 `*-mobile-900x900.webp`，natural size 皆為 `900 × 900`，rendered size 皆為 1:1；桌機維持 16:9；五個系列頁手機首屏仍為 1:1。 |

### BUG-005 回歸必檢

- [x] `articles.html#series` 於手機 viewport，五張系列卡片 rendered size 接近 1:1。
- [x] `articles.html#series` 手機版 `currentSrc` 使用 `*-mobile-900x900.webp`。
- [x] `articles.html#series` 桌機版仍可維持 16:9，且無水平溢出。
- [x] 五個系列頁手機首屏仍維持 1:1。
- [x] 檢查正式網址，不得只做靜態檔案檢查。2026-06-21 已以 Chrome headless 驗證 `https://yuchienpsy.com/articles.html#series`：五張系列卡片皆為 1:1，皆載入 `*-mobile-900x900.webp`，無水平溢出。

## 殘餘風險

- 本次獨立驗收沒有重新執行長時間、全頁面的五尺寸瀏覽器巡覽；響應式及主控台結果採用本輪工程 AI 的瀏覽器測試證據。
- `assets/illu-adult.png`、`illu-chair.png`、`illu-chair2.png`、`illu-child.png`
  尚未追蹤，但目前沒有被網站引用，不影響本次專欄上線。
- 法律內容只完成使用者指定的核心範圍保守化處理，不等同完整法律審稿或個別法律意見。
- 依使用者決議，部分研究、統計與影劇引文保留原稿且不增加來源清單。

## 上線前狀態

- 驗收狀態：上線後發現 BUG-005，已退回 `main` 前一版，待修正後重新驗收
- Commit：尚未建立
- Push／部署：尚未執行
- 下一階段：確認 Git 提交範圍後 commit、push，再建立 release log 與 Search Console 追蹤基準。
