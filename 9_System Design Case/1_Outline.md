### Step 1 釐清系統需求(System requirements)
- Non-Functional Requirements
	- **Latency**：p50 / p95 / p99？
	- **Throughput**：QPS / TPS？
	- **Availability**：99% / 99.9% / 99.99%？
	- **Consistency**：強一致 or 最終一致？
	- **Durability**：資料能不能丟？

### **Step 2 粗略估算（Back-of-the-envelope）**
- Traffic Estimate
	- DAU / MAU	
	- Peak QPS
	- Read : Write

- Data Size Estimates 
	- **單筆資料大小**
	- **每天新增多少**
	- **1 年總量**

- Bandwidth / Storage
	- **每秒進出資料量**

**Step.3 定義 System Interface**


### **Step.4 定義 Data Model | DB Schema**

### **Step.5 High-level design**

### **Step.6 System Detailed design**

**Step.7 找到系統可能瓶頸或 trade off 並嘗試給出解決方案**