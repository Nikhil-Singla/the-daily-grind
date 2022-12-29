class Solution {
public:
    string removeDuplicates(string s) 
    {
        vector<char> ans;
        for(int i = 0; i < s.length() ; i++)
        {
            ans.push_back(s[i]);
            while(ans[ans.size()-2] == ans.back() && ans.size()>2)
            {
                ans.pop_back();
                ans.pop_back();
            }
        }
        string result(ans.begin(),ans.end());
        return result;
    }
};