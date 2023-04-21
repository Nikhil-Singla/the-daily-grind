class Solution {
public:
    string truncateSentence(string s, int k) 
    {
        string ans = "";
        for(auto &c : s)
        {
            if(c == ' ')
            {
                k--;
                if(k == 0)
                {
                    return ans;
                }
                ans += c;
            }
            else
            {
                ans += c;
            }
        }
        return ans;    
    }
};