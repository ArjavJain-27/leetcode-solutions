class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
        n = len(nums)

        k = k % n

      
        self.reverse(nums, 0, n - 1) 
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)