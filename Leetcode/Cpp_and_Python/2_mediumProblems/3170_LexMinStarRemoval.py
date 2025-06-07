class Solution:
    def clearStars(self, s: str) -> str:
        # Update based on rightmost element
        alphabet = [[] for _ in range(26)]
        removeIndex = []
        ans = list(s)

        for idx, i in enumerate(ans):
            # print(i)
            if i == '*':
                # print(alphabet)
                for i in range(26):
                    if alphabet[i]:
                        removeIndex.append(alphabet[i].pop())
                        break
            else:
                chrCode = ord(i) - 97
                alphabet[chrCode].append(idx)

        # print(removeIndex)
        removeIndex.sort()
        for affectedPos, i in enumerate(removeIndex):
            # print(affectedPos, i)
            ans.pop(i - affectedPos)

        # print(ans)
        return ''.join(a for a in ans if a != '*')