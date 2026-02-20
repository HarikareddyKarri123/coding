class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Step 1: count frequency
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Step 2: find first unique character index
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1   