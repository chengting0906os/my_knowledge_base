# 7.4 Java 同步機制 — Monitor

## 四種機制

```
1. Java Monitor（最原始，本篇主要內容）
2. Reentrant Lock
3. Semaphore
4. Condition Variable
```

---

## 核心概念：每個物件都有一把鎖

Java 裡每一個物件天生就帶著：
- 一把 **Lock**
- 一個 **Wait Set**（等待集合）

---

## `synchronized` 關鍵字

```java
public class BoundedBuffer<E> {
    public synchronized void insert(E item) { ... }
    public synchronized E remove() { ... }
}
```

呼叫 synchronized 方法前，執行緒必須先拿到物件的鎖。

---

## Entry Set vs Wait Set

```
┌─────────────────────────────┐
│          Lock Owner         │  ← 正在執行的 Thread（只有一個）
└─────────────────────────────┘
         ↑            ↑
┌──────────────┐  ┌──────────────┐
│  Entry Set   │  │   Wait Set   │
│  等著搶鎖的  │  │  主動放棄鎖  │
│   Thread     │  │  在等條件的  │
└──────────────┘  └──────────────┘
```

|  | Entry Set | Wait Set |
|--|-----------|----------|
| 為什麼在這 | 鎖被別人拿走，**被迫等** | 條件不符合，**主動放棄等** |
| 怎麼進來 | 搶鎖失敗 | 呼叫 `wait()` |
| 怎麼出去 | 鎖被釋放，被選中 | 被 `notify()` 叫醒 |

---

## `wait()` 三步驟

```java
while (count == BUFFER_SIZE) {
    wait();
}
```

1. 釋放鎖（讓別人可以進來）
2. 把自己狀態設為 Blocked
3. 把自己丟進 Wait Set

---

## `notify()` 三步驟

```java
count--;
notify();
```

1. 從 Wait Set 隨機挑一個 Thread
2. 把它移到 Entry Set
3. 狀態從 Blocked 改回 Runnable

> `notify()` 不會馬上釋放鎖，要等整個 synchronized 方法執行完才釋放。

---

## Block Synchronization

不一定要鎖整個方法，可以只鎖關鍵區段：

```java
public void someMethod() {
    // 不需要鎖的部分正常執行

    synchronized(this) {
        // 只鎖這段關鍵區域
    }

    // 不需要鎖的部分正常執行
}
```

> 鎖的範圍越小 → 其他 Thread 等待時間越短 → 效能越好

---

## 一句話總結

> `synchronized` 控制誰能進入，`wait()` 讓條件不符的 Thread 主動讓出鎖去睡覺，`notify()` 在條件改變時把它叫醒。
> **Entry Set 管搶鎖，Wait Set 管等條件。**

---

## 對應範例

見 [BoundedBuffer.java](BoundedBuffer.java)
