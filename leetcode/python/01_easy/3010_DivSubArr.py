class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        lowest = heapq.nsmallest(2, nums[1:])
        lowest.extend([nums[0]])

        return sum(lowest)
