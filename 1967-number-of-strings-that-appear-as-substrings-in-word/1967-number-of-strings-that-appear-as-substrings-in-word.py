class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        output = 0
        for s in patterns:
            if s in word:
                output += 1
        return output
