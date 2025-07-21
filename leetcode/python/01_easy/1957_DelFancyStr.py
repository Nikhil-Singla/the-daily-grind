class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        first = s[0]
        second = s[1]

        retStr = first + second

        for i in s[2:]:
            if i == first and i == second:
                pass
            else:
                retStr += i
                first, second = second, i

        return retStr