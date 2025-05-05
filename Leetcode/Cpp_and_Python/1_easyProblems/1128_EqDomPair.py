from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        answer = 0
        d = defaultdict(int)
            
        for dominoPair in dominoes:
            dominoSet = frozenset(dominoPair)
            d[dominoSet] += 1

        for oneVal in d.values():
            if oneVal >= 2:
                answer += (oneVal * (oneVal-1))/2   # Combination selection

        return int(answer)
