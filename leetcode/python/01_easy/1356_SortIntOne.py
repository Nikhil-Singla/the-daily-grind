class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        buckets = [[] for _ in range(32)]

        for i in arr:
            buckets[bin(i).count('1')].append(i)

        ans = []
        for i in buckets:
            i.sort()
            for j in i:
                ans.append(j)

        return ans
