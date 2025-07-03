class Solution:
    def kthCharacter(self, k: int) -> str:

        maxIndex = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

        alphabet = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']

        start = ['a']

        idxPointer = 0

        for i in range(0, k):
            idx = i + 1

            if idx >= len(start):
                for j in range(maxIndex[idxPointer]):
                    start.append( alphabet[ord(start[j]) - 97] )

                idxPointer += 1
            
            if idx == k:
                return start[i]

        return 'a'