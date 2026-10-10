class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(d - mid, 0) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        remaining = k

        for i in range(len(diff)):
            remaining -= max(0, diff[i] - left)
            diff[i] = min(diff[i], left)

        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == left:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)