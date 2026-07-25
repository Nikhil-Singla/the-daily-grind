class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        high, low = sorted(digits, reverse=True)[0:2]
        return high*low
