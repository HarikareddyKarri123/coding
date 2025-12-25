class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                curr = mat[i][j]

                top = mat[i-1][j] if i > 0 else float('-inf')
                bottom = mat[i+1][j] if i < n-1 else float('-inf')
                left = mat[i][j-1] if j > 0 else float('-inf')
                right = mat[i][j+1] if j < m-1 else float('-inf')

                if curr >= top and curr >= bottom and curr >= left and curr >= right:
                    return [i, j]
