class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Convert stones into prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # If all stones are taken, this is the score difference
        best = stones[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best