# Process Communication (IPC)

## What is IPC?

IPC (Inter-Process Communication) is how different processes exchange data and coordinate actions.

程序彼此記憶體隔離，不能像 thread 一樣直接共享變數，所以需要 IPC 機制。

## Why do we need IPC?

- Data exchange between services/processes
- Work coordination (producer/consumer)
- State notification (event/signal)
- Isolation + collaboration in multi-process systems

## Common IPC Mechanisms

### 1. Pipe (Anonymous Pipe)

- Usually used between parent/child processes
- Byte stream, simple and fast for local one-way communication
- Often written as `A | B` in shell

### 2. Named Pipe (FIFO)

- Like pipe, but has a filesystem path
- Unrelated processes can communicate through it

### 3. Message Queue

- Send structured messages instead of raw byte stream
- Async style communication; can decouple producer/consumer
- Kernel or middleware can manage queue order and buffering

### 4. Shared Memory

- Multiple processes map the same memory region
- Fastest data exchange (minimal copy)
- Must use synchronization (mutex/semaphore) to avoid race condition

### 5. Semaphore / Mutex (Synchronization IPC)

- Not mainly for payload data; used for coordination and access control
- Prevent concurrent write conflicts on shared resources

### 6. Signal

- Lightweight notification mechanism (`SIGINT`, `SIGTERM`, etc.)
- Good for event notification; not ideal for carrying rich data

### 7. Socket (Unix Domain / TCP)

- Most general IPC interface
- Unix domain socket: same host, lower overhead
- TCP socket: cross-host network communication

## Quick Comparison

- `Pipe/FIFO`: simple stream communication
- `Message Queue`: structured async messages
- `Shared Memory`: highest throughput, sync complexity is on you
- `Signal`: control/notification only
- `Socket`: most flexible, local + remote

## Interview Framing

- If asked "fastest IPC": usually `shared memory` (plus sync primitives)
- If asked "simplest local chaining": `pipe`
- If asked "distributed communication": `socket`
- If asked "safe decoupling": `message queue`
