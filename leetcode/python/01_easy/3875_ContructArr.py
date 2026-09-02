class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even = 0
        odd = 0
        odd_val_chosen = 0
        for i in nums1:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
                odd_val_chosen = i

        if even == 0 or odd == 0:
            return True # Array is pure even or pure odd.

        # If mixed, we can use the chosen odd_val to create nums2 as so
        nums2 = [0] * len(nums1)
        for idx, i in enumerate(nums1):
            if i%2 == 1:
                nums2[idx] = i
            else:
                nums2[idx] = i - odd_val_chosen
        
        # Converted to odd only array, hence its always true
        return True
