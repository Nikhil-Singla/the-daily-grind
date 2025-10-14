class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        size, prev = 1, nums[0]
        prevSize = 0
        for i in nums[1:]:
            if i > prev:
                size += 1
            else:
                if max(size/2, min(size, prevSize)) >= k:
                    return 1
                
                prevSize = size
                size = 1

            prev = i

        return max(size/2, min(size, prevSize)) >= k
