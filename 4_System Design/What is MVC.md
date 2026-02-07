Controller 負責業務邏輯
Model 負責與資料庫互動
View 負責呈現的格式

不過由於現代前後端分離，我個人沒有遇到 View 層，而如果全把業務邏輯放在 Controller 也會過度擁擠，所以我個人沒有使用過傳統的 MVC 架構，現在的Controller 層也是負責與前端的欄位驗證與資料格式轉換，業務邏輯都不在 controller 層

以我個人而言是用 Clean Achitecture，會把業務邏輯跟實作分離，業務邏輯不應該依賴實作