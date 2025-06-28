class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k:
            return nums

        ans = [0] * k
        i = 0
        temp = Counter(sorted(nums, reverse=True)[:k])

        for j in nums:
            
            if temp[j]:

                temp[j] -= 1

                ans[i] = j
                i += 1

                if i == k:
                    break

        return ans