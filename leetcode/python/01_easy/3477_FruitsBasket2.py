class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        m = len(baskets)
        count = 0
        for i in range(n):
            for j in range(m):
                if baskets[j] >= fruits[i]:
                    baskets[j], fruits[i] = 0, 0
                    break

            if fruits[i] != 0:
                count += 1

        return count
                
