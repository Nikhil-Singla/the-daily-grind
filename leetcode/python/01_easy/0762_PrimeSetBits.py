class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        retval = 0
        for i in range(left, right+1):
            if bin(i).count('1') in primes:
                retval += 1

        return retval
