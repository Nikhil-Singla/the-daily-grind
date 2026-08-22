class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(str(n))
        ds = 0
        dp = 1

        for i in digits:
            ds += int(i)
            dp *= int(i)

        return (n%(ds+dp)) == 0
