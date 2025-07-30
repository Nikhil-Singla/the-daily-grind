class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mbit = nums[0]
        mcount = 0
        count = 0

        for i in nums:
            if i > mbit:
                mbit = i
                count = 1
                mcount = 1
            elif i == mbit:
                count += 1
            else:
                count = 0
                
            if count > mcount:
                mcount = count

        return mcount
