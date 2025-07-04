class Solution:
    

    def kMirror(self, k: int, n: int) -> int:
        
        def isPal(num, base):
            digits = []
            while num > 0:
                digits.append(num % base)
                num //= base
            try:
                return digits == digits[::-1]
            except:
                return False
        
        def createPal(num, isOdd):
            mirNum = num
            if isOdd:
                mirNum //= 10

            while mirNum > 0:
                num = (num*10) + (mirNum %10)
                mirNum //= 10
            return num

        Sum = 0
        length = 1
        while (n > 0):
            for i in range(length, length*10):
                if n <= 0:
                    break

                pal = createPal(i, True)

                if isPal(pal, k):
                    Sum += pal
                    n -= 1
            
            for i in range(length, length*10):
                if n <= 0:
                    break
                pal = createPal(i, False)
                if isPal(pal, k):
                    Sum += pal
                    n -= 1
            
            length *= 10
        return Sum