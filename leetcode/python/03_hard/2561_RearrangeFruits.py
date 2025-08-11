class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        fruitsCounter = defaultdict(int)
        minVal = min(basket1 + basket2)

        leftSide = list()
        rightSide = list()

        for i, j in zip(basket1, basket2):
            fruitsCounter[i] += 1
            fruitsCounter[j] -= 1

        for i, val in fruitsCounter.items():
            j = abs(val) 
            if j % 2 != 0:
                return -1

            if val > 0:
                left = [i] * (j//2)
                leftSide.extend(left)
            elif val < 0:
                right = [i] * (j//2)
                rightSide.extend(right)

        leftSide.sort()
        rightSide.sort(reverse=True)
        cost = 0

        for i, j in zip(leftSide, rightSide):
            cost += min(i, j, minVal*2)

        return cost
