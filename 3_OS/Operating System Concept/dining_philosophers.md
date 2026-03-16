# 哲學家進餐問題（Dining Philosophers Problem）

## 問題描述

五位哲學家圍坐圓桌，每人面前有一碗飯，相鄰之間共用一支筷子（共 5 支）。
哲學家只有兩種狀態：**思考** 和 **進餐**。
進餐需要同時拿起**左右兩支筷子**，吃完後放下。

## 核心挑戰

| 問題 | 說明 |
|------|------|
| 死鎖（Deadlock） | 每人都拿起左邊的筷子，等待右邊，全部卡死 |
| 飢餓（Starvation） | 某位哲學家永遠搶不到資源 |
| 資源競爭（Race Condition） | 同一支筷子被兩人同時拿取 |

## 常見解法

1. **限制最大進餐人數**：最多允許 4 人同時拿筷子，保證至少一人能拿到兩支
2. **奇偶策略**：奇數編號先拿左，偶數先拿右，打破對稱性
3. **資源排序**：依編號順序取筷子，避免循環等待
4. **信號量 / Monitor**：集中控制，確保每次只有一人能成功拿到兩支

## 實作（C + pthread）

此實作使用 **Monitor 模式**：一把全域 mutex + 每人一個 condition variable，狀態集中管理。

```c
// dining_philosophers.c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_PHILOSOPHERS 5
#define THINKING 0
#define HUNGRY   1
#define EATING   2

pthread_mutex_t mutex;
pthread_cond_t  cond[NUM_PHILOSOPHERS];
int state[NUM_PHILOSOPHERS];
int phil[NUM_PHILOSOPHERS] = {0, 1, 2, 3, 4};

void *philosopher(void *arg);
void take_forks(int phil_num);
void put_forks(int phil_num);
void test(int phil_num);

int main() {
    pthread_t thread_id[NUM_PHILOSOPHERS];

    pthread_mutex_init(&mutex, NULL);
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_cond_init(&cond[i], NULL);

    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_create(&thread_id[i], NULL, philosopher, &phil[i]);

    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_join(thread_id[i], NULL);

    pthread_mutex_destroy(&mutex);
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_cond_destroy(&cond[i]);

    return 0;
}

void *philosopher(void *arg) {
    int n = *(int *)arg;
    while (1) {
        printf("Philosopher %d is thinking\n", n);
        sleep(rand() % 3 + 1);

        take_forks(n);

        printf("Philosopher %d is eating\n", n);
        sleep(rand() % 3 + 1);

        put_forks(n);
    }
}

void take_forks(int n) {
    pthread_mutex_lock(&mutex);
    state[n] = HUNGRY;
    test(n);
    while (state[n] != EATING)
        pthread_cond_wait(&cond[n], &mutex);  // 等到鄰居放下筷子才被喚醒
    pthread_mutex_unlock(&mutex);
}

void put_forks(int n) {
    pthread_mutex_lock(&mutex);
    state[n] = THINKING;
    test((n + 4) % NUM_PHILOSOPHERS);  // 通知左鄰
    test((n + 1) % NUM_PHILOSOPHERS);  // 通知右鄰
    pthread_mutex_unlock(&mutex);
}

void test(int n) {
    int left  = (n + 4) % NUM_PHILOSOPHERS;
    int right = (n + 1) % NUM_PHILOSOPHERS;
    if (state[n] == HUNGRY && state[left] != EATING && state[right] != EATING) {
        state[n] = EATING;
        pthread_cond_signal(&cond[n]);  // 喚醒此哲學家
    }
}
```

編譯與執行：

```bash
gcc -o dining_philosophers dining_philosophers.c -lpthread
./dining_philosophers
# Ctrl+C 終止
```

## 關鍵機制說明

### `take_forks`
1. 鎖住 mutex
2. 設為 HUNGRY
3. 呼叫 `test()` — 若左右都沒在吃，立刻進入 EATING
4. 若還不能吃 → `cond_wait` **釋放 mutex 並睡眠**，等人喚醒
5. 醒來後重新檢查，確認是 EATING 才繼續

### `put_forks`
1. 設為 THINKING
2. 通知左右鄰居去 `test()`
3. 若鄰居符合條件，`cond_signal` 喚醒他們

### `test`
- 三個條件全符合才能吃：自己是 HUNGRY、左鄰不在吃、右鄰不在吃
- 這是避免死鎖的核心邏輯

## 為什麼不會死鎖？

傳統死鎖來自「每人先拿一支再等另一支」的循環等待。
此實作把「能不能吃」的判斷集中在 `test()` 裡，且由全域 mutex 保護：
- 哲學家不直接搶筷子，而是**申請進入 EATING 狀態**
- 只有在左右鄰居都沒吃時才成功，否則直接睡眠等通知
- 不存在「各持一支互等」的情況
