class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        x = n
        while True:
            # Calculate product of digits of x
            product = 1
            temp = x
            
            # Handle the specific case where x itself is 0
            if temp == 0:
                product = 0
                
            while temp > 0:
                product *= temp % 10
                temp //= 10
                
            # Check if the product is divisible by t
            if product % t == 0:
                return x
            
            x += 1
