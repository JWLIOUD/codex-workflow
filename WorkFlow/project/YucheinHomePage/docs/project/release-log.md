# 網站更新紀錄

此文件記錄每次網站更新的時間、需求與影響頁面，供 Search Console 流量影響分析使用。

## 更新紀錄範本

### REL-YYYYMMDD-01：更新名稱

- 上線日期與時間：
- Git 分支：
- Commit：
- 對應需求：REQ-xxx
- 對應待辦：TASK-xxx
- 變更類型：內容／SEO／版面／導覽／功能／效能／其他
- 影響頁面：
- 影響查詢主題：
- 修改前目的：
- 實際修改內容：
- 預期流量影響：
- 是否可能影響索引：是／否／待確認
- 是否已確認正式網站上線：是／否
- 備註：

## 更新原則

- 每次正式網站更新都建立唯一 `REL-xxx` 編號。
- 多個需求同時上線時，可共用一筆版本紀錄，但須列出所有需求。
- 必須記錄實際上線時間，不能只記錄程式完成時間。
- 影響頁面應使用 Search Console 中可對應的完整網址。
- 若同一觀察期間有其他重大更新，應另外記錄，避免錯誤歸因。

## 更新紀錄

### REL-20260614-02：文章來源連結與網站名稱 SEO 補強

- 上線日期與時間：2026-06-14 13:44 +08:00
- Git 分支：`main`
- Commit：`06784d5 Add article source links and site metadata`
- 對應需求：文章原刊來源揭露、Google 搜尋結果網站名稱改善
- 對應待辦：`QA-CHECK-001`
- 變更類型：內容／SEO／結構化資料
- 影響頁面：
  - `https://yuchienpsy.com/`
  - `https://yuchienpsy.com/articles.html`
  - `https://yuchienpsy.com/articles/*.html`
  - `https://yuchienpsy.com/series/*.html`
- 影響查詢主題：
  - 品牌字：黃郁倩、黃郁倩心理師、黃郁倩 諮商心理師
  - 非品牌主題：成癮、短影音、咖啡因依賴、職場 PUA、職業倦怠、同情疲勞、性騷擾、關係控制、自我照顧
- 修改前目的：
  - 文章頁缺少台北市社區心理衛生中心原刊來源連結。
  - Google 搜尋結果可能顯示 `yuchienpsy.com`，而非期待的網站名稱「黃郁倩 諮商心理師」。
- 實際修改內容：
  - 25 篇文章頁新增原刊來源卡片。
  - 25 篇文章 Article JSON-LD 新增 `isBasedOn`。
  - 首頁新增 `WebSite` JSON-LD。
  - 首頁、專欄首頁、文章頁與系列頁補上 `og:site_name`。
- 預期流量影響：
  - 短期主要提升可信度與搜尋語意清楚度，不預期當日流量立即上升。
  - 中長期觀察非品牌主題查詢是否開始帶來曝光。
- 是否可能影響索引：是
- 是否已確認正式網站上線：是，已 push 至 `origin/main`
- 備註：
  - 來源 URL 驗證方法與更正方式已寫入 `requirements-source-links-and-serp-title-20260614.md`。
  - Day 0 分析報告：`post-launch-day0-analysis-20260614.md`
