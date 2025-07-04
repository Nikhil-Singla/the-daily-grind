class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        direction = [0] * 4
        distance = [0] * 2
        ans = 0

        for j in range(len(s)):
            i = s[j]
            if i == 'N':
                distance[0] += 1
                direction[0] += 1
            elif i == 'S':
                distance[0] -= 1
                direction[1] += 1
            elif i == 'E':
                distance[1] += 1
                direction[2] += 1
            elif i == 'W':
                distance[1] -= 1
                direction[3] += 1

            horCap = abs(distance[1])
            vertCap = abs(distance[0])
            manhattan = horCap + vertCap

            dist = manhattan + min(2*k, j+1-manhattan)
            ans = max(ans, dist)

        return ans