class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        # Iterates from 0, 0 -> n, 0 for the inner loop
        for i in range(n):
            array_size = n - i
            arr = []

            for j in range(array_size):
                heappush(arr, -grid[i+j][j])    # Negative to implement max heap, and sort by descending order as data is added

            for j in range(array_size):
                grid[i+j][j] = -heappop(arr)
        
        # Iterates from 0, 1 -> 0, n for the outer loop
        for i in range(1, n):
            array_size = n - i
            arr = []

            for j in range(array_size):
                heappush(arr, grid[j][i+j])     # Positive to implement min heap, and sort by ascending order as data is added

            for j in range(array_size):
                grid[j][i+j] = heappop(arr)

        return grid
