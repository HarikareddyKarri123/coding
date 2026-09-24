class Solution:
    def smallestIndex(self, nums):
        for i, x in enumerate(nums):
            digit_sum = 0

            while x > 0:
                digit_sum += x % 10
                x //= 10

            if digit_sum == i:
                return i

        return -1