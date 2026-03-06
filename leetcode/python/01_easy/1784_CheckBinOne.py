class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = True
        for i in s:
            if i != '1':
                    flag = False

            if not flag and i == '1':
                return flag

        return True
