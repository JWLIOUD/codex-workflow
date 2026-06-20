# Search Console Follow-Up Prompt

現狀分析 AI：接續 yuchienpsy.com 的 Google Search Console SEO 索引任務。

請先確認：

- Search Console 仍登入
- property 為 `sc-domain:yuchienpsy.com` 或 `https://yuchienpsy.com/`
- sitemap 為 `https://yuchienpsy.com/sitemap.xml`

對目標 URL 執行 URL Inspection，記錄：

- URL 是否在 Google 上
- Page indexing 狀態
- 是否由 sitemap 發現
- Last crawl
- Crawled as
- Crawl allowed
- Page fetch
- Indexing allowed
- User-declared canonical
- Google-selected canonical

配額保護規則：

- 若已顯示「已要求建立索引」，不得再次按 Request indexing。
- 若已顯示「網址在 Google 服務中」，不得再次按 Request indexing。
- 若 Page indexing 已顯示「網頁已編入索引」，不得再次按 Request indexing。
- 只有尚未編入索引、尚未要求過、且 Search Console 允許操作時，才可以按 Request indexing。

完成後更新：

`WorkFlow/project/YucheinHomePage/docs/project/search-performance.md`
