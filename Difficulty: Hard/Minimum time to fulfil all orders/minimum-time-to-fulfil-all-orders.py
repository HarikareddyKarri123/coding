class Solution:
    def minTime(self, rank, n):
        low = 0
        high = min(rank) * n * (n + 1) // 2

        while low < high:
            mid = (low + high) // 2
            donuts = 0

            for r in rank:
                time = r
                cnt = 0
                while time <= mid:
                    cnt += 1
                    time += r * (cnt + 1)
                donuts += cnt

                if donuts >= n:   # 🔥 early break (optimization)
                    break

            if donuts >= n:
                high = mid
            else:
                low = mid + 1

        return low

