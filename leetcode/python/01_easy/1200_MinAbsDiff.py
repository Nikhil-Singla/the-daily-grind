class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        pairs = []
        minDiff = float('inf')

        for i in range(n-1):
            curDiff = arr[i+1] - arr[i]

            if curDiff == minDiff:
                pairs.append([arr[i], arr[i+1]])

            elif curDiff < minDiff:
                minDiff = curDiff
                pairs = [[arr[i], arr[i+1]]]

            
        return pairs
