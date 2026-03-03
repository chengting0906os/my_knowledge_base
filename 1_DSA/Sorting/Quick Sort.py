import random
from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    left, mid, right = [], [], []
    pivot = random.choice(arr)

    for val in arr:
        if val < pivot:
            left.append(val)
        elif val == pivot:
            mid.append(val)
        else:
            right.append(val)

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    data = quick_sort(data)
    print("after: ", data)
