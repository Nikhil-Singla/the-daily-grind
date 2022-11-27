class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int maxProfit = 0;
        for(int i = 0; i<prices.size(); i++)
        {
            for(int j = i; j<prices.size(); j++)
            {
                int profit = prices[j]-prices[i];
                if(profit > maxProfit)
                {
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
    }
};