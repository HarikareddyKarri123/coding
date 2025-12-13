class Solution:
    def swapDiagonal(self, mat):
        n = len(mat)
        for i in range(n):
            mat[i][i], mat[i][n - i - 1] = mat[i][n - i - 1], mat[i][i]
        return mat


