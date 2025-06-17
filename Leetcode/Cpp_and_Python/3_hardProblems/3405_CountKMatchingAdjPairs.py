class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:        
        MOD = 10**9 + 7

        totalPairs = n-1
        totalNonEqualPairs = n-1-k
        totalEqualPairs = k

        numberOfAdjPairs = math.comb(totalPairs, totalEqualPairs) 
        # Out of n-1 pairs, k of them MUST be the same.

        optionsForFirstElement = m
        totalAdjacentChances = m*numberOfAdjPairs % MOD
        # For the adjacent chances, the very first one can be anything in the range of 1-m

        optionsForRemainingElements = m-1
        # The remaining elements i will just need to not be the element i-1 to prevent
        # Another pair. So it will be any element except the i-1th element.

        totalRemainingChances = pow(optionsForRemainingElements, totalNonEqualPairs, MOD)
        # For the remaining n-k-1 non equal pairs, the value varies upto m-1 times
        # That is, not the i-1th value for the index i to prevent adjacent pairs.

        return int(totalAdjacentChances * totalRemainingChances % MOD)