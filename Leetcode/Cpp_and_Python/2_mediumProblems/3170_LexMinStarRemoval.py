class Solution:
    def clearStars(self, s: str) -> str:
        # Update based on rightmost element
        
        alphabet = [[] for _ in range(26)]
        removeIndex = set()
        ans = list(s)

        for idx, i in enumerate(ans):
            if i == '*':
                for i in range(26):
                    if alphabet[i]:
                        removeIndex.add(alphabet[i].pop())
                        break
            else:
                chrCode = ord(i) - 97
                alphabet[chrCode].append(idx)
        
        retVal = ""
        for idx, char in enumerate(ans):
            if idx not in removeIndex:
                if char != '*':
                    retVal += char

        return retVal