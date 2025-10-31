class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = [0] * len(nums)
        ans = []
        for i in nums:
            if seen[i]:
                ans.append(i)
            
            seen[i] = 1

        return ans

# Bits solution
# class Solution:
#     def getSneakyNumbers(self, nums: List[int]) -> List[int]:
#         bits = 0
#         ans = []
#         for i in nums:
#             if bits & (1 << i) != 0: 
#                 ans.append(i)
            
#             bits |= 1 << i

#         return ans
