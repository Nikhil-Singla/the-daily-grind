class Solution:
    def maxFreqSum(self, s: str) -> int:
        s = Counter(s)
        vowels = "aeiou"
        maxV = 0
        maxC = 0

        a = [0]
        b = [0]

        for i in s.keys():
            if i in vowels:
                a.append(s[i])
            else:
                b.append(s[i])

        return max(a) + max(b)