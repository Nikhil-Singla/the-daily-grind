class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        ongoing = 0

        for idx, i in enumerate(nums):
            ongoing += (idx*i)
        
        ret = ongoing

        for i in range(1, n):
            ongoing = ongoing + total - (n * (nums[n-i]) )
            ret = max(ret, ongoing)

        return ret
