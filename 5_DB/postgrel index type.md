# PostgreSQL Index Types（整理＋中文翻譯）

PostgreSQL 提供多種索引型別：`B-tree`、`Hash`、`GiST`、`SP-GiST`、`GIN`、`BRIN`，以及擴充套件 `bloom`。  
每種索引背後使用不同演算法，適合不同查詢條件（indexable clauses）。

`CREATE INDEX` 預設建立的是 `B-tree`。  
若要指定其他型別，使用 `USING`：

```sql
CREATE INDEX name ON table USING HASH (column);
```

## 11.2.1 B-Tree

`B-tree` 適合可排序資料上的「等值 + 範圍」查詢。  
當欄位使用下列比較運算子時，查詢規劃器通常會考慮 B-tree：

`<   <=   =   >=   >`

也支援由上述運算子組合而成的條件，例如：

- `BETWEEN`
- `IN`
- `IS NULL`
- `IS NOT NULL`

`LIKE` 與正規表示式也可能用到 B-tree（需符合條件）：

- 可用：模式為常數且從字首開始，例如 `col LIKE 'foo%'`、`col ~ '^foo'`
- 不可用：前綴不固定，例如 `col LIKE '%bar'`

補充：

- 若資料庫不是 `C locale`，要用特定 operator class 才能有效支援 pattern matching 索引。
- `ILIKE`、`~*` 只有在 pattern 以「不受大小寫影響字元」開頭時，才有機會受益。
- B-tree 也可用來支援排序讀取（不一定永遠比 scan + sort 快，但常常有幫助）。

## 11.2.2 Hash

`Hash` 索引儲存的是索引欄位值計算出的 `32-bit hash code`，  
因此只適合「等值比對」：

`=`

不適合範圍查詢（例如 `<`, `>`, `BETWEEN`）。

## 11.2.3 GiST

`GiST` 不是單一索引結構，而是可擴充的索引框架。  
可用哪些運算子，取決於該資料型別對應的 operator class。

以 PostgreSQL 內建的 2D 幾何型別為例，可支援：

`<<   &<   &>   >>   <<|   &<|   |&>   |>>   @>   <@   ~=   &&`

`GiST` 也支援最近鄰搜尋（nearest-neighbor），例如：

```sql
SELECT * FROM places
ORDER BY location <-> point '(101,456)'
LIMIT 10;
```

是否可用距離排序，同樣取決於 operator class。

## 11.2.4 SP-GiST

`SP-GiST` 跟 `GiST` 一樣是框架型索引，但偏向支援「非平衡」磁碟資料結構，  
例如 `quadtrees`、`k-d trees`、`radix trees (tries)`。

以內建 2D points 為例，可支援：

`<<   >>   ~=   <@   <<|   |>>`

同樣支援最近鄰搜尋（nearest-neighbor），  
實際可用的距離排序運算子依 operator class 而定。

## 11.2.5 GIN

`GIN` 是倒排索引（inverted index），  
適合「一個欄位包含多個組件值」的資料，例如 `arrays`、全文檢索 tokens、`jsonb` 等情境。

它會為每個 component value 建立索引條目，  
因此很適合查「是否包含某元素」的查詢。

以內建 array operator class 為例，可支援：

`<@   @>   =   &&`

和 `GiST` / `SP-GiST` 一樣，可用哪些運算子取決於 operator class。

## 11.2.6 BRIN

`BRIN`（Block Range INdexes）不是記錄每一列，而是記錄「連續區塊範圍」的摘要資訊。  
因此非常省空間，適合超大表。

它最適合「欄位值與實體儲存順序高度相關」的情況（correlation 高），  
例如時間序遞增的資料。

對於具線性排序的資料型別，通常可支援：

`<   <=   =   >=   >`

實際支援仍取決於 operator class。

## 面試可用一句話總結

- `B-tree`：預設萬用款，等值/範圍/排序最常用。
- `Hash`：只做等值比對。
- `GiST`：通用空間與複合資料框架，能做最近鄰。
- `SP-GiST`：適合非平衡分割結構（如 k-d tree、trie）。
- `GIN`：多值欄位（array/jsonb/text search）查包含關係很強。
- `BRIN`：超大表且資料有物理順序關聯時，超省空間。

參考：  
https://www.postgresql.org/docs/current/indexes-types.html

---

# English Notes (Original Content Kept)

PostgreSQL provides several index types: `B-tree`, `Hash`, `GiST`, `SP-GiST`, `GIN`, `BRIN`, and the extension `bloom`.  
Each index type uses a different algorithm and is best suited to different indexable clauses.

By default, `CREATE INDEX` creates a `B-tree` index.  
To choose another type, use `USING`:

```sql
CREATE INDEX name ON table USING HASH (column);
```

## 11.2.1 B-Tree

B-trees support equality and range queries on data that can be sorted.  
The planner considers a B-tree index for:

`<   <=   =   >=   >`

Equivalent constructs such as `BETWEEN` and `IN` can also use B-tree.  
`IS NULL` and `IS NOT NULL` conditions can also use B-tree indexes.

For pattern matching, B-tree may be used for `LIKE` and `~` when:

- the pattern is a constant
- and anchored at the beginning (`col LIKE 'foo%'`, `col ~ '^foo'`)

Not usable for suffix-only patterns like `col LIKE '%bar'`.

If the DB collation is not `C locale`, you may need a special operator class for pattern indexing.  
`ILIKE` and `~*` can use B-tree only in limited cases (for example, leading non-alphabetic characters).

B-tree can also be used for sorted retrieval.

## 11.2.2 Hash

Hash indexes store a 32-bit hash code of the indexed value,  
so they support only simple equality:

`=`

## 11.2.3 GiST

GiST is a framework, not a single index type.  
Supported operators depend on the operator class.

For built-in 2D geometric types, common operators include:

`<<   &<   &>   >>   <<|   &<|   |&>   |>>   @>   <@   ~=   &&`

GiST can also optimize nearest-neighbor queries, for example:

```sql
SELECT * FROM places
ORDER BY location <-> point '(101,456)'
LIMIT 10;
```

## 11.2.4 SP-GiST

SP-GiST is also a framework for non-balanced disk-based structures  
(for example, quadtrees, k-d trees, radix trees / tries).

For built-in 2D points, operators include:

`<<   >>   ~=   <@   <<|   |>>`

Like GiST, SP-GiST can support nearest-neighbor searches depending on operator class.

## 11.2.5 GIN

GIN is an inverted index, suitable for values containing multiple components  
(for example arrays, tokens, jsonb elements).

For built-in array operator classes, operators include:

`<@   @>   =   &&`

Supported operators depend on the operator class.

## 11.2.6 BRIN

BRIN (Block Range Indexes) stores summaries for ranges of physical blocks.  
It is most effective when column values are well-correlated with physical row order.

For linearly ordered data types, BRIN commonly supports:

`<   <=   =   >=   >`

Supported operators depend on the indexing strategy / operator class.

## reference

- https://www.youtube.com/watch?v=iWcskTGXM-o
