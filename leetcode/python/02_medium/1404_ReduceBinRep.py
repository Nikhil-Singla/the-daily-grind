class Solution:
    def numSteps(self, s: str) -> int:
        s = s[::-1]
        carry = 0
        count = 0

        for i in s[:-1:]:
            num = int(i) + carry
            carry = 0
            match num:
                case 0:
                    count += 1
                case 1:
                    carry = 1
                    count += 2
                case 2:
                    carry = 1
                    count += 1

        if carry and s[-1] == '0':
            return count
        elif carry and s[-1] == '1':
            return count + 1
        elif s[-1] == '0':
            return count + 1
        else:
            return count
        
        ## Fallback just in case
        return count
