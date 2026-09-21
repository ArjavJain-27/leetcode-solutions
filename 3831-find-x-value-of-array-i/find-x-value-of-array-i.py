class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            mod = num % k

            # Start a new subarray with only num
            new_dp[mod] += 1

            # Extend previous subarrays
            for r in range(k):
                new_r = (r * mod) % k
                new_dp[new_r] += dp[r]

            # Add current subarrays to answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans