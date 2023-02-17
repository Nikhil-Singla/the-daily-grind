class Solution {
public:
    char repeatedCharacter(string s) 
    {
        set<char> check;
        for(auto c : s)
        {
            if(check.find(c) != check.end())
            {return c;}
            else
            {check.insert(c);}
        }    
        return 'c';
    }
};