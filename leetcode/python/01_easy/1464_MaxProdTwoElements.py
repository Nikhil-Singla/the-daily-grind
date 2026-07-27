class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        # nums[i] is always > 0, so no need to worry about negative cases.
        low, hi = nums[-2], nums[-1]

        return (low-1)*(hi-1)
