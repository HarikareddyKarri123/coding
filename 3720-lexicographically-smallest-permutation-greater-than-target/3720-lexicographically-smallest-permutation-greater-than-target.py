from typing import List

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        answer = []

        for i in range(len(target)):

            t = ord(target[i]) - ord('a')

            # Try to use the same character
            if count[t] > 0:

                answer.append(target[i])
                count[t] -= 1

            else:
                # Find the smallest character bigger than target[i]
                bigger = -1

                for c in range(t + 1, 26):
                    if count[c] > 0:
                        bigger = c
                        break

                if bigger != -1:

                    answer.append(chr(bigger + ord('a')))
                    count[bigger] -= 1

                    # Put remaining characters in sorted order
                    for c in range(26):
                        answer.append(chr(c + ord('a')) * count[c])

                    return ''.join(answer)

                # Can't make answer greater here.
                # We need to backtrack.
                break

        # If we reached here, we may need to backtrack.
        answer = []

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for i in range(len(target) - 1, -1, -1):

            # Put target[0:i] if possible
            temp = count[:]

            possible = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if temp[c] == 0:
                    possible = False
                    break

                temp[c] -= 1

            if not possible:
                continue

            t = ord(target[i]) - ord('a')

            # Find a character bigger than target[i]
            for c in range(t + 1, 26):

                if temp[c] > 0:

                    result = target[:i]
                    result += chr(c + ord('a'))

                    temp[c] -= 1

                    # Add remaining characters smallest first
                    for x in range(26):
                        result += chr(x + ord('a')) * temp[x]

                    return result

        return ""