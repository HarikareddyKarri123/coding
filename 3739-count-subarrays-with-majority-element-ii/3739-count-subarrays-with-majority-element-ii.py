from typing import List

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = [0]
        curr = 0

        for x in nums:
            if x == target:
                curr += 1
            else:
                curr -= 1
            prefix.append(curr)

        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = Fenwick(len(vals))
        ans = 0

        for p in prefix:
            idx = rank[p]
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans