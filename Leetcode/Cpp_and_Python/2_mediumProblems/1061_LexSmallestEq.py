ORD_A = 97

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Range is exclusive at the end
        alphabet = list(range(26))

        def find(x):
            if alphabet[x] != x:
                alphabet[x] = find(alphabet[x])

            return alphabet[x]

        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return

            elif xRoot < yRoot:
                alphabet[yRoot] = xRoot

            elif xRoot >  yRoot:
                alphabet[xRoot] = yRoot

        for i in range(len(s1)):
            firstElement = ord(s1[i]) - ORD_A
            secondElement = ord(s2[i]) - ORD_A

            union(firstElement, secondElement)

        ans = ""

        for i in baseStr:
            iStr = ord(i) - ORD_A
            actual = find(iStr)
            actual += ORD_A
            ans += chr(actual)

        return ans
