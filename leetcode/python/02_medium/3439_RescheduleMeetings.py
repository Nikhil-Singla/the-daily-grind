class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        events = [i for i in zip(startTime, endTime)]
        events.sort(key=lambda tuple : tuple[0])

        timeGap = [0] * (n + 1)

        timeGap[0] = events[0][0] - 0

        for idx in range(1, n):
            timeGap[idx] = events[idx][0] - events[idx-1][1]

        timeGap[-1] = eventTime - events[-1][1]

        if len(timeGap) <= k+1:
            return sum(timeGap)

        window = sum(timeGap[:k+1])
        maxSum = window

        for idx, i in enumerate(timeGap[k+1:]):
            window += i
            window -= timeGap[idx]

            maxSum = max(maxSum, window)

        return maxSum
            