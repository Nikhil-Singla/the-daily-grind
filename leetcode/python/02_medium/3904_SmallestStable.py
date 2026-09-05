class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        small = nums[-1]
        large = nums[0]
        largest_so_far = []
        smallest_from_right = []

        n = len(nums)

        for i in range(n):
            front = nums[i]
            back = nums[n-i-1]
            if front > large:
                large = front
            
            if back < small:
                small = back

            largest_so_far.append(large)
            smallest_from_right.append(small)

        smallest_from_right.reverse()

        for i in range(n):
            if largest_so_far[i] - smallest_from_right[i] <= k:
                return i

        return -1
