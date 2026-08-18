from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: Subarray size is 1
        if k == 1:
            counts = Counter(nums)
            valid = [num for num, count in counts.items() if count == 1]
            return max(valid) if valid else -1
            
        # Case 2: Subarray size equals array size
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n
        # Only the first and last elements can ever appear in exactly one subarray.
        first_element = nums[0]
        last_element = nums[-1]
        
        first_count = nums.count(first_element)
        last_count = nums.count(last_element)
        
        ans = -1
        if first_count == 1:
            ans = max(ans, first_element)
        if last_count == 1:
            ans = max(ans, last_element)
            
        return ans
