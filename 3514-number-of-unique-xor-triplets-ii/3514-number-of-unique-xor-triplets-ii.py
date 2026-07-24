from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        values = list(set(nums))

        MAXX = 2048

        pair = [False] * MAXX

        # All possible XORs of two values
        for a in values:
            for b in values:
                pair[a ^ b] = True

        ans = [False] * MAXX

        # XOR with the third value
        for x in range(MAXX):
            if pair[x]:
                for v in values:
                    ans[x ^ v] = True

        return sum(ans)