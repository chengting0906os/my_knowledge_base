# Docker

## 什麼是 Docker

Docker 是一種容器化技術，用來把應用程式與其依賴打包成可攜、可重現的執行單位（container）。

## 核心原理（Linux）

- **Namespace**：提供隔離視角（PID、Network、Mount、UTS、IPC、User）。
- **cgroups**：限制與統計資源（CPU、Memory、I/O）。
- **Union Filesystem**：用分層方式組 image，啟動快、重用高。

你可以把容器理解成：  
一組被 namespace 隔離、被 cgroups 限流的 process（通常有一個主 process）。

## Docker 不是什麼

- 不是 VM（不含完整 Guest OS）。
- 不是單純「跑一個 process」而已，而是帶有隔離、資源控制、映像管理的執行環境。

## 面試 30 秒版

Docker 是 OS 層虛擬化。它用 namespace 做隔離、用 cgroups 做資源限制，把應用與依賴封裝成 image，在不同環境以一致方式執行。和 VM 相比更輕、更快，但共享 Host Kernel。
