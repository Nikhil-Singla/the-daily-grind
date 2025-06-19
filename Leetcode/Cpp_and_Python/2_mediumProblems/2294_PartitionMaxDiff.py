class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 0
        ans = 1 

        for i in range(0, len(nums)):
            if nums[right] - nums[left] > k:                
                ans += 1
                left = right

            right += 1

        return ans