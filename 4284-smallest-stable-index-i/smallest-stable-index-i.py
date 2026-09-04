class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix minimum
        suffix_min = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # prefix maximum + check
        prefix_max = float("-inf")

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1