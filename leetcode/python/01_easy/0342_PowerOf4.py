class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        if n.bit_count() != 1:
            return False

        for i in range(32):
            mask = 1 << i
            if mask & n:
                if i % 2 == 0:
                    return True
                else:
                    return False

        return False
