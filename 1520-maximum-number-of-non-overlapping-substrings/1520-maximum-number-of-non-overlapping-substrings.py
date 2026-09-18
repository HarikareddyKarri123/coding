class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []

        for c in first:
            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                ch = s[i]

                if first[ch] < l:
                    valid = False
                    break

                r = max(r, last[ch])
                i += 1

            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans