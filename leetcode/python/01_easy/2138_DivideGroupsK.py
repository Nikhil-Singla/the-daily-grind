class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = ((len(s) + k - 1) // k) * k
        ans = ""
        retVal = []
        for i in range(length):
            try:
                ans += s[i]
            except:
                ans += fill

            if len(ans) % k == 0:
                retVal.append(ans)
                ans = ""
        
        return retVal