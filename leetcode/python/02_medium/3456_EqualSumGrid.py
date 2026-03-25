class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def checker(iteratable, summation):
            if summation % 2 == 1:
                return False
            
            summation //= 2
            count = 0
            for i in iteratable:
                count += i
                if count == summation:
                    return True
            
            return False
        
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        row_sum = [0] * num_rows
        col_sum = [0] * num_cols

        for i in range(num_rows):
            for j in range(num_cols):
                element = grid[i][j]
                row_sum[i] += element
                col_sum[j] += element

        row_half = sum(row_sum)
        col_half = sum(col_sum)

        return checker(row_sum, row_half) or checker(col_sum, col_half)
        
