class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        l = len(s)
        prev = -1
        retdist = 0

        for i in range(l):
            if s[i] == '1': 
                if prev == -1:
                    prev = i
                    continue
                
                retdist = max(retdist, i-prev)
                prev = i

        return retdist
