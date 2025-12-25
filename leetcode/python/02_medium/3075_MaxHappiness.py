class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ret_val = 0
        despair = 0

        for i in range(k):
            curr = happiness[i]
            if curr <= i:
                break

            ret_val += curr - i

        return ret_val
