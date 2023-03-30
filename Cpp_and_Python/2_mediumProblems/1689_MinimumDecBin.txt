class Solution {
public:
    int minPartitions(string n) 
    {
        int result = 1;
        for(auto const &c : n)
        {
            result = max(result, c - '0');
        }
        return result;    
    }
};