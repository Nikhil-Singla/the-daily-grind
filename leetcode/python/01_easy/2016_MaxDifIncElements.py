class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDif = -1
        currentMin = nums[0]

        for i in nums[1:]:
            if i < currentMin:
                currentMin = i
            elif i > currentMin:
                maxDif = max(maxDif, i-currentMin)

        return maxDif