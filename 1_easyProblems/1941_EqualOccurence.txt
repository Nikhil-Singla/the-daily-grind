class Solution {
public:
    bool areOccurrencesEqual(string s) 
    {
        unordered_map<char, int> count;
        for(auto c : s)
        {
            count[c]++;
        }    
        bool flag = true;
        int num;
        for(auto c : count)
        {
            if(flag)
            {
                flag = false;
                num = c.second;
            }
            if(num != c.second)
            {
                return false;
            }
        }
        return true;
    }
};