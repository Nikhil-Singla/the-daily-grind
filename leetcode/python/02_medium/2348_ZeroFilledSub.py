class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        counter = 0

        for i in nums:
            if i != 0:
                ans += (counter * (counter+1))//2
                counter = 0
            else:
                counter += 1

        if counter:
            ans += (counter * (counter+1))//2
            
        return ans
