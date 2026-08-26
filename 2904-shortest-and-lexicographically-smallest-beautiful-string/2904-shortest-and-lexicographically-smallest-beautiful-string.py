from typing import List

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        left = 0
        ones = 0
        answer = ""

        for right in range(len(s)):

            if s[right] == '1':
                ones += 1

            # Too many 1s
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove unnecessary zeros from the left
            while ones == k and s[left] == '0':
                left += 1

            # We have exactly k ones
            if ones == k:
                current = s[left:right + 1]

                if answer == "":
                    answer = current

                elif len(current) < len(answer):
                    answer = current

                elif len(current) == len(answer) and current < answer:
                    answer = current

        return answer