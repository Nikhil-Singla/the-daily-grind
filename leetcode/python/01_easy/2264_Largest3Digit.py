class Solution:
    # Changed to nums cuz I am used to that lol

    def largestGoodInteger(self, nums: str) -> str:
        maxStr = ""        
        window = 3
        last_term = len(nums) - 2
        i = 0

        while i < last_term:
            if nums[i] == nums[i+1]:
                if nums[i] == nums[i+2]:
                    maxStr = max(maxStr, nums[i:i+3])
                    i += 3
                else:
                    i += 2
            else:
                i += 1
                
        return maxStr