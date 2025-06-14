class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = [int(digit) for digit in str(num)]

        minD, maxD = -1, -1

        for idx, i in enumerate(nums):
            if i != 9:
                if maxD == -1:
                    maxD = i

            if i != 0:
                if minD == -1:
                    minD = i
        numsMax = 0
        numsMin = 0

        for i in nums:
            numsMax *= 10
            numsMin *= 10

            if i == maxD:
                numsMax += 9
            else:
                numsMax += i

            if i == minD:
                numsMin += 0
            else:
                numsMin += i

        return numsMax - numsMin