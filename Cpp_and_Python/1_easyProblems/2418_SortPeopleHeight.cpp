class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) 
    {
        map<int, string> list;
        for(int i = 0; i < heights.size(); i++)
        {
            list.insert({heights[i], names[i]});
        }
        vector<string> ans;
        for(auto i = list.rbegin(); i != list.rend(); ++i)
        {
            ans.push_back(i->second);
        }
        return ans;
    }
};