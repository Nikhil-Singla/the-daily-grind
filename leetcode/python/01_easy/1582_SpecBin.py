class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    valid = True
                    for l in range(m):
                        if mat[l][j] == 1 and l != i:
                            valid = False
                            break
                    if valid:    
                        for k in range(n):
                            if mat[i][k] == 1 and k != j:
                                valid = False
                                break
                    if valid:
                        count += 1
        return count
