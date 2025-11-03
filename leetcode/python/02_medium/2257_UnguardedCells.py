class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        rows = set(range(m))
        cols = set(range(n))
        
        for i, j in walls:
            grid[i][j] = 2  # Wall marker

        for i, j in guards:
            grid[i][j] = 3  # Guard marker

        for i, j in guards:
            # Down
            start = i + 1
            while (start in rows) and grid[start][j] != 2 and grid[start][j] != 3:

                grid[start][j] = 1
                start += 1

            # Up
            start = i - 1
            while (start in rows) and grid[start][j] != 2 and grid[start][j] != 3:
                grid[start][j] = 1
                start -= 1

            # Right
            start = j + 1
            while (start in cols) and grid[i][start] != 2 and grid[i][start] != 3:
                grid[i][start] = 1
                start += 1
            
            # Left
            start = j - 1
            while (start in cols) and grid[i][start] != 2 and grid[i][start] != 3:
                grid[i][start] = 1
                start -= 1

        return sum(x.count(0) for x in grid)
