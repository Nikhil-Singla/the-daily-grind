class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n
        even = n // 2
        odd = (n+1) // 2
        
        m
        even = m // 2
        odd = (m+1) // 2

        ans = ((n // 2) * ((m+1) // 2))) + (((n+1) // 2) * (m // 2))

        return ans
