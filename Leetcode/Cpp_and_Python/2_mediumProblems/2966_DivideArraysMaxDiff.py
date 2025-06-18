class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
            if abs(nums[i+2] - nums[i]) <= k:
                ans.append([nums[i], nums[i+1], nums[i+2]])
                i += 3
            else:
                return []
        
        return ans