class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])

        maxD = 0

        for i in range(1, len(nums)):
            D = abs(nums[i-1] - nums[i])
            maxD = max(maxD, D)

        return maxD