class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        first = 0
        last = len(nums) - 1
        count = 0

        MOD = 10**9 + 7

        while(first <= last):
            summation = nums[first] + nums[last]

            if summation > target:
                last -= 1
            else:
                count = (count + pow(2, last - first, MOD)) % MOD
                first += 1

        return count