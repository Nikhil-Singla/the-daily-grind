# [A1] [MF] [SF]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                left = triangle[i+1][j]
                right = triangle[i+1][j+1]

                triangle[i][j] += min(left, right)

        return triangle[0][0]