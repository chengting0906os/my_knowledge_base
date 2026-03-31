# Q3. 實作 flatten generator，將任意深度的 nested list 展平

from typing import Any, Generator


def flatten(nested: list) -> Generator[Any, None, None]:
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    assert list(flatten([1, [2, [3, 4]], [5, 6]])) == [1, 2, 3, 4, 5, 6]
    assert list(flatten([[[1]], 2, [3, [4, [5]]]])) == [1, 2, 3, 4, 5]
    print("passed")
