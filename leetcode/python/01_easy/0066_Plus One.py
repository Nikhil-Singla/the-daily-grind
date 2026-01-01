class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        remainder = 1
        digits.reverse()

        for i in range(n):
            if digits[i] == 9:
                digits[i] = 0

            else:
                digits[i] += 1
                remainder = 0
                break

        if remainder:
            digits.append(1)
            
        digits.reverse()
        return digits
            
