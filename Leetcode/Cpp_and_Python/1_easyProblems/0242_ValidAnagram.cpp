class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        int count[128] = {0};
        if(s.length() != t.length())
        {
            return false;
        }    
        for(const auto&c: s)
        {
            count[c]++;
        }
        for(const auto&c: t)
        {
            count[c]--;
        }
        for(const auto&c: count)
        {
            if(c != 0)
            {
                return false;
            }
        }
        return true;
    }
};

------------------------------------------------------------- Similar Time -------------------------------------------------------------
class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        unordered_map<char, int> hash1;
        if(s.length() != t.length())
        {
            return false;
        }    
        for(int i = 0; i < s.length(); i++)
        {
            hash1[s[i]]++;
            hash1[t[i]]--;
        }
        for(const pair<const char, int>& values : hash1)
        {
            if(values.second != 0)
            {
                return false;
            }
        }
        return true;
    }
};
class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        unordered_map<char, int> hash1, hash2;
        if(s.length() != t.length())
        {
            return false;
        }    
        for(int i = 0; i < s.length(); i++)
        {
            hash1[s[i]]++;
            hash2[t[i]]++;
        }
        return (hash1 == hash2);
    }
};
---------------------------------------------------------------------------------------------------------------------------------------