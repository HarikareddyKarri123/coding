class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits to number
        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))

            # 4. Clamp to 32-bit range
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 - 1:
                return 2**31 - 1

            i += 1

        return sign * num
