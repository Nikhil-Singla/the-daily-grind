class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        ans = []

        if n % 10 != 9:
            count = n+1
        else:
            count = n

        for i in range(count):
            if num <= n:
                ans.append(num)

            if num*10 <= n:
                num *= 10
            else:
                while (num > n) or (num % 10 == 9):
                    num = num // 10 

                num += 1

        return ans