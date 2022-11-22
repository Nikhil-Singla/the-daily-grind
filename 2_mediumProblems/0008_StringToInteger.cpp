class Solution {
public:
    bool isNum(char a)          //Function to check if the input char is a number or not
    {
        if(a < 58 && a>47)      //ASCII code based checker
        {
            return true;        //Character is number
        }
        return false;           //Character is not number
    }

    int myAtoi(string s)        //Convert string to int
    {
        long long result = 0;   //Store our result
        int i = 0;              //Keep track of the current input character from the entire string
        bool negate = false;    //Keep track if the number is negative or not

        while(s[i] == ' ')
        {
            i++;
        }
        if(s[i] == '-')
        {
            negate = true;
            i++;
        }
        else if(s[i] == '+')
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
