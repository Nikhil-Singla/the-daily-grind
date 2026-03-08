class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numbers = set([int(i,2) for i in nums])

        n = len(nums)
        for i in range(n+1):
            if i not in numbers:
                return bin(i)[2:].zfill(n)

        return ""