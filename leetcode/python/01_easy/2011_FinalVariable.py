class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        start = 0
        
        for i in op:
            if i[0] == "+" or i[-1] == "+":
                start += 1
            else:
                start -= 1

        return start
