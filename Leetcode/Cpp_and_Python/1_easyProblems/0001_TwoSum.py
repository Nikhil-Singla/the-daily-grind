from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(lambda: -1)

        for index, oneNumber in enumerate(nums):
            diffNum = target - oneNumber
            duoNum = hashMap[diffNum]
            
            if duoNum >= 0:
                return [index, duoNum]
                
            hashMap[oneNumber] = index
        
        return 0