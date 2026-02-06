class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        cur_len = 1
        max_len = 1

        nums.sort()
        
        n = len(nums)

        while j < n:
            lowest = nums[i]
            highest = nums[j]

            if lowest * k >= highest:
                j += 1
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                max_len = max(max_len, cur_len)

                while (nums[i] * k) < highest:
                    i += 1
                    cur_len -= 1

        max_len = max(max_len, cur_len)
        return n - max_len + 1
