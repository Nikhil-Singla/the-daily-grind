class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        for i in range(k, 101+k, k):
            if i not in nums:
                return i

        return -1
