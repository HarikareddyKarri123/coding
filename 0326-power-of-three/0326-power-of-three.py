class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3^19 = 1162261467 is the largest power of 3 within 32-bit signed int
        return n > 0 and 1162261467 % n == 0
