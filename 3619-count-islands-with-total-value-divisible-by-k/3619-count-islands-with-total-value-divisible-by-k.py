from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            total = grid[r][c]
            grid[r][c] = 0  # Mark as visited

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    total += dfs(nr, nc)

            return total

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = dfs(i, j)

                    if island_sum % k == 0:
                        count += 1

        return count