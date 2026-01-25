class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        retVal = float('inf')

        while((k+count) <= n):
            window = nums[count:k+count]

            diff = window[-1] - window[0]
            retVal = min(retVal, diff)
            count +=1
            
            ## print(window, diff)

        return retVal 
