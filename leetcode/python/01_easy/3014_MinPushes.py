class Solution:
    def minimumPushes(self, word: str) -> int:
        alpha = Counter(word)
        f_map = 8
        s_map = 8
        t_map = 8
        fo_map = 2

        pushes = 0

        for i in sorted(alpha.keys()):
            count = alpha[i]
            if count <= 0:
                continue

            if f_map:
                f_map -= 1
                pushes += count
            elif s_map:
                s_map -= 1
                pushes += count*2
            elif t_map:
                t_map -= 1
                pushes += count*3
            else:
                fo_map -= 1
                pushes += count*4

        return pushes
