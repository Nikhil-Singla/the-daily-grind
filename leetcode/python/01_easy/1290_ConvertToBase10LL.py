# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = [False] * 30
        count = 0

        while head is not None:
            if head.val == 1:
                ans[count] = True
            
            head = head.next
            count += 1

        count -= 1
        power = 0
        retVal = 0

        while count >= 0:
            if ans[count]:
                retVal += pow(2, power)

            power += 1
            count -= 1

        return retVal