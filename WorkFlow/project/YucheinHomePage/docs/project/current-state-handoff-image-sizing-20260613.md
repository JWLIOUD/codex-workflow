# 現狀分析交接：上線後圖片比例問題

- 日期：2026-06-13
- 角色：現狀分析 AI
- 觀察對象：目前上線網站 `https://yuchienpsy.com/`
- 問題來源：使用者回報「目前上線的網站看起來圖片大小設定有問題」
- 目前上線狀態：已先依使用者要求將 GitHub `main` 退回上一個版本。

## 一、線上檢查結論

上線網站當時已載入新版 CSS，問題不是部署延遲，也不是圖片檔案缺失。
真正問題集中在 `articles.html#series` 的手機版系列卡片圖片比例。

### 正常項目

- `articles.html` 首屏主視覺：
  - 桌機載入 `ill-001-articles-hero-1600x900.webp`，顯示約 `564 × 317`。
  - 手機載入 `ill-001-articles-hero-mobile-900x1125.webp`，顯示約 `356 × 445`。
  - 比例符合桌機 16:9、手機 4:5。
- `series/addiction.html` 等系列頁手機版主圖：
  - 載入 `900 × 900` 手機圖。
  - 顯示約 `356 × 356`。
  - 比例符合 1:1，未被壓扁。

### 問題項目

- `articles.html#series` 首頁五個系列卡片：
  - 手機版載入 `900 × 900` 系列圖。
  - CSS 仍以 `aspect-ratio: 16 / 9` 顯示。
  - 實際顯示約 `356 × 200`。
  - 結果：方形手機圖被裁成過扁橫圖，人物與構圖被裁掉太多。

## 二、根因判斷

`articles.css` 中 `.series-card-art img` 對所有尺寸套用 `aspect-ratio: 16 / 9`。
但插畫交接文件中系列圖片的手機版本是 `900 × 900`，設計用途包含手機卡片與系列頁。
因此手機版首頁系列卡片應使用 1:1 或至少 4:3，不應沿用桌機 16:9。

## 三、交接給網頁工程 AI 的修改建議

### 必改

在 `articles.css` 加入手機斷點，讓首頁系列卡片在手機版使用方形比例：

```css
@media (max-width: 639px) {
  .series-card-art img {
    aspect-ratio: 1 / 1;
  }
}
```

### 同步處理

- 因為修改 `articles.css`，`articles.html` 的 CSS 版本號需同步升版，例如：
  `articles.css?v=20260613-3`
- 不需要修改插畫素材本身。
- 不需要修改系列頁，系列頁手機比例已正常。
- 不需要修改文章頁社群圖，社群圖使用 PNG 與本問題無關。

## 四、交接給驗收 AI 的必檢項目

後續上線前不得只驗靜態路徑與 JSON-LD，必須加入「實際 rendered size」檢查。

### 必檢頁面

- `articles.html`
- `articles.html#series`
- `series/addiction.html`
- `series/workplace.html`
- `series/boundary.html`
- `series/self-care.html`
- `series/insights.html`

### 必檢尺寸

- 手機：`390 × 844`
- 桌機：`1440 × 1000`

### 必檢條件

- `articles.html` 首屏主視覺：
  - 手機顯示比例約 4:5。
  - 桌機顯示比例約 16:9。
- `articles.html#series` 系列卡片：
  - 手機版載入 `*-mobile-900x900.webp`。
  - 手機 rendered size 應接近 1:1，不得被顯示成 16:9。
  - 桌機版可維持 16:9。
- 系列頁首屏：
  - 手機版載入 `*-mobile-900x900.webp`。
  - rendered size 應接近 1:1。
- 檢查 `currentSrc`、`naturalWidth/naturalHeight`、`getBoundingClientRect()`。
- 檢查實際上線網址或本地預覽網址，不只檢查原始檔。

## 五、狀態

- `main` 已建立 rollback commit 並推送，避免錯誤比例繼續作為正式上線版本。
- 修正應在功能分支完成並重新驗收後，再合併回 `main`。
