class Solution {
public:
    vector<string> letterCombinations(string digits) 
    {
        vector<string> ans;
        unordered_map <int, string> map;
        if(digits.empty())
        {return ans;}
        map[2] = "abc";
        map[3] = "def";
        map[4] = "ghi";
        map[5] = "jkl";
        map[6] = "mno";
        map[7] = "pqrs";
        map[8] = "tuv";
        map[9] = "wxyz";
        ans.push_back("");
        for(auto c : digits)
        {
            vector<string> temp;
            for(auto d : map[c - '0'])
            {
                for(auto e : ans)
                {
                    temp.push_back(e + d);
                }
            }
            ans.swap(temp);
        }
        return ans;
    }

    
};