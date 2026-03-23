from typing import List


def selection_sort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    selection_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average / Worst: O(n²)
#   always scans the entire unsorted portion to find the minimum
#   regardless of input order, does n + (n-1) + ... + 1 = n(n+1)/2 comparisons
#
# Space Complexity: O(1)
#   fully in-place — only swaps within the array
#
# Note: NOT stable — swapping may move an equal element past another
#   e.g. [3a, 3b, 1] → swap 3a with 1 → [1, 3b, 3a], order of 3s changed
