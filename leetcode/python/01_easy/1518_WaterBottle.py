class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles

        while(empty >= numExchange):
            empty -= numExchange
            empty += 1
            ans += 1
        
        return ans
