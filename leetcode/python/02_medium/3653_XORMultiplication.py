class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        for l, r, k ,v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i]*v) % mod

        ret = nums[0]
        for i in nums[1:]:
            ret ^= i

        return ret
