from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        print("=" * 60)
        print(f"nums: {nums}")
        print(f"total: {total}")

        if total % 2 != 0:
            print("Total is odd, cannot partition equally")
            return False

        target = total // 2
        n = len(nums)
        print(f"target: {target} (half of {total})")
        print(f"n: {n} elements")
        print("=" * 60)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base case
        print("\n[BASE CASE] dp[i][0] = True for all i")
        print("  Reason: Empty subset always sums to 0\n")
        for i in range(n + 1):
            dp[i][0] = True

        print("Initial DP table:")
        self.print_dp(dp, nums, target)

        for i in range(1, n + 1):
            print(f"\n{'='*60}")
            print(f"STEP {i}: Considering nums[{i-1}] = {nums[i-1]}")
            print(f"  Items available so far: {nums[:i]}")
            print("=" * 60)

            for j in range(1, target + 1):
                print(f"\n  Target sum j={j}:")

                if nums[i - 1] <= j:
                    skip = dp[i - 1][j]
                    take = dp[i - 1][j - nums[i - 1]]
                    dp[i][j] = skip or take

                    print(f"    nums[{i-1}]={nums[i-1]} <= {j}, we have 2 choices:")
                    print(f"    Option 1 - SKIP {nums[i-1]}:")
                    print(f"      dp[{i-1}][{j}] = {skip}")
                    print(f"      (Can we make {j} without {nums[i-1]}?)")
                    print(f"    Option 2 - TAKE {nums[i-1]}:")
                    print(f"      dp[{i-1}][{j - nums[i-1]}] = {take}")
                    print(f"      (Take {nums[i-1]}, need remaining {j}-{nums[i-1]}={j - nums[i-1]})")
                    print(f"    --> dp[{i}][{j}] = {skip} OR {take} = {dp[i][j]}")
                else:
                    dp[i][j] = dp[i - 1][j]
                    print(f"    nums[{i-1}]={nums[i-1]} > {j}, too big to take")
                    print(f"    --> dp[{i}][{j}] = dp[{i-1}][{j}] = {dp[i][j]}")

            print(f"\nDP table after processing {nums[i-1]}:")
            self.print_dp(dp, nums, target)

        print(f"\n{'='*60}")
        print("FINAL RESULT")
        print("=" * 60)
        print(f"dp[{n}][{target}] = {dp[n][target]}")
        if dp[n][target]:
            print(f"YES! Can partition {nums} into two subsets with sum {target}")
        else:
            print(f"NO! Cannot partition {nums} into equal subsets")

        return dp[n][target]

    def print_dp(self, dp, nums, target):
        header = "      " + "".join(f"{j:^5}" for j in range(target + 1))
        print(header)
        print("      " + "-" * (5 * (target + 1)))

        for i, row in enumerate(dp):
            label = f"[{nums[i-1]:>2}]" if i > 0 else "[ 0]"
            row_str = f"{label} |" + "".join(
                f"{'T':^5}" if v else f"{'·':^5}" for v in row
            )
            print(row_str)


# Test with smaller example
if __name__ == "__main__":
    sol = Solution()
    sol.canPartition([1, 5, 11, 5])
