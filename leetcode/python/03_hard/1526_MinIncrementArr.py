class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]

        for i in range(1, n):
            diff = target[i] - target[i-1]
            if diff > 0:
                ans += diff

        return ans