class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        def isSorted(arr):
            return all(
                    [
                        arr[i] <= arr[i+1] for i in range(len(arr)-1)
                    ]
                
                )
        
        def getMinPair(arr):
            size = len(arr)
            mp = float('inf')
            idx = -1

            for i in range(size-1):
                if arr[i] + arr[i+1] < mp:
                    mp = arr[i] + arr[i+1]
                    idx = i

            return mp, idx

        while (not isSorted(nums)):            
            pair, index = getMinPair(nums)
            nums[index:index+2] = [pair]
            count += 1

        return count
