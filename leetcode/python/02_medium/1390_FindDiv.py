class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def findDivisor(input_num):
            count = 2
            sum = input_num + 1
            for i in range(2, math.isqrt(input_num) + 1):
                rem = input_num / i
                if rem == int(rem):
                    if count >= 4:
                        return 0

                    if i*i != input_num:
                        sum += i + rem
                        count += 2
                    else:
                        sum += i
                        count += 1

            # print(input_num, count)
            if count == 4:
                return int(sum)
            else:
                return 0

        ret_val = 0
        for i in nums:
            # print(ret_val, i)
            ret_val += findDivisor(i)

        return ret_val
