class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def shoelaceFormula(point1, point2, point3):
            xa, ya = map(float, point1)
            xb, yb = map(float, point2)
            xc, yc = map(float, point3)
            
            return abs(((xa-xc)*(yb-ya))-((xa-xb)*(yc-ya)))

        ans = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):

                    area = shoelaceFormula(points[i], points[j], points[k])
                    ans = max(ans, area)

        return ans*0.5