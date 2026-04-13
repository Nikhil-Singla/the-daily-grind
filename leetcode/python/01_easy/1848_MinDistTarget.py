class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ret = 10**5
        for i in range(n):
            if nums[i] == target:
                ret = min(abs(i-start), ret)

        return ret
