class Solution {
public:
    int minimumCost(vector<int>& cost) 
    {
        sort(cost.begin(), cost.end(), greater<int>());
        int sum = 0;
        for(int i = 0; i <cost.size(); i += 3)
        {
            sum += cost[i];
            if(i < cost.size()-1) {sum += cost[i+1];}
        }    
        return sum;
    }
};

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