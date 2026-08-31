# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        index = 0

        tmp = head.next
        prev = head
        
        critical_points = []

        while(tmp.next != None):
            if (prev.val < tmp.val > tmp.next.val) or (prev.val > tmp.val < tmp.next.val):
                critical_points.append(index)

            index += 1
            prev = tmp
            tmp = tmp.next

        if len(critical_points) < 2:
            return [-1, -1]

        maxDist = critical_points[-1] - critical_points[0]
        minDist = maxDist
        for i in range(len(critical_points) - 1):
            tmpDist = critical_points[i+1] - critical_points[i]
            if tmpDist < minDist:
                minDist = tmpDist

        return [minDist, maxDist]
