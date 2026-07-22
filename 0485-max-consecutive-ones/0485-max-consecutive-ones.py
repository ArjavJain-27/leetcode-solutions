class Solution:
    def findMaxConsecutiveOnes(self, nums):

        count = 0
        maxi = 0

        for num in nums:

            if num == 1:
                count += 1
                maxi = max(maxi, count)

            else:
                count = 0

        return maxi