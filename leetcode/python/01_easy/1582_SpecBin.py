class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        count = 0

        row_range = [0] * m
        col_range = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_range[i] += 1
                    col_range[j] += 1            
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_range[i] == 1 and col_range[j] == 1:
                    count += 1

        return count
