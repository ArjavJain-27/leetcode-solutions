from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(i, j):
            # Only one stone
            if i >= j:
                return 0

            ans = 0

            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    ans = max(ans, left + dp(i, k))

                elif left > right:
                    ans = max(ans, right + dp(k + 1, j))

                else:
                    ans = max(
                        ans,
                        left + dp(i, k),
                        right + dp(k + 1, j)
                    )

            return ans

        return dp(0, len(stoneValue) - 1)