class Solution:
    def moveZeroes(self, nums):
        temp = []

        # Store non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        # Copy back
        for i in range(len(temp)):
            nums[i] = temp[i]

        # Fill remaining with zeros
        for i in range(len(temp), len(nums)):
            nums[i] = 0