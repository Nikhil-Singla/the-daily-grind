class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(digit) for digit in s]
        n = len(s)

        binomialCoeffs = [1] * (n-1)
        for i in range(1, n-1):
            binomialCoeffs[i] = binomialCoeffs[i-1] * (n-2-i+1) // i

        leftDigit = sum([digit * coeff for digit, coeff in zip(s[:-1], binomialCoeffs)]) % 10
        rightDigit = sum([digit * coeff for digit, coeff in zip(s[1:], binomialCoeffs)]) % 10

        return leftDigit == rightDigit
