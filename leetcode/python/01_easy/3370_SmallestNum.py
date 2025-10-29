class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return n

        start = 1
        # times = n.bit_length()

        times = 0
        while (n > start):
            start *= 2
            times += 1


        for i in range(times):
            shifted = 1 << i
            n |= shifted

        return n
