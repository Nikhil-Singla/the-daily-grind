class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        retVal = float('inf')

        while((k+count-1) < n):
            diff = nums[k+count-1] - nums[count]
            retVal = min(retVal, diff)
            count +=1
            
            ## print(window, diff)

        return retVal 
