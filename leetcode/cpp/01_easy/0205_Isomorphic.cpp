//Faster solution using mapping to a fixed length array
class Solution {
public:
    bool isIsomorphic(string s, string t) 
    {
        int_fast16_t mapS[256] = {0}, mapT[256] = {0};
        for(int_fast16_t i = 0; i < s.length(); i++)
        {
            if(mapS[s[i]] != mapT[t[i]])
            {
                return false;
            }
            mapS[s[i]] = i+1;
            mapT[t[i]] = i+1;
        }
        return true;
    }
};


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