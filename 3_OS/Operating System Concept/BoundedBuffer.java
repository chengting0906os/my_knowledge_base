// BoundedBuffer.java
// 編譯：javac BoundedBuffer.java
// 執行：java BoundedBuffer

public class BoundedBuffer {

    private static final int BUFFER_SIZE = 5;

    // 環形 buffer，用陣列模擬
    private final Object[] buffer = new Object[BUFFER_SIZE];

    // in：下一個要寫入的位置
    // out：下一個要讀取的位置
    // count：目前 buffer 裡有幾個元素
    private int in = 0, out = 0, count = 0;

    // Producer 呼叫：把 item 放進 buffer
    // synchronized 確保同一時間只有一個 thread 能執行
    public synchronized void insert(Object item) throws InterruptedException {

        // buffer 滿了，等 Consumer 拿走東西再繼續
        // 用 while 而不是 if，是為了防止 spurious wakeup（假性喚醒）
        // 被喚醒後要重新檢查條件，不能直接繼續
        while (count == BUFFER_SIZE) {
            wait();  // 1) 釋放鎖  2) 把自己放進 Wait Set  3) 睡眠
        }

        buffer[in] = item;           // 把 item 放進 buffer
        in = (in + 1) % BUFFER_SIZE; // 移動寫入位置（環形）
        count++;                     // buffer 元素數 +1

        System.out.println("Producer inserted: " + item + " | count=" + count);

        // 通知等待中的 Consumer：buffer 裡有東西了
        // notify() 把 Wait Set 裡的一個 Thread 移到 Entry Set
        // 但不會馬上釋放鎖，等這個方法結束才釋放
        notify();
    }

    // Consumer 呼叫：從 buffer 取出一個 item
    public synchronized Object remove() throws InterruptedException {

        // buffer 空了，等 Producer 放東西再繼續
        while (count == 0) {
            wait();
        }

        Object item = buffer[out];     // 取出 item
        out = (out + 1) % BUFFER_SIZE; // 移動讀取位置（環形）
        count--;                       // buffer 元素數 -1

        System.out.println("Consumer removed:  " + item + " | count=" + count);

        // 通知等待中的 Producer：buffer 有空位了
        notify();

        return item;
    }

    // ──────────────────────────────────────────────
    // main：建立一個 Producer thread 和一個 Consumer thread
    // ──────────────────────────────────────────────
    public static void main(String[] args) {
        BoundedBuffer bb = new BoundedBuffer();

        // Producer thread：每隔一段時間放一個數字進去
        Thread producer = new Thread(() -> {
            for (int i = 1; i <= 10; i++) {
                try {
                    bb.insert(i);
                    Thread.sleep(500); // 模擬生產時間（500ms）
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        // Consumer thread：每隔一段時間拿一個數字出來
        Thread consumer = new Thread(() -> {
            for (int i = 1; i <= 10; i++) {
                try {
                    bb.remove();
                    Thread.sleep(800); // 模擬消費時間（800ms，比 Producer 慢）
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        producer.start(); // 啟動 Producer thread
        consumer.start(); // 啟動 Consumer thread
    }
}
