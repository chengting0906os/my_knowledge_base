from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == "__main__":
    heights = [7, 1, 7, 2, 2, 4]
    expected = 8

    ans = Solution().largestRectangleArea(heights)
    print(f"Input: heights = {heights}")
    print(f"Output: {ans}")
    print(f"Expected: {expected}")

    assert ans == expected, f"Expected {expected}, got {ans}"
    print("Test passed.")
