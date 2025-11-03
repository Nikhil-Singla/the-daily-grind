class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = range(1, len(colors))
        time = 0
        for i in n:
            if colors[i] == colors[i-1]:
                time += min(neededTime[i], neededTime[i-1])
                max_time = max(neededTime[i], neededTime[i-1])
                neededTime[i], neededTime[i-1] = max_time, max_time

        return time
