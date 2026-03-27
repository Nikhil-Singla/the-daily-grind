class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])


        shifts = k % cols # After this its cyclic

        for i in range(rows):
            for j in range(cols):
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j + shifts) % cols]:
                        return False
                else:
                    if mat[i][j] != mat[i][(j - shifts) % cols]:
                        return False
        return True
