class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxBitwise = 0
        for i in nums:
            maxBitwise |= i
        
        nums.sort()
        count = 0

        def helper(array, index, ongoingOR, maxOR):
            if index == len(nums):
                return 1 if ongoingOR == maxOR else 0

            if ongoingOR == maxOR:
                remainingElements = len(nums) - (index)
                # Doesn't matter if you do or don't pick all the remaining elements, 
                # so we need to count both cases!
                permutations = math.pow(2, remainingElements)
                return permutations

            countingElement = helper(array, index+1, ongoingOR|array[index], maxOR)
            notCountingElement = helper(array, index+1, ongoingOR, maxOR)

            return countingElement + notCountingElement

        return int(helper(nums, 0, 0, maxBitwise))