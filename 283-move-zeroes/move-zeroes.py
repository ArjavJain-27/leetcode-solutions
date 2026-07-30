class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1