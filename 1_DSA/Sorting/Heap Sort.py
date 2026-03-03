from typing import List


def heap_sort(arr: List[int]) -> None:
    n = len(arr)

    # Build max heap (heapify from bottom up)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move current max to end
        heapify(arr, i, 0)               # restore heap on reduced array


def heapify(arr: List[int], n: int, i: int) -> None:
    largest = i
    left    = 2 * i + 1
    right   = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # fix the affected subtree


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    heap_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average / Worst: O(n log n)
#   building the max heap takes O(n)
#   each of the n extractions calls heapify → O(log n) each
#   total: O(n log n) guaranteed, no worst-case degradation
#
# Space Complexity: O(1)
#   fully in-place — no extra arrays created
#   heapify uses O(log n) call stack but that is typically ignored
#
# Note: not stable — swapping elements during extraction can change
#   the relative order of equal values
