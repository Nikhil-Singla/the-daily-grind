class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            ret = -1
            pos = 1
            while(nums[i] & pos) != 0:
                ret = nums[i] - pos
                pos <<= 1

            nums[i] = ret

        return nums
