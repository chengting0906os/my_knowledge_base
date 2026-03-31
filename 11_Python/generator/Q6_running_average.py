# Q6. 實作一個 generator，每次 yield 目前為止所有數字的平均值
# 用 send() 傳入新數字

# 用法：
# gen = running_average()
# next(gen)          # 初始化（必須先呼叫一次）
# gen.send(10)       # → 10.0
# gen.send(20)       # → 15.0
# gen.send(30)       # → 20.0

from typing import Generator


def running_average() -> Generator[float, float, None]:
    total = 0
    count = 0
    value = yield
    while True:
        total += value
        count += 1
        value = yield total / count


if __name__ == "__main__":
    gen = running_average()
    next(gen)
    assert gen.send(10) == 10.0
    assert gen.send(20) == 15.0
    assert gen.send(30) == 20.0
    assert gen.send(30) == 22.5
    print("passed")
