class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            # Start a new subarray with this number
            new_dp[r] += 1

            # Extend previous subarrays
            for old_r in range(k):
                new_r = (old_r * r) % k
                new_dp[new_r] += dp[old_r]

            # Add all subarrays ending here to the answer
            for x in range(k):
                ans[x] += new_dp[x]

            dp = new_dp

        return ans