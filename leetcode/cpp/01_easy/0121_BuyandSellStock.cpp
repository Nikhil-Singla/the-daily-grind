class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int current_least_price = prices[0];
        int maxProfit = 0;
        int currentProfit = 0;
        for(int i = 1; i < prices.size(); i++)
        {
            if(prices[i] < current_least_price)
            {
                current_least_price = prices[i];
            }
            currentProfit = prices[i] - current_least_price;
            if(currentProfit > maxProfit)
            {
                maxProfit = currentProfit;
            }
        }
        return maxProfit;
    }
};