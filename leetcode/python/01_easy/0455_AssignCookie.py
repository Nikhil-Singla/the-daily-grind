class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greedIndex = 0
        sizeIndex = 0

        content = 0

        while greedIndex < len(g) and sizeIndex < len(s):
            if s[sizeIndex] >= g[greedIndex]:
                greedIndex += 1
                content += 1
            
            sizeIndex += 1

        return content
