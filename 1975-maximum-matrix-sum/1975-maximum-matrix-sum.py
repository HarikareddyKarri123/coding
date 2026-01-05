from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negatives = 0
        min_abs = float('inf')

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    negatives += 1
                min_abs = min(min_abs, abs(val))

        if negatives % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
