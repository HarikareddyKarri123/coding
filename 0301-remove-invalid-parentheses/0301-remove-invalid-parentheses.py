class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(x):
            balance = 0

            for ch in x:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        queue = [s]
        seen = {s}

        while queue:
            valid = []

            for cur in queue:
                if is_valid(cur):
                    valid.append(cur)

            # If we found valid strings at this level,
            # they require the minimum removals.
            if valid:
                return valid

            next_level = []

            for cur in queue:
                for i in range(len(cur)):
                    if cur[i] not in "()":
                        continue

                    nxt = cur[:i] + cur[i + 1:]

                    if nxt not in seen:
                        seen.add(nxt)
                        next_level.append(nxt)

            queue = next_level

        return [""]