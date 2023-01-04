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