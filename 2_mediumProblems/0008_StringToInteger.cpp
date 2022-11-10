class Solution {
public:
    int myAtoi(string s) 
    {
        int len = s.size();
        int result = 0;
        int flag = 0;
        bool negate = false;
        for(int i = 0; i < len; i++)
        {
            while(s[i] == " ")
            {
                i++;
            }
            
            if(flag == 0)
            {
                if(s[i] == "-")
                {
                    negate = true;
                }
            }
        }
        if(negate)
        {
            result *= 1;
        }
        return result;
    }
};