from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed):
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a + b].append(c)

        memo = set()

        def dfs(curr):
            if len(curr) == 1:
                return True
            if curr in memo:
                return False

            def build(i, next_row):
                if i == len(curr) - 1:
                    return dfs(next_row)
                key = curr[i] + curr[i + 1]
                if key not in mp:
                    return False
                for ch in mp[key]:
                    if build(i + 1, next_row + ch):
                        return True
                return False

            if not build(0, ""):
                memo.add(curr)
                return False
            return True

        return dfs(bottom)
