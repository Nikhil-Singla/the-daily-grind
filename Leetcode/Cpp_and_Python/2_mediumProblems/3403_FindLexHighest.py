class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        size = len(word)
        excess = size - numFriends
        answer = ord(word[0])

        if not excess:
            for letter in word:
                answer = max(answer, ord(letter))
            return chr(answer)
        
        highestList = []
        # print(ord('d'), ord('a'))

        for index, letter in enumerate(word):
            if answer == ord(letter):
                highestList.append(index)
            elif answer < ord(letter):
                highestList = []
                highestList.append(index)
                answer = ord(letter)
            elif answer > ord(letter):            
                continue

        word = list(word)
        startSpot = highestList[0]
        answer = word[startSpot:startSpot+excess+1]
        # print(word, answer, highestList)

        for spot in highestList:
            current = word[spot:spot+excess+1]
            curSize = len(current)
            anSize = len(answer)
            
            if curSize == anSize:
                for i in range(curSize):
                    comparator = ord(answer[i]) - ord(current[i])

                    if comparator < 0:
                        for idx in range(i, len(answer)):
                            # print(answer)
                            answer[idx] = current[idx]
                    elif comparator > 0:
                        break
                    else:
                        continue

            if curSize > anSize:
                answer = current
            
        retVal = ""
        for s in answer:
            retVal += s 

        return retVal

