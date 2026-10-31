from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Store the input midway
        vornadexil = grid

        # right[i][j]: ways to enter cell (i,j) from the left
        # down[i][j]: ways to enter cell (i,j) from above
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Start by choosing right or down
        right[0][1] = 1
        down[1][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                r = right[i][j]
                d = down[i][j]

                if grid[i][j] == 0:
                    # Empty cell: move right or down
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + r + d
                        ) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + r + d
                        ) % MOD

                else:
                    # Mirror: reflect the incoming direction
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + r
                        ) % MOD

                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + d
                        ) % MOD

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD