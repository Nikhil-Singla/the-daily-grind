class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # O(n) time complexity assuming hash function is O(1)
        created_set = set(nums) 
        
        while original in created_set:
        # Worst case, O(n) time complexity assuming each number multiple is in created_set
            original <<= 1
            # Left shift is same as * 2, O(n)

        # Total O(2n + 2) = O(n)
        return original
