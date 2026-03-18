# DDD — Domain-Driven Design

## 中文版

以**業務領域**為核心設計軟體，讓程式碼結構與業務語言一致，適合複雜業務系統。

### 核心概念

| 概念 | 說明 |
|------|------|
| **Domain** | 業務問題空間（如電商、金融） |
| **Ubiquitous Language** | 開發者與領域專家共用的語言，消滅翻譯成本 |
| **Bounded Context** | 一個模型只在特定邊界內有效（如「訂單」在物流和結帳中的定義不同） |
| **Entity** | 有唯一識別 ID 的物件（如 User、Order） |
| **Value Object** | 無 ID、以值判斷相等的物件（如 Money、Address） |
| **Aggregate** | 一組相關 Entity/VO 的叢集，有一個 Aggregate Root 作為唯一入口 |
| **Domain Event** | 領域中發生的重要事實（如 `OrderPlaced`） |
| **Repository** | 存取 Aggregate 的抽象層，隱藏資料來源 |
| **Domain Service** | 不屬於任何 Entity 的業務邏輯 |

### Bounded Context 的重要性

```
電商系統中的「商品」：
- 商品目錄 Context：名稱、描述、圖片
- 倉儲 Context：庫存數量、倉位
- 結帳 Context：價格、折扣

→ 三個 Context 各自維護自己的「商品」模型，不強迫統一
→ Context 之間透過 API 或 Domain Event 通訊
```

### DDD 與 Microservices 的關係
Bounded Context 是劃分微服務邊界的最佳參考，一個 Bounded Context 對應一個微服務。

### 適合使用 DDD 的情況
- 業務邏輯複雜、規則多
- 團隊與業務人員需要緊密協作
- 系統需要長期維護與擴展

## English Version

Design software around the **business domain**, aligning code structure with business language — best suited for complex business systems.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Domain** | The business problem space (e.g., e-commerce, finance) |
| **Ubiquitous Language** | Shared vocabulary between developers and domain experts — eliminates translation |
| **Bounded Context** | A model is only valid within a specific boundary (e.g., "product" means different things in logistics vs checkout) |
| **Entity** | Object with a unique identity (e.g., User, Order) |
| **Value Object** | No identity; equality determined by value (e.g., Money, Address) |
| **Aggregate** | Cluster of related Entities/VOs with one Aggregate Root as the single entry point |
| **Domain Event** | Significant fact that happened in the domain (e.g., `OrderPlaced`) |
| **Repository** | Abstraction for accessing Aggregates; hides the data source |
| **Domain Service** | Business logic that doesn't naturally belong to any Entity |

### Why Bounded Context matters

```
"Product" in an e-commerce system:
- Catalog Context: name, description, images
- Warehouse Context: stock quantity, location
- Checkout Context: price, discounts

→ Each Context owns its own "Product" model independently
→ Contexts communicate via APIs or Domain Events
```

### DDD and Microservices
Bounded Contexts are the best guide for defining microservice boundaries — one Bounded Context typically maps to one microservice.

### When to use DDD
- Complex business logic with many rules
- Close collaboration between engineering and business teams is needed
- System requires long-term maintenance and evolution
