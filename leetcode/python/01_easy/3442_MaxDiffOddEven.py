class Solution:
    def maxDifference(self, s: str) -> int:
        alpha = [0] * 26

        for i in s:
            alpha[ord(i) - 97] += 1

        maxO = 0
        minE = 101
        for i in alpha:
            if i:
                if i % 2 == 0:
                    minE = min(minE, i)
                else:
                    maxO = max(maxO, i)

        return (maxO - minE)