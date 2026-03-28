# Hashing

- Hash Map / Dictionary
- Hash Set





Hash Table 用 key % size 把資料映射到陣列位置。兩個 key 映射到同一格稱為 collision。解決方法有兩種：

- **Chaining**：每個 bucket 掛一條 linked list，collision 的元素接在後面，查詢時遍歷該 list
- **Open Addressing**：衝突時不另開 list，直接在陣列裡往下找空格（線性探測 linear probing），直到找到空位為止

**Load factor** = 已存元素數 / table 總格數（n / size）。

例如 table 有 10 格、存了 7 個元素，load factor = 0.7。數值越高代表越擁擠，collision 機率越大，查詢效能從 O(1) 退化成 O(n)。當 load factor 超過閾值（通常 0.66 即 2/3），會觸發 rehash：建一個更大的 table，把所有元素重新 hash 一遍放進去。