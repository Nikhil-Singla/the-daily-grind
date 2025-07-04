class Solution:
    def findLHS(self, nums: List[int]) -> int:

        freq = Counter(nums)
        integers = freq.keys()
        retVal = 0

        for i in integers:
            if i-1 in integers:
                retVal = max(retVal, freq[i] + freq[i-1])

            if i+1 in integers:
                retVal = max(retVal, freq[i] + freq[i+1])

        return retVal
