class Solution:
    def minOperations(self, s: str) -> int:
        s = [int(i) for i in s]
        mask = 1
        s_zero = 0
        s_one = 1

        zero_c = 0
        one_c = 0

        for i in s:
            if i != s_zero:
                zero_c += 1

            if i != s_one:
                one_c += 1

            s_zero ^= mask
            s_one ^= mask

        return min(zero_c, one_c)
