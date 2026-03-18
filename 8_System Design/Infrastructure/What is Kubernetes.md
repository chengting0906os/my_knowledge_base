# What is Kubernetes

## 中文版

Kubernetes（K8s）是一個開源的**容器編排平台**，自動化容器的部署、擴展與管理。

### 核心概念

| 概念 | 說明 |
|------|------|
| **Pod** | K8s 最小部署單位，包含一個或多個 Container |
| **Node** | 執行 Pod 的實體/虛擬機器 |
| **Cluster** | 多個 Node 組成的叢集 |
| **Deployment** | 宣告式管理 Pod 副本數，支援滾動更新 |
| **Service** | 為一組 Pod 提供穩定的網路入口（ClusterIP / NodePort / LoadBalancer） |
| **ConfigMap / Secret** | 管理設定與敏感資訊，與容器解耦 |
| **Namespace** | 叢集內的邏輯隔離 |

### 架構

```
Control Plane
├── API Server        ← 所有操作的入口
├── etcd              ← 叢集狀態儲存
├── Scheduler         ← 決定 Pod 要放到哪個 Node
└── Controller Manager← 確保叢集狀態符合宣告

Worker Node
├── kubelet           ← 管理 Node 上的 Pod
├── kube-proxy        ← 網路規則
└── Container Runtime ← Docker / containerd
```

### K8s 解決什麼問題？
- 自動重啟掛掉的容器
- 根據負載自動擴縮（HPA）
- 滾動更新與回滾
- 服務發現與負載均衡
- 跨多主機的容器網路

### K8s vs Docker Compose
- Docker Compose：單機，適合開發環境
- K8s：多機叢集，適合 Production 大規模部署

## English Version

Kubernetes (K8s) is an open-source **container orchestration platform** that automates container deployment, scaling, and management.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Pod** | Smallest deployable unit; contains one or more containers |
| **Node** | Physical or virtual machine running Pods |
| **Cluster** | Group of Nodes managed together |
| **Deployment** | Declaratively manages Pod replicas; supports rolling updates |
| **Service** | Stable network endpoint for a set of Pods (ClusterIP / NodePort / LoadBalancer) |
| **ConfigMap / Secret** | Manage config and sensitive data decoupled from containers |
| **Namespace** | Logical isolation within a cluster |

### Architecture

```
Control Plane
├── API Server         ← Entry point for all operations
├── etcd               ← Cluster state store
├── Scheduler          ← Decides which Node a Pod runs on
└── Controller Manager ← Reconciles desired vs actual state

Worker Node
├── kubelet            ← Manages Pods on the Node
├── kube-proxy         ← Network rules
└── Container Runtime  ← Docker / containerd
```

### What problems does K8s solve?
- Automatically restarts crashed containers
- Auto-scales based on load (HPA)
- Rolling updates and rollbacks
- Service discovery and load balancing
- Container networking across multiple hosts

### K8s vs Docker Compose
- Docker Compose: single machine, great for development
- K8s: multi-machine cluster, designed for large-scale production deployments
