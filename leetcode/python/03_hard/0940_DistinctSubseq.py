class Solution:
    def distinctSubseqII(self, s: str) -> int:
        alphabet_dp = [0] * 26
        count = 0

        MOD = 10**9 + 7
        n = len(s)

        for i in range(n):
            character = ord(s[i]) - ord('a')

            current = (count + 1) - alphabet_dp[character]
            
            alphabet_dp[character] += current % MOD

            count = (count + current) % MOD

        return count % MOD
