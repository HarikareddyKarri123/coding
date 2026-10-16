class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, l, r):
            d = lazy[node]
            if d == 0:
                return

            length = r - l + 1
            tree_sq[node] = (
                tree_sq[node] + 2 * d * tree_sum[node]
                + length * d * d
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + length * d
            ) % MOD

            if l != r:
                lazy[node * 2] += d
                lazy[node * 2 + 1] += d

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            push(node, l, r)

            if qr < l or r < ql:
                return

            if ql <= l and r <= qr:
                d = 1
                length = r - l + 1

                tree_sq[node] = (
                    tree_sq[node] + 2 * d * tree_sum[node]
                    + length * d * d
                ) % MOD

                tree_sum[node] = (
                    tree_sum[node] + length * d
                ) % MOD

                if l != r:
                    lazy[node * 2] += d
                    lazy[node * 2 + 1] += d

                return

            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + tree_sq[1]) % MOD
            last[x] = i

        return ans