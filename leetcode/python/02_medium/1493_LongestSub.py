class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = [0, 0]
        left = 0
        right = 0
        ans = 0

        n = len(nums)

        while right < n:
            count[nums[right]] += 1
            right += 1

            if count[0] >= 2:
                ans = max(ans, count[1])
                while(count[0] >= 2):
                    count[nums[left]] -= 1
                    left += 1

        ans = max(ans, count[1])
        if count[0]:
            return ans
        else:
            return ans-1