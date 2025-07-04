import math as m
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arrayElement = []
        median = 0
        ongoingRemainder = grid[0][0] % x
        
        for oneRow in grid:
            for oneElement in oneRow:
                if oneElement%x != ongoingRemainder:
                    return -1
                
                arrayElement.append(oneElement)

        arrayElement.sort()
        itemCount = len(arrayElement)

        if itemCount == 1:
            return 0

        median = arrayElement[int(itemCount/2)] 
        steps = 0

        for eachElement in arrayElement:
            if eachElement != median: 
                steps += abs(eachElement - median)/x

        return int(steps)