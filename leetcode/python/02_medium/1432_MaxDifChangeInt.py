class Solution:
    def maxDiff(self, num: int) -> int:
        nums = [int(n) for n in str(num)]

        maxP = 9
        minP = 0

        for i in nums:
            if i != 9:
                maxP = i
                break

        for i in nums:
            if (i != 1) and (i != 0):
                minP = i
                break

        maxNum = 0
        minNum = 0

        if maxP != 9:
            for i in nums:
                maxNum *= 10
                if i == maxP:
                    maxNum += 9
                else:
                    maxNum += i
        else:
            maxNum = num

        if (minP != 1) and (minP != 0):
            repElement = (1 if nums[0] == minP else 0)

            for i in nums:
                minNum *= 10
                if i == minP:
                    minNum += repElement
                else:
                    minNum += i
        else:
            minNum = num

        return maxNum - minNum