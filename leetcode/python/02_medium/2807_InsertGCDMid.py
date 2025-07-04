# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getGCD(self, num1, num2):
        while num2:
            num1, num2 = num2, (num1 % num2)

        return abs(num1)
    
    def insertMid(self, node: Optional[ListNode]):
        cur = node.val
        nextVal = node.next.val
        gcd = self.getGCD(cur, nextVal)

        midNode = ListNode(gcd, node.next)
        node.next = midNode
        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ss = head

        while ss.next != None:
            temp = ss.next
            self.insertMid(ss)
            ss = temp

        return head
