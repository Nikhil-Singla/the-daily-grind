class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        counter = 0

        for i in nums:
            if i == 0:
                counter += 1
            elif counter:
                ans += (counter * (counter+1))//2
                counter = 0

        if counter:
            ans += (counter * (counter+1))//2
            
        return ans

# CACHING Method, but slightly slower due to smaller value of nums.length():
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        counter = 0
        hot_cache = {}


        for i in nums:
            if i == 0:
                counter += 1
            elif counter:
                ans += hot_cache.setdefault(counter, (counter * (counter+1)) // 2)
                counter = 0
        
        if counter:
            ans += hot_cache.setdefault(counter, (counter * (counter+1)) // 2)

        return ans
