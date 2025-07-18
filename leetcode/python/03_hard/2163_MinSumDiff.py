class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        minHeap_Right = nums[2*n:]      # Taking min heap to remove the min element via heappop
        heapq.heapify(minHeap_Right)    # to maximize the right side sum    
        
        maxHeap_Left = [-x for x in nums[:n]]   # Taking max heap to remove the max element via heappop
        heapq.heapify(maxHeap_Left)             # to minimize the left side sum     

        leftSum = -sum(maxHeap_Left)    # For maxheap implementation, I'm reversing the values from a
                                        # minheap implementation.
        rightSum = sum(minHeap_Right)

        minDif = float('inf')

        leftMinSum = [0] * (n+1)    # Sum of n min left elements as we go from nth index to 2*n th index
        rightMaxSum = [0] * (n+1)   # Sum of n max right elements as we go from 2*n th index, to nth index

        leftMinSum[0] = leftSum
        rightMaxSum[n] = rightSum

        for idx, i in enumerate(range(n, 2*n)):
            leftSum += nums[i]
            leftSum -= heapq.heappushpop(maxHeap_Left, nums[i] * (-1)) * (-1)

            # First, we push the inverted value to minheap. Then pop the smallest value. 
            # Inverting this value gives us the largest value that we can subtract from leftSum
            # Finally, we update the minSum array with this leftSum value

            leftMinSum[idx+1] = leftSum


            rightSum += nums[(2*n) - 1 - idx]
            rightSum -= heapq.heappushpop(minHeap_Right, nums[(2*n) - 1 - idx]) 
            
            # For rightmaxsum, we can directly pop the minimum element, and subtract from the sum
            # as we are traversing from right side to the left.  n-1 <--- 2*n

            rightMaxSum[n - 1 - idx] = rightSum

        for i, j in zip(leftMinSum, rightMaxSum):
            minDif = min(minDif, (i - j))

        return minDif

        