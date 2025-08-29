class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        
        if n%2 == 0:
            even = n//2
            odd = n - even
        else:
            even = (n - 1) // 2
            odd = n - even

        for i in range(1, m+1):
            if i & 1:
                ans += even
            else:
                ans += odd

        return ans
