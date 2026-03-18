# CAP Theorem

## 中文版

分散式系統中，**一致性（Consistency）**、**可用性（Availability）**、**分區容忍性（Partition Tolerance）** 三者最多只能同時滿足兩個。

| 字母  | 名稱                | 說明                                                 |
| ----- | ------------------- | ---------------------------------------------------- |
| **C** | Consistency         | 所有節點在同一時間看到相同的資料（讀一定讀到最新值） |
| **A** | Availability        | 每個請求都一定會收到回應（不會卡住）                 |
| **P** | Partition Tolerance | 網路斷線時系統還能繼續運作                           |

**現實中，P 幾乎不可放棄**（網路故障無可避免），所以真正的選擇是 **CP 或 AP**。

### CP vs AP

|                | CP                     | AP                           |
| -------------- | ---------------------- | ---------------------------- |
| 發生網路分區時 | 拒絕服務（保一致性）   | 繼續服務（可能回傳舊資料）   |
| 典型系統       | HBase、Zookeeper、etcd | Cassandra、DynamoDB、CouchDB |
| 適合場景       | 金融、庫存扣減         | 購物車、DNS、社交動態        |

### 常見系統的選擇

| 系統 | 選擇 | 說明 |
|------|------|------|
| **MySQL** | CP | 關聯式資料庫，資料一致性優先，主從同步期間可能拒絕寫入 |
| **MongoDB** | CP（預設） | 預設強一致讀寫到 Primary，可調整為 AP（允許讀 Secondary） |
| **Cassandra** | AP | 高可用優先，多節點分散，允許最終一致 |
| **Redis Cluster** | AP | 速度優先，分區時允許部分節點繼續服務，可能讀到舊值 |
| **Zookeeper** | CP | 分散式配置管理，一致性是核心需求，分區時停止服務 |
| **etcd** | CP | Raft 共識算法，配置與服務發現需要強一致 |
| **DynamoDB** | AP（預設） | 預設最終一致，可選強一致讀（額外費用） |
| **HBase** | CP | 建立在 HDFS 上，強一致性，分區時可能不可用 |

### PACELC（延伸）

CAP 只討論分區時的取捨；PACELC 進一步考慮**正常情況下** Latency 與 Consistency 的取捨（也要選）。

## English Version

In a distributed system, you can only guarantee **two out of three**: Consistency, Availability, and Partition Tolerance.

| Letter | Name                | Description                                                                         |
| ------ | ------------------- | ----------------------------------------------------------------------------------- |
| **C**  | Consistency         | All nodes see the same data at the same time (reads always return the latest write) |
| **A**  | Availability        | Every request receives a response (not necessarily the latest value)                |
| **P**  | Partition Tolerance | System continues operating despite network partitions                               |

**In practice, P cannot be sacrificed** (network failures are inevitable), so the real choice is **CP or AP**.

### CP vs AP

|                          | CP                                     | AP                                       |
| ------------------------ | -------------------------------------- | ---------------------------------------- |
| During network partition | Reject requests (preserve consistency) | Continue serving (may return stale data) |
| Typical systems          | HBase, Zookeeper, etcd                 | Cassandra, DynamoDB, CouchDB             |
| Use cases                | Finance, inventory deduction           | Shopping cart, DNS, social feeds         |

### Real-World System Choices

| System | Choice | Reason |
|--------|--------|--------|
| **MySQL** | CP | Relational DB prioritizes consistency; may reject writes during primary-replica sync |
| **MongoDB** | CP (default) | Default strong-consistent reads/writes to Primary; configurable to AP (read from Secondary) |
| **Cassandra** | AP | High availability first; multi-node distribution allows eventual consistency |
| **Redis Cluster** | AP | Speed first; during partition, nodes continue serving — may return stale data |
| **Zookeeper** | CP | Distributed config management; consistency is critical — stops serving during partition |
| **etcd** | CP | Raft consensus; config and service discovery require strong consistency |
| **DynamoDB** | AP (default) | Eventual consistency by default; strongly consistent reads available (extra cost) |
| **HBase** | CP | Built on HDFS; strong consistency — may become unavailable during partition |

### PACELC (Extension)

CAP only covers the partition scenario. PACELC also considers the **Latency vs Consistency** trade-off during **normal operation**.
