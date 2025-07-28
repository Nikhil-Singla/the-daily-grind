class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        modified = [nums[0]]

        for i in nums[1:]:
            if modified[-1] != i:
                modified.append(i)

        for i in range(1, len(modified)-1):
            if (modified[i-1] < modified[i] > modified[i+1]) or (modified[i-1] > modified[i] < modified[i+1]):
                count += 1

        return count
