class Solution {
public:
    int candy(vector<int>& ratings) 
    {
        vector<int> result(ratings.size(), 1);

        for(uint i = 1; i < ratings.size(); i++)
        {
            if(ratings[i] > ratings[i-1])
            {
                result[i] = result[i-1]+1;
            }
        }
        for(uint i = ratings.size()-1; i > 0; i--)
        {
            if(ratings[i-1] > ratings[i])
            {
                result[i-1] = max(result[i]+1, result[i-1]);
            }
        }
        uint solution = 0;
        for(auto &c : result)
        {
            solution += c;
        }
        return solution;
    }
};