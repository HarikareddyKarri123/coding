class Solution:
    def subarraySum(self, arr, s):
        n = len(arr)
        curr = 0
        left = 0
        
        for right in range(n):
            curr += arr[right]
            
            while curr > s and left <= right:
                curr -= arr[left]
                left += 1
            
            if curr == s:
                return [left + 1, right + 1]
        
        return [-1]
