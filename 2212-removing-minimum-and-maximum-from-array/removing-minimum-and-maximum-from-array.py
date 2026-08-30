class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = 0
        max_idx = 0

        # Find indices of minimum and maximum
        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i

            if nums[i] > nums[max_idx]:
                max_idx = i

        # Make min_idx the smaller index
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 3 possibilities:
        # 1. Both from front
        from_front = right + 1

        # 2. Both from back
        from_back = n - left

        # 3. One from each side
        from_both = (left + 1) + (n - right)

        return min(from_front, from_back, from_both)