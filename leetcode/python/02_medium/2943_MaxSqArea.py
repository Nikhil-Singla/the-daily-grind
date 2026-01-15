class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_maxlength(bars):
            prev = bars[0]
            max_len = 0
            cur_len = 1
            for i in bars[1:]:
                if prev+1 == i:
                    cur_len += 1
                else:
                    max_len = max(max_len, cur_len)
                    cur_len = 1

                prev = i

            max_len = max(max_len, cur_len)

            return max_len

        vBars.sort()
        hBars.sort()
        
        return (min(get_maxlength(vBars) , get_maxlength(hBars)) + 1 )**2
