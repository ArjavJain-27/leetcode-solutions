class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)

        s = set(nums)

        ans = []

        for i in range(small, large + 1):
            if i not in s:
                ans.append(i)

        return ans