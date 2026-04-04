class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        ret = []
        for i in range(cols):   
            for j in range(i, n, cols+1):
                # print(j, encodedText[j])
                ret.append(encodedText[j])

        return "".join(ret).rstrip()
