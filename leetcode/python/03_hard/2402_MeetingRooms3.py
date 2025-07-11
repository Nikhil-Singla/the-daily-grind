class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        def min_time(leftPair, rightPair):
            if rightPair[0] < leftPair[0]:
                return rightPair
            else:
                return leftPair
        
        # n <<< meetings.length
        
        roomStatus = [[0, 0, 0, i] for i in range(n)]
        # Start time, duration, count, index

        meetings.sort(key=lambda tuple: tuple[0])
        
        t = 0

        for i in meetings:
            if t < i[0]:
                t = i[0]
            
            flag = False

            earliestFreeTime = [float('inf'), -1]
            
            for idx, j in enumerate(roomStatus):
                # if t >= (startTime + duration)

                freeTime = [(j[0] + j[1]), j[3]]
                earliestFreeTime = min(earliestFreeTime, freeTime)
                
                if t >= freeTime[0]:
                    j[0] = t
                    j[1] = i[1] - i[0]
                    j[2] += 1
                    flag = True
                    break

            if not flag:
                t = earliestFreeTime[0]
                j = roomStatus[earliestFreeTime[1]]

                j[0] = t
                j[1] = i[1] - i[0]
                j[2] += 1

        maxMeeting = -1
        for i in roomStatus:
            maxMeeting = max(maxMeeting, i[2])

        for i in roomStatus:
            if i[2] == maxMeeting:
                return i[3]

        return -1
