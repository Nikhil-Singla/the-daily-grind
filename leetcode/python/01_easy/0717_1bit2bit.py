class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        if n == 1:
            return True

        if n == 2:
            return bits[0] != 1

        if bits[-1] == 1:
            return False

        if bits[-2] == 0:
            return True

        i = 0
        flag = True
        while i < n:
            if bits[i] == 0:
                i += 1
                flag = True
            else:
                i += 2
                flag = False

        return flag
