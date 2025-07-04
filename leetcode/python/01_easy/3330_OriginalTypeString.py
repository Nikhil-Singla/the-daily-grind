class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]
        count = 0
        # There's an extra count being kept IN
        # Because it accounts for the original string.
        # So the actual answer should count from 1 to n-1
        # and then add 1, but we do it by counting from 0
        # and 0 index always adds 1. So it balances for time/speed 

        for i in word:
            if i == prev:
                count += 1

            prev = i

        return count