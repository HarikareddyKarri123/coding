from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        # Prefix sum
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        # Start with total sum
        best = stones[-1]

        # Work backwards
        for i in range(len(stones) - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best
        