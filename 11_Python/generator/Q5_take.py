# Q5. 實作 take(n, iterable)，從 iterable 取前 n 個值並 yield
# 不能用 itertools.islice，手動實作

from typing import Any, Generator, Iterable, NoReturn


def take(n: int, iterable: Iterable) -> Generator[Any, None, None]:
    count = 0
    for item in iterable:
        if count >= n:
            return 
        yield item
        count += 1


if __name__ == "__main__":
    def fibonacci() -> Generator[int, Any, NoReturn]:
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    assert list(take(3, fibonacci())) == [0, 1, 1]
    assert list(take(0, fibonacci())) == []
    assert list(take(5, range(3))) == [0, 1, 2]  # n > iterable 長度
    print("passed")
