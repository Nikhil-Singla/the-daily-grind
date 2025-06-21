class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        freq = [0] * 26
        for i in word:
            freq[ord(i) - ord('a')] += 1

        retVal = float('inf')
        print(freq)

        for i in range(26):
            if (freq[i] == 0):
                continue

            tempC = 0

            for j in range(26):
                if (i == j) or (freq[j] == 0):
                    continue
                
                x = freq[i]
                y = freq[j]

                if (y < x):
                    tempC += y
                elif y-x > k:
                    tempC += (y - x - k)


            retVal = min(retVal, tempC)

        return retVal