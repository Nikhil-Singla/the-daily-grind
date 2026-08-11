class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen = set(nums)

        on_sum = nums[0]
        seq = nums[0]
        cnt = 1

        for i in nums[1:]:
            if i == seq+1:
                cnt += 1
                on_sum += i
            else:
                break            
            
            seq = i

        ret = on_sum
        for _ in range(51):
            if ret not in seen:
                return ret
            else:
                ret += 1

        raise ValueError("Something went wrong.")
        return -1
