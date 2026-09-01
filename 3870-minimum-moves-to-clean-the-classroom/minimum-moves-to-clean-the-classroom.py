from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        # Store start position and give every litter
        # a unique bit index.
        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        # No litter
        if k == 0:
            return 0

        # All litter collected
        target = (1 << k) - 1

        # state = (row, col, energy, mask, moves)
        queue = deque()
        queue.append((sr, sc, energy, 0, 0))

        # visited = (row, col, energy, mask)
        visited = set()
        visited.add((sr, sc, energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, curr_energy, mask, moves = queue.popleft()

            # All litter collected
            if mask == target:
                return moves

            # Cannot move without energy
            if curr_energy == 0:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving normally costs 1 energy
                new_energy = curr_energy - 1

                # Reset area restores energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Copy current mask
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)

                    queue.append(
                        (nr, nc, new_energy, new_mask, moves + 1)
                    )

        return -1