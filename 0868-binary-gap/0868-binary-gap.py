class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_index = -1
        index = 0
        
        while n > 0:
            if n & 1:   # if current bit is 1
                if last_index != -1:
                    max_gap = max(max_gap, index - last_index)
                last_index = index
            n >>= 1
            index += 1
        
        return max_gap