class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        flag = True
        for i in str(num):
            if i == '6' and flag:
                ans += '9'
                flag = False

            else:
                ans += i

        return int(ans)
