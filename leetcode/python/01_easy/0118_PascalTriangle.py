class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return [] ## Base case with no elements
        elif numRows == 1: return [[1]] ## Base case for 1 element
        Tri = [[1]] ## initializing first row of the overall triangle
        for i in range(1,numRows): ## Running the list for each row
            row = [1] ## First term of each row is a 1
            for j in range(1,i):
                row.append(Tri[i-1][j-1] + Tri[i-1][j]) ## Each element is the sum of the above two elements 
            row.append(1) ## Ending element in pascals triangle
            Tri.append(row) ## Appending row to overall triangle
        return Tri ## Returning the required triangle


# Daily Leetcode solution, August 1st. Code passes all testcases, and beats 100%
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows <= 1:
            return triangle

        for i in range(1, numRows):
            row = [1]
            for j in range(i-1):
                row.append(triangle[i-1][j] + triangle[i-1][j+1])

            row.append(1)
            triangle.append(row)
        
        return triangle
            
