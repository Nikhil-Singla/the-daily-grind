class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s

        ans = [[''] for i in range(numRows) ]

        rowPointer = 0
        flag = True

        for i in s:
            if rowPointer == numRows and flag:
                rowPointer -= 2
                flag = not flag
            elif rowPointer == -1 and not flag:
                rowPointer += 2
                flag = not flag

            ans[rowPointer].append(i)
            
            rowPointer += (1 if flag else -1)

        retVal = ""

        for i in ans:
            for j in i:
                retVal += j

        return retVal
        