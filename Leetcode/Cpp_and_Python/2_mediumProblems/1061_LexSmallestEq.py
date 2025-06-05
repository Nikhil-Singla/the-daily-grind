class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        smallEq = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                        'q','r','s','t','u','v','w','x','y','z']

        for i in range(len(s1)):
            alpha1, alpha2 = ord(s1[i])-97, ord(s2[i])-97
            diff = ord(smallEq[alpha1]) - ord(smallEq[alpha2])
            if diff < 0:
                smallEq[alpha2] = smallEq[alpha1]
            elif diff > 0:
                smallEq[alpha1] = smallEq[alpha2]

        # print(smallEq)

        ans = ""
        for i in baseStr:
            letter = ord(i) - 97
            actual = smallEq[letter]

            while actual != chr(letter+97):
                letter = ord(actual) - 97
                actual = smallEq[letter]
                # print(smallEq, actual, letter)

            ans += actual

        return ans
