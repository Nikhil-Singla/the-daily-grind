import math
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        root = complexity[0]
        MOD = 10**9 + 7
        ans = 1
        n = len(complexity)

        for idx, i in enumerate(complexity[1:]):
            if i <= root:
                return 0

        for i in range(2, n):
            ans = (ans*i) % MOD

        return ans
