class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k = -1

        for i, num in enumerate(nums):
            if num != i:
                k &= num

        return max(k, 0)