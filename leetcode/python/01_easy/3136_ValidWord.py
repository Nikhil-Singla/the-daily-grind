class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        flags = [False, False] # (Vowel, Consonant)
        
        incorrectChar = set(["@", "#", "$"])
        vowelSet = set(["a", "e", "i", "o", "u"])


        for i in word:
            if i in incorrectChar:
                return False

            if i.lower() in vowelSet:
                flags[0] = True

            elif (97 <= ord(i.lower()) <= 122):
                flags[1] = True
        
        return (flags[0] and flags[1])