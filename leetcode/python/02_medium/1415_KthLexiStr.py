class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        item = []
        letters = ['a', 'b', 'c']
        def dfs(current, depth):
            if depth == 1:
                item.append(current)
            else:
                for i in letters:
                    if current and (i == current[-1]):
                        continue
                    else:
                        dfs(current+i, depth-1)

        for i in letters:
            dfs(i, n)

        if k > len(item):
            return ""
        else:
            return item[k-1]
