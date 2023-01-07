class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) 
    {
        int diff = 0;
        uint count = 0;
        uint n = gas.size();
        for(int i = 0; i < n*2; i++)
        {
            diff += (gas[i % n] - cost[i % n]);
            count++;
            if(diff < 0)
            {
                diff = 0;
                count = 0;
            }
            if(count == n)
            {
                return ((i+1) % n);
            }
        }
        return -1;
    }
};