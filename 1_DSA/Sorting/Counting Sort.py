from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1

    count = [0] * k
    for val in arr:
        count[val - min_val] += 1

    # prefix sum — count[i] now holds the position of arr[i] in output
    for i in range(1, k):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for val in reversed(arr):  # reversed to preserve stability
        idx = count[val - min_val] - 1
        output[idx] = val
        count[val - min_val] -= 1

    return output


if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("before:", data)
    data = counting_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average / Worst: O(n + k)
#   k = range of values (max - min + 1)
#   one pass to count (O(n)), one pass over count array (O(k)), one pass to place (O(n))
#   efficient when k is small relative to n
#
# Space Complexity: O(k)
#   count array of size k; output array of size n (also O(n))
#
# Note: stable — iterating in reverse during placement preserves original order
#   NOT comparison-based → not bounded by Ω(n log n) lower bound
