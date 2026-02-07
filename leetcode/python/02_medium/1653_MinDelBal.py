class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        dels_needed = 0 

        for i in s:
            if i == 'a':
                dels_needed = min(dels_needed+1, b_count)
            else:
                b_count += 1

        return dels_needed
