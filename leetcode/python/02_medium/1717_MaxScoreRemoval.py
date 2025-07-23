class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            firstString, firstScore = "ab", x
            secondString, secondScore = "ba", y
        else:
            firstString, firstScore = "ba", y
            secondString, secondScore = "ab", x

        stack = [""] * len(s)
        score = 0
        stackPointer = 0

        for i in s:
            if stackPointer == 0:
                stack[stackPointer] = i
                stackPointer += 1
                continue

            if i == firstString[1] and stack[stackPointer-1] == firstString[0]:
                score += firstScore
                stackPointer -= 1
            else:
                stack[stackPointer] = i
                stackPointer += 1

        count_1 = 0

        for i in stack[:stackPointer]:
            if i == secondString[0]:
                count_1 += 1
            elif i == secondString[1] and count_1 > 0:
                count_1 -= 1
                score += secondScore
            else:
                count_1 = 0

        return score