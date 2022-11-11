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
        long long result = 0;
        int i = 0;
        bool negate = false;

        while(s[i] == ' ')
        {
            i++;
        }
        if(s[i] == '-')
        {
            negate = true;
            i++;
        }
        if(s[i] == '+')
        {
            i++;
        }
        while(isNum(s[i]))
        {
            result = result*10 + (s[i] - 48);
            i++;
            if(result >= INT_MAX) 
            {
                break;
            }   
        }

        if(negate) 
        {
            result *= -1;
        }
        if(result <= INT_MIN) 
        {
            return INT_MIN;
        }
        if(result >= INT_MAX) 
        {
            return INT_MAX;
        }

        return result;
    }
};