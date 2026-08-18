from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter(nums)

        # Case 1: k == 1
        # Every element is its own subarray.
        if k == 1:
            ans = -1

            for x in nums:
                if count[x] == 1:
                    ans = max(ans, x)

            return ans

        # Case 2: k == n
        # There is only one subarray: the whole array.
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n
        ans = -1

        # Only first and last elements can occur
        # in exactly one window.
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans