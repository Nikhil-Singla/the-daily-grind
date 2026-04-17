class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ret = 100000
        hash_m = {}

        for i, n in enumerate(nums):
            if n in hash_m:
                ret = min(ret, i - hash_m[n])
            
            hash_m[int(str(n)[::-1])] = i

        return -(ret == 100000) | ret