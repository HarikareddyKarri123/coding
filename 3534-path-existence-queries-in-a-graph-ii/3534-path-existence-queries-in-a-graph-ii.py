from typing import List
from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        vals = [v for v, _ in arr]

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(vals, vals[i] + maxDiff) - 1

        LOG = 18

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            if a == b:
                ans.append(0)
                continue

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans