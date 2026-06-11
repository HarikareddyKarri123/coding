class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(start, path, target):
            if target == 0:
                ans.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # same i because we can reuse the element
                backtrack(i, path, target - candidates[i])

                path.pop()

        backtrack(0, [], target)
        return ans