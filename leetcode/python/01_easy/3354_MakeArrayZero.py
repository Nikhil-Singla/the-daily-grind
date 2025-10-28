class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        totSum = sum(nums)
        leftSum = 0
        ans = 0
        for i in nums:
            if i == 0:
                rightSum = totSum-leftSum
                if leftSum == rightSum:
                    ans += 2
                elif abs(leftSum - rightSum) == 1:
                    ans += 1

            leftSum += i

        return ans
