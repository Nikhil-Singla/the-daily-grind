class Solution:    
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mult = 1
        if n == 3:
            return math.prod(nums)
        
        nums.sort()
        three_biggest = math.prod(nums[-1:-4:-1])
        two_negative_and_largest = math.prod([nums[0], nums[-1], nums[1]])

        return max(three_biggest, two_negative_and_largest)
