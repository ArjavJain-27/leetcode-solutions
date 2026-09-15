class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[l][r] = True if s[l:r+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        # Build palindrome DP
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length == 2:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]

        # best[i] = maximum palindromes using s[0:i]
        best = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't choose a palindrome ending at i-1
            best[i] = best[i - 1]

            # Try every palindrome ending at i-1
            for l in range(i):
                if i - l >= k and dp[l][i - 1]:
                    best[i] = max(best[i], best[l] + 1)

        return best[n]