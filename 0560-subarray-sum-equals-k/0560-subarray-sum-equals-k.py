class Solution:
    def subarraySum(self, nums, k):
        prefix = 0
        count = 0

        mp = {0: 1}

        for num in nums:

            prefix += num

            if prefix - k in mp:
                count += mp[prefix - k]

            mp[prefix] = mp.get(prefix, 0) + 1

        return count