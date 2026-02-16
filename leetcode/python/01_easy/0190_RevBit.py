class Solution:
    def reverseBits(self, n: int) -> int:
        a = format(n, '032b')
        b = int(a[::-1], 2) 

        return b

        ## return int(format(n, '032b')[::-1], 2) 
