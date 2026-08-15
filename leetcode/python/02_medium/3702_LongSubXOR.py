class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        result = 0
        has_non_zero = False

        for i in nums:
            if i != 0:
                has_non_zero = True

            result ^= i

        n = len(nums)

        if has_non_zero == False:
            return 0

        if result == 0:
            return n-1
        else:
            return n
