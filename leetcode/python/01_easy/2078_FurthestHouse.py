class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ret = 0
        n = len(colors) - 1
        leftmost = colors[0]
        rightmost = colors[n]

        for i in range(n+1):
            if colors[n-i] != leftmost or colors[i] != rightmost:
                return n - i

        return 0
