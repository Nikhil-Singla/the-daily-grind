import math as m
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arrayElement = []
        median = [0, 0]
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

        if itemCount%2:
            itemCount -= 1
            median[0] = arrayElement[int(itemCount/2)]
            median[1] = arrayElement[int(itemCount/2)]
        else:
            median[0] = arrayElement[int(itemCount/2)] 
            median[1] = arrayElement[int(itemCount/2)-1]
        
        steps = [0, 0]

        for eachElement in arrayElement:
            if eachElement != median[0]: 
                steps[0] += abs(eachElement - median[0])/x
            if eachElement != median[1]: 
                steps[1] += abs(eachElement - median[1])/x

        return int(min(steps))