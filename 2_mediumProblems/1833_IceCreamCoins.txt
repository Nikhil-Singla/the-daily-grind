class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) 
    {
        uint i;
        uint num = 0;
        sort(costs.begin(), costs.end());
        for(auto c : costs)
        {
            if(coins >= c)
            {
                coins -= c;
                num++;
            }
            if(!coins)
            {
                break;
            }
        }
        return num;
    }
};