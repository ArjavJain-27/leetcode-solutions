class Solution:
    def longestSubsequence(self, nums):
        xor = 0
        zeros = 0

        for x in nums:
            xor ^= x
            if x == 0:
                zeros += 1

        n = len(nums)

        if xor != 0:
            return n

        if zeros == n:
            return 0

        return n - 1