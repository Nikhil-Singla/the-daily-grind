class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        orset = set()
        lastset = set()

        for i in arr:
            temp = set([i])
            for j in lastset:
                temp.add(i|j)

            orset.update(temp)
            lastset = temp

        return len(orset)
