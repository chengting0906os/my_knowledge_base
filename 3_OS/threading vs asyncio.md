# Threading vs Asyncio

Threading：由 OS kernel 強制調度，context switch 開銷較大且時序不可控，需自行管理 lock 以避免 race condition。  
Threading: Scheduled preemptively by the OS kernel. Context switching is relatively expensive, timing is less predictable, and locks are required to prevent race conditions.

Asyncio：由 event loop 在 user space 邏輯調度，透過 `await` 主動讓出控制權；通常是 single-thread、cooperative multitasking，切換成本低，主要解高併發 I/O-bound 問題。  
Asyncio: Scheduled by a user-space event loop. Tasks yield explicitly via `await`; it is typically a single-thread cooperative multitasking model with low overhead, designed for high-concurrency I/O-bound workloads.

Asyncio 的核心不是 CPU 並行，而是把 I/O 等待時間重疊：當一個 task 發出 I/O request 後，不會阻塞整個流程，而是先切去跑其他可執行 task。  
Asyncio concurrency comes from overlapping I/O wait time, not CPU parallel execution: when one task issues an I/O request, the loop runs other ready tasks instead of idling.
