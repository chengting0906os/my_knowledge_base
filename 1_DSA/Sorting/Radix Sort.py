from typing import List


def counting_sort_by_digit(arr: List[int], exp: int) -> None:
    """Stable sort by the digit at position exp (1, 10, 100, ...)."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for val in arr:
        digit = (val // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for val in reversed(arr):  # reversed to preserve stability
        digit = (val // exp) % 10
        count[digit] -= 1
        output[count[digit]] = val

    arr[:] = output


def radix_sort(arr: List[int]) -> None:
    if not arr:
        return

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10


if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("before:", data)
    radix_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average / Worst: O(nk)
#   k = number of digits in the largest value
#   performs k passes, each a O(n) counting sort
#
# Space Complexity: O(n + b)
#   b = base (10 here), output array of size n
#
# Note: stable — each digit pass uses a stable counting sort
#   NOT comparison-based; works only on integers (or fixed-length keys)
