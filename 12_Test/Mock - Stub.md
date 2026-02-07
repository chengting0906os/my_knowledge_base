**單元測試之 mock/stub/spy/fake ? 傻傻搞不清楚**
https://medium.com/@henry-chou/%E5%96%AE%E5%85%83%E6%B8%AC%E8%A9%A6%E4%B9%8B-mock-stub-spy-fake-%E5%82%BB%E5%82%BB%E6%90%9E%E4%B8%8D%E6%B8%85%E6%A5%9A-ba3dc4e86d86

https://www.cythilya.tw/2024/04/18/breaking-dependencies-with-stubs/


Mock 在意互動是否符合預期，比如 assert_called_once(), assert_called_once_with()
Stub 回傳固定假資料，不驗證互動
Spy 記錄互動供事後驗證，比如測試 SSE 的時候，用list 去接回應，或測試執行順序 idx 的時候
Fake 用「**可運作但簡化**」的實作來替代昂貴/外部依賴，讓流程照跑但成本低；想測 DB 行為，但把 DB class 全部換成自己寫的實作，只要它真的能存、能查、能影響流程，比如要測產生 log 檔案但放在指定的地方，模擬**可配置的物件，類似是可動態調整的 fake class 服務**
Dummy: 為了補參數，不會被呼叫，比如依賴注入的時候會傳 repo 進去，repo class 變成 object()
