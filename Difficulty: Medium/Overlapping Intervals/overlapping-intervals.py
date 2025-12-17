class Solution:
    def mergeOverlap(self, arr):
        if not arr:
            return []

        # Sort intervals by start time
        arr.sort(key=lambda x: x[0])

        merged = []
        start, end = arr[0]

        for i in range(1, len(arr)):
            curr_start, curr_end = arr[i]

            if curr_start <= end:
                end = max(end, curr_end)
            else:
                merged.append([start, end])
                start, end = curr_start, curr_end

        merged.append([start, end])
        return merged

