class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        
        seen_remainders = set([1])
        start = 1
        length = 1

        while (start != 0):
            start *= 10
            start += 1
            length += 1
            start %= k

            if start in seen_remainders:
                return -1

            seen_remainders.add(start)

        return length
