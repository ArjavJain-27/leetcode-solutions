class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        i = 1
        while True:
            multiple = k * i

            if multiple not in nums_set:
                return multiple

            i += 1