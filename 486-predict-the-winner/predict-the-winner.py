from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dp(left, right):
            if left == right:
                return nums[left]

            take_left = nums[left] - dp(left + 1, right)
            take_right = nums[right] - dp(left, right - 1)

            return max(take_left, take_right)

        return dp(0, len(nums) - 1) >= 0