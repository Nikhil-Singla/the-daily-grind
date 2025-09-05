# [A1] [SO] [Mo]
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-y) == abs(z-x):
            return 0
        
        return int(abs(z-y) < abs(z-x)) + 1
    
# [A2] [SO] [MO] [ALT]
# Solution passed SO and was taken leetcode MO section
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        d1=abs(z-x)
        d2=abs(z-y)

        if d1<d2:
            return 1
        
        elif d1>d2:
            return 2
        
        else:
            return 0