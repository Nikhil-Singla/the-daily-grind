class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        left, right, up, down = 1001, -1, 1001, -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    up = min(up, j)
                    left = min(left, i)
                    
                    down = max(down, j)
                    right = max(right, i)

        return (right-left+1) * (down-up+1)
