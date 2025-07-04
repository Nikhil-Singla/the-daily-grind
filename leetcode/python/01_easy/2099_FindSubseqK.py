class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k:
            return nums

        ans = [0] * k
        i = 0
        temp = Counter(sorted(nums, reverse=True)[:k])

        for j in nums:
            
            if temp[j]:

                temp[j] -= 1

                ans[i] = j
                i += 1

                if i == k:
                    break

        return ans
    


# Reference code for faster solution:
# class Solution:
#     def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
#         # Step 1: Keep track of original indices
#         indexed = [(num, i) for i, num in enumerate(nums)]
        
#         # Step 2: Sort by value (descending) and take top k
#         top_k = sorted(indexed, key=lambda x: x[0], reverse=True)[:k]
        
#         # Step 3: Sort selected k elements by original index
#         top_k.sort(key=lambda x: x[1])
        
#         # Step 4: Extract the numbers only
#         return [num for num, _ in top_k]