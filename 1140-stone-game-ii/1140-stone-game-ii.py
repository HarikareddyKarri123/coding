from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                next_M = max(M, X)

                # Stones current player can get
                current = suffix[i] - dp(i + X, next_M)

                best = max(best, current)

            return best

        return dp(0, 1)