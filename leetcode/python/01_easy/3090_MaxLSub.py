class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = 0

        count = defaultdict(int)
        n = len(s)

        ret = 1

        while (right < n):
            count[s[right]] += 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            ret = max(ret, right-left+1)
            right += 1

        return ret
