class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        items = []

        for i in s:
            if i in vowels:
                items.append(i)
        
        s = list(s)
        items.sort()
        
      j = 0

        for idx, i in enumerate(s):
            if i in vowels:
                s[idx] = items[j]
                j += 1
        
        return ''.join(s)
