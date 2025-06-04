class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        size = len(word)
        excess = size - numFriends
        answer = ord(word[0])

        if not excess:
            for letter in word:
                answer = max(answer, ord(letter))
            return chr(answer)

        answer = ['a'] * (excess+1)

        for index, count in enumerate(word):
            if (index + excess) >= size:
                break

            current = word[index : index+excess+1]
            # print(current)

            for idx, letter in enumerate(answer):
                comparator = ord(answer[idx]) - ord(current[idx])
                
                if comparator < 0:
                    for i in range(idx, excess - idx + 1):
                        answer[i] = current[i]
                elif comparator > 0:
                    break
                else:
                    continue
        
        retVal = ""
        for s in answer:
            retVal += s 

        return retVal
        