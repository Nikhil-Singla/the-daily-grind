class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        hash_set = [False] * (2**k)

        for i in range(0, n-k+1):
            hash_set[int(s[i:i+k], 2)] = True

        return all(hash_set)
