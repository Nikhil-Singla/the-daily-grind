class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        order = [0] * k**2
        idx = 0
        for i in range(x, x+k):
            for j in range(y, y+k):
                order[idx] = grid[i][j]
                idx += 1
        idx = 0

        for i in range(x+k-1, x-1, -1):
            for j in range(y, y+k):
                grid[i][j] = order[idx]
                idx += 1

        return grid
