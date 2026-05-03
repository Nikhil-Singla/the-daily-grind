class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)

        first = 0
        second = 0

        for _ in range(n):
            temp = second
            
            if s[first] == goal[second]:
                
                count = 0
                while (first < n) and (s[first] == goal[second]):
                    count += 1
                    first += 1
                    second = (second + 1) % n
                
                if count == n:
                    return True
            
            first = 0
            second = temp + 1

        return False
