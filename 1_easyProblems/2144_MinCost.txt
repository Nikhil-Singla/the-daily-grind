class Solution {
public:
    int minimumCost(vector<int>& cost) 
    {
        sort(cost.begin(), cost.end());
        int sum = 0;
        for(int i = cost.size()-1; i >=0; i -= 3)
        {
            if(i < 2)
            {
                while(i >= 0)
                {
                    sum += cost[i--];
                }
                return sum;
            }
            sum += cost[i] + cost[i-1];
        }    
        return sum;
    }
};