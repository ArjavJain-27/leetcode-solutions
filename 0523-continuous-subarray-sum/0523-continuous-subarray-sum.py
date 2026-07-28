class Solution:
    def checkSubarraySum(self, nums, k):
        prefix = 0
        hashmap = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k

            if remainder in hashmap:
                if i - hashmap[remainder] > 1:
                    return True
            else:
                hashmap[remainder] = i

        return False