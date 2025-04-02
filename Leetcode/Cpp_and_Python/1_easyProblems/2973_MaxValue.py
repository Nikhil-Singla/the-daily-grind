class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxN = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    value = (nums[i] - nums[j]) 
                    if value < 0:
                        continue
                    maxN = max(maxN, value*nums[k])

                
        return maxN