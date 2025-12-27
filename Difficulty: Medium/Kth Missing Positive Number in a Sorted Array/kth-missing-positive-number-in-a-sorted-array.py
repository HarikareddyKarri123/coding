class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)

        # If kth missing is before the first element
        if arr[0] > k:
            return k

        # Binary search
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        # kth missing number
        return k + high + 1
