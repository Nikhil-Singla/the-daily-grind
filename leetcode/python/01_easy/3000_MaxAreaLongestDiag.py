class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = 0
        maxArea = 0
        squares = [0] * 100
        
        for i, j in dimensions:
            # print(i, j)
            if squares[i-1] == 0:
                squares[i-1] = i*i
            
            if squares[j-1] == 0:
                squares[j-1] = j*j

            add = squares[i-1] + squares[j-1]
            # print(add) 

            if add > maxDiag: 
                maxDiag = add
                maxArea = i * j
            elif add == maxDiag:
                maxArea = max(maxArea, i*j)

        return maxArea
