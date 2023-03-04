class Solution {
public:
    int maximumValue(vector<string>& strs) 
    {
        int ans = 0;
        for(auto c : strs)
        {
            bool flag = false;
            for(auto d : c)
            {
                if(isalpha(d))
                {
                    flag = true;
                    break;
                }
            }
            if(flag) 
            {
                ans = max(ans, int(c.length()));
            }
            else {ans = max(ans, std::stoi(c));}
        }    
        return ans;
    }
};