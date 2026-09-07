class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of distinct subsequences ending with character i
        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # All previous subsequences + current character itself
            dp[i] = (sum(dp) + 1) % MOD

        return sum(dp) % MOD