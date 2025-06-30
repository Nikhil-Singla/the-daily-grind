class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        retVal = 0

        for i in nums:
            if freq[i+1]:
                s1 = freq[i+1] + freq[i]
            else:
                s1 = 0

            if freq[i-1]:
                s2 = freq[i-1] + freq[i]
            else:
                s2 = 0

            retVal = max(retVal, s1, s2)

        return retVal
