class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        
        # prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = mat[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
        
        def square_sum(x1, y1, k):
            x2, y2 = x1 + k, y1 + k
            return ps[x2][y2] - ps[x1][y2] - ps[x2][y1] + ps[x1][y1]
        
        lo, hi, ans = 1, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if square_sum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
