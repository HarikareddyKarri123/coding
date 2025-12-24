class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)

        # Find index of minimum element (pivot)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid

        pivot = low  # index of smallest element

        # Binary search helper
        def upper_bound(l, r):
            ans = l - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= x:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        # Count elements <= x in both sorted halves
        count = 0
        if pivot > 0:
            idx = upper_bound(0, pivot - 1)
            count += max(0, idx + 1)

        idx = upper_bound(pivot, n - 1)
        count += max(0, idx - pivot + 1)

        return count


        