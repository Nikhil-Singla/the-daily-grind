# [A1] [MF] [S.CHECK]

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = [0] * 100
        
        for i in nums:
            counter[i-1] += 1

        elements = []
        max_element = 0
        
        for idx, i in enumerate(counter):
            if i > max_element:
                max_element = i
                elements = [idx+1]
            elif i == max_element:
                elements.append(idx+1)

        return len(elements) * max_element
