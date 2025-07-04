class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1e9 + 7
        dp = [1, 1, 2, 5]  # For first n digits, starting from 0
        for i in range(4, n+1):
            if len(dp) >= n+1:
                return dp[n]
            
            vertBF = dp[i-1] * 2  # Either adding one vert, or replacing last two with horizontals.
            tromSum = dp[i-3]  # Trom replacement to set of last 2
            latestAns = float(tromSum + vertBF) % mod  # Mod value added.
            dp.append(latestAns)
        
        return int(dp[n])  # Solution shouldn't have ".0" in answer.
