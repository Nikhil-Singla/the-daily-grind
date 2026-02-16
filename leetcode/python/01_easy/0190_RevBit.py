class Solution:
    def reverseBits(self, n: int) -> int:
        a = format(n, '032b')
        b = int(a[::-1], 2) 

        return b
