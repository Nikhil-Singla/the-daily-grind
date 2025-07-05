# Bi_Weekly Contest 160
# Q1 : Code passing all test cases
class Solution:

    def concatHex36(self, n: int) -> str:
        digit16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
        digit32 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
               'W', 'X', 'Y', 'Z']

        def hexDiv(number, base):
            str = ""
    
            digits = (digit16 if base == 16 else digit32)
            
            while number:
                remainder = int(number % base)
                digit = digits[remainder]
                
                str = digit + str
    
                number -= remainder
                number /= base
    
            return str
        
        return hexDiv(n*n, 16) + hexDiv(n*n*n, 36)


# Q2 : Code passing all test cases
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        rows = m
        cols = n
        
        totalCost = [[0 for _ in range(cols)] for _ in range(rows)]
        totalCost[0][0] = 1
        
        for i in range(1, cols):
            totalCost[0][i] = (i+1) + waitCost[0][i] + totalCost[0][i-1]

        for i in range(1, rows):
            totalCost[i][0] = (i+1) + waitCost[i][0] + totalCost[i-1][0]

        if m == 1 or n == 1:
            return totalCost[rows-1][cols-1] - waitCost[rows-1][cols-1]
        
        for i in range(1, rows):
            for j in range(1, cols):
                totalCost[i][j] = min(
                    totalCost[i-1][j],    # One row before
                    totalCost[i][j-1]     # One col before
                ) + waitCost[i][j] + ((i+1)*(j+1))
        
        return totalCost[rows-1][cols-1] - waitCost[rows-1][cols-1]
    
# Q3 : 