class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = int(s[0] == 'b')  # True = 1, False = 0
        dels_needed = 0 

        for i in s[1:]:
            if i == 'a':
                dels_needed = min(dels_needed+1, b_count)
            else:
                b_count += 1

        return dels_needed
