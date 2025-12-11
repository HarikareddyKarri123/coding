class Solution:
    def titleToNumber(self, columnTitle):
        res = 0
        for ch in columnTitle:
            res = res * 26 + (ord(ch) - 64)
        return res
