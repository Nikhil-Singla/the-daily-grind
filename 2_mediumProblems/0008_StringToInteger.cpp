class Solution {
public:
    int myAtoi(string s) 
    {
        int len = s.size();
        int result = 0;
        int flag = 0;
        bool negate = false;
        int insert = 0;
        for(int i = 0; i < len; i++)
        {
            while(s[i] == ' ')
            {
                i++;
            }
            if(s[i] == '-')
            {
                negate = true;
            }
            else
            {
                while(s[i] < 58 && s[i]>47)
                {
                    insert = s[i] - 47;
                    result *= 10;
                    result += insert;
                    i++;
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