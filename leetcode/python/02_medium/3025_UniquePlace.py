class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        for i in range(n):
            currPoint = points[i]

            for j in range(n):
                checkPoint = points[j]
                if i == j or not(currPoint[0] <= checkPoint[0] and currPoint[1] >= checkPoint[1]):
                    continue
                if n == 2:
                    ans += 1
                    continue

                invalid = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    testPoint = points[k]
                    
                    isXContained = (testPoint[0] >= currPoint[0] and testPoint[0] <= checkPoint[0])
                    isYContained = (testPoint[1] <= currPoint[1] and testPoint[1] >= checkPoint[1])
                    
                    if isXContained and isYContained:
                        invalid = True
                        break
                    
                if not invalid:
                    ans += 1

        return ans