class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def sum_to_n(number):
            return (number * (number+1))//2

        ans = 0
        counter = 0

        for i in nums:
            if i == 0:
                counter += 1
            elif counter != 0:
                ans += sum_to_n(counter)
                counter = 0

        ans += sum_to_n(counter)
        return ans
