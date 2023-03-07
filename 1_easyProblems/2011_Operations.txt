class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) 
    {
        int x = 0;
        for(auto c : operations)
        {
            if(c[0] == '+' || c[1] == '+')
            {
                x++;
            }
            else
            {
                x--;
            }
        }    
        return x;
    }
};