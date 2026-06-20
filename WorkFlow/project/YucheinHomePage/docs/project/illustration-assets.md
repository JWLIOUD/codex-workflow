# 插畫素材與工程交接

本文件由插畫家 AI 維護。只有狀態為「可供工程使用」的素材，網頁工程
AI 才能接入正式頁面。

## 路徑規則

- 網站專案：
  `/Users/liuzhewei/Documents/Codex/therapist-profile`
- 正式素材資料夾：
  `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/`
- 網站根目錄頁面的相對路徑：
  `assets/illustrations/{檔名}`
- `/articles/`、`/series/` 頁面的相對路徑：
  `../assets/illustrations/{檔名}`

## 素材狀態

- 可供工程使用：6
- 待視覺確認：0
- 退回修改：0
- 下一個編號：`ILL-ASSET-007`

## 產製批次

- 批次：`ILL-BATCH-20260613-01`
- 產製日期：2026-06-13
- 產製方式：Codex 內建 ImageGen 產生 PNG，並以 Pillow 輸出桌機與手機裁切版本及 WebP。
- 視覺方向：溫暖手繪水彩、細棕色線條、米白紙張質感、鼠尾草綠、暖棕與低飽和粉橘。
- 品質檢查：已檢查無文字、Logo、浮水印、明顯手部錯誤；已建立桌機與手機預覽裁切。
- 建議工程使用：優先使用 WebP；PNG 保留作為原始備援。

## 可供工程使用

以下六張素材已於 2026-06-13 經使用者確認，可接入正式頁面。

### ILL-ASSET-001：心理專欄首頁主視覺

- 對應圖片需求：ILL-REQ-001
- 對應正式需求：REQ-004、REQ-005
- 狀態：可供工程使用
- 用途：專欄首頁主視覺、專欄首頁社群分享圖
- 目標頁面／區塊：`articles.html` 首屏
- 實體檔案：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-001-articles-hero-1600x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-001-articles-hero-mobile-900x1125.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-001-articles-hero-1600x900.png`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-001-articles-hero-mobile-900x1125.png`
- 網頁相對路徑：
  - 根目錄：`assets/illustrations/ill-001-articles-hero-1600x900.webp`
  - 手機：`assets/illustrations/ill-001-articles-hero-mobile-900x1125.webp`
- 桌機尺寸：1600 × 900
- 手機尺寸：900 × 1125
- 檔案格式與大小：
  - WebP 桌機：153 KB
  - WebP 手機：129 KB
- 建議 `alt`：一位讀者坐在溫暖的閱讀角落中閱讀，周圍有植物、書頁與象徵心理主題的柔和線條。
- 純裝飾圖片：否
- 建議 `object-fit`／焦點：`object-fit: cover; object-position: 70% center;`
- 生成或編修方式：ImageGen 生成，Pillow 裁切與 WebP 壓縮。
- 使用的參考素材：現有網站手繪插畫風格、`illu-chair.png` 色彩與線條。
- 已知限制：作為首屏使用時，左側留白適合放標題；若放滿版背景需加淡色遮罩。
- 工程注意事項：使用 `<picture>` 提供桌機與手機版本；避免裁切右側人物臉部。
- 完成日期：2026-06-13

### ILL-ASSET-002：「癮」未條系列圖

- 對應圖片需求：ILL-REQ-002
- 對應正式需求：REQ-003、REQ-005
- 狀態：可供工程使用
- 用途：系列頁主視覺、首頁系列卡片、成癮系列文章 OG 分享圖
- 目標頁面／區塊：`series/addiction.html`、`articles.html` 成癮系列卡片、`articles/addiction-*.html`
- 實體檔案：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-002-addiction-series-1600x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-002-addiction-series-mobile-900x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-002-addiction-series-1600x900.png`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-002-addiction-series-mobile-900x900.png`
- 網頁相對路徑：
  - 根目錄：`assets/illustrations/ill-002-addiction-series-1600x900.webp`
  - 文章／系列頁：`../assets/illustrations/ill-002-addiction-series-1600x900.webp`
  - 手機／卡片：`../assets/illustrations/ill-002-addiction-series-mobile-900x900.webp`
- 桌機尺寸：1600 × 900
- 手機尺寸：900 × 900
- 檔案格式與大小：
  - WebP 桌機：187 KB
  - WebP 手機：112 KB
- 建議 `alt`：一位成人坐在沙發上看向窗外，手中手機旁有柔和循環線條，象徵停不下來的習慣與重新選擇。
- 純裝飾圖片：否
- 建議 `object-fit`／焦點：`object-fit: cover; object-position: 68% center;`
- 生成或編修方式：ImageGen 生成，Pillow 裁切與 WebP 壓縮。
- 使用的參考素材：現有網站手繪插畫風格。
- 已知限制：手機畫面偏重人物與手機，左側留白較少。
- 工程注意事項：成癮系列 OG 圖可共用此桌機版 WebP。
- 完成日期：2026-06-13

### ILL-ASSET-003：「咖啡哪有工作苦」系列圖

- 對應圖片需求：ILL-REQ-003
- 對應正式需求：REQ-003、REQ-005
- 狀態：可供工程使用
- 用途：系列頁主視覺、首頁系列卡片、職場系列文章 OG 分享圖
- 目標頁面／區塊：`series/workplace.html`、`articles.html` 職場系列卡片、`articles/workplace-*.html`
- 實體檔案：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-003-workplace-series-1600x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-003-workplace-series-mobile-900x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-003-workplace-series-1600x900.png`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-003-workplace-series-mobile-900x900.png`
- 網頁相對路徑：
  - 根目錄：`assets/illustrations/ill-003-workplace-series-1600x900.webp`
  - 文章／系列頁：`../assets/illustrations/ill-003-workplace-series-1600x900.webp`
  - 手機／卡片：`../assets/illustrations/ill-003-workplace-series-mobile-900x900.webp`
- 桌機尺寸：1600 × 900
- 手機尺寸：900 × 900
- 檔案格式與大小：
  - WebP 桌機：130 KB
  - WebP 手機：90 KB
- 建議 `alt`：一位上班族坐在工作桌前伸展肩膀，桌上有筆電、咖啡與待辦紙張，窗邊植物帶來休息感。
- 純裝飾圖片：否
- 建議 `object-fit`／焦點：`object-fit: cover; object-position: 68% center;`
- 生成或編修方式：ImageGen 生成，Pillow 裁切與 WebP 壓縮。
- 使用的參考素材：現有網站手繪插畫風格。
- 已知限制：桌面紙張有抽象格線，但沒有可讀文字。
- 工程注意事項：可作為職場系列共用 OG 圖。
- 完成日期：2026-06-13

### ILL-ASSET-004：「性騷擾是什麼？」系列圖

- 對應圖片需求：ILL-REQ-004
- 對應正式需求：REQ-003、REQ-005
- 狀態：可供工程使用
- 用途：系列頁主視覺、首頁系列卡片、界線系列文章 OG 分享圖
- 目標頁面／區塊：`series/boundary.html`、`articles.html` 界線系列卡片、`articles/boundary-*.html`
- 實體檔案：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-004-boundary-series-1600x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-004-boundary-series-mobile-900x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-004-boundary-series-1600x900.png`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-004-boundary-series-mobile-900x900.png`
- 網頁相對路徑：
  - 根目錄：`assets/illustrations/ill-004-boundary-series-1600x900.webp`
  - 文章／系列頁：`../assets/illustrations/ill-004-boundary-series-1600x900.webp`
  - 手機／卡片：`../assets/illustrations/ill-004-boundary-series-mobile-900x900.webp`
- 桌機尺寸：1600 × 900
- 手機尺寸：900 × 900
- 檔案格式與大小：
  - WebP 桌機：106 KB
  - WebP 手機：66 KB
- 建議 `alt`：一位成人以溫和但清楚的手勢表達界線，周圍有柔和光線與支持者的身影。
- 純裝飾圖片：否
- 建議 `object-fit`／焦點：`object-fit: cover; object-position: 72% center;`
- 生成或編修方式：ImageGen 生成，Pillow 裁切與 WebP 壓縮。
- 使用的參考素材：現有網站手繪插畫風格。
- 已知限制：畫面有第三位支持者，適合傳達安全與陪伴；未描繪侵害情節。
- 工程注意事項：敏感議題頁面使用此圖時，不要搭配過度刺激的動畫或對比。
- 完成日期：2026-06-13

### ILL-ASSET-005：「自我理解與心理照顧」系列圖

- 對應圖片需求：ILL-REQ-005
- 對應正式需求：REQ-003、REQ-005
- 狀態：可供工程使用
- 用途：系列頁主視覺、首頁系列卡片、自我照顧文章 OG 分享圖
- 目標頁面／區塊：`series/self-care.html`、`articles.html` 自我理解系列卡片、`articles/self-care-*.html`
- 實體檔案：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-005-self-care-series-1600x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-005-self-care-series-mobile-900x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-005-self-care-series-1600x900.png`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-005-self-care-series-mobile-900x900.png`
- 網頁相對路徑：
  - 根目錄：`assets/illustrations/ill-005-self-care-series-1600x900.webp`
  - 文章／系列頁：`../assets/illustrations/ill-005-self-care-series-1600x900.webp`
  - 手機／卡片：`../assets/illustrations/ill-005-self-care-series-mobile-900x900.webp`
- 桌機尺寸：1600 × 900
- 手機尺寸：900 × 900
- 檔案格式與大小：
  - WebP 桌機：139 KB
  - WebP 手機：94 KB
- 建議 `alt`：一位成人坐在扶手椅上輕抱自己，胸前有柔和光點，象徵接納脆弱與自我照顧。
- 純裝飾圖片：否
- 建議 `object-fit`／焦點：`object-fit: cover; object-position: 72% center;`
- 生成或編修方式：ImageGen 生成，Pillow 裁切與 WebP 壓縮。
- 使用的參考素材：現有網站手繪插畫風格。
- 已知限制：畫面有抽象光點，使用時不宜搭配過度宗教或神秘化文案。
- 工程注意事項：可與「心理師的心靈雞湯」副標搭配，但不要呈現為勵志雞湯素材。
- 完成日期：2026-06-13

### ILL-ASSET-006：「其他文章／心理觀點」系列圖

- 對應圖片需求：ILL-REQ-006
- 對應正式需求：REQ-003、REQ-005
- 狀態：可供工程使用
- 用途：系列頁主視覺、首頁系列卡片、其他文章 OG 分享圖
- 目標頁面／區塊：`series/insights.html`、`articles.html` 其他文章卡片、`articles/love-and-imperfection.html`、`articles/post-election-self-care.html`、`articles/relationship-control.html`
- 實體檔案：
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-006-insights-series-1600x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-006-insights-series-mobile-900x900.webp`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-006-insights-series-1600x900.png`
  - `/Users/liuzhewei/Documents/Codex/therapist-profile/assets/illustrations/ill-006-insights-series-mobile-900x900.png`
- 網頁相對路徑：
  - 根目錄：`assets/illustrations/ill-006-insights-series-1600x900.webp`
  - 文章／系列頁：`../assets/illustrations/ill-006-insights-series-1600x900.webp`
  - 手機／卡片：`../assets/illustrations/ill-006-insights-series-mobile-900x900.webp`
- 桌機尺寸：1600 × 900
- 手機尺寸：900 × 900
- 檔案格式與大小：
  - WebP 桌機：151 KB
  - WebP 手機：120 KB
- 建議 `alt`：三個生活片段以紙頁拼貼呈現，包含關係對話、社會事件後的休息與獨處書寫。
- 純裝飾圖片：否
- 建議 `object-fit`／焦點：`object-fit: cover; object-position: 65% center;`
- 生成或編修方式：ImageGen 生成，Pillow 裁切與 WebP 壓縮。
- 使用的參考素材：現有網站手繪插畫風格。
- 已知限制：多片段構圖在小卡片中細節會較多，建議卡片最小高度不要過低。
- 工程注意事項：可作為其他文章共用 OG 圖；避免再加政治或社會事件圖示。
- 完成日期：2026-06-13

## 退回修改

目前無。
