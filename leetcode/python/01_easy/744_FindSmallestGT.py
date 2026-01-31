class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        present = set(letters)
        alpha = [0] * 26
        start = ord('a')

        for i in present:
            alpha[ord(i) - start] = 1

        s_range = ord(target) - start + 1

        for i in range(s_range, 26):
            if alpha[i]:
                return chr(i+start)

        return letters[0]
