class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alphabet_start = [-1] * 26
        alphabet_end = [-1] * 26
        for idx, i in enumerate(s):
            ascii_of_letter = ord(i) - ord('a')
            if alphabet_start[ascii_of_letter] == -1:
                alphabet_start[ascii_of_letter] = idx
            else:
                alphabet_end[ascii_of_letter] = idx

        unique_pairs = 0
        for i in range(26):
            if alphabet_end[i] != -1:
                unique_pairs += len(set(list(s[alphabet_start[i]+1:alphabet_end[i]])))

        return unique_pairs
