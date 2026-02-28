# CDN vs Reverse Proxy vs Load Balancer

## 一句話先分清楚

- CDN：把內容快取到離使用者更近的節點，重點是「加速與降源站壓力」。
- Reverse Proxy：站在源站前面代理請求，重點是「保護源站與統一入口控制」。
- Load Balancer：把流量分配到多台後端，重點是「擴展性與高可用」。

## 快速比較

| 元件 | 主要目標 | 常做的事 | 是否快取內容 | 主要放置位置 |
| --- | --- | --- | --- | --- |
| CDN | 降延遲、降頻寬成本 | 邊緣節點快取靜態/可快取內容、就近回應 | 會（核心能力） | 使用者與源站之間（全球邊緣） |
| Reverse Proxy | 保護/隱藏源站、統一入口 | TLS 終止、WAF、壓縮、快取、路由、限流 | 可選（看設定） | 源站前方 |
| Load Balancer | 分流與高可用 | 健康檢查、流量分配、故障切換 | 通常不以快取為主 | 多台後端前方 |

## 典型架構關係

1. 使用者先打到 CDN（命中快取就直接回）
2. 未命中時到 Reverse Proxy / API Gateway
3. 再由 Load Balancer 分流到多台 App Server

可同時存在，不衝突。

## 常見面試追問

### 1. CDN 跟 Reverse Proxy 不是都能快取嗎？

- 是，但定位不同：
  - CDN 的核心是「分散式邊緣快取」
  - Reverse Proxy 的核心是「源站前控制層」

### 2. Reverse Proxy 跟 Load Balancer 不一樣嗎？

- Reverse Proxy 偏「入口治理」；
- Load Balancer 偏「後端分流與高可用」。
- 實務上同一產品可能同時提供兩種能力（例如 Nginx / Envoy / 雲端 LB）。

### 3. 什麼內容適合放 CDN？

- 靜態資源：JS/CSS/圖片/字型
- 可快取 API（有明確快取策略）
- 不適合直接長時間快取：高度個人化或即時變動資料

## 30 秒面試版

CDN、Reverse Proxy、Load Balancer 都在源站前，但目標不同。  
CDN 主要做全球邊緣快取來加速；Reverse Proxy 主要做統一入口治理與保護源站；Load Balancer 主要把流量分到多台後端確保高可用與擴展。  
實務上三者常一起用：CDN 在最外層，內層 reverse proxy，再到 LB 分流。
