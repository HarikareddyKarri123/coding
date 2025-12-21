import bisect

class Solution:
    def countXInRange(self, arr, queries):
        res = []
        for l, r, x in queries:
            # find first index >= x
            left = bisect.bisect_left(arr, x, l, r + 1)
            # find first index > x
            right = bisect.bisect_right(arr, x, l, r + 1)
            res.append(right - left)
        return res
