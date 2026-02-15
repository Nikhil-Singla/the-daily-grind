class Solution:
    def addBinary(self, a: str, b: str) -> str:   
        ans = []
        c = 0

        for tup in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            f, s = map(int, tup)
            
            val = c + f + s
            c = int(val > 1)
            
            match val:                    
                case 0 | 2:
                    ans.append('0')
                case 1 | 3:
                    ans.append('1')

        if c:
            ans.append('1')

        return ''.join(ans[::-1])
