class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        
        best = [float('inf')] * n
        left = 0
        total = 0
        ans = float('inf')
        
        for right in range(n):
            total += arr[right]
            
            while total > target:
                total -= arr[left]
                left += 1
            
            if total == target:
                length = right - left + 1
                
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])
                
                best[right] = length
            
            if right > 0:
                best[right] = min(best[right], best[right - 1])
        
        return -1 if ans == float('inf') else ans