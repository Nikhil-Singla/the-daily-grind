class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Looped variant
        if n <=0 :
            return False

        while n > 1:
            if n%3 == 0: n //= 3
            else: return False

        return n == 1        

        # Alternate no loop solution, is slower
        # Calculate biggest power of 3 in range, and then do the divisibility test.
        # It works as 3^19 is only divisible by other powers of 3.
        return 1162261467 % n == 0
