class Solution {
public:
    int maxPower(string s) 
    {
        unsigned short c = 1, a = 1;
        for(unsigned short i = 1; i < s.length(); i++)
        {
            if(s[i] == s[i-1])
            {
                c++;
                if(c > a) {a = c;}
            } else c = 1;
        }    
        return a;
    }
};