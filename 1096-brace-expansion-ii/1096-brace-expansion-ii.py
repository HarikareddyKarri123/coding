class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def dfs(exp):
            j = exp.find('}')

            if j == -1:
                result.add(exp)
                return

            i = exp.rfind('{', 0, j)

            left = exp[:i]
            right = exp[j + 1:]

            for part in exp[i + 1:j].split(','):
                dfs(left + part + right)

        result = set()
        dfs(expression)

        return sorted(result)