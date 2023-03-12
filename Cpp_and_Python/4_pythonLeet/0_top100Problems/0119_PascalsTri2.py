class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1] ## Base case for 0th row
        Tri = [[1]] ## initializing first row of the overall triangle
        for i in range(1,rowIndex+1): ## Running the list for each row
            row = [1] ## First term of each row is a 1
            for j in range(1,i):
                row.append(Tri[i-1][j-1] + Tri[i-1][j]) ## Each element is the sum of the above two elements 
            row.append(1) ## Ending element in pascals triangle
            Tri.append(row) ## Appending row
        return Tri[rowIndex] ## Returning the rowIndex'th Element