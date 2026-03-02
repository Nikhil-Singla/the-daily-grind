from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        counts = []
        for row in grid:
            trailing = 0
            for val in reversed(row):
                if val == 1:
                    break
                trailing += 1
            counts.append(trailing)

        ans = 0

        for i in range(n):
            # Getting the next row with at least n-i 0's for the diagonal. Greedy approach
            j = next((k for k in range(i, n) if counts[k] >= n - i - 1), n)
            if j == n:
                return -1

            ans += j - i
            
            # Simulate swapping and moving all the rows
            counts[i:j+1] = [counts[j]] + counts[i:j]

        return ans
