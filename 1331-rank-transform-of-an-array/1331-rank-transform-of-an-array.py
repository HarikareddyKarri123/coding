from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Sort the unique elements
        sorted_arr = sorted(set(arr))

        # Store rank of each element
        rank = {}

        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1

        # Replace each element with its rank
        ans = []

        for num in arr:
            ans.append(rank[num])

        return ans
        