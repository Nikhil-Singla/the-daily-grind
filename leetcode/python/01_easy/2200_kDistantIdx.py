class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        retVal = set()
        for j in range(n):
            if nums[j] == key:
                leftBound = max(0, j-k)
                rightBound = min(n, j+k+1)
                temp = set(range(leftBound, rightBound))
                retVal.update(temp)

        return list(retVal)