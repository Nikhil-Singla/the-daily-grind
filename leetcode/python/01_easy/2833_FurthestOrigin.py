class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        final = 0
        count = 0
        for i in moves:
            if i == "L":
                final -= 1
            elif i == "R":
                final += 1
            elif i == "_":
                count += 1
        
        return abs(final) + count
