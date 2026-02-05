class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            curr = nums[i]
            
            if curr == 0:
                continue
            else:
                moved_idx = i + curr
                while(moved_idx < 0):
                    moved_idx += n
                moved_idx = moved_idx % n
                ans[i] = nums[moved_idx]

        return ans
