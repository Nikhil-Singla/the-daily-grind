class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        coordinate_offsets = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        rows = len(grid)
        cols = len(grid[0])
        memo = [[[[-1 for _ in range(2)] for _ in range(4)] for _ in range(cols)] for _ in range(rows)]

        def dfs(x, y, direction, turn, target):
            if memo[x][y][direction][turn] > -1:
                return memo[x][y][direction][turn]
            
            nextx, nexty = x + coordinate_offsets[direction][0], y + coordinate_offsets[direction][1]
            
            if nextx >= rows or nexty >= cols or nextx < 0 or nexty < 0:
                return 0
            
            if grid[nextx][nexty] != target:
                return 0

            it_can_turn = turn
            current_step = dfs(nextx, nexty, direction, turn, 2-target)

            if it_can_turn:
                current_step = max(current_step, dfs(nextx, nexty, (direction + 1) % 4, False, 2-target))

            memo[x][y][direction][turn] = current_step + 1
            return current_step + 1

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for dir in range(4):
                        print(coordinate_offsets[dir])
                        ans = max(ans, dfs(i, j, dir, True, 2) + 1)
                        print(ans)
        return ans