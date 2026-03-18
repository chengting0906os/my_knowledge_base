# Design Patterns

## 中文版

設計模式是針對常見軟體設計問題的可重複使用解法，分為三大類。

### Creational（創建型）— 物件如何被創建

| 模式 | 說明 | 場景 |
|------|------|------|
| **Singleton** | 確保一個 class 只有一個實例 | 設定檔、Logger、DB 連線池 |
| **Factory Method** | 由子類決定創建哪種物件 | 跨平台 UI 元件 |
| **Abstract Factory** | 創建一族相關的物件 | 不同主題的 UI 套件 |
| **Builder** | 分步驟構建複雜物件 | 建構 SQL Query、HTTP Request |
| **Prototype** | 透過複製現有物件來創建新物件 | 複製成本高的物件 |

### Structural（結構型）— 物件如何組合

| 模式 | 說明 | 場景 |
|------|------|------|
| **Adapter** | 讓不相容的介面能一起工作 | 舊 API 轉接、第三方 SDK 包裝 |
| **Decorator** | 動態為物件新增功能 | I/O Stream、Middleware |
| **Facade** | 為複雜子系統提供簡化介面 | SDK 封裝 |
| **Proxy** | 控制對物件的存取 | 延遲載入、權限控制、快取 |
| **Composite** | 樹狀結構統一處理單個與群組 | 檔案系統、UI 元件樹 |

### Behavioral（行為型）— 物件如何互動

| 模式 | 說明 | 場景 |
|------|------|------|
| **Observer** | 一對多通知，狀態改變時通知所有訂閱者 | Event System、MQ、React State |
| **Strategy** | 封裝算法，讓算法可互換 | 排序策略、支付方式 |
| **Command** | 將請求封裝為物件 | Undo/Redo、Job Queue |
| **Iterator** | 統一遍歷集合的方式 | for-each |
| **Template Method** | 定義算法骨架，子類填入細節 | 框架 Hook |

## English Version

Design patterns are reusable solutions to common software design problems, grouped into three categories.

### Creational — How objects are created

| Pattern | Description | Use cases |
|---------|-------------|-----------|
| **Singleton** | Ensures only one instance of a class exists | Config, Logger, DB connection pool |
| **Factory Method** | Subclass decides which object to create | Cross-platform UI components |
| **Abstract Factory** | Creates families of related objects | Themed UI kits |
| **Builder** | Constructs complex objects step by step | SQL query builder, HTTP request builder |
| **Prototype** | Creates new objects by cloning existing ones | Expensive-to-create objects |

### Structural — How objects are composed

| Pattern | Description | Use cases |
|---------|-------------|-----------|
| **Adapter** | Makes incompatible interfaces work together | Legacy API wrapping, third-party SDK integration |
| **Decorator** | Dynamically adds behavior to objects | I/O Streams, Middleware |
| **Facade** | Simplified interface for a complex subsystem | SDK wrapping |
| **Proxy** | Controls access to an object | Lazy loading, access control, caching |
| **Composite** | Tree structure treating individual and groups uniformly | File system, UI component tree |

### Behavioral — How objects interact

| Pattern | Description | Use cases |
|---------|-------------|-----------|
| **Observer** | One-to-many notification when state changes | Event systems, MQ, React state |
| **Strategy** | Encapsulates interchangeable algorithms | Sort strategies, payment methods |
| **Command** | Encapsulates a request as an object | Undo/Redo, job queue |
| **Iterator** | Uniform way to traverse a collection | for-each |
| **Template Method** | Defines algorithm skeleton; subclasses fill in details | Framework hooks |
