class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

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
        wordLen = len(answer)

        for spot in highestList:
            current = word[spot:spot+excess+1]
            curSize = len(current)
            anSize = len(answer)
            minsize = min(curSize, anSize)

            for i in range(minsize):
                comparator = ord(answer[i]) - ord(current[i])

                if comparator < 0:
                    for idx in range(i, minsize):
                        # print(answer)
                        answer[idx] = current[idx]
                        wordLen = minsize
                elif comparator > 0:
                    break
                else:
                    continue
            
        retVal = ""
        for s in answer:
            retVal += s 

        return retVal[:wordLen]

