# [A2] [SO] [ME] [IMP]

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = max(counter.values())

        addon = 0

        for i in counter.values():
            if i == max_freq:
                addon += max_freq

        return addon
