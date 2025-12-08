class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            for j in range(1, n):
                a = i
                b = j
                c = math.sqrt(a**2 + b**2)
                if c//1 == c and c <= n:
                    count += 1

        return count
