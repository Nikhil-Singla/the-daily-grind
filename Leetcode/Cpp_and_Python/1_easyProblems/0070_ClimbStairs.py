class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n 
        
        answers = [None] * n
        answers[0] = 1
        answers[1] = 2

        for i in range(2, n):
            answers[i] = answers[i-1] + answers[i-2]
        
        return answers[n-1]