class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        lar = nums[-1]
        sma = nums[-2]
        return (lar - 1) * (sma - 1)
        