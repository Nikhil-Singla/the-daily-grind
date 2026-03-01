class Solution:
    def minPartitions(self, n: str) -> int:
        alpha = set(n)
        retval = -1
        for i in alpha:
            if int(i) > retval:
                retval = int(i)

        return retval
