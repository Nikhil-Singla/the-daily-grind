class Solution:
    def maximumLength(self, nums: List[int]) -> int:        
        oddCounter = 0
        evenCounter = 0

        altSeries = 1  # Alternate sequences, starting from the first digit
        # It can be proven that the alt series, as a subseq,
        # will always include the frontmost digit and start 
        # counting from there.

        lastParity = nums[0] % 2 # Track the parity of the previous num, starting from the front

        EVEN = 0
        ODD = 1

        for i in nums:
            if i & 1:
                oddCounter += 1
                if lastParity == EVEN:
                    lastParity = ODD
                    altSeries += 1

            else:
                evenCounter += 1
                if lastParity == ODD:
                    lastParity = EVEN
                    altSeries += 1
        
        return max(altSeries, oddCounter, evenCounter)