class Solution {
public:
    string interpret(string command) 
    {
        string ans = "";
        for(auto &c : command)
        {
            if(c == 'G' || c == 'l')
            {
                ans += c;
            }
            else if(c == '(')
            {
                ans += "o";
            }
            else if( c == 'a')
            {
                ans.pop_back();
                ans += c;
            }
        }    
        return ans;
    }
};