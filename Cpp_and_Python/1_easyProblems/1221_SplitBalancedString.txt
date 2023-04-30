class Solution {
public:
    int balancedStringSplit(string s) 
    {
        int result = 0, count = 0;
        for (const auto& c : s) 
        {
            if(c == 'L')
            {
                count += 1;
            }
            else
            {
                count += -1;
            }
            if (count == 0) 
            {
                ++result;
            }
        }
        return result;        
    }
};