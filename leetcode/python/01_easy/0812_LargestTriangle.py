class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        n = len(points)
        for i in range(n):
            xa, ya = points[i]
            for j in range(i+1, n):
                xb, yb = points[j]
                for k in range(j+1, n):
                    xc, yc = points[k]
                    ans = max(ans, abs(((xa-xc)*(yb-ya))-((xa-xb)*(yc-ya))))

        return ans*0.5