class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            array_size = n - i
            arr = []

            for j in range(array_size):
                heappush(arr, -grid[i+j][j])

            for j in range(array_size):
                grid[i+j][j] = -heappop(arr)

        for i in range(1, n):
            array_size = n - i
            arr = []

            for j in range(array_size):
                heappush(arr, grid[j][i+j])

            for j in range(array_size):
                grid[j][i+j] = heappop(arr)

        return grid
