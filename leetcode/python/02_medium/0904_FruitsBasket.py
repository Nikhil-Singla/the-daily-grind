class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        current = defaultdict(int)
        left = 0
        sets = 0
        count = 0
        retVal = 0

        for i in fruits:
            if sets < 2:
                if current[i] == 0:
                    sets += 1

                current[i] += 1
                count += 1

            elif current[i] > 0:
                current[i] += 1
                count += 1
            
            else:
                while sets >= 2:
                    current[fruits[left]] -= 1
                    count -= 1

                    if current[fruits[left]] <= 0:
                        sets -= 1
                    
                    left += 1

                current[i] += 1
                count += 1
                sets += 1

            retVal = max(count, retVal)

        return retVal
