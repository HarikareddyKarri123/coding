from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        # Store (value, original index)
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # Sort by value
        arr.sort()

        groups = []
        current = []

        for i in range(n):

            if i == 0 or arr[i][0] - arr[i - 1][0] <= limit:
                current.append(arr[i])
            else:
                groups.append(current)
                current = [arr[i]]

        groups.append(current)

        # Put smallest values in smallest indices
        for group in groups:

            values = []
            indices = []

            for value, index in group:
                values.append(value)
                indices.append(index)

            indices.sort()

            for i in range(len(group)):
                nums[indices[i]] = values[i]

        return nums