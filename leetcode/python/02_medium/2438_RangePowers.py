# MEMORY EFFICIENT SOLUTION, BEATS 100%

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        powers = []
        
        for i in range(32):
            mask = 1 << i
            if mask & n:
                powers.append(pow(2, i))

        length = len(powers)
        prefMult = [powers[0]]
        sufMult = [powers[-1]]
        maxMult = powers[0]

        for i in range(1, length):
            prefMult.append((powers[i] * prefMult[i-1] ) % MOD)
            sufMult.append((powers[length-i-1] * sufMult[i-1]) % MOD)
            maxMult = (maxMult * powers[i]) % MOD


        sufMult.reverse()
        # print(powers, sufMult, prefMult)
        answers = []

        for start, end in queries:
            if start <= 0:
                answers.append(prefMult[end])
            elif end >= length - 1:
                answers.append(sufMult[start])
            else:
                answers.append((maxMult * pow(sufMult[end+1], MOD - 2, MOD) % MOD) * pow(prefMult[start-1], MOD - 2, MOD) % MOD)

        return answers