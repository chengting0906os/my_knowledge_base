# Q1. 實作一個 generator，產生無限的費波那契數列

from typing import Any, Generator, NoReturn


def fibonacci() -> Generator[int, Any, NoReturn]:
    dp1 = 0
    dp2 = 1
    while True:
        yield dp1
        temp = dp1
        dp1 = dp2
        dp2 = temp + dp2


if __name__ == "__main__":
    gen = fibonacci()
    assert [next(gen) for _ in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]
    print("passed")
