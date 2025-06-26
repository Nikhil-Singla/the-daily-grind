class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ongoingLength = 0
        ongoingVal = 0
        flag = True
        for i in s[::-1]:
            # print(i, flag, ongoingLength)
            if flag and i == '1':
                ongoingVal += pow(2, ongoingLength)
                ongoingLength += 1
            
            elif i == '0':
                ongoingLength += 1

            if flag and ongoingVal > k:
                ongoingLength -= 1
                flag = False 

        return ongoingLength