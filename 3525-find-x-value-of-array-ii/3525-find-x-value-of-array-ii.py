class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node stores:
        # prod = product of the whole segment % k
        # cnt[r] = number of prefixes whose product % k == r
        tree = [(1, [0] * k) for _ in range(4 * n)]

        def merge(left, right):
            lp, lc = left
            rp, rc = right

            prod = (lp * rp) % k
            cnt = lc[:]

            for r in range(k):
                cnt[(lp * r) % k] += rc[r]

            return prod, cnt

        def build(node, l, r):
            if l == r:
                x = nums[l] % k
                cnt = [0] * k
                cnt[x] = 1
                tree[node] = (x, cnt)
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, pos, value):
            if l == r:
                value %= k
                cnt = [0] * k
                cnt[value] = 1
                tree[node] = (value, cnt)
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans