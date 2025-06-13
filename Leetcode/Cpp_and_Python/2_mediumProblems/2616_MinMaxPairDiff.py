class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if p == 0:
            return 0


        def greedCheck(minimumSum):
            pointer = 0
            count = 0
            while pointer < (len(nums) - 1):
                diff = abs(nums[pointer] - nums[pointer+1])

                if diff <= minimumSum:
                    count += 1
                    if count >= p:
                        return True
                    pointer += 2
                else:
                    pointer += 1

            return False

        nums.sort()

        upper = abs(nums[0] - nums[-1])
        lower = 0
        ans = upper
        
        while lower <= upper:
            mid = (lower + upper) // 2

            if greedCheck(mid):
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1

        return ans