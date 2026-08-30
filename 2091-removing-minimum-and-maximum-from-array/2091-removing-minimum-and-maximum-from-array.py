from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        # Find position of smallest number
        small = nums.index(min(nums))

        # Find position of largest number
        large = nums.index(max(nums))

        # Make sure small comes before large
        if small > large:
            small, large = large, small

        # Option 1: Remove both from the left
        left = large + 1

        # Option 2: Remove both from the right
        right = n - small

        # Option 3: Remove small from left and large from right
        both = (small + 1) + (n - large)

        return min(left, right, both)