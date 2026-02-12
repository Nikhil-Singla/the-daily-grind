class Solution:
    def longestBalanced(self, s: str) -> int:
        idx = 0
        n = len(s)
        mlen = 0
        if n < 3:
            return n

        for i in range(n):
            alpha = [0] * 26    
            clen = 0
            for j in s[i:]:
                alpha[ord(j) - ord('a')] += 1
                clen += 1
                values = set(alpha)
                values.discard(0)
                if values and len(values) == 1:
                    mlen = max(clen, mlen)
                    

        return mlen
