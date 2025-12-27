class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)

        low = mat[0][0]
        high = mat[n-1][n-1]

        while low < high:
            mid = (low + high) // 2
            count = 0
            j = n - 1

            for i in range(n):
                while j >= 0 and mat[i][j] > mid:
                    j -= 1
                count += (j + 1)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
