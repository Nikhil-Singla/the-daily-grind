class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start, end = nums[0], nums[0]
        check = set(nums)
        for i in nums:
            if i < start:
                start = i
            if i > end:
                end = i

        ans = []
        for i in range(start+1, end):
            if i not in check:
                ans.append(i)

        return ans
