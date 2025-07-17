class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        maxLen = 0

        for i in nums:
            currentRemainder = i % k

            for previousRemainder in range(k):
                dp[previousRemainder][currentRemainder] = dp[currentRemainder][previousRemainder] + 1
                # The streak will alternate, as 1+2, and then 2+3. So 1 == 3. So the longest sequence
                # will go in this step from prevRemainder to currentRemainder, as a continuation from
                # one step before that, which was currentRemainder to previousRemainder. 

                # The subseq can be thought of as currRemainder -> prevRemainder -> currRemainder
                
                maxLen = max(maxLen, dp[previousRemainder][currentRemainder])

        return maxLen