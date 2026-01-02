class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ele = set()
        
        for i in nums:
            if i in ele:
                return i
            ele.add(i)

        return -1
