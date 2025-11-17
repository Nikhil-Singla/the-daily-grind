class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        check = 0
        
        for i in nums:
            if i == 1:
                if check > 0:
                    return False
                check = k
        
            else:
                check -= 1

        return True
