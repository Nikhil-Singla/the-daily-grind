#include <cstring>
class Solution {
public:
    string toLowerCase(string s) 
    {
        for(int i = 0; i<s.size(); i++)
        {
            if(s[i] < 97)
            {
                s[i] += 32;
            }
        }    
        return s;
    }
};