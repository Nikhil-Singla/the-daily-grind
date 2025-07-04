class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        pos = 1

        def count(num):
            nei = num + 1
            result = 0

            while num <= n:
                result += min(nei, n+1) - num
                num *= 10
                nei *= 10

            return result

        while pos < k:
            steps = count(num)

            if pos + steps <= k:
                num += 1
                pos += steps
            else:
                num *= 10
                pos += 1

        return num
                