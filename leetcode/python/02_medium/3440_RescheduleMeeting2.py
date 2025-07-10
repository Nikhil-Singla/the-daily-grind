class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        events = [pair for pair in zip(startTime, endTime)]
        n = len(events)
        events.sort(key=lambda tuple: tuple[0])

        timeGap = [0] * (n + 1)
        timeGap[0] = events[0][0] - 0
        timeGap[-1] = eventTime - events[-1][1]
        
        for i in range(1, n):
            timeGap[i] = events[i][0] - events[i-1][1]

        prefArr = [0] * (n + 1)
        prefArr[0] = 0
        for i in range(1, n+1):
            prefArr[i] = max(prefArr[i-1], timeGap[i-1])

        suffArr = [0] * (n + 1)
        suffArr[n] = 0
        for i in range(n-1, -1, -1):
            suffArr[i] = suffArr[i+1]
            if i + 2 <= n:
                suffArr[i] = max(suffArr[i], timeGap[i+2])

        timeMax = 0
        for i in range(n):
            currTime = events[i][1] - events[i][0]

            if prefArr[i] >= currTime or suffArr[i] >= currTime:
                tempTime = timeGap[i] + timeGap[i+1] + currTime
            else:
                tempTime = timeGap[i] + timeGap[i+1]
                
            timeMax = max(timeMax, tempTime)

        return timeMax
