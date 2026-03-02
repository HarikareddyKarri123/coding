class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Handle negative numbers (32-bit two's complement)
        num &= 0xffffffff
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        while num > 0:
            digit = num & 15        # last 4 bits
            result = hex_chars[digit] + result
            num >>= 4               # shift 4 bits
        
        return result 