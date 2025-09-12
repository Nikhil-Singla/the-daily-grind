# [A1] [ME] [SE]
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o' , 'u'])

        for i in s:
            if i in vowels:
                return True

        return False
    

# [A2] [SO] [MO]

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return bool(re.search(r"[aeiou]", s))

# [A3] [SO] [ME] [ALT]
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u"): return True
        else: return False

