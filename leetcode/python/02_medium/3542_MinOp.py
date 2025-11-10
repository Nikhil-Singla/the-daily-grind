class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for i in nums:
            if stack:
                while stack and stack[-1] > i:
                    stack.pop()
                    ans += 1
                
                if stack and stack[-1] == i:
                    continue

            if i:       # Filter out zeroes directly instead of later as their work is already done in the while loop.
                stack.append(i)

        return ans + len(stack)
