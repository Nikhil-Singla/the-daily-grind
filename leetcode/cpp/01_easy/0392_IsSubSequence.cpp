//Daily Leetcode Solution
class Solution {
public:
    bool isSubsequence(string s, string t) 
    {
        int length = s.length();
        if(length <= 0)
        {
            return true;
        }
        if(s.length() > t.length())
        {return false;}
        for(int i = 0, j = 0; i < t.length(); i++)
        {
            if(t[i] == s[j])
            {
                j++;
            }
            if(j == length)
            {
                return true;
            }
        }    
        return false;
    }
};

class Solution {
public:
    bool isSubsequence(string s, string t) 
    {
        uint index = 0;
        for(uint i = 0; i < t.length(); i++)
        {
            if(index >= s.length())
            {
                break;
            }
            if(t[i] == s[index])
            {
                index++;
            }
        }    
        return index == s.length();
    }
};

// FOLLOWUP Solution using Hashing for the initial vector
class Solution {
public:
    bool isSubsequence(string s, string t) 
    {
        unordered_map<char, vector<int>> hash;
        for(uint i = 0; i < t.length(); i++)
        {
            hash[t[i]].push_back(i);
        }

        for(auto const c : s)
        {
            int prev = -1;
            auto const iterator = hash.find(c);
            if(iterator == hash.end())
            {
                return false;
            }
            auto const indexVector = iterator->second;
            uint position = upper_bound(indexVector.begin(), indexVector.end(), prev) - indexVector.begin();
            if(position == indexVector.size()) 
            {
                return false;
            }
            prev = indexVector[position];
        }
        return true;
    }
};