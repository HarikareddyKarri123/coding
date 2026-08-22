class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        for digit in str(n):
            digit = int(digit)

            digit_sum += digit
            digit_product *= digit

        total = digit_sum + digit_product

        return n % total == 0