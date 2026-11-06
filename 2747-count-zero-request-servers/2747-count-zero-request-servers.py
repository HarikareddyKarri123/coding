from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)

        count = defaultdict(int)
        left = 0
        right = 0

        for q, idx in sorted_queries:
            start = q - x

            # Add logs inside the right boundary
            while right < len(logs) and logs[right][1] <= q:
                count[logs[right][0]] += 1
                right += 1

            # Remove logs outside the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            result[idx] = n - len(count)

        return result
        