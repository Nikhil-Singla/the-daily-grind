# LEARNING NOTE:
# Assigning input%10 to "a" somehow gave much better speeds than directly testing with the if statement.
# Difference between pre-allocation of memory and on the spot allocation I reckon.
 
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasNoZero(input):
            while input:
                a = input%10
                if a == 0:
                    return False
                else:
                    input //= 10
            
            return True
        
        for i in range(1, n):
            if hasNoZero(i) and hasNoZero(n-i):
                return [i, n-i]