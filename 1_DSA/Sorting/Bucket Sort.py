from typing import List


def bucket_sort(arr: List[float]) -> List[float]:
    """
    Sorts floats in [0, 1). Works best when input is uniformly distributed.
    For integer input, normalise first or adjust bucket mapping accordingly.
    """
    if not arr:
        return []

    n = len(arr)
    buckets: List[List[float]] = [[] for _ in range(n)]

    for val in arr:
        idx = int(val * n)          # map value to bucket index
        idx = min(idx, n - 1)       # clamp edge case val == 1.0
        buckets[idx].append(val)

    result = []
    for bucket in buckets:
        bucket.sort()               # insertion sort on small buckets is O(k²)
        result.extend(bucket)

    return result


if __name__ == "__main__":
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("before:", data)
    data = bucket_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average: O(n + k)  — k = number of buckets
#   with uniform distribution each bucket holds ~1 element → sort per bucket is O(1)
#   total: O(n) bucket assignment + O(n) sorting across all buckets
#
# Worst: O(n²)
#   all elements fall into the same bucket → degrades to insertion sort on n elements
#
# Space Complexity: O(n)
#   n buckets + all elements distributed across them
#
# Note: stability depends on the sub-sort used (Python's list.sort() is stable)
