class Solution {
public:
    string removeDuplicates(string s) 
    {
        vector<char> ans;
        for(auto c:s)
        {
            if((ans.size() > 0) && (ans.back()==c))
            {
                ans.pop_back();
            }
            else
            ans.push_back(c);
        }
        string result(ans.begin(),ans.end());
        return result;
    }
};