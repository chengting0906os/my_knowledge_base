# Q4. 實作一個 decorator @cache
# 把函式的結果快取起來，相同參數不重複計算
# （簡易版 lru_cache）

from functools import wraps


def cache(func):
    pass


call_count = 0


@cache
def expensive(n):
    global call_count
    call_count += 1
    return n * 2


if __name__ == "__main__":
    assert expensive(3) == 6
    assert expensive(3) == 6   # 第二次應該走 cache，不重新計算
    assert expensive(5) == 10
    assert call_count == 2     # 只實際執行過 2 次（n=3 和 n=5）
    print("passed")
