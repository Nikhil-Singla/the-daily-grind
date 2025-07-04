class Solution {
public:
    vector<string> findWords(vector<string>& words) 
    {
        vector<string> ans;
        string top = "qwertyuiop", mid = "asdfghjkl", bot = "zxcvbnm";
        for(auto n : words)
        {
            uint a = 0, b = 0, c = 0;
            for(auto i : n)
            {
                i = tolower(i);
                if(top.find(i) != string::npos)
                {
                    a++; continue;
                }
                if(mid.find(i) != string::npos)
                {
                    b++; continue;
                }
                if(bot.find(i) != string::npos)
                {
                    c++; continue;
                }
            }
            if(n.size() == max({a, b, c})) {ans.push_back(n);}
        }
        return ans;
    }
};