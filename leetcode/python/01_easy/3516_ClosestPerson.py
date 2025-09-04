class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-y) == abs(z-x):
            return 0
        
        return int(abs(z-y) < abs(z-x)) + 1