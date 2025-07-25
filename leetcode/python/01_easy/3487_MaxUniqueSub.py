class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        retVal = 0

        for i in nums[:-1]:
            if i > 0 and i not in seen:
                seen.add(i)
                retVal += i

        if nums[-1] not in seen:
            retVal += nums[-1]

        return retVal