class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bi = bin(n)[2:]
        for i in range(len(bi) - 1):
            if bi[i] == bi[i+1]:
                return False
        
        return True
