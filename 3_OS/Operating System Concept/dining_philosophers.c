// dining_philosophers.c
// 編譯：gcc -o dining_philosophers dining_philosophers.c -lpthread
// 執行：./dining_philosophers
// 終止：Ctrl+C

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>  // POSIX thread 函式庫
#include <unistd.h>   // sleep() 函式

#define NUM_PHILOSOPHERS 5  // 哲學家數量（也是筷子數量）
#define THINKING 0          // 狀態：思考中
#define HUNGRY   1          // 狀態：想吃飯（等筷子）
#define EATING   2          // 狀態：正在吃飯

// 全域互斥鎖：確保同一時間只有一個 thread 能修改共享狀態
// 等同 Python 的 threading.Lock()
pthread_mutex_t mutex;

// 每位哲學家各自的 condition variable
// 當哲學家搶不到筷子時，在這裡睡眠等待
// 等同 Python 的 threading.Condition()
pthread_cond_t cond[NUM_PHILOSOPHERS];

// 每位哲學家的當前狀態（THINKING / HUNGRY / EATING）
int state[NUM_PHILOSOPHERS];

// 哲學家編號陣列，建立 thread 時當作參數傳入
int phil[NUM_PHILOSOPHERS] = {0, 1, 2, 3, 4};

// 函式宣告
void *philosopher(void *arg);
void take_forks(int phil_num);
void put_forks(int phil_num);
void check(int phil_num);

int main() {
    pthread_t thread_id[NUM_PHILOSOPHERS];  // 儲存每個 thread 的 ID

    // 初始化互斥鎖（NULL 表示使用預設設定）
    pthread_mutex_init(&mutex, NULL);

    // 初始化每位哲學家的 condition variable
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_cond_init(&cond[i], NULL);

    // 建立 5 個 thread，每個代表一位哲學家
    // philosopher 是 thread 要執行的函式，&phil[i] 是傳入的參數（哲學家編號的記憶體位址）
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_create(&thread_id[i], NULL, philosopher, &phil[i]);

    // 等待所有 thread 結束（這裡會永久阻塞，因為哲學家是無限迴圈）
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_join(thread_id[i], NULL);

    // 釋放資源（實際上因為無限迴圈不會跑到這裡）
    pthread_mutex_destroy(&mutex);
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_cond_destroy(&cond[i]);

    return 0;
}

// 每位哲學家的行為：無限循環「思考 → 拿筷子 → 吃飯 → 放筷子」
// void *arg：接收傳入的哲學家編號（型別是 void* 因為 pthread 規定）
void *philosopher(void *arg) {
    int n = *(int *)arg;  // 把 void* 轉回 int*，再取值得到哲學家編號

    while (1) {
        printf("Philosopher %d is thinking\n", n);
        // rand() 產生一個隨機整數
        // rand() % 3 → 結果是 0, 1, 2 其中一個（取餘數）
        // rand() % 3 + 1 → 結果是 1, 2, 3 其中一個
        // sleep(n) → 讓這個 thread 暫停 n 秒
        sleep(rand() % 3 + 1);  // 隨機思考 1~3 秒（模擬思考時間）

        take_forks(n);  // 嘗試拿兩支筷子（可能會等待）

        printf("Philosopher %d is eating\n", n);
        sleep(rand() % 3 + 1);  // 隨機吃飯 1~3 秒（同上）

        put_forks(n);   // 放下兩支筷子，通知旁邊的人
    }
}

// 拿筷子：設為 HUNGRY，嘗試進入 EATING，不行就睡眠等待
void take_forks(int n) {
    pthread_mutex_lock(&mutex);  // 上鎖，確保以下操作不被其他 thread 干擾

    state[n] = HUNGRY;  // 宣告自己想吃飯
    check(n);            // 檢查左右鄰居是否都沒在吃，是的話直接進入 EATING

    // 如果 test() 沒有讓自己進入 EATING，就在這裡睡眠等待
    // pthread_cond_wait 會同時：1) 解鎖 mutex 2) 進入睡眠
    // 被喚醒時會自動重新上鎖，然後再檢查一次條件
    while (state[n] != EATING)
        pthread_cond_wait(&cond[n], &mutex);

    pthread_mutex_unlock(&mutex);  // 解鎖，讓其他 thread 可以繼續
}

// 放筷子：設為 THINKING，通知左右鄰居去搶筷子
void put_forks(int n) {
    pthread_mutex_lock(&mutex);  // 上鎖

    state[n] = THINKING;  // 自己吃完了，不再佔用筷子

    // 通知左鄰（編號 n-1，用 +4 取代 -1 避免負數）
    check((n + 4) % NUM_PHILOSOPHERS);

    // 通知右鄰（編號 n+1）
    check((n + 1) % NUM_PHILOSOPHERS);

    pthread_mutex_unlock(&mutex);  // 解鎖
}

// 判斷哲學家 n 能不能開始吃飯
// 條件：自己是 HUNGRY，且左右鄰居都不是 EATING
void check(int n) {
    int left  = (n + 4) % NUM_PHILOSOPHERS;  // 左鄰編號
    int right = (n + 1) % NUM_PHILOSOPHERS;  // 右鄰編號

    if (state[n] == HUNGRY &&
        state[left]  != EATING &&
        state[right] != EATING) {

        state[n] = EATING;  // 成功拿到兩支筷子，開始吃飯

        // 喚醒正在 cond_wait 睡眠的哲學家 n
        // 如果他還沒睡（第一次 take_forks 直接成功），這個 signal 也無害
        pthread_cond_signal(&cond[n]);
    }
}
