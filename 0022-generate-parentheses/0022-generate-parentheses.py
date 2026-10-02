class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(s, open_count, close_count):
            if open_count == n and close_count == n:
                ans.append(s)
                return

            # We can add '(' if we still have some left
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # We can add ')' only when there is an unmatched '('
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return ans