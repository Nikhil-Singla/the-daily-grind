class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        # Mod sum with remainders = 0, 1 and 2
        dp = [0, 0, 0]

        for one_element in nums:

            for modular_sum in dp[:]:
                updated_modular_sum = one_element + modular_sum
                dp[(updated_modular_sum) % 3] = max(dp[(updated_modular_sum) % 3], updated_modular_sum)

        return dp[0]
