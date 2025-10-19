class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        next_inc = {
            str(n) : str((n+a)%10) for n in range(10)
        }

        def addition(s):
            result = list(s)

            for i in range(n):
                if i % 2 == 1:
                    result[i] = next_inc[s[i]]

            return "".join(result)

        def rotation(s):
            return s[n-b:] + s[:n-b]

        seen = set()

        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(addition(s))
            dfs(rotation(s))
            return

        dfs(s)
        return min(seen)
