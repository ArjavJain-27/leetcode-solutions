from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:
        comp = [0] * n
        group = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group += 1
            comp[i] = group

        return [comp[u] == comp[v] for u, v in queries]