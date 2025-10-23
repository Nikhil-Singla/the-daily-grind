class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            n = len(s)
            temp = ['a'] * (n-1)
            
            for i in range(1, n):
                temp[i-1] = str((int(s[i]) + int(s[i-1]))%10)

            s = "".join(temp)

        return s[0] == s[1]
