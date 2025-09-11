[A1] [SE] [ME] 
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

[A2] [S.CHECK] [MO] [ALT] [CPY] [IGN]
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4, 'a':5, 'e':6, 'i':7, 'o':8, 'u':9}
        vowels_rvrs = {0:'A', 1:'E', 2:'I', 3:'O', 4:'U', 5:'a', 6:'e', 7:'i', 8:'o', 9:'u'}
        vowels_cnt = [0]*len(vowels)
        for char in s:
            if self.is_vowel(char):
                vowels_cnt[vowels[char]] += 1
        
        index = 0
        while index < len(vowels) and vowels_cnt[index] == 0:
            index += 1

        for i, char in enumerate(s):
            if self.is_vowel(char):
                s = s[:i] + vowels_rvrs[index] + s[i+1:]
                vowels_cnt[index] -= 1
                while index < len(vowels) and vowels_cnt[index] == 0:
                    index += 1
        return s

    def is_vowel(self, c: chr) -> bool:
        c = c.lower()
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            return True
        else:
            return False
