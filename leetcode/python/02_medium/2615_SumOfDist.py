class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        buckets = {}
        n = len(nums)
        for idx, i in enumerate(nums):
            if i in buckets:
                buckets[i].append(idx)
            else:
                buckets[i] = [idx]

        ret = [0] * n
        for one_list in buckets.values():
            total = sum(one_list)
            prefix = 0
            n = len(one_list)
            for idx, i in enumerate(one_list):
                ret[i] = total - prefix*2 + i*(2*idx-n)
                prefix += i

        return ret
