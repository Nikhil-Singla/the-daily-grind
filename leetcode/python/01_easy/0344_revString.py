class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

## Alternate Solution using two pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        front, back = 0, len(s) - 1 ## Initialize Tuples pointing to first and last element of list
        while front < back:
            s[front], s[back] = s[back], s[front] ## Swap using tuples
            front, back = front+1, back-1 ## Appropriate Index Modification

## Alternate Solution using string splicing
class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev = s[::-1] ## We need to choose the Initial and End value according to a reversed list 
                      ## if the IndexJump value is negative. 
        for i in range(len(s)):
            s[i] = rev[i]