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

