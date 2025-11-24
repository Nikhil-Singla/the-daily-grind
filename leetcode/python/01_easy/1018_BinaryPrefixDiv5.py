class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ongoing_sum = 0
        ans = []

        for i in nums:
            ongoing_sum <<= 1
            ongoing_sum += i

            if (ongoing_sum/5).is_integer():
                ans.append(True)
            else:
                ans.append(False)
                
            ongoing_sum %= 5

        return ans
