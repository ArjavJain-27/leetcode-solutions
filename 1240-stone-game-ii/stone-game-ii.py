class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        dp = {}

        def solve(i, M):
            # No piles left
            if i == n:
                return 0

            # Can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                opponent = solve(i + X, max(M, X))

                # Remaining total - opponent's best
                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return solve(0, 1)