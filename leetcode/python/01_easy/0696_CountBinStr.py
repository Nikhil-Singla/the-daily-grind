class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur_pair = s[0]
        cur_count = 1
        prev_count = 0
        retval = 0

        for i in s[1:]:
            if i == cur_pair:
                cur_count += 1
            else:
                retval += min(cur_count, prev_count)
                cur_pair = i
                prev_count, cur_count = cur_count, 1

        return retval+min(prev_count, cur_count)
