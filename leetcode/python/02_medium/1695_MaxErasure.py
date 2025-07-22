class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        elementsSeen = set()
        maxSum = ongoingSum = 0
        left = right = 0
        n = len(nums)

        while(right < n):
            if nums[right] not in elementsSeen:
                elementsSeen.add(nums[right])
                ongoingSum += nums[right]
                right += 1
            else:
                maxSum = max(maxSum, ongoingSum)
                while(nums[left] != nums[right]):
                    ongoingSum -= nums[left]
                    elementsSeen.remove(nums[left])
                    left += 1

                ongoingSum -= nums[left]
                elementsSeen.remove(nums[left])
                left += 1

        maxSum = max(maxSum, ongoingSum)        
        return maxSum