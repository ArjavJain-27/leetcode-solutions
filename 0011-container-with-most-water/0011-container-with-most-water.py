class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:

            width = right - left

            h = min(height[left], height[right])

            area = width * h

            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans