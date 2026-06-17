class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = cur * 2

            else:  # %
                lengths[i + 1] = cur

        final_len = lengths[n]

        if k >= final_len:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            curr_len = lengths[i + 1]
            prev_len = lengths[i]

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                k %= prev_len

            else:  # %
                k = curr_len - 1 - k

        return '.'