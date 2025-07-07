class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        t = 1
        idx = 0
        count = 0     
        n = len(events)
        activeEvents = []
        events.sort(key=lambda tuple: tuple[0])

        while idx < n:

            while (idx < n) and (events[idx][0] <= t):
                heapq.heappush(activeEvents, events[idx][1])
                idx += 1
            
            while activeEvents:
                smallest = heapq.heappop(activeEvents)
                if smallest >= t:
                    count += 1
                    break
            
            t += 1

        while activeEvents:
            smallest = heapq.heappop(activeEvents)
            if smallest >= t:
                count += 1            
                t += 1

        return count