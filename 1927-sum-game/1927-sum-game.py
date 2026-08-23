class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0

        left_count = 0
        right_count = 0

        # Left half
        for i in range(half):
            if num[i] == '?':
                left_count += 1
            else:
                left_sum += int(num[i])

        # Right half
        for i in range(half, n):
            if num[i] == '?':
                right_count += 1
            else:
                right_sum += int(num[i])

        # Odd number of ? → Alice wins
        if (left_count + right_count) % 2 == 1:
            return True

        # Check whether Bob can make the sums equal
        if left_sum - right_sum == 9 * (right_count - left_count) // 2:
            return False

        return True