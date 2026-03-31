# Q4. 實作 chunked generator，將 iterable 切成固定大小的 chunk
# 最後一組不足 size 也要 yield

from typing import Any, Generator, Iterable


def chunked(iterable: Iterable, size: int) -> Generator[list[Any], None, None]:
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


if __name__ == "__main__":
    assert list(chunked(range(7), 3)) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunked(range(6), 2)) == [[0, 1], [2, 3], [4, 5]]
    assert list(chunked([], 3)) == []
    print("passed")
