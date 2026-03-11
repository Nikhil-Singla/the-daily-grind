class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ret = [int(i) for i in bin(n)[2:]]
        for i in range(len(ret)):
            ret[i] ^= 1
        ret = [str(i) for i in ret]

        return int("".join(ret), 2)