class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        cur_row = rows - 1
        cur_col = 0

        while cur_row >= 0 and cur_col < cols:
            if grid[cur_row][cur_col] < 0:
                ans += cols - cur_col
                cur_row -= 1
            else:
                cur_col += 1

        return ans
