class Solution:
    def smallerNumbersThanCurrent(self, nums):

        ans = []

        for i in range(len(nums)):

            count = 0

            for j in range(len(nums)):

                if nums[j] < nums[i]:
                    count += 1

            ans.append(count)

        return ans