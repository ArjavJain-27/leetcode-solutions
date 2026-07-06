class Solution:
    def leftRightDifference(self, nums):
        total = sum(nums)
        left = 0
        ans = []

        for num in nums:
            right = total - left - num
            ans.append(abs(left - right))
            left += num

        return ans