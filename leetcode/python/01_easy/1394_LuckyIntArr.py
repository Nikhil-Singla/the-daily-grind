class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * 500

        for i in arr:
            freq[i-1] += 1

        retVal = -1
        for idx, i in enumerate(freq):
            if idx == i-1:
                retVal = i

        return retVal