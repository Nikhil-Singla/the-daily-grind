class Solution {
public:
    int countSegments(string s) 
    {
        uint count = 0;
        bool flag = false, space = false;
        if(!s.length()) {return 0;}
        while(s[0] == ' ')
        {
            s.erase(s.begin());
        }
        for(auto i : s)
        {
            if(i == ' ')
            {space = true;}
            else
            {
                flag = true;
                if(space)
                {
                    space = false;
                    count++;
                }
            }
        }    
        if(flag) return count+1;
        else return 0;
    }
};