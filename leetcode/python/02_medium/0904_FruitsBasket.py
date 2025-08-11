class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        currents = defaultdict(int)
        left = 0
        maxCount = 0

        for i in fruits:
            if i in currents:
                currents[i] += 1
            elif len(currents) < 2:
                currents[i] = 0
                currents[i] += 1
            else:
                maxCount = max(maxCount, sum(currents.values()))
                while len(currents) >= 2:
                    currents[fruits[left]] -= 1
                    if currents[fruits[left]] == 0:
                        del currents[fruits[left]]

                    left += 1

                currents[i] += 1

        maxCount = max(maxCount, sum(currents.values()))
        return maxCount
