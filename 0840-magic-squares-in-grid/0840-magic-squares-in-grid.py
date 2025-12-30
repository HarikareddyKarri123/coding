class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        def isMagic(r, c):
            # Center must be 5
            if grid[r+1][c+1] != 5:
                return False

            # Collect all 9 numbers
            nums = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r+i][c+j]
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)

            if len(nums) != 9:
                return False

            # Check rows and columns
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != 15:
                    return False
                if sum(grid[r+k][c+i] for k in range(3)) != 15:
                    return False

            # Check diagonals
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False

            return True

        # Check all 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count
