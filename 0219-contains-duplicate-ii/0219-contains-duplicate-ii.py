class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last = {}
        for i, v in enumerate(nums):
            if v in last and i - last[v] <= k:
                return True
            last[v] = i
        return False
