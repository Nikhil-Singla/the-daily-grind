class Solution {
public:

    bool isNum(char a)
    {
        if(a < 58 && a>47)
        {
            return true;
        }
        return false;
    }

    int myAtoi(string s) 
    {
        int len = s.size();
        long unsigned result = 0;
        int flag = 0;
        bool negate = false;
        int insert = 0, i = 0;
        long unsigned low = 0, high = 2147483647, higher = 2147483648;
        while(s[i] == ' ')
        {
            i++;
        }
        if(s[i] == '-')
        {
            negate = true;
            i++;
        }
        while(isNum(s[i]))
        {
            insert = s[i] - 48;
            result *= 10;
            result += insert;
            i++;
        }
        if(negate)
        {
            result = clamp(result, low, higher);
            insert = result;
            insert *= -1;
        }
        else
        {
            result = clamp(result, low, high);
            insert = result;
        }
        //cout<<negate;
        return insert;
    }
};