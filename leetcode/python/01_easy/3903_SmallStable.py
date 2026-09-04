class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mini_arr = [nums[-1]]
        ele = nums[-1]
        n = len(nums)
        
        for i in range(n-2, -1, -1):
            if nums[i] < ele:
                ele = nums[i]

            mini_arr.append(ele)

        mini_arr = mini_arr[::-1]
        checker = nums[0]

        for i in range(0, n):
            if nums[i] > checker:
                checker = nums[i]

            tmp = checker - mini_arr[i]
            if tmp <= k:
                return i
                
        return -1