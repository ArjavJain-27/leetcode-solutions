class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        points1 = []
        points2 = []

        # Store coordinates of all 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))

                if img2[r][c] == 1:
                    points2.append((r, c))

        # Count how many pairs have the same relative shift
        count = {}

        for r1, c1 in points1:
            for r2, c2 in points2:
                shift = (r1 - r2, c1 - c2)

                count[shift] = count.get(shift, 0) + 1

        # Maximum number of overlapping 1s
        return max(count.values(), default=0)