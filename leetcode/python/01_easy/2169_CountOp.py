class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 and num2:
            if num1 > num2:
                temp = num1 // num2
                count += temp
                num1 -= num2*temp
            else:
                temp = num2 // num1
                count += temp
                num2 -= num1*temp

        return count
