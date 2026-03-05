class Solution:
    def minOperations(self, s: str) -> int:
        zero_s, zero_c = '0', 0
        one_s, one_c = '1', 0

        for i in s:
            if i != zero_s:
                zero_c += 1
            if i != one_s:
                one_c += 1
                
            zero_s, one_s = one_s, zero_s

        return min(zero_c, one_c)
