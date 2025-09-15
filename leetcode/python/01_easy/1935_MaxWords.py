# [A1] [SO] [M.CHECK]
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        ans = 0


        for word in text:
            ans += 1
            for letter in word:
                if letter in brokenLetters:
                    ans -= 1
                    break

        return ans

# [A2] [IMP] [SO] [MO]
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        ans = len(text)

        for word in text:
            for letter in word:
                if letter in brokenLetters:
                    ans -= 1
                    break

        return ans