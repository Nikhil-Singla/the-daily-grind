class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        arr = defaultdict(list)
        n = len(nums)
        good = None

        for i in range(n):
            arr[nums[i]].append(i)

        for key, value in arr.items():
            if len(value) >= 3:

                n = len(value)
                for i in range(1, n-1):
                    if good:
                        good = min(good, 2*(value[i+1]-value[i-1]))
                    else:
                        good = 2*(value[i+1]-value[i-1])

        return good if good else -1
