from typing import List


class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # (value, original index)
        arr = sorted((value, index) for index, value in enumerate(nums))

        ans = [0] * n

        i = 0

        while i < n:

            # Find the current group
            j = i + 1

            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Get original indices of this group
            indices = sorted(index for _, index in arr[i:j])

            # Smallest values go to smallest original indices
            for k, index in enumerate(indices):
                ans[index] = arr[i + k][0]

            i = j

        return ans