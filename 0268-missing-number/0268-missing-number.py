class Solution:
    def missingNumber(self, nums):
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res
    