# CI/CD

## 中文版

### CI — Continuous Integration（持續整合）

每次 Push 或 PR 時自動執行：Build → Test → Static Analysis

目的：**盡早發現問題**，避免「在我電腦上沒問題」的整合地獄。

### CD — Continuous Delivery / Deployment（持續交付 / 部署）

| | Continuous Delivery | Continuous Deployment |
|---|---|---|
| 說明 | 自動化到「可部署的產出物」，需人工觸發才部署 | 全自動，通過測試後直接部署到 Production |
| 適合 | 需要審核的系統（金融、醫療） | 快速迭代的產品 |

### 典型 Pipeline

```
Push Code
    ↓
CI: Build → Unit Test → Integration Test → Lint / SAST
    ↓ 通過
CD: Build Docker Image → Push to Registry
    ↓
Deploy to Staging → E2E Test
    ↓ 通過
Deploy to Production（自動 or 人工觸發）
```

### 常見工具

| 類型 | 工具 |
|------|------|
| CI/CD 平台 | GitHub Actions、GitLab CI、Jenkins、CircleCI |
| Container Registry | Docker Hub、ECR、GCR |
| 部署 | Kubernetes、ECS、Helm |
| 監控 | Datadog、Prometheus、Grafana |

### 最佳實踐
- **Fast feedback**：Pipeline 盡量在 10 分鐘內完成
- **Fail fast**：便宜的測試先跑（Unit → Integration → E2E）
- **Immutable artifact**：同一個 Image 從 Staging 到 Production，不重新 build
- **Feature flags**：部署與功能上線解耦，隨時可回滾

## English Version

### CI — Continuous Integration

Automatically triggered on every push or PR: Build → Test → Static Analysis

Goal: **Catch problems early**, preventing integration hell ("it works on my machine").

### CD — Continuous Delivery / Deployment

| | Continuous Delivery | Continuous Deployment |
|---|---|---|
| Description | Automates up to a deployable artifact; manual trigger to deploy | Fully automated — passes tests → deploys to Production |
| Best for | Systems requiring approval (finance, healthcare) | Fast-iteration products |

### Typical Pipeline

```
Push Code
    ↓
CI: Build → Unit Test → Integration Test → Lint / SAST
    ↓ Pass
CD: Build Docker Image → Push to Registry
    ↓
Deploy to Staging → E2E Test
    ↓ Pass
Deploy to Production (automated or manual trigger)
```

### Common Tools

| Category | Tools |
|----------|-------|
| CI/CD platform | GitHub Actions, GitLab CI, Jenkins, CircleCI |
| Container registry | Docker Hub, ECR, GCR |
| Deployment | Kubernetes, ECS, Helm |
| Monitoring | Datadog, Prometheus, Grafana |

### Best Practices
- **Fast feedback**: keep the full pipeline under 10 minutes
- **Fail fast**: run cheap tests first (Unit → Integration → E2E)
- **Immutable artifact**: promote the same image from Staging to Production — never rebuild
- **Feature flags**: decouple deployment from feature release for instant rollback capability
