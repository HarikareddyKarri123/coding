class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        curr_xor = 0
        for i in range(k):
            curr_xor ^= arr[i]

        max_xor = curr_xor

        for i in range(k, n):
            curr_xor ^= arr[i]      # add new element
            curr_xor ^= arr[i - k]  # remove element leaving window
            max_xor = max(max_xor, curr_xor)

        return max_xor

        
       