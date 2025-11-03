class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = range(1, len(colors))
        time = 0
        for i in n:
            if colors[i] == colors[i-1]:
                if neededTime[i] < neededTime[i - 1]:
                    time += neededTime[i]
                    neededTime[i] = neededTime[i - 1]
                else:
                    time += neededTime[i - 1]
                    neededTime[i - 1] = neededTime[i]

        return time
