class Solution {
public:
    bool isIsomorphic(string s, string t) 
    {
        unordered_map <char, char> map;
        unordered_set <char> assigned;
        for(int i = 0; i < s.length(); i++)
        {
            char key = s[i];
            if(map.find(key) == map.end())
            {
                if(assigned.find(t[i]) != assigned.end())
                {
                    return false;
                }
                map[key] = t[i];
                assigned.insert(t[i]);
            } 
            else
            {
                if(map[key] != t[i])
                {
                    return false;
                } 
            }
        }    
        return true;
    }
};