class Solution:
    def totalMoney(self, n: int) -> int:
        
        if n <= 7:
            return (n*(n+1)) // 2

        first_seven = 28
        quotient = n // 7
        remainder = n % 7

        retVal = (quotient * first_seven) + ((quotient - 1) * 7 * quotient)/2
        start = quotient + 1

        for i in range(remainder):
            retVal += start + i

        return int(retVal)
