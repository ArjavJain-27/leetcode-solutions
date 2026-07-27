class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix = 0
        mp = {0: 1}

        for num in nums:
            prefix += num

            rem = prefix % k

            if rem in mp:
                count += mp[rem]

            mp[rem] = mp.get(rem, 0) + 1

        return count