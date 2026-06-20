# Google Search Console 流量影響分析

此文件記錄網站更新前後的 Google 自然搜尋表現。資料來源為 `sc-domain:yuchienpsy.com` 的 Google Search Console。

## 存取設定

- Search Console 資源：`sc-domain:yuchienpsy.com`
- 權限原則：唯讀分析，不變更網站資源、使用者或設定
- 存取方式：Codex 瀏覽器中的使用者登入工作階段
- 登入狀態：已登入並確認可讀取
- 最後確認日期：2026-06-13

## 分析原則

- 先從 `project/release-log.md` 取得實際上線日期與影響頁面。
- 主要比較相同長度的更新前後期間，並盡量對齊星期分布。
- 更新後資料尚未完整時，標示為「觀察中」，不急於下結論。
- 同時檢查點擊、曝光、CTR、平均排名，不只看單一指標。
- 分開分析整站、受影響頁面及相關搜尋字詞。
- 品牌字與非品牌字應盡可能分開觀察。
- 若期間內有其他更新、季節性、媒體曝光或索引變化，必須註記。
- 流量變化只代表關聯；沒有足夠證據時，不宣稱由單一更新直接造成。

## 固定觀察節點

| 節點 | 建議期間 | 用途 |
|---|---|---|
| 更新前基準 | 上線前 28 天 | 建立原始表現 |
| 初步觀察 | 上線後 7 天 | 發現明顯異常，不做最終判斷 |
| 第一階段 | 上線後 28 天 | 與更新前 28 天比較 |
| 第二階段 | 上線後 56 天 | 確認趨勢是否延續 |
| 長期追蹤 | 上線後 90 天 | 評估較慢的搜尋與索引影響 |

## 分析紀錄範本

### IMPACT-YYYYMMDD-01：REL-YYYYMMDD-01 更新影響

- 分析日期：
- 對應更新：REL-YYYYMMDD-01
- Search Console 資料截止日：
- 分析狀態：基準完成／觀察中／可初步判讀／長期完成
- 更新前期間：
- 更新後期間：
- 比較方式：前後期間／去年同期／自訂控制組
- 影響頁面：
- 相關查詢：
- 品牌字定義：
- 資料限制：

#### 整體指標

| 指標 | 更新前 | 更新後 | 差異 | 變化率 |
|---|---:|---:|---:|---:|
| 點擊 |  |  |  |  |
| 曝光 |  |  |  |  |
| CTR |  |  |  |  |
| 平均排名 |  |  |  |  |

#### 受影響頁面

| 頁面 | 點擊變化 | 曝光變化 | CTR 變化 | 排名變化 | 判讀 |
|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |

#### 相關查詢

| 查詢 | 頁面 | 點擊變化 | 曝光變化 | CTR 變化 | 排名變化 |
|---|---|---:|---:|---:|---:|
|  |  |  |  |  |  |

#### 發現

- 

#### 可能干擾因素

- 

#### 結論信心

- 信心：低／中／高
- 判讀：
- 證據：
- 尚不能確認的事項：

#### 後續行動

- [ ] 

---

## BASELINE-20260613-01：首次搜尋流量基準

- 分析日期：2026-06-13
- Search Console 資料截止日：2026-06-11
- 分析期間：Search Console「最近 3 個月」，目前可見約 2026-04-23 至 2026-06-11
- 分析狀態：基準完成
- 對應更新：尚未建立 release log

### 整站指標

| 指標 | 數值 |
|---|---:|
| 點擊 | 51 |
| 曝光 | 270 |
| CTR | 18.9% |
| 平均排名 | 2.4 |

### 頁面

| 頁面 | 點擊 | 曝光 |
|---|---:|---:|
| `https://yuchienpsy.com/` | 47 | 250 |
| `https://yuchienpsy.com/talks.html` | 4 | 68 |

### 可見查詢

| 查詢 | 點擊 | 曝光 |
|---|---:|---:|
| 黃郁倩 心理師 | 14 | 61 |
| 黃郁倩 | 11 | 79 |
| 黃郁倩心理師 | 11 | 31 |

### 基準判讀

- 可見查詢全部是姓名品牌字。
- 目前數據能證明已知姓名使用者容易找到網站，尚不能證明網站能吸引非品牌的新個案或合作窗口。
- 首頁承接大部分點擊；講座頁已有少量搜尋進站，但尚無可見的非品牌合作需求字詞。
- 後續更新應依 `REL-xxx` 對照受影響頁面，於上線後 7、28、56 與 90 天追蹤。

---

## BASELINE-20260614-01：專欄頁上線與 sitemap 提交後基準

- 分析日期：2026-06-14 02:48 CST
- Search Console 資源：`sc-domain:yuchienpsy.com`
- Search Console 成效資料期間：最近 3 個月
- Search Console 成效上次更新：3.5 小時前
- Search Console 索引資料上次更新：2026-06-05
- 對應網站版本：`c5ce18d Add sitemap for search console`
- sitemap：`https://yuchienpsy.com/sitemap.xml`
- sitemap 狀態：成功
- sitemap 已送出：2026年6月14日
- sitemap 上次讀取：2026年6月14日
- sitemap 系統探索到的網頁：33
- 分析狀態：新版網站流量基準完成，索引影響觀察中

### 當下網站現狀

| 項目 | 狀態 |
|---|---|
| 網站定位 | 心理師個人首頁，承接潛在個案、家長、伴侶、合作單位與講座行政窗口 |
| 主要入口 | 首頁、講座頁、心理專欄首頁 |
| 專欄架構 | 5 個主題系列頁：成癮與依賴、職場壓力與自我照顧、界線與心理安全、自我理解與照顧、生活與關係心理 |
| 已建立文章頁 | 25 篇正式文章頁 |
| sitemap 收錄 URL | 33 筆 |
| `robots.txt` | 已指向 sitemap |
| 目前 Search Console 可見流量頁 | 首頁、講座頁 |
| 新文章頁搜尋狀態 | sitemap 已提交，但成效與索引報表尚未反映新頁面 |

### Search Console 整站成效

| 指標 | 數值 |
|---|---:|
| 點擊 | 51 |
| 曝光 | 270 |
| CTR | 18.9% |
| 平均排名 | 2.4 |

### 可見查詢

| 查詢 | 點擊 | 曝光 | CTR | 平均排名 | 判讀 |
|---|---:|---:|---:|---:|---|
| 黃郁倩 心理師 | 14 | 61 | 23% | 1.5 | 品牌姓名字，已能有效承接明確搜尋 |
| 黃郁倩 | 11 | 79 | 13.9% | 2.1 | 品牌姓名字，曝光最高但 CTR 可觀察 |
| 黃郁倩心理師 | 11 | 31 | 35.5% | 1.5 | 品牌姓名字，意圖明確且 CTR 佳 |

### 可見頁面

| 頁面 | 點擊 | 曝光 | CTR | 平均排名 | 判讀 |
|---|---:|---:|---:|---:|---|
| `https://yuchienpsy.com/` | 47 | 250 | 18.8% | 2.4 | 目前主要自然搜尋入口 |
| `https://yuchienpsy.com/talks.html` | 4 | 68 | 5.9% | 8.3 | 已有合作／講座相關承接面，但點擊仍少 |

### 索引狀態

| 指標 | 數值 | 備註 |
|---|---:|---|
| 已建立索引 | 2 | 資料上次更新 2026-06-05，尚未反映 2026-06-14 sitemap |
| 未建立索引 | 6 | 舊資料，需等下次更新後再判斷 |
| 重複網頁，未選取標準網頁 | 4 | 暫列觀察，不直接視為新版問題 |
| 頁面會重新導向 | 2 | 暫列觀察，不直接視為新版問題 |
| 已檢索，目前尚未建立索引 | 0 | 目前未看到新文章頁卡在此狀態 |

### 現況判讀

- 目前自然搜尋幾乎完全由品牌字支撐，代表「已經知道黃郁倩心理師的人」可以找到網站。
- 新增的 25 篇文章頁與 5 個系列頁已經透過 sitemap 交給 Google，但尚未在成效報表中出現，短期內不應用流量零成長判定內容失敗。
- 下一階段的核心觀察不是總點擊是否立刻上升，而是非品牌查詢是否開始出現，例如成癮、短影音、咖啡因依賴、職場壓力、界線、性騷擾、自我照顧、關係控制等主題。
- 首頁目前承接能力穩定；講座頁有曝光但 CTR 偏低，若後續合作單位導流仍不足，可再回頭檢查標題、描述與講座頁首屏訊息是否更像行政窗口需要的答案。
- 目前最重要的每週追蹤指標是：新頁被索引數、新頁曝光數、非品牌查詢數、專欄首頁與系列頁是否開始取得曝光。

### 下週追蹤重點

- [ ] 檢查 sitemap 狀態是否仍為成功，探索網頁是否維持 33 或增加。
- [ ] 檢查索引報表是否開始反映 2026-06-14 新提交頁面。
- [ ] 檢查 `articles.html` 與 5 個系列頁是否出現在成效頁面表。
- [ ] 檢查是否出現非品牌查詢。
- [ ] 將品牌字與非品牌字分開統計。
- [ ] 若新文章頁曝光增加但 CTR 低，交給需求分析 AI 討論標題與 meta description 調整。
- [ ] 若新文章頁長期未索引，交給網頁工程師 AI 檢查 canonical、內部連結、sitemap 與頁面品質訊號。

### 每週自動追蹤設定

- Codex 自動化：已建立
- 自動化 ID：`automation`
- 執行型態：附在目前專案對話的每週追蹤
- 預期任務：每週讀取 Search Console、網站專案與本文件，追加最新流量分析與交接事項。
- 注意：若自動化執行時 Search Console 登入失效，需重新登入後再補跑該週紀錄。

## 每週流量分析紀錄範本

---

## IMPACT-20260614-02：文章來源連結與網站名稱 SEO 補強 Day 0

- 分析日期：2026-06-14
- 對應更新：`REL-20260614-02`
- 對應 commit：`06784d5 Add article source links and site metadata`
- Search Console 資料截止日：沿用 `BASELINE-20260614-01`，尚未取得此 commit 上線後的新成效資料
- 分析狀態：Day 0 現狀紀錄，觀察中
- 更新前期間：`BASELINE-20260614-01`
- 更新後期間：尚未累積
- 比較方式：待上線後 7 天與 28 天再進行前後比較
- 影響頁面：首頁、心理專欄首頁、25 篇文章頁、5 個系列頁
- 相關查詢：品牌字與文章主題非品牌字
- 資料限制：Search Console 成效資料不會即時反映當日更新；本紀錄不判定流量成敗

### 當日已確認的網站狀態

| 項目 | 數值／狀態 |
|---|---:|
| sitemap URL 數 | 33 |
| 文章來源卡片 | 25 |
| Article `isBasedOn` | 25 |
| `og:site_name` | 32 |
| 最新上線 commit | `06784d5` |

### Day 0 判讀

- 本次更新主要補強文章可信度、來源透明度與網站名稱 SEO 訊號。
- 短期內不應期待 Search Console 點擊立即上升。
- 後續應觀察新文章頁是否被索引、是否開始取得曝光，以及非品牌查詢是否出現。
- Google site name 是否從 `yuchienpsy.com` 改為「黃郁倩 諮商心理師」需等待重新抓取與搜尋結果重算。

### 後續行動

- [ ] 上線後 7 天檢查專欄首頁、系列頁與文章頁是否出現在成效報表。
- [ ] 上線後 7 天檢查是否出現非品牌查詢。
- [ ] 上線後 28 天分開比較品牌字與非品牌字。
- [ ] 若文章頁長期未索引，交給網頁工程師 AI 檢查 sitemap、canonical、內部連結與頁面品質訊號。
- [ ] 若曝光增加但 CTR 低，交給需求分析 AI 檢討標題與 meta description。

### Search Console 操作紀錄

- 2026-06-14 22:54：已對 `https://yuchienpsy.com/` 執行「要求建立索引」。
  - 當下狀態：網址在 Google 服務中，網頁已編入索引。
  - 結果：已將網址加入優先檢索佇列。
- 2026-06-14 22:54：已對 `https://yuchienpsy.com/talks.html` 執行「測試線上網址」。
  - Google 索引既有狀態：舊資料仍顯示已編入索引。
  - 即時測試結果：Google 無法為網址建立索引。
  - 原因：在 `robots` 中繼標記中偵測到 `noindex`。
  - 使用者宣告的標準網址：`https://yuchienpsy.com/`
  - 判讀：最新版線上頁已正確要求 `talks.html` 從搜尋結果退場；不應對此頁按「要求建立索引」。

### Search Console 操作紀錄：2026-06-20 sitemap 與代表文章索引檢查

- 執行者：現狀分析 AI
- 執行日期：2026-06-20
- 目標：確認 GitHub Pages 靜態網站可被 Google 發現、抓取與索引，並先處理入口頁與代表文章頁。

#### 終端機可抓取性檢查

| 檢查項目 | 結果 | 判讀 |
|---|---|---|
| `curl -I https://yuchienpsy.com/` | `HTTP/2 200` | 首頁可抓取 |
| `curl -I https://yuchienpsy.com/sitemap.xml` | `HTTP/2 200` | sitemap 可抓取 |
| `curl -I https://yuchienpsy.com/articles/addiction-01.html` | `HTTP/2 200` | 代表文章可抓取 |
| `curl https://yuchienpsy.com/robots.txt` | `User-agent: *` / `Allow: /` / `Sitemap: https://yuchienpsy.com/sitemap.xml` | 未阻擋 Google 抓取 |
| `curl -s https://yuchienpsy.com/sitemap.xml \| grep -c "<loc>"` | `32` | sitemap 目前列出 32 個 URL |

#### Sitemap 提交結果

| 項目 | Search Console 顯示 |
|---|---|
| property | `sc-domain:yuchienpsy.com` |
| sitemap | `https://yuchienpsy.com/sitemap.xml` |
| 提交結果 | 已成功提交 Sitemap |
| 已送出日期 | 2026年6月20日 |
| 上次讀取時間 | 2026年6月18日 |
| 狀態 | 成功 |
| 系統探索到的網頁 | 32 |
| 系統探索到的影片 | 0 |

#### 代表文章 URL Inspection：`https://yuchienpsy.com/articles/addiction-01.html`

| 欄位 | Search Console 顯示 |
|---|---|
| URL 是否在 Google 上 | 網址在 Google 服務中 |
| Page indexing 狀態 | 網頁已編入索引 |
| Referring sitemap | `https://yuchienpsy.com/sitemap.xml` |
| 參照網頁 | 未偵測到任何參照網頁 |
| Last crawl | 2026年6月20日 凌晨12:51:15 |
| Crawled as | Googlebot 智慧型手機 |
| Crawl allowed? | 是 |
| Page fetch | 成功 |
| Indexing allowed? | 是 |
| User-declared canonical | 不適用 |
| Google-selected canonical | 受檢測網址 |
| Live test | Google 可為網址建立索引 |
| Request indexing | 已要求建立索引，已加入優先檢索佇列 |

#### 本次已處理的入口頁與代表頁

| URL | Search Console 狀態 | 本次動作 |
|---|---|---|
| `https://yuchienpsy.com/` | 網址在 Google 服務中，網頁已編入索引 | 已要求建立索引 |
| `https://yuchienpsy.com/articles.html` | 網址在 Google 服務中，網頁已編入索引 | 已檢查 |
| `https://yuchienpsy.com/articles/addiction-01.html` | 網址在 Google 服務中，網頁已編入索引 | 已測試線上網址，已要求建立索引 |
| `https://yuchienpsy.com/articles/boundary-01.html` | 網址不在 Google 服務中；已找到，目前尚未建立索引 | 已要求建立索引 |
| `https://yuchienpsy.com/articles/self-care-07.html` | 網址不在 Google 服務中；已找到，目前尚未建立索引 | 要求建立索引時遇到 Search Console 配額限制 |
| `https://yuchienpsy.com/articles/love-and-imperfection.html` | 網址不在 Google 服務中；網頁未編入索引 | 已檢查；因配額限制未再要求索引 |

> 批次處理曾依序推進到 `boundary-01.html`，但工具等待逾時未保留完整逐項輸出。後續請優先複核 5 個系列頁、`workplace-01.html` 與 `self-care-07.html` 是否已顯示「已要求建立索引」。

#### 判讀

- 網站本身沒有 HTTP、robots 或 sitemap 層級的阻擋問題。
- Google 已能讀到 sitemap，且 sitemap 顯示成功、探索 32 個 URL。
- 代表文章 `addiction-01.html` 已被索引，表示文章模板、HTTPS、導覽標記與基本索引訊號可正常運作。
- 尚未索引的文章目前主要是「已找到 - 目前尚未建立索引」或尚未完整發現，不是抓取失敗。
- Search Console 出現要求建立索引配額限制，接下來應分批補做，不需要一次提交 25 篇。

#### 下一步建議

- [ ] 24-48 小時後複核 `self-care-07.html` 與 `love-and-imperfection.html`，配額恢復後再要求建立索引。
- [ ] 複核 5 個系列頁：`addiction.html`、`workplace.html`、`boundary.html`、`self-care.html`、`insights.html`。
- [ ] 複核 `workplace-01.html` 是否已要求建立索引。
- [ ] 若文章頁持續「已找到 - 目前尚未建立索引」超過 2-4 週，交由需求分析 AI 檢查文章標題、摘要、頁內獨特性與內部連結錨文字。
- [ ] 網頁工程師 AI 可加強文章首頁與系列頁對代表文章的內部連結權重，例如首頁或專欄首頁放置「最新／精選文章」區塊。

### Search Console 自動化追蹤：2026-06-20 10:07 配額恢復檢查

- 執行者：現狀分析 AI
- 執行時間：2026-06-20 10:07（Asia/Taipei）
- 自動化 ID：`automation`
- 目的：確認「要求建立索引」配額是否恢復，並接續處理尚未要求索引的入口頁與代表文章。

#### 登入與 property 狀態

| 項目 | 結果 |
|---|---|
| Search Console 登入 | 正常 |
| property | `sc-domain:yuchienpsy.com` |
| Search Console 概述顯示點擊 | 網頁搜尋總點擊次數：60 次 |
| Search Console 概述顯示索引 | 2 個已編入索引的網頁；6 個沒有編入索引的網頁 |

#### 本次抽查 URL：`https://yuchienpsy.com/articles/self-care-07.html`

| 欄位 | Search Console 顯示 |
|---|---|
| URL 是否在 Google 上 | 網址不在 Google 服務中 |
| Page indexing 狀態 | 網頁未編入索引：已找到 - 目前尚未建立索引 |
| Referring sitemap | `https://yuchienpsy.com/sitemap.xml` |
| 參照網頁 | 未偵測到任何參照網頁 |
| Last crawl | 不適用 |
| Crawled as | 不適用 |
| Crawl allowed? | 不適用 |
| Page fetch | 不適用 |
| Indexing allowed? | 不適用 |
| User-declared canonical | 不適用 |
| Google-selected canonical | 不適用 |
| Request indexing | 失敗：超過配額 |

#### 配額狀態

- Search Console 顯示「超過配額」。
- 錯誤訊息：提交的網址數量已超過單日配額，系統無法處理要求，請明天再嘗試提交。
- 判讀：配額尚未恢復；這不是網站端錯誤，也不是 robots、HTTP、sitemap 或 canonical 問題。

#### 後續處理

- [ ] 保留暫時自動化，下一次再檢查配額是否恢復。
- [ ] 配額恢復後，優先對 `self-care-07.html` 重新要求建立索引。
- [ ] 接著處理 `love-and-imperfection.html`、5 個系列頁與 `workplace-01.html`。
- [ ] 全部目標 URL 處理完成後，將自動化恢復為原本每週一的網站現狀流量分析。

### WEEKLY-YYYYMMDD-01：每週網站現狀與自然搜尋分析

- 分析日期：
- Search Console 資料截止日：
- 比較基準：
- 網站版本／最新提交：
- 本週是否有上線更新：
- 資料限制：

#### 整站成效

| 指標 | 本週 | 上週／基準 | 差異 | 判讀 |
|---|---:|---:|---:|---|
| 點擊 |  |  |  |  |
| 曝光 |  |  |  |  |
| CTR |  |  |  |  |
| 平均排名 |  |  |  |  |

#### 查詢變化

| 查詢 | 類型 | 點擊 | 曝光 | CTR | 平均排名 | 判讀 |
|---|---|---:|---:|---:|---:|---|
|  | 品牌／非品牌／合作需求 |  |  |  |  |  |

#### 頁面變化

| 頁面 | 點擊 | 曝光 | CTR | 平均排名 | 判讀 |
|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |

#### 索引與 sitemap

| 項目 | 狀態 | 判讀 |
|---|---|---|
| sitemap |  |  |
| 已建立索引頁面 |  |  |
| 未建立索引頁面 |  |  |
| 新文章頁索引狀態 |  |  |

#### 對內容方向的建議

- 

#### 交接事項

- [ ] 需求分析 AI：
- [ ] 網頁工程師 AI：
- [ ] 驗收工程師 AI：

## 異常判斷

出現下列情況時，應先交由現況分析或測試角色檢查，不直接視為內容策略失敗：

- 重要頁面曝光或點擊突然接近零。
- 頁面網址變更後，舊網址仍持續取得曝光。
- 曝光增加但 CTR 明顯下降。
- 平均排名變好但點擊下降。
- 只有品牌字成長，非品牌字沒有改善。
- 單一裝置、國家或頁面出現異常差異。
- Search Console 顯示的頁面與實際 canonical 不一致。
