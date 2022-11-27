class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int leastPrice = prices[0];
        int currentProfit = 0;
        int maxProfit = 0;
        int cycleProfit = 0;
        for(int i = 0; i < prices.size(); i++)
        {
            if(prices[i] < leastPrice)
            {
                leastPrice = prices[i];
                maxProfit += cycleProfit; 
                cycleProfit = 0;
            }
            currentProfit = prices[i] - leastPrice;
            if(currentProfit > cycleProfit)
            {
                cycleProfit = currentProfit;
            }
        }
        return maxProfit;
    }
};